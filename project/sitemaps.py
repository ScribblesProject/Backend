from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap
import datetime


class ViewSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""

    def __init__(self, pages):
        """
		Parameters:
		``pages``
			A list of three-tuples containing name, priority, and changefreq:

			e.g. [('website', 0.5, 'daily'), ('search', 0.5, 'never')]
		"""
        self.pages = pages

    def items(self):
        return self.pages

    def lastmod(self, obj):
        return datetime.datetime.now()

    def location(self, obj):
        return reverse(obj[0])

    def priority(self, obj):
        return obj[1]

    def changefreq(self, obj):
        return obj[2]
