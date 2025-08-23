from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    # Put paths like:  img/yourfile.png   (lives under portfolio/static/img/)
    image_path = models.CharField(max_length=300, blank=True)

    github_url = models.URLField()
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return self.title
