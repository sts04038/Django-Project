from django.contrib import admin

from blog.models import Post

# Register your models here.

# 데코레이터 패턴을 사용하지 않는 방법
# admin.site.regiter(Bookmark, BookmarkAdmin)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ','.join(tag.name for tag in obj.tags.all())