from django.shortcuts import render
from .models import Customers, Bookings, Events
from .forms import BookEvent, EditEvent

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
    # uname = "testaccount"
    # myprof = Customers.objects.get(username=uname)
    # bookings = Bookings.objects.filter(customer_id=myprof)
    # events = Events.objects.get(event_id=1)
    # booked = {}
    # i = 0
    # for b in bookings:
    #     booked[i] = b
    #     i += 1
    # res = {"profile": myprof, "bookings": booked, "events": events}
    res = get_prof_det(1)
    return render(request, "EMSapp/profile.html", res)


def book_event(request):
    if request.method == "POST":
        cust_id = Customers.objects.get(cust_id=1)
        event_id = Events.objects.get(event_id=1)
        eve = event_id.location
        form = BookEvent(request.POST)
        if form.is_valid():
            new_booking = Bookings(
                slots=form.cleaned_data.get('slots'),
                event_type=form.cleaned_data['event_type'],
                capacity=form.cleaned_data['capacity'],
                services=form.cleaned_data.get('services'),
                location=eve,
                date=form.cleaned_data['date'],
                customer_id=cust_id,
                cust_event_id=event_id
            )
            new_booking.save()
            res = get_prof_det(1)
            return render(request, "EMSapp/profile.html", res)

    else:
        form = BookEvent()
    return render(request, 'EMSapp/book_event.html', {'form': form})


def delete_event(request, part_id=None):
    object = Bookings.objects.get(book_id=part_id)
    object.delete()
    res = get_prof_det(1)
    return render(request, "EMSapp/profile.html", res)


def get_prof_det(id):
    myprof = Customers.objects.get(cust_id=id)
    bookings = Bookings.objects.filter(
        customer_id=myprof)
    booked = {}
    i = 0
    for b in bookings:
        booked[i] = b
        i += 1
    res = {"profile": myprof, "bookings": booked}
    return res


def edit_event(request, part_id=None):
    obj = Bookings.objects.get(
        book_id=part_id)
    if request.method == "POST":
        form = EditEvent(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            res = get_prof_det(1)
            return render(request, "EMSapp/profile.html", res)

    else:
        form = EditEvent(instance=obj)
    return render(request, 'EMSapp/edit_event.html', {'form': form})
