from django.shortcuts import render
from EMSapp.models import Customers

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
    uname = "test"
    myprof = Customers.objects.get(username=uname)
    res = {"profile": myprof}
    return render(request, "EMSapp/profile.html", res)
