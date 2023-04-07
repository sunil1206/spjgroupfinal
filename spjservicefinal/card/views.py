

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

# def entry(request):
#     if request.method == 'POST':
#         name = request.POST.get('name', )
#         gender = request.POST.get('desc', )
#         email = request.POST.get('year', )
#         address = request.FILES['img']
#         post = request.POST.get('name', )
#         aadhar_card = request.POST.get('desc', )
#         ration_card = request.POST.get('year', )
#         request = request(name=name, gender=gender, email=email, phone=phone, address=address, post=post,aadhar_card=aadhar_card,ration_number=ration_number,purpose=purpose)
#         request.save()
#         return redirect('person_add')
#     return render(request, 'persons/request.html')

from . models import entry

def admin(request):
    entry_=entry.objects.all()
    context={
        'entry_id': entry_
    }
    return render(request,'admin.html',context)
