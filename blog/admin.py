from django.contrib import admin

from .models import Profile, CoreSkills, OtherSkills, WorkExperience, WorkExperienceComplements, LatestWorks, About, Details, Tools, ToolsTopics, Articles, DetailsArticles

admin.site.register(Profile)
admin.site.register(About)
admin.site.register(CoreSkills)
admin.site.register(OtherSkills)
admin.site.register(WorkExperience)
admin.site.register(WorkExperienceComplements)
admin.site.register(LatestWorks)
admin.site.register(Details)
admin.site.register(Tools)
admin.site.register(ToolsTopics)
admin.site.register(Articles)
admin.site.register(DetailsArticles)


