from django.shortcuts import render, redirect
from .models import Reservation, Table

# Create your views here.
def book_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = ReservationForm()
    return render(request, 'restaurant_booking/view_reservations.html', {'form':form})


def view_reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'restaurant_booking/view_reservations.html', {'reservations': reservations})

