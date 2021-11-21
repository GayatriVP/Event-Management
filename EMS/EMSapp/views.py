from django.shortcuts import render
from .models import Customers, Bookings, Events
from .forms import BookEvent

# Create your views here.


def profile(request):
    # newrec = Customers(
    #     cust_id=1,
    #     name="test account",
    #     username="test",
    #     password="test@123",
    #     email="testemail@gmail.com"
    # )
    # newrec.save()
    uname = "testaccount"
    myprof = Customers.objects.get(username=uname)
    cust_id = myprof.cust_id
    bookings = Bookings.objects.filter(customer_id=cust_id)
    booked = {}
    i = 0
    for b in bookings:
        booked[i] = b
        i += 1
    res = {"profile": myprof, "bookings": booked}
    return render(request, "EMSapp/profile.html", res)


def book_event(request):
    if request.method == "POST":
        cust_id = Customers.objects.get(cust_id=1)
        event_id = Events.objects.get(event_id=1)
        form = BookEvent(request.POST)
        if form.is_valid():
            new_booking = Bookings(
                slots=form.cleaned_data['slots'],
                event_type=form.cleaned_data['event_type'],
                capacity=form.cleaned_data['capacity'],
                services=form.cleaned_data['services'],
                date=form.cleaned_data['date'],
                customer_id=cust_id,
                cust_event_id=event_id
            )
            new_booking.save()
            res = {"profile": cust_id}
            return render(request, "EMSapp/profile.html", res)

    else:
        form = BookEvent()
    return render(request, 'EMSapp/book_event.html', {'form': form})
