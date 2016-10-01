import json
from django.http import HttpResponse
from api.models.asset import Asset, Category, Type, Location
from dispatcher import ViewRequestDispatcher
from geoposition import Geoposition
from api.common.errors import InvalidFieldException

class TypeList(ViewRequestDispatcher):
    def get(self, request):
    	""" List of Asset-Type.

        Endpoint:       /api/asset/type/list/
        HTTP method:    GET
        HTTP headers:   <none>
        Query string:   <none>
        Request body:   <none>

        Response:
        {
            "types": [{
                'id':              Integer
                'name':            String
                'category-id':     Integer
                'category-name':   String
            }, ...]
        }
        """
        result = {
            'types': [],
        }

        # Get assets from database
        objects = Type.objects.all()

        # Parse assets into result
        for obj in objects:
            # Compile info and append
            asset = {
            	'id': obj.id,
            	'name': obj.name,
                'category-id': obj.category.id,
                'category-name': obj.category.name,
            }

            result['types'].append(asset)

        return HttpResponse(self.json_dump(request, result), content_type="application/json")

class NestedTypeList(ViewRequestDispatcher):
    def get(self, request, category_id):
        """ List of Asset-Type.

        Endpoint:       /api/asset/type/list/<category_id>/
        HTTP method:    GET
        HTTP headers:   <none>
        Query string:   <none>
        Request body:   <none>

        Response:
        {
            "types": [{
                'id':              Integer
                'name':            String
                'category-id':     Integer
                'category-name':   String
            }, ...]
        }
        """

        result = {
            'types': [],
        }

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return HttpResponse(self.json_dump(request, result), content_type="application/json")

        # Get assets from database
        objects = Type.objects.filter(category=category)

        # Parse assets into result
        for obj in objects:
            # Compile info and append
            asset = {
                'id': obj.id,
                'name': obj.name,
                'category-id': obj.category.id,
                'category-name': obj.category.name,
            }

            result['types'].append(asset)

        return HttpResponse(self.json_dump(request, result), content_type="application/json")

