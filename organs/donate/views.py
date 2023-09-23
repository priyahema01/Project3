from django.shortcuts import render
from .models import register


# Create your views here.
def registerpage(request):
    if request.method == 'POST':
        getfirstname = request.POST.get('firstname')
        getlastname = request.POST.get('lastname')
        getfathername = request.POST.get('fathername')
        getaddress = request.POST.get('address')
        getcontact = request.POST.get('contact')
        getmailid = request.POST.get('mailid')
        getage = request.POST.get('age')
        getdob = request.POST.get('dob')
        getdate = request.POST.get('date')
        getbloodgroup = request.POST.get('bloodgroup')
        getgender = request.POST.get('gender')
        users = register()
        users.FirstName = getfirstname
        users.LastName = getlastname
        users.FatherName = getfathername
        users.Address = getaddress
        users.Contact = getcontact
        users.MailId = getmailid
        users.Age = getage
        users.DOB = getdob
        users.BloodGroup = getbloodgroup
        users.Age = getage
        users.Gender = getgender
        users.save()
    return render(request, 'register.html')