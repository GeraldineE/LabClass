from django.contrib import admin
from .models import Curso, lesson

# Register your models here.


#class LessonInline(admin.StackedInline):
class LessonInline(admin.TabularInline):
    model = lesson

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]

admin.site.register(Curso, CourseAdmin)
admin.site.register(lesson)
