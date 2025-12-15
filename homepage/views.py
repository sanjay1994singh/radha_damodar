from django.shortcuts import render

from seva.models import Seva

from owner.models import Owner

from service.models import Service

from bank.models import BankDetail

from darshan.models import DailyDarshan

from god.models import God

from blog.models import Blog

from pooja.models import PoojaCategory, Pooja
from django.shortcuts import render, get_object_or_404

from patrika.models import Patrika


# Create your views here.
def homepage(request):
    daily_darshan = DailyDarshan.objects.last()
    if daily_darshan:
        daily_darshan = daily_darshan.img.url
    else:
        daily_darshan = ''
    seva = Seva.objects.all()
    owner = Owner.objects.all()
    service = Service.objects.all()
    bank = BankDetail.objects.all()
    god = God.objects.all()
    blog = Blog.objects.all()[:5]
    pooja_category = PoojaCategory.objects.all()
    pooja = Pooja.objects.all()
    context = {
        'daily_darshan': daily_darshan,
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


def history(request):
    return render(request, 'history.html')


def patrika(request):
    selected_date = request.GET.get("date")

    if selected_date:
        latest_pdf = Patrika.objects.filter(
            uploaded_at__date=selected_date
        ).first()
        patrika = Patrika.objects.get(id=latest_pdf.id)
        absolute_image_url = request.build_absolute_uri(latest_pdf.featured_image.url)
    else:
        latest_pdf = Patrika.objects.last()
        patrika = Patrika.objects.get(id=latest_pdf.id)
        absolute_image_url = request.build_absolute_uri(latest_pdf.featured_image.url)
    context = {
        'pdf': latest_pdf,
        'patrika': patrika,
        'absolute_image_url': absolute_image_url,
    }
    return render(request, 'patrika.html', context)


def samadhis(request):
    return render(request, 'samadhis.html')


def biographies(request):
    return render(request, 'biographies.html')


def gaushala(request):
    return render(request, 'gaushala.html')


def deities(request, id):
    god = get_object_or_404(God, id=id)
    paragraphs = god.desc.split('\n\n') if god.desc else []
    context = {
        'god': god,
        'paragraphs': paragraphs
    }
    return render(request, 'deities.html', context)
