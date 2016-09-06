from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.conf import settings
import json


class InitSystem(View):
    def get(self, request):

        User = get_user_model()

        response_data = {
            'initialization': "",
        }

        if Site.objects.count() == 0:
        	new_site = Site.objects.create(pk=settings.SITE_ID, domain='foo.com', name='foo.com')
        	response_data['initialization'] = response_data['initialization'] + "New Site created with ID: %d." % (new_site.id)
        else:
        	response_data['initialization'] = response_data['initialization'] + "Site already created."

        if User.objects.count() > 0:
            response_data['initialization'] = response_data['initialization'] + " Admin user already initialized."
        else:
            User.objects.create_superuser('admin@example.com', 'admin')
            response_data['initialization'] = response_data['initialization'] + " Admin user initialized. email: admin@example.com  pass: admin"


        return HttpResponse(json.dumps(response_data), content_type="application/json")
