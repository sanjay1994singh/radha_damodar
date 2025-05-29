from django.shortcuts import render

from seva.models import Seva

from owner.models import Owner

from service.models import Service

from bank.models import BankDetail

from darshan.models import DailyDarshan

from god.models import God

from blog.models import Blog

from pooja.models import PoojaCategory, Pooja


# Create your views here.
def homepage(request):
    daily_darshan = DailyDarshan.objects.last()
    seva = Seva.objects.all()
    owner = Owner.objects.all()
    service = Service.objects.all()
    bank = BankDetail.objects.all()
    god = God.objects.all()
    blog = Blog.objects.all()[:5]
    pooja_category = PoojaCategory.objects.all()
    pooja = Pooja.objects.all()
    context = {
        'daily_darshan': daily_darshan.img.url,
        'seva': seva,
        'owner': owner,
        'service': service,
        'bank': bank,
        'god': god,
        'blog': blog,
        'pooja_category': pooja_category,
        'pooja': pooja,
    }
    return render(request, 'index.html', context)
