from django.contrib import admin
from .models import Product, Category


def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = "Published Article"
    else:
        message_bit = "Published Articles"
    modeladmin.message_user(request, "{} article {}".format(rows_updated, message_bit))


make_published.short_description = "Publish Selected Articles"


def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated == 1:
        message_bit = "Drafed Article"
    else:
        message_bit = "Drafed Articles"
    modeladmin.message_user(request, "{} article {}".format(rows_updated, message_bit))


make_draft.short_description = "Draft Selected Articles"


class PostAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'available', 'publish')
    list_filter = ('publish', 'available')
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['available', '-publish']
    actions = [make_published, make_draft]


admin.site.register(Product, PostAdmin)

admin.site.register(Category)

