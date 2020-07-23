from django.views import View
from .models import User, Profile, Assignment, Course, Ticket
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from .forms import LoginForm, CreateAccountForm, FileForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage


class CreateAccount(FormView):
    template_name = 'createAccount.html'
    form_class = CreateAccountForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        password2 = form.cleaned_data['password2']
        phone_number = form.cleaned_data['phone_number']

        result = User.objects.get_or_create(username=username)
        # check unique user
        # check password fields
        # check phone number unique

        user = result[0]
        user.set_password(password)
        user.save()

        result2 = Profile.objects.get_or_create(user=user,
                                                phone_number=phone_number)

        profile = result2[0]
        profile.save()

        return super().form_valid(form)


class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')


class UserPage(View):
    template_name = 'userpage.html'

    def get(self, request):
        assignments = Assignment.objects.all()
        user_assignments = []

        if request.user.profile.type_of_profile == 'st':

            for assignment in assignments:
                if assignment.student == request.user.profile:
                    user_assignments.append(assignment)

            return render(request,
                      self.template_name, {'assignments': user_assignments})

        else:

            courses = Course.objects.all().filter(teacher=request.user.profile)
            students_list = []

            for course in courses:
                students_list.append(course.student)

            for assignment in assignments:
                if assignment.teacher == request.user.profile:
                    user_assignments.append(assignment)

            return render(request,
                          self.template_name, {'assignments': user_assignments,
                                               'students': students_list})

    def post(self, request):

        if 'answer' in request.FILES:
            id = request.POST['id']
            file = request.FILES['answer']
            assignment = Assignment.objects.get(pk=id)
            assignment.file_student.save(file.name, file)

        elif "assignment" in request.FILES:
            student_id = request.POST['student_id']
            title = request.POST['a_title']
            file = request.FILES['assignment']

            student = Profile.objects.get(pk=student_id)

            assignment = Assignment(title=title, teacher=request.user.profile, student=student)
            assignment.file_teacher.save(file.name, file)
            assignment.save()

        elif "update" in request.POST:
            user = request.user
            first_name = request.POST['update_first_name']
            last_name = request.POST['update_last_name']
            email = request.POST['update_email']
            phone_number = request.POST['update_phone_number']

            if len(first_name) > 0:
                user.first_name = first_name

            if len(last_name) > 0:
                user.last_name = last_name

            if len(email) > 0:
                user.email = email
            user.save()

            profile = user.profile

            if len(phone_number) > 0:
                profile.phone_number = phone_number
            profile.save()

            if len(request.FILES) != 0:
                file = request.FILES["picture"]
                user.profile.image.save(file.name, file)

        elif "ticket" in request.POST:

            if len(request.POST['ticket_email']) > 0:
                email = request.POST['ticket_email']

            else:
                email = request.user.email

            text = request.POST['ticket_text']

            ticket = Ticket(email=email, text=text, ticket_type="su")

            ticket.save()

        return redirect('user:profile')




def Logout(request):
    logout(request)
    return redirect('index')