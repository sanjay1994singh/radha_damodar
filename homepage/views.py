from django.shortcuts import render

from seva.models import Seva

from owner.models import Owner

from service.models import Service

from bank.models import BankDetail

from darshan.models import DailyDarshan

from god.models import God

from blog.models import Blog


# Create your views here.
def homepage(request):
    darshan = DailyDarshan.objects.last()
    seva = Seva.objects.all()
    owner = Owner.objects.all()
    service = Service.objects.all()
    bank = BankDetail.objects.all()
    god = God.objects.all()
    blog = Blog.objects.all()[:5]
    context = {
        'darshan': darshan.img.url,
        'seva': seva,
        'owner': owner,
        'service': service,
        'bank': bank,
        'god': god,
        'blog': blog,
    }
    return render(request, 'index.html', context)
