import os
import uuid

# from django.utils import timezone
def isNum(data):
    try:
        int(data)
        return True
    except ValueError:
        return False
def delete_file(path):
    """ Deletes file from filesystem. """
    if os.path.isfile(path):
        os.remove(path)
def handle_uploaded_file(f,directory): 
    """ File upload for the Material """ 
    ext = f.name.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    upload_dir = 'media/'+str(directory)+'/'

    with open(upload_dir+filename, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)
    return upload_dir+filename