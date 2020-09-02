from s3_access import access_key, secret_access_key

import boto3
import os

client = boto3.client('s3',
                       aws_access_key_id = access_key,
                       aws_secret_access_key = secret_access_key)


for file in os.listdir():
    if '.py' in file:
        bucket_name = 'dh3h47h'
        upload_file_key = 'python/' + str(file)
        client.upload_file(file, bucket_name, upload_file_key)