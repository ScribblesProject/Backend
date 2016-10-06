from django.http import HttpResponse
from dispatcher import ViewRequestDispatcher
from api.models.asset import Asset, MediaImage, MediaVoiceMemo
import sys
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from api.common.errors import InvalidRequestException
import time

class ImageUpload(ViewRequestDispatcher):
    def content_type_extention(self, content_type):
        if content_type == "image/png":
            return "png"
        if content_type == "image/gif":
            return "gif"
        if content_type == "image/jpeg":
            return "jpg"
        if content_type == "image/bmp":
            return "bmp"
        return ""


    def post(self, request, asset_id):

        asset = Asset.objects.get(id=asset_id)
        response_data = {
            'status': "success"
        }

        # grab the headers
        try:
            content_type = request.META["CONTENT_TYPE"].split(';')[0]
            size = int(request.META["CONTENT_LENGTH"])
        except:
            raise InvalidRequestException('missing headers')

        # determine file extension
        extension = self.content_type_extention(content_type)
        if len(extension) == 0:
            raise InvalidRequestException('content-type invalid')

        # create temp file
        timestamp = int(time.time())
        filename = "image-%d.%s" % (timestamp, extension)
        upload_file = SimpleUploadedFile(filename, request.body, content_type=content_type)

        # attach to model & save
        try:
            current_media = MediaImage.objects.get(asset=asset)
            current_media.image = upload_file
            current_media.save()
        except MediaImage.DoesNotExist:
            current_media = MediaImage.objects.create(asset=asset)
            current_media.image = upload_file
            current_media.save()
        except Exception as error:
            response_data['status'] = "failed"
            response_data['description'] = repr(error)
        except:
            response_data['status'] = "failed"

        return HttpResponse(self.json_dump(request, response_data), content_type="application/json")


class VoiceUpload(ViewRequestDispatcher):
    def content_type_extention(self, content_type):
        if content_type == "audio/aac":
            return "aac"
        if content_type == "audio/wav" :
            return "wav"
        if content_type == "audio/m4a":
            return "m4a"
        if content_type == "audio/mp3":
            return "mp3"
        return ""

    def post(self, request, asset_id):
        asset = Asset.objects.get(id=asset_id)
        response_data = {
            'status': "success"
        }

        # grab the headers
        try:
            content_type = request.META["CONTENT_TYPE"].split(';')[0]
            size = int(request.META["CONTENT_LENGTH"])
        except:
            raise InvalidRequestException('missing headers')

        # determine file extension to use
        extension = self.content_type_extention(content_type)
        if len(extension) == 0:
            raise InvalidRequestException('content-type invalid')

        # create temp file
        timestamp = int(time.time())
        filename = "voice-%d.%s" % (timestamp, extension)
        upload_file = SimpleUploadedFile(filename, request.body, content_type=content_type)

        # attach to model & save
        try:
            current_media = MediaVoiceMemo.objects.get(asset=asset)
            current_media.voice_memo = upload_file
            current_media.save()
        except MediaVoiceMemo.DoesNotExist:
            current_media = MediaVoiceMemo.objects.create(asset=asset)
            current_media.voice_memo = upload_file
            current_media.save()
        except:
            response_data['status'] = "failed"

        return HttpResponse(self.json_dump(request, response_data), content_type="application/json")
