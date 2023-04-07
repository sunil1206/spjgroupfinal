from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from .models import service, upcoming, about, slide, upcoming2, upcoming3, client, associate, CarouselItem, gallery,gallery_foundation


# Create your views here.
def index(request):
    obj = service.objects.all()
    upc=upcoming.objects.all()
    wid=slide.objects.all()
    upc2 = upcoming2.objects.all()
    upc3 = upcoming3.objects.all()
    client_=client.objects.all()
    ass=associate.objects.all()
    # gvdo=gallery.objects.all()
    return render(request,"index.html",{'result':obj,'result2':upc,'result3':wid,'result4':upc2,'result5':upc3,'result6':client_,'ass':ass})


def about(request):

    return render(request, "about.html")

# def activecard(request):
#
#     return render(request, "active_card.html")

def status(request):

    return render(request, "status.html")

def Associate(request):

    return render(request, "associate.html")

def services(request):
    readmore=service.objects.all()
    return render(request, "services.html",{'result':readmore})


def detail(request,service_id):
    # return HttpResponse('this is service no %s' % service_id)
    service_ = service.objects.get(id=service_id)
    return render(request, 'detail.html',{'service_':service_})

# def gallery(request):
#     carousel_items = CarouselItem.objects.all()
#     context = {'carousel_items': carousel_items}
#     return render(request, 'home/gallery.html', context=context)





def contact(request):
    if request.method == "POST":
        name= request.POST['name']
        email= request.POST['email']
        phone_number= request.POST['phone_number']
        massage= request.POST['massage']

        #send email
        send_mail(
            'Contact Form Submission',  # subject
            f'Name: {name}\nEmail: {email}\nPhone: {phone_number}\n\n{massage}',  # message
            email,  # from email
            ['spjrights@gmail.com'],  # may add more email
        )
        return render(request, "contact.html", {'name':name})
    else:
        return render(request, "contact.html", {})


from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import SubscribeForm

def subscribe(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'Code Band'
            message = 'Sending Email through Gmail'
            recipient = form.cleaned_data.get('email')
            send_mail(subject,
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('subscribe')
    return render(request, 'subscriptions/home.html', {'form': form})


def gallery_page(request):
    images = gallery.objects.all()
    images2 = gallery_foundation.objects.all()
    images3 = gallery.objects.all()
    paginator = Paginator(images, 6) # Show 12 images per page.
    paginator2 = Paginator(images2, 6)
    paginator3 = Paginator(images3, 6)
    page_number = request.GET.get('page')
    page_gallery = paginator3.get_page(page_number)
    page_foun = paginator2.get_page(page_number)
    page_obj = paginator.get_page(page_number)
    return render(request, 'gallery.html', {'page_obj': page_obj,'page_foun': page_foun,'page_gallery':page_gallery})



def g_detail(request,gallery_id):
    # return HttpResponse('this is service no %s' % service_id)
    gallery_ = gallery.objects.get(id=gallery_id)
    return render(request, 'gallery.html', {'gallery_': gallery_})

