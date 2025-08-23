from django.contrib import admin
from django.utils.html import format_html
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "github_url", "sort_order", "thumb")
    list_editable = ("sort_order",)
    search_fields = ("title", "description", "github_url")

    def thumb(self, obj):
        p = (obj.image_path or "").strip()
        if not p:
            return "—"
        # If user pasted a full URL or an absolute path, use as-is
        if p.startswith(("http://", "https://", "/")):
            url = p
        else:
            # Relative like "img/file.png" -> serve from /static/
            url = f"/static/{p.lstrip('/')}"
        return format_html('<img src="{}" style="height:40px;width:auto;border-radius:4px;" />', url)

    thumb.short_description = "Preview"
