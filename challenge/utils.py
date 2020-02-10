import cloudinary as Cloud
import cloudinary.uploader as uploader
import cloudinary.api
import os


Cloud.config(
    
    cloud_name= os.environ.get('CLOUD_NAME'),
    api_key= os.environ.get('API_KEY')
    api_secret = os.environ.get('API_SECRET')
)

def upload_file(filename: str):
    upload_data = Cloud.uploader.upload_image(filename)
    return upload_data.url

