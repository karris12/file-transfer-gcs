# file-transfer-gcs
automated transfer of files
To automate file transfer between two Google Cloud Storage (GCS) buckets using a Cloud Function with the Python runtime, you can follow these steps:

**Enable necessary APIs:** 
Ensure that the Google Cloud Storage and Cloud Functions APIs are enabled in your Google Cloud project.

**Set up IAM permissions:**
Ensure the Cloud Function's service account has the necessary permissions to read from the source bucket (jethro123a) and write to the destination bucket (chris231b).

**Create a Cloud Function:**
Write the Python code for the Cloud Function that will be triggered by an event in the source bucket and copy the file to the destination bucket.
