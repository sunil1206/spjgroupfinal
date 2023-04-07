from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect




from . models import entry

def adminpanel(request):
    entry_=entry.objects.all()
    context={
        'entry_id': entry_
    }
    return render(request,'admin.html',context)

# def detail(request, entry_id):
#     return HttpResponse('This')

def apply(request):
    if request.method=='POST':
        name=request.POST.get('name',)

        email = request.POST.get('email', )
        phone = request.POST.get('phone', )
        address = request.POST.get('address', )
        address2 = request.POST.get('address2', )
        post = request.POST.get('post', )
        aadhar_card = request.POST.get('aadhar_card', )
        ration_number = request.POST.get('ration_number', )

        if not all([name, email, phone, address, post, aadhar_card, ration_number]):
            # If any required fields are missing, render the form again with an error message
            context = {'error_message': 'Please fill out all required fields'}
            return render(request, 'apply.html', context)

            # If all required fields are present, create a new entry and save it
        apply = entry(name=name, email=email, phone=phone, address=address, address2=address2, post=post,
                      aadhar_card=aadhar_card, ration_number=ration_number)
        apply.save()
        messages.success(request, 'Your registration was successful!')
        return render(request, "apply.html", {'name':name})
    else:
        return render(request, 'apply.html')






    #     apply=entry(name=name,email=email,phone=phone,address=address,address2=address2,post=post,aadhar_card=aadhar_card,ration_number=ration_number)
    #     apply.save()
    #     return redirect('/')
    # return render(request, 'apply.html')
