from django.db import models


class ResumeAnalysis(models.Model):

    resume_name = models.CharField(max_length=255)

    ats_score = models.IntegerField()

    job_match = models.IntegerField()

    ai_analysis = models.TextField()

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.resume_name