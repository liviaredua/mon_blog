from django.contrib import admin

from .models import Profile, CoreSkills, OtherSkills, WorkExperience, WorkExperienceComplements, LatestWorks, About, Details

admin.site.register(Profile)
admin.site.register(About)
admin.site.register(CoreSkills)
admin.site.register(OtherSkills)
admin.site.register(WorkExperience)
admin.site.register(WorkExperienceComplements)
admin.site.register(LatestWorks)
admin.site.register(Details)

