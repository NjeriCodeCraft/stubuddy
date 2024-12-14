from django.contrib import admin
from .models import NavbarItem, StudyTip, Course


# Register your models here.



@admin.register(NavbarItem)
class NavbarItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'is_active')
    list_filter = ('is_active',)

@admin.register(StudyTip)
class StudyTipAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'description', 'icon')
    search_fields = ('title', 'subtitle')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration')
    search_fields = ('name',)






