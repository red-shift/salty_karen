from django.contrib import admin
from app_karen.models import KarenPost, Comment


class KarenPostAdmin(admin.ModelAdmin):
    model = KarenPost


class CommentAdmin(admin.ModelAdmin):
    model = Comment


admin.site.register(KarenPost, KarenPostAdmin)
admin.site.register(Comment, CommentAdmin)
