from django.shortcuts import render, get_object_or_404
from .models import Medicine
from cart.forms import CartAddMedicineForm

# Create your views here.


def medicines_list(request):
    medicine_list = Medicine.objects.all()
    context = {
        'medicine_list': medicine_list,
    }
    return render(request, 'pharmacy/medicines_list.html', context)


def detail(request, medicine_id):
    medicine = get_object_or_404(Medicine, pk=medicine_id)
    return render(request, 'pharmacy/detail.html', {'medicine': medicine})


# сторінка товару
def MedicineDetail(request, id, slug):
    medicine = get_object_or_404(Medicine, id=id, slug=slug, available=True)
    cart_medicine_form = CartAddMedicineForm()
    return render('pharmacy/detail.html', {
                                  'medicine': medicine,
                                  'cart_medicine_form': cart_medicine_form
    }
    )
