from django.contrib import admin
from .models import Post
# Register your models here.

# admin에 등록 방법들
#
# # 등록법 1
# admin.site.register(Post)

#
# # 등록법 2
# class PostAdmin(admin.ModelAdmin):
#     list_display=['id', 'title', 'created_at', 'updated_at']
#
# admin.site.register(Post, PostAdmin)
#
#
# # 등록법 3
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'created_at', 'updated_at']


###################################
####customizing admin register#####
###################################
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size','created_at', 'updated_at']

    def content_size(self, post):
        return '{} words'.format(len(post.content))
    content_size.short_description = "글자수"  # renaming