from django.contrib import admin
from .models import University, Specialty, SpecialtyScoreForUniversity, Subject

class SpecialtyScoreForUniversityInline(admin.TabularInline):
    model = SpecialtyScoreForUniversity
    extra = 1

class UniversityAdmin(admin.ModelAdmin):
    inlines = (SpecialtyScoreForUniversityInline,)

admin.site.register(University, UniversityAdmin)
admin.site.register(Specialty)
admin.site.register(Subject)
