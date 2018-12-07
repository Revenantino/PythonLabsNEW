from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from pharmacy.models import Medicine
from .cart import Cart
from .forms import CartAddMedicineForm


@require_POST
def CartAdd(request, medicine_id):
    cart = Cart(request)
    medicine = get_object_or_404(Medicine, id=medicine_id)
    form = CartAddMedicineForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(medicine=medicine, quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:CartDetail')


def CartRemove(request, medicine_id):
    cart = Cart(request)
    medicine = get_object_or_404(Medicine, id=medicine_id)
    cart.remove(medicine)
    return redirect('cart:CartDetail')


def CartDetail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
