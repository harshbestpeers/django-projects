from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from .models import members, user
from django.views import View

# Create your views here.


class Main(View):
    def get(self, request):
        template = loader.get_template("index.html")
        return HttpResponse(template.render())


class Edit(View):
    def post(self, request, id):
        mydata = members.objects.get(id=id)
        context = {"mydata": mydata}
        return render(request, "update.html", context)


class CurdOperation(View):
    def get(self, request):
        mydata = members.objects.all().values()
        template = loader.get_template("members.html")
        context = {"mydata": mydata}
        return HttpResponse(template.render(context, request))


class Delete(View):
    def post(self, request, id):
        mydata = members.objects.get(id=id)
        mydata.delete()

        mydata = members.objects.all().values()
        template = loader.get_template("members.html")
        context = {"mydata": mydata}
        return HttpResponse(template.render(context, request))


class Update(View):
    def post(self, request, id):
        mydata = members.objects.get(id=id)
        print(mydata)
        mydata.firstname = request.POST.get("firstname")
        mydata.lastname = request.POST.get("lastname")
        mydata.phone = request.POST.get("phone")
        mydata.joined_date = request.POST.get("date")
        mydata.save()

        mydata = members.objects.all().values()
        context = {"mydata": mydata}
        return render(request, "members.html", context)


class AddMember(View):
    def get(self, request):
        return render(request, "add_member.html")

    def post(self, request):
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        phone = request.POST.get("phone")
        joined_date = request.POST.get("date")
        mydata = members(
            firstname=firstname, lastname=lastname, phone=phone, joined_date=joined_date
        )
        mydata.save()

        mydata = members.objects.all().values()
        context = {"mydata": mydata}
        return render(request, "members.html", context)


class SignUp(View):
    def get(self, request):
        return render(request, "signin_and_signup/sign_up.html")

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 == password2 :
            userdata = user(
            name=name, email=email, password=password1)
            userdata.save()
            return render(request, "signin.html")
        else:
            messages.error(request,'password is not same')
            return render(request, "signin_and_signup/sign_up.html")


class SignIn(View):
    def get(self, request):
        return render(request, "signin_and_signup/sign_in.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user_is_valid = user.objects.filter(email=email, password=password).values()
        if len(user_is_valid) > 0:
            return render(request, "index.html")

        else:
            return render(request, "signin_and_signup/sign_in.html")
