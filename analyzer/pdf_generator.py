from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(file_path, data):

    doc = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Resume Report</b>", styles["Heading1"]))

    story.append(Paragraph(f"ATS Score : {data['ats_score']}", styles["Normal"]))

    story.append(Paragraph(f"Job Match : {data['job_match']}%", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>AI Analysis</b>", styles["Heading2"]))

    story.append(Paragraph(data["ai_analysis"].replace("\n", "<br/>"), styles["Normal"]))

    doc.build(story)