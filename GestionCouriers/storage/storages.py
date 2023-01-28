from django.core.files.storage import FileSystemStorage
from django.db import models

fs = FileSystemStorage(location='/media/file')

class Storages(object):
    @staticmethod
    def MyLocalStorage():
        return fs
    
    @staticmethod
    def MyRemoteStorage():
        DEFAULT_FILE_STORAGE='storages.backends.s3boto3.S3Boto3Storage'
        return DEFAULT_FILE_STORAGE