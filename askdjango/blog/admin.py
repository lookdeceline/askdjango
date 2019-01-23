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
    list_display = ['id', 'title', 'content_size','status','created_at', 'updated_at']


    def content_size(self, post):
        return ('{} words'.format(len(post.content)))
    content_size.short_description = "글자수"  # renaming


    ######## Post 페이지의 bulk action을 위한 ########
    ######## 'action' 옵션 추가 ########

    actions = ['make_draft', 'make_published', 'make_withdrawl']


    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='p') #QuerySet.update
        self.message_user(request, '{}건의 포스팅을 Draft 상태로 변경'.format(updated_count))  #django message framework 활용
    make_draft.short_description = 'Draft'


    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p') #QuerySet.update
        self.message_user(request, '{}건의 포스팅을 Published 상태로 변경'.format(updated_count))  #django message framework 활용
    make_published.short_description = 'Published'



    def make_withdrawl(self, request, queryset):
        updated_count = queryset.update(status='p') #QuerySet.update
        self.message_user(request, '{}건의 포스팅을 Withdrawn 상태로 변경'.format(updated_count))  #django message framework 활용
    make_withdrawl.short_description = 'Withdrawn'