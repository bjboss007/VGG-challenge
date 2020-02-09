import cloudinary as Cloud
import cloudinary.uploader as uploader
import cloudinary.api


Cloud.config(
    
    cloud_name= 'habib007',
    api_key= '529763968212671',
    api_secret = '31HLIveDpLlDzvRmxD-l4iWVHxE'
)

def upload_file(filename: str):
    upload_data = Cloud.uploader.upload_image(filename)
    return upload_data.url

