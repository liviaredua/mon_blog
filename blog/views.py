from distutils import core
from django.shortcuts import render
from .models import Profile, CoreSkills, OtherSkills, WorkExperience, WorkExperienceComplements, LatestWorks



def about(request):
    profile = Profile.objects.get(id=1)

    data = {
        'profile':{
            'first_name':profile.first_name, 
            'last_name':profile.last_name,
            'birth':profile.birth,
            'linkedin':profile.linkedin,
            'gitHub':profile.gitHub
            },
        'coreSkills' : [{'skill':obj.skill, 'level':obj.level} for obj in CoreSkills.objects.all()],
        'OtherSkills' : [{'skill':obj.skill, 'level':obj.level} for obj in OtherSkills.objects.all()],

    }
    return render(request, 'about.html', data)