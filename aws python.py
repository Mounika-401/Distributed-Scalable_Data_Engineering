import boto3

# Create a connection to the S3 service
s3 = boto3.client('s3',
                  aws_access_key_id='ASIATCKAPLFDP6GBLUEI',
                  aws_secret_access_key='PNq4LJIQD6iivMeGS2PphtxZ/w32BULK/1WgB3I+')

# Specify the bucket name and file key (path)
bucket_name = 'influencer1234'
file_key = 's3://influencer1234/social media influencers - youtube.csv'

# Download the CSV file from S3
s3.download_file(bucket_name, file_key, 'youtube.csv')

# Now you can read the CSV file into your Python project using Pandas or other libraries
import pandas as pd

df = pd.read_csv('youtube.csv')