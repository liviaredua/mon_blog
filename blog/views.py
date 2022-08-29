from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile, CoreSkills, OtherSkills, WorkExperience, WorkExperienceComplements, LatestWorks, About, Details, Tools, ToolsTopics
from django.core.paginator import Paginator

from .NewsView import News

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
    WorkExperience_col1, WorkExperience_col2, nCols = formatExperience()

    data = {
        'profile': {
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'birth': profile.birth,
            'linkedin': profile.linkedin,
            'gitHub': profile.gitHub
        },
        'about': {
            'salutation': about.salutation,
            'textSalutation': about.textSalutation,
            'aboutMe': about.aboutMe
        },
        'coreSkills': [{'skill': obj.skill, 'level': obj.level} for obj in CoreSkills.objects.all()],
        'OtherSkills': [{'skill': obj.skill, 'level': obj.level} for obj in OtherSkills.objects.all()],
        'workExperience_col_1': [
            {
                'timeRange': obj.timeRange,
                'officename': obj.officename,
                'department': obj.department,
                'description': obj.description,
                'complements': [comp.complemtText for comp in WorkExperienceComplements.objects.filter(idWork_id=obj.id)]
            } for obj in WorkExperience_col1
        ],

        'workExperience_col_2': [
            {
                'timeRange': obj.timeRange,
                'officename': obj.officename,
                'department': obj.department,
                'description': obj.description,
                'complements': [comp.complemtText for comp in WorkExperienceComplements.objects.filter(idWork_id=obj.id)]
            } for obj in WorkExperience_col2
        ] if nCols else None,
        'latestWorks': [
            {
                'title': obj.workTilte,
                'description': obj.description,
                'idWK': obj.id
            } for obj in LatestWorks.objects.all()]

    }
    return render(request, 'about.html', data)


def download(request):
    with open('blog/media/cv.pdf', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/pdf")
        return response

    return response


def detail(request, idWK):
    profile = Profile.objects.get(id=1)
    choisenItem = Details.objects.get(idWK=idWK)


    data = {
        'profile': {
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'birth': profile.birth,
            'linkedin': profile.linkedin,
            'gitHub': profile.gitHub
        },
        'detail': {
            'title': choisenItem.title,
            'subtitle': choisenItem.subtitle,
            'year': choisenItem.year,
            'description': choisenItem.description
        }
    }
    return render(request, 'details.html', data)


def news(request):
    profile = Profile.objects.get(id=1)
    listTopics = []
    buscas = ['Atlassian jira', 'asana', 'gestion', 'outils+de+gestion']
    buscas = ['+'.join(i.split(' ')) for i in buscas]
    for busca in buscas:
        news = News(busca)
        news.fillTopicsNews()
        tp = News.selectTopics(news.topics, 1)[0]
        listTopics.append(tp)

    data = {
        'profile': {
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'birth': profile.birth,
            'linkedin': profile.linkedin,
            'gitHub': profile.gitHub
        },
        'topics_line1': listTopics[0:2],
        'topics_line2': listTopics[2:]
    }
    return render(request, 'news.html', data)


def createTopics(topics, group=3):
    arr = []
    size_topics = len(topics)
    start = [i for i in range(0, len(topics),group)]
    if size_topics > group:
        size_start = len(start) - 1
        for i in range(size_start):
            arr.append(topics[start[i]:start[i+1]])
        
        arr.append(topics[start[size_start-group]:])
        return arr
    else:
        return arr.append(topics)

def tools(request):
    profile = Profile.objects.get(id=1)
    tool = Tools.objects.all()
    tool_pag = Paginator(tool, 1)
    page_number = request.GET.get('page')
    page_obj = tool_pag.get_page(page_number)

    pag_now = int(page_number) if page_number != None else 1
    topics = ToolsTopics.objects.filter(idToll=tool[pag_now-1].id).order_by('id')
    arr = []
    group = 3
    size_topics = len(topics)
    start = [i for i in range(0, len(topics),group)]
    if size_topics > group:
        size_start = len(start) - 1
        for i in range(size_start):
            arr.append(topics[start[i]:start[i+1]])
        
        arr.append(topics[start[size_start-group]:])
    else:
        arr.append(topics)

    data = {
        'profile': {
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'birth': profile.birth,
            'linkedin': profile.linkedin,
            'gitHub': profile.gitHub
        },
        'page_obj': page_obj,
        'topics': arr
    }
    return render(request, 'tools.html', data)
