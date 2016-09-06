#!/usr/bin/python

from django.http import HttpResponse


def robots(request):
    return HttpResponse("User-agent: *\nAllow: /\n\nSitemap: http://www.danj.co/sitemap.xml",
                        content_type='text/plain')
