from django.contrib import admin

from .models import Profile, CoreSkills, OtherSkills, WorkExperience, WorkExperienceComplements, LatestWorks

admin.site.register(Profile)
admin.site.register(CoreSkills)
admin.site.register(OtherSkills)
admin.site.register(WorkExperience)
admin.site.register(WorkExperienceComplements)
admin.site.register(LatestWorks)
