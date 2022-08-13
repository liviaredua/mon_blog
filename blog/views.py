from distutils import core
from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile, CoreSkills, OtherSkills, WorkExperience, WorkExperienceComplements, LatestWorks, About


def formatExperience():
    RawExperience = WorkExperience.objects.all()
    size = len(RawExperience)
    nCols = False
    col1 = RawExperience
    col2 = None
    if size > 1:
        nCols = True
        col1 = RawExperience[0:size//2]
        col2 = RawExperience[size//2:]

    return (col1, col2, nCols)

def about(request):
    profile = Profile.objects.get(id=1)
    about = About.objects.get(id=1)
    WorkExperience_col1, WorkExperience_col2, nCols= formatExperience()

    data = {
        'profile':{
            'first_name':profile.first_name, 
            'last_name':profile.last_name,
            'birth':profile.birth,
            'linkedin':profile.linkedin,
            'gitHub':profile.gitHub
            },
        'about': {
            'salutation':about.salutation,
            'textSalutation':about.textSalutation,
            'aboutMe': about.aboutMe
        },
        'coreSkills' : [{'skill':obj.skill, 'level':obj.level} for obj in CoreSkills.objects.all()],
        'OtherSkills' : [{'skill':obj.skill, 'level':obj.level} for obj in OtherSkills.objects.all()],
        'workExperience_col_1':[
                            {
                            'timeRange': obj.timeRange,
                            'officename': obj.officename,
                            'department': obj.department,
                            'description': obj.description, 
                            'complements': [comp.complemtText for comp in WorkExperienceComplements.objects.filter(idWork_id=obj.id)]
                            } for obj in WorkExperience_col1
                        ],

        'workExperience_col_2':[
                            {
                            'timeRange': obj.timeRange,
                            'officename': obj.officename,
                            'department': obj.department,
                            'description': obj.description, 
                            'complements': [comp.complemtText for comp in WorkExperienceComplements.objects.filter(idWork_id=obj.id)]
                            } for obj in WorkExperience_col2
                        ] if nCols else None,
        'latestWorks': [{'title':obj.workTilte, 'description':obj.description} for obj in LatestWorks.objects.all()] 

    }
    return render(request, 'about.html', data)


def download(request):
    with open('blog/media/cv.pdf', 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            return response
    
    return response