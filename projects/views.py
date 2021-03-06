from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectList = [
    {
        'id': '1',
        'title': 'commerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'portfolio Website',
        'description': 'Project build by me'
    },
    {
        'id': '3',
        'title': 'social Website',
        'description': 'open source website'
    }
]


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': projectObj, })
