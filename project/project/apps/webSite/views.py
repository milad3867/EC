from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login
from project.apps.userManager.models import Profile, Ticket
from django.contrib.auth.models import User
from django.shortcuts import redirect


class Index(View):
    template_name = 'Main_page.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):

        if "login" in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

            return redirect('index')

        elif "sign_up" in request.POST:
            username = request.POST['username_sign_up']
            password = request.POST['password_sign_up']
            email = request.POST['email_sign_up']
            first_name = request.POST['first_name_sign_up']
            last_name = request.POST['last_name_sign_up']
            phone_number = request.POST['phone_sign_up']

            user = User(username=username, email=email, first_name=first_name,
                        last_name=last_name)

            user.set_password(password)

            user.save()

            profile = Profile(user=user, type_of_profile="st",
                              phone_number=phone_number)

            profile.save()

            return redirect('index')

        elif "ticket" in request.POST:

            email = request.POST['ticket_email']
            text = request.POST['ticket_text']
            name = request.POST['ticket_name']
            last_name = request.POST['ticket_last_name']
            subject = request.POST['ticket_subject']

            ticket = Ticket(email=email, text=text, ticket_type="ge", name=name, last_name=last_name, subject=subject)

            ticket.save()

            return redirect('index')


class Test(View):
    template_name = 'Level_Test.html'

    def get(self, request):
        tickets = Ticket.objects.all().filter(ticket_type="co",
                                              type_of_course=0)

        tickets_count = len(tickets)

        return render(request, self.template_name,
                      {"tickets": tickets, "tickets_count": tickets_count})

    def post(self, request):

        if "ticket" in request.POST:

            email = request.POST['ticket_email']
            text = request.POST['ticket_text']
            name = request.POST['ticket_name']
            last_name = request.POST['ticket_website']

            ticket = Ticket(email=email, text=text, ticket_type="co",
                            name=name, last_name=last_name, type_of_course=0)

            ticket.save()

        return redirect('test')


class Level_Awli(View):
    template_name = 'Level_Awli.html'

    def get(self, request):
        tickets = Ticket.objects.all().filter(ticket_type="co",
                                              type_of_course=3)

        tickets_count = len(tickets)

        return render(request, self.template_name,
                      {"tickets": tickets, "tickets_count": tickets_count})

    def post(self, request):

        if "ticket" in request.POST:

            email = request.POST['ticket_email']
            text = request.POST['ticket_text']
            name = request.POST['ticket_name']
            last_name = request.POST['ticket_website']

            ticket = Ticket(email=email, text=text, ticket_type="co",
                            name=name, last_name=last_name, type_of_course=3)

            ticket.save()

        return redirect('awli')


class Level_khosh(View):
    template_name = 'Level_khosh.html'

    def get(self, request):
        tickets = Ticket.objects.all().filter(ticket_type="co",
                                              type_of_course=2)

        tickets_count = len(tickets)

        return render(request, self.template_name,
                      {"tickets": tickets, "tickets_count": tickets_count})

    def post(self, request):

        if "ticket" in request.POST:

            email = request.POST['ticket_email']
            text = request.POST['ticket_text']
            name = request.POST['ticket_name']
            last_name = request.POST['ticket_website']

            ticket = Ticket(email=email, text=text, ticket_type="co",
                            name=name, last_name=last_name, type_of_course=2)

            ticket.save()

        return redirect('khosh')


class Level_Momtaz(View):
    template_name = 'Level_Momtaz.html'

    def get(self, request):
        tickets = Ticket.objects.all().filter(ticket_type="co",
                                              type_of_course=4)

        tickets_count = len(tickets)

        return render(request, self.template_name,
                      {"tickets": tickets, "tickets_count": tickets_count})

    def post(self, request):

        if "ticket" in request.POST:

            email = request.POST['ticket_email']
            text = request.POST['ticket_text']
            name = request.POST['ticket_name']
            last_name = request.POST['ticket_website']

            ticket = Ticket(email=email, text=text, ticket_type="co",
                            name=name, last_name=last_name, type_of_course=4)

            ticket.save()

        return redirect('momtaz')


class Level_Motevasset(View):
    template_name = 'Level_Motevasset.html'

    def get(self, request):
        tickets = Ticket.objects.all().filter(ticket_type="co",
                                              type_of_course=1)

        tickets_count = len(tickets)

        return render(request, self.template_name,
                      {"tickets": tickets, "tickets_count": tickets_count})

    def post(self, request):

        if "ticket" in request.POST:

            email = request.POST['ticket_email']
            text = request.POST['ticket_text']
            name = request.POST['ticket_name']
            last_name = request.POST['ticket_website']

            ticket = Ticket(email=email, text=text, ticket_type="co",
                            name=name, last_name=last_name, type_of_course=1)

            ticket.save()

        return redirect('motevaset')
