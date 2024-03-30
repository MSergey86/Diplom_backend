import os
from django.http import HttpResponse


from .models import File

def redirect_to_file(request, hash):
    try:
        share_link = f"{os.getenv('http://127.0.0.1:8000')}/s/{hash}"
        file_obj = File.objects.get(share_link=share_link)
        response = HttpResponse(file_obj.file)
        response['Content-Disposition'] = f'attachment; filename="{file_obj.filename}"'
        return response
    except File.DoesNotExist:
         return HttpResponse("Share link not found", status=404)