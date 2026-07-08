from django.contrib import admin
from .models import ResumeAnalysis

@admin.register(ResumeAnalysis)
class ResumeAnalysisAdmin(admin.ModelAdmin):
    list_display = (
        "resume_name",
        "ats_score",
        "job_match",
        "uploaded_at",
    )

    search_fields = ("resume_name",)

    list_filter = ("uploaded_at",)

    ordering = ("-uploaded_at",)