from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.FileField(upload_to='profile_pictures/', null=True, blank=True)
    phone_number = models.CharField(unique=True, blank=True, null=True, max_length=256)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=256, default="", blank=True)

    profile_choices = [
        ('te', 'teacher'),
        ('st', 'student'),

    ]

    type_of_profile = models.CharField(
        max_length=2,
        choices=profile_choices,
        default='st')

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Assignment(models.Model):
    title = models.CharField(max_length=256, blank=True)
    teacher = models.OneToOneField(Profile, related_name='teacher', on_delete=models.CASCADE, blank=True, null=True)
    student = models.OneToOneField(Profile, related_name='student', on_delete=models.CASCADE, blank=True, null=True)

    file_teacher = models.FileField(upload_to='assignments/', blank=True)
    file_student = models.FileField(upload_to='answers/', blank=True)


    def __str__(self):
        return self.title


class Course(models.Model):
    name = models.CharField(max_length=256)
    teacher = models.ForeignKey(Profile, related_name='course_teacher', on_delete=models.CASCADE, blank=True, null=True)
    student = models.ForeignKey(Profile, related_name='course_student', on_delete=models.CASCADE, blank=True, null=True)

    course_choices = [
        (4, 'momtaz'),
        (3, 'Awli'),
        (2, 'khosh'),
        (1, 'motevaset'),
        (0, 'test'),
    ]

    type_of_course = models.IntegerField(
        choices=course_choices,
        default=0,
    )

    def __str__(self):
        return self.name


class Ticket(models.Model):
    name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    subject = models.CharField(max_length=256, blank=True)
    website = models.CharField(max_length=256, blank=True)
    email = models.EmailField()
    text = models.CharField(max_length=256)

    ticket_choices = [
        ('co', 'course'),
        ('ge', 'general'),
        ('su', 'suport'),
    ]

    ticket_type = models.CharField(
        choices=ticket_choices,
        default=0,
        max_length=2
    )

    course_choices = [
        (5, 'none'),
        (4, 'momtaz'),
        (3, 'Awli'),
        (2, 'khosh'),
        (1, 'motevaset'),
        (0, 'test'),
    ]

    type_of_course = models.IntegerField(
        choices=course_choices,
        default=5,
    )

    def __str__(self):
        return self.text
