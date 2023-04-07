
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PersonCreationForm
# from .models import Person, City
# #
# # def index(request):
# #     return render (request,'index.html')
#
def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # print('hiii')
            messages.success(request, 'Your registration was successful!')
            return redirect('apply.html')

    return render(request, 'persons/request.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(request, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()

            return redirect('person_change', pk=pk)
    return render(request, 'persons/request.html', {'form': form})
#
#
# AJAX
# def load_cities(request):
#     country_id = request.GET.get('country_id')
#     cities = City.objects.filter(country_id=country_id).all()
#     return render(request, 'persons/city_dropdown_list_options.html', {'cities': cities})
