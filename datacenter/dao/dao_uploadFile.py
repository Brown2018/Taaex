from django.conf import settings
from random import randint
import os

from PIL import Image
import io
from pathlib import Path
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile
import boto3
from botocore.exceptions import NoCredentialsError
#-------------- TIME --------------------------------#
import datetime


class dao_uploadfile(object):
    @staticmethod
    def returnfilepath(data,username,dossier):
        try:

            jour=datetime.datetime.now()
            #ou doit loger le media uploadé
            #media_dir = settings.MEDIA_ROOT
            media_dir=str(dossier)
            #media_dir='media'
            randomId = randint(0, 9999)
            if data:
                account_file_dir = ''+ str(jour.date()) +'/'
                media_dir =media_dir + '/' + account_file_dir
                save_path =os.path.join(media_dir, str(username) + str(randomId) + str(data.name))
                if default_storage.exists(save_path):
                    default_storage.delete(save_path)
                    raise Exception

                #Saving
                default_storage.save(save_path, data)
                #to save a image
                """save_path_to_bucket="https://tklogiciel001.s3-us-west-1.amazonaws.com/"+save_path"""
                #to resize an image by a template
                """ save_path="https://d10n5le1cffas0.cloudfront.net/fit-in/400x400/"+save_path"""

            return save_path #save_path_to_bucket,save_path_to_bucket
        except Exception as e:
            print('Erreur Creating pathfile')
            print(e)
            return None
