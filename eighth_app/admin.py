from django.contrib import admin
from .models import StudentFeedback
# Register your models here.

class StudentFeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'email', 'feedback']
    
admin.site.register(StudentFeedback, StudentFeedbackAdmin)