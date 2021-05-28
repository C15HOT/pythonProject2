from django.http import HttpResponse
from django.shortcuts import render
from django.views import View, generic
from advertisements.models import Advertisement
#
#
def advertisement_list(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    return render(request, 'advertisements/advertisement_list.html', {'advertisements':advertisements})

def contacts(request, *args, **kwargs):
    contact = '8-800-708-19-45, email: sales@company.com'
    return render(request, 'advertisements/contacts.html', {'contact':contact})

def about(request, *args, **kwargs):
    description = 'Бесплатные объявления в вашем городе!'
    return render(request, 'advertisements/about.html', {'description':description})

class Regions(View):
    def get(self, request, *args, **kwargs):
        regions = ['Москва', 'Московская область', 'республика Алтай',' Вологодская область']
        return render(request, 'advertisements/regions.html', {'regions':regions})

    def post(self, request):
        return HttpResponse('Регион успешно создан')



class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name ='advertisement_list'
    queryset = Advertisement.objects.all()[:5]

class AdvertisementDetailView(generic.DetailView):
    model = Advertisement