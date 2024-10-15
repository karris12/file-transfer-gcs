# file-transfer-gcs
automated transfer of files
To automate file transfer between two Google Cloud Storage (GCS) buckets using a Cloud Function with the Python runtime, you can follow these steps:

**Enable necessary APIs:** 
Ensure that the Google Cloud Storage and Cloud Functions APIs are enabled in your Google Cloud project.

**Set up IAM permissions:**
Ensure the Cloud Function's service account has the necessary permissions to read from the source bucket (jethro123a) and write to the destination bucket (chris231b).

**Create a Cloud Function:**
Write the Python code for the Cloud Function that will be triggered by an event in the source bucket and copy the file to the destination bucket.


**Explanation**
main.py: Contains the Python function transfer_file, which is triggered whenever a new file is finalized (uploaded) in the source bucket jethro123a.

The function uses the Google Cloud Storage client library to access the buckets and copy the file from the source bucket to the destination bucket chris231b.
requirements.txt: Specifies the google-cloud-storage dependency needed to interact with Google Cloud Storage.

gcloud functions deploy: Deploys the Cloud Function with the specified settings:

--runtime python311: Specifies the Python runtime version.
--trigger-resource jethro123a: Sets the source bucket as the trigger for the function.
--trigger-event google.storage.object.finalize: Specifies that the function should be triggered when a new file is finalized in the source bucket.
--entry-point transfer_file: Specifies the entry point for the function.
By following these steps, you will have a Cloud Function that automatically transfers files from the jethro123a bucket to the chris231b bucket whenever a new file is uploaded to the jethro123a bucket.
