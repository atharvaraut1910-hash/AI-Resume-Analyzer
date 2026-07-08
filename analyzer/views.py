from django.http import FileResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


from .pdf_generator import generate_pdf
from .models import ResumeAnalysis
from .ai import analyze_resume, generate_cover_letter
from .parser import extract_text
from .ats import calculate_ats_score


def home(request):
    return render(request, "analyzer/home.html")


def upload_resume(request):

    context = {}

    if request.method == "POST" and request.FILES.get("resume"):

        # Upload Resume
        resume = request.FILES["resume"]

        fs = FileSystemStorage(location="media")

        filename = fs.save(resume.name, resume)

        file_url = fs.url(filename)

        # Extract Resume Text
        text = extract_text(fs.path(filename))

        # Job Description
        job_description = request.POST.get("job_description", "")

        # AI Resume Analysis
        ai_analysis = analyze_resume(text)

        # AI Cover Letter
        cover_letter = generate_cover_letter(
            text,
            job_description
        )

        # ATS Analysis
        score, suggestions, detected_skills, missing_skills, job_match = calculate_ats_score(
            text,
            job_description
        )

        # Save Analysis
        ResumeAnalysis.objects.create(
            resume_name=filename,
            ats_score=score,
            job_match=job_match,
            ai_analysis=ai_analysis,
        )

        # Send to HTML
        context = {
            "filename": filename,
            "file_url": file_url,
            "resume_text": text,
            "ats_score": score,
            "suggestions": suggestions,
            "detected_skills": detected_skills,
            "missing_skills": missing_skills,
            "job_description": job_description,
            "job_match": job_match,
            "ai_analysis": ai_analysis,
            "cover_letter": cover_letter,
        }

    return render(request, "analyzer/upload.html", context)


def history(request):

    resumes = ResumeAnalysis.objects.all().order_by("-uploaded_at")

    total_resumes = resumes.count()

    if total_resumes > 0:
        average_ats = round(
            sum(r.ats_score for r in resumes) / total_resumes
        )

        highest_ats = max(r.ats_score for r in resumes)

    else:

        average_ats = 0
        highest_ats = 0

    context = {
        "resumes": resumes,
        "total_resumes": total_resumes,
        "average_ats": average_ats,
        "highest_ats": highest_ats,
    }

    return render(request, "analyzer/history.html", context)


def download_report(request, id):

    resume = ResumeAnalysis.objects.get(id=id)

    file_path = f"media/report_{id}.pdf"

    data = {
        "ats_score": resume.ats_score,
        "job_match": resume.job_match,
        "ai_analysis": resume.ai_analysis,
    }

    generate_pdf(file_path, data)

    return FileResponse(
        open(file_path, "rb"),
        as_attachment=True,
        filename=f"Resume_Report_{id}.pdf"
    )