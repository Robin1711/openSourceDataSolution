from minio import Minio
from minio.error import S3Error

minio_host = 'localhost:9000'
minio_access_key = "minioadmin"
minio_secret_key = "minioadmin"
minio_isSecure = False

minio_client = Minio(
    endpoint=minio_host,
    access_key=minio_access_key,
    secret_key=minio_secret_key,
    secure=minio_isSecure
)

bucket_name = "my-bucket"
try:
    # Check if the bucket exists, if not, create it
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)
        print(f"Bucket '{bucket_name}' created successfully.")
except Exception as e:
    print("Error occurred during creation of bucket:", e)

try:
    if minio_client.bucket_exists(bucket_name):
        print("Bucket exists.")
except S3Error as e:
    print("Error minio opperation:", e)
