from google.cloud import storage

def transfer_file(event, context):
    source_bucket_name = 'jethro123a'
    destination_bucket_name = 'chris231b'

    # Extract the file name and other details from the event
    file_name = event['name']

    # Initialize the storage client
    storage_client = storage.Client()

    # Get the source and destination buckets
    source_bucket = storage_client.bucket(source_bucket_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    # Get the blob from the source bucket
    source_blob = source_bucket.blob(file_name)

    # Copy the blob to the destination bucket
    destination_blob = source_bucket.copy_blob(source_blob, destination_bucket, file_name)

    print(f'File {file_name} transferred from {source_bucket_name} to {destination_bucket_name}')

