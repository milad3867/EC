from django.views import View
from django.conf import settings
from django.shortcuts import render
from django.http import FileResponse
from django.views.generic.base import TemplateView
from project.apps.userManager.models import Assignment, Profile
import os


class GetVideoTemplate(TemplateView):

    template_name = 'videos.html'


class Getvideo(View):

    def get(self, request, *args, **kwargs):
        video_id = kwargs['id']

        video = open(os.path.join(settings.MEDIA_ROOT, '1.mp4'), 'rb')

        response = FileResponse(video)
        response['Accept-Ranges'] = 'bytes'

        return response


class GetAssignment(View):

    def get(self, request, *args, **kwargs):
        assignment_id = kwargs['id']
        assignment_object = Assignment.objects.get(pk=assignment_id)

        assignment = open(os.path.join(settings.MEDIA_ROOT, assignment_object.file_teacher.path), 'rb')

        response = FileResponse(assignment)
        response['Accept-Ranges'] = 'bytes'

        return response


class GetAnswer(View):

    def get(self, request, *args, **kwargs):
        assignment_id = kwargs['id']
        assignment_object = Assignment.objects.get(pk=assignment_id)

        answer = open(os.path.join(settings.MEDIA_ROOT, assignment_object.file_student.path), 'rb')

        response = FileResponse(answer)
        response['Accept-Ranges'] = 'bytes'

        return response
    
    
class GetProfilePicture(View):

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        profile = Profile.objects.get(pk=id)

        image = open(os.path.join(settings.MEDIA_ROOT, profile.image.path), 'rb')

        response = FileResponse(image)
        response['Accept-Ranges'] = 'bytes'

        return response