import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse

def upload(request):
    if request.method == 'POST':
        user = request.user
        message = request.POST.get('message', '')
        file = request.FILES.get('file', None)
        
        # Handle file upload and save the message to the database
        if file:
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            uploaded_file_url = fs.url(filename)
            message_obj = Message.objects.create(user=user, content=message, file=file)
            response_data = {'message': 'Success', 'file_link': settings.MEDIA_URL + uploaded_file_url}
        else:
            message_obj = Message.objects.create(user=user, content=message)
            response_data = {'message': 'Success'}
        
        # Return the response with the readable file link
        return JsonResponse(response_data)
