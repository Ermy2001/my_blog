from django.contrib import admin, messages
from .models import Article, Category
from django.utils.translation import ngettext

# Admin Header Change
admin.site.site_header = "وبلاگ جنگویی من"

# Register your models here.


@admin.action(description="انشار مقالات انتخاب شده")
def make_published(modeladmin, request, queryset):
    updated = queryset.update(status="p")
    modeladmin.message_user(
        request,
        ngettext(
            "%d مقاله منتشر شد.",
            "%d مقاله منتشر شدند.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )


@admin.action(description="پیشنویس کردن مقالات انتخاب شده")
def make_draft(modeladmin, request, queryset):
    updated = queryset.update(status="d")
    modeladmin.message_user(
        request,
        ngettext(
            "%d مقاله پیشنویس شد.",
            "%d مقاله پیشنویس شدند.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = (['status'])
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag', 'slug', 'jpublish', 'status', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-status', 'publish')
    actions = [make_published, make_draft]

    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category.active()])


admin.site.register(Article, ArticleAdmin)
