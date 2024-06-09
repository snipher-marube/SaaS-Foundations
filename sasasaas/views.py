from django.shortcuts import render

from visits.models import PageVisits

def home(request):
    queryset = PageVisits.objects.filter(path=request.path).count()
    context = {
        'queryset': queryset
    }
    PageVisits.objects.create(path=request.path)
    return render(request, 'home.html', context)