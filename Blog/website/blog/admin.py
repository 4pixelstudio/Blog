from django.contrib import admin

from .models import Post, Tag

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","author","timestamp","updated"]
    list_filter = ["updated","timestamp"]
    list_display_links = ["title"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)

admin.site.register(Tag)