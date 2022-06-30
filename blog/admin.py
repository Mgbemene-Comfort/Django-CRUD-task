from django.contrib import admin

# Register your models here.
admin.action(
    permissions=['blog'],
    description='Mark selected stories as published',
)
def make_published(self, request, queryset):
    queryset.update(status='p')
def make_published(self, request, queryset):
    queryset.update(status='p')
make_published.allowed_permissions = ['blog']
make_published.short_description = 'Mark selected stories as published'