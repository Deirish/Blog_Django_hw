from django.contrib import admin
from .models import Post, Topic, Comment


class TopicModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Topic


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date_create', 'date_update']
    list_display_links = ['id', 'date_update']
    list_editable = ['title']
    list_filter = ['date_update', 'date_create']
    search_fields = ['title', 'text']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
admin.site.register(Topic, TopicModelAdmin)
admin.site.register(Comment)
