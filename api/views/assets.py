import json
from django.http import HttpResponse
from api.models.asset import Asset, Category, MediaImage, MediaVoiceMemo, Type, Location
from dispatcher import ViewRequestDispatcher
from geoposition import Geoposition
from api.common.errors import InvalidFieldException

"""
NOTES: 

ViewRequestDispatcher - what all requests inherit from
  It catches all exceptions, formulates an error as defined in common/errors.py
  and then displays a consistant error message

@verify_token - decorates all requests
  It calls out to decorators/verify_token.py to validate the token supplied in
  the request headers
"""


def assemble_asset_info(asset_obj):
    result = {
        'id': asset_obj.id,
        'name': asset_obj.name,
        'description': asset_obj.description,
        'category': asset_obj.category.name,
        'category-description': asset_obj.category.description,
        'asset-type': asset_obj.asset_type.name,
        'locations':{},
        'media-image-url': "",
        'media-voice-url': "",
    }

    # Get asset location
    locations = Location.objects.filter(asset=asset_obj)
    for loc in locations:
        newLocation = {}
        newLocation['latitude'] = float(loc.position.latitude)
        newLocation['longitude'] = float(loc.position.longitude)
        orderStr = "%d" % (int(loc.order))
        result['locations'][orderStr] = newLocation

    # Get asset media
    mediaImages = MediaImage.objects.filter(asset=asset_obj)
    if len(mediaImages) > 0:
        if mediaImages[0].image:
            result['media-image-url'] = mediaImages[0].image.url

    mediaMemos = MediaVoiceMemo.objects.filter(asset=asset_obj)
    if len(mediaMemos) > 0:
        if mediaMemos[0].voice_memo:
            result['media-voice-url'] = mediaMemos[0].voice_memo.url

    return result


class AssetList(ViewRequestDispatcher):
    def get(self, request):
        """Fetch list of assets.

        Endpoint:       /api/asset/list/
        HTTP method:    GET
        HTTP headers:   <none>
        Query string:   <none>
        Request body:   <none>

        Response:
        {
            "assets": [{
                'id':              Integer
                'name':            String
                'description':     String
                'category':        String
                'asset-type':      String
                'media-image-url': String
                'media-voice-url': String
                'locations': { 
                    '0': {
                        'latitude':             Double
                        'longitude':            Double
                    }
                    '1': ...
                    '2': ...
                }
            }, ...]
        }
        """
        result = {
            'assets': [],
        }

        # Get assets from database
        objects = Asset.objects.all()

        # Parse assets into result
        for obj in objects:
            # Compile info and append
            result['assets'].append(assemble_asset_info(obj))

        return HttpResponse(self.json_dump(request, result), content_type="application/json")


class AssetFetch(ViewRequestDispatcher):
    def get(self, request, asset_id):
        """Fetch asset information.

        Endpoint:       /api/asset/<asset_id>/
        HTTP method:    GET
        HTTP headers:   <none>
        Query string:   <none>
        Request body:   <none>

        Response:
        {
            'id':              Integer
            'name':            String
            'description':     String
            'category':        String
            'asset-type':      String
            'media-image-url': String
            'media-voice-url': String
            'locations': {
                '0': {
                    'latitude':             Double
                    'longitude':            Double
                }
                '1': ...
                '2': ...
            }
        }
        """
        # Fetch asset object
        asset_obj = Asset.objects.get(id=asset_id)

        # Compile asset info
        result = assemble_asset_info(asset_obj)

        return HttpResponse(self.json_dump(request, result), content_type="application/json")


class AssetDelete(ViewRequestDispatcher):
    def delete(self, request, asset_id):
        """Delete an asset.

        Endpoint:       /api/asset/delete/<asset_id>/
        HTTP method:    DELETE
        HTTP headers:   <none>
        Query string:   <none>
        Request body:   <none>

        Response:
        {
            'success': Boolean
        }
        """

        result = {'success': True}
        try:
            Asset.objects.get(id=asset_id).delete()
        except:
            result['success'] = False            

        return HttpResponse(self.json_dump(request, result), content_type="application/json")


class AssetUpdate(ViewRequestDispatcher):
    def put(self, request, asset_id):
        """Update an asset

        Endpoint:       /api/asset/update/<asset_id>/
        HTTP method:    PUT
        HTTP headers:   <none>
        Query string:   <none>

        # all fields must be present
        Request body: {
            'name':                 String
            'description':          String
            'category-name':        String  # If category doesnt exist, it will be created
            'category-description': String
            'type-name':            string  # If type doesnt exist, it will be created
            'locations': {
                '0': {
                    'latitude':             Double
                    'longitude':            Double
                }
                '1': ...
                '2': ...
            }
        }

        Response:
        {
            'success': Boolean
        }
        """

        asset_obj = Asset.objects.get(id=asset_id)

        data = json.loads(request.body)
        try:
            name = data['name']
            description = data['description']
            categ = data['category']
            categ_description = data['categ_description']
            asset_t = data['asset-type']
            locations = data['locations']

            # verify location array inputs
            for order in locations.keys():
                latitude = locations[order]['latitude']
                longitude = locations[order]['longitude']      
        except KeyError:
            raise InvalidFieldException('Body not formatted correctly')

        asset_obj.name = name
        asset_obj.description = description

        # Update Positions
        for order in locations.keys():
            latitude = locations[order]['latitude']
            longitude = locations[order]['longitude'] 
            try:
                asset_location = Location.objects.get(order=int(order), asset=asset_obj)
                asset_location.position.longitude = longitude
                asset_location.position.latitude = latitude
                asset_location.save()
            except Location.DoesNotExist:
                new_location = Location.objects.create(order=int(order), position=Geoposition(latitude, longitude), asset=asset_obj)
                new_location.save()

        # Update Category
        if asset_obj.category.name == categ:
            asset_obj.category.description = categ_description
        else:
            try:
                # If exists, replace and update
                new_categ = Category.objects.get(name=categ)
                new_categ.description = categ_description
                new_categ.save()
                asset_obj.category = new_categ
            except Category.DoesNotExist:
                # If D.N.E, create and replace
                new_categ = Category.objects.get(name=categ, description=categ_description)
                new_categ.save()
                asset_obj.category = new_categ

        # Update AssetType
        if not asset_obj.asset_type.name == asset_t:
            try:
                # If exists, update and replace
                new_type = Type.objects.get(name=asset_t)
                new_type.save()
                asset_obj.asset_type = new_type
            except Type.DoesNotExist:
                # If D.N.E, create and replace
                new_type = Type.objects.get(name=asset_t)
                new_type.save()
                asset_obj.asset_type = new_type

        asset_obj.save()

        return HttpResponse(self.json_dump(request, {'success': True}), content_type="application/json")


class AssetCreate(ViewRequestDispatcher):
    def post(self, request):
        """Create an asset

        Endpoint:       /api/asset/create/
        HTTP method:    POST
        HTTP headers:   <none>
        Query string:   <none>

        # all fields must be present
        Request body: {
            'name':                 String
            'description':          String
            'category':             String  # If category doesnt exist, it will be created
            'category-description': String
            'type-name':            string  # If type doesnt exist, it will be created
            'locations': {
                '0': {
                    'latitude':             Double
                    'longitude':            Double
                }
                '1': ...
                '2': ...
            }
        }

        Response:
        {
            'id': Int
            'success': Boolean
        }
        """

        try:
            data = json.loads(request.body)
            name = data['name']
            categ = data['category']
            categ_description = data['category-description']
            asset_t = data['type-name']
            locations = data['locations']

            print('FOUND LOCATION!!!!!! ', locations)

            # verify location array inputs
            for order in locations.keys():
                latitude = locations[order]['latitude']
                longitude = locations[order]['longitude']

        except KeyError:
            raise InvalidFieldException('Body not formatted correctly')

        description = data.get('description')
        if description == None:
            description = ""


        result = {'success': True}

        # AssetCategory
        try:
            # If exists, replace and update
            new_categ = Category.objects.get(name=categ)
            new_categ.description = categ_description
            new_categ.save()
        except Category.DoesNotExist:
            # If D.N.E, create and replace
            new_categ = Category.objects.create(name=categ, description=categ_description)
            new_categ.save()

        # AssetType
        try:
            # If exists, update and replace
            new_type = Type.objects.get(name=asset_t)
            new_type.save()
        except Type.DoesNotExist:
            # If D.N.E, create and replace
            new_type = Type.objects.create(name=asset_t)
            new_type.save()

        new_asset = Asset.objects.create(name=name, description=description, category=new_categ, asset_type=new_type)
        new_asset.save()
        result['id'] = new_asset.id

        # Add locations
        for order in locations.keys():
            latitude = locations[order]['latitude']
            longitude = locations[order]['longitude']

            new_location = Location.objects.create(order=int(order),position=Geoposition(latitude, longitude), asset=new_asset)
            new_location.save()

        return HttpResponse(self.json_dump(request, result), content_type="application/json")




