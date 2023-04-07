
from django.shortcuts import render, get_object_or_404
from .models import card

def rightcard(request):
    card_number = 191610
    if request.method == 'POST':
        card_number = request.POST.get('card_number', '')

    try:
        obj = card.objects.get(cardno=card_number)
    except card.DoesNotExist:

        obj = None
        error_message = f"Card with number {card_number} does not exist."
        return render(request, 'active_card.html', {'error_message': error_message})
    card_number_str = str(card_number)
    formatted_card_number = " ".join([card_number_str[i:i + 4] for i in range(0, len(card_number_str), 4)])
    context = {
        'obj': obj,
        'card_number': formatted_card_number,
    }

    return render(request, "active_card.html", context)





def get_card_details(request, card=None):
    if request.method == 'POST':
        card_number = request.POST.get('cardno', '')


        try:
            card = card.objects.get(card_number=card_number)
            return render(request, 'card_details.html', {'card': card})
        except card.DoesNotExist:
            error_message = f"Card with number {card_number} does not exist."
            return render(request, 'card_details.html', {'error_message': error_message})
    else:
        return render(request, 'card_details.html')

