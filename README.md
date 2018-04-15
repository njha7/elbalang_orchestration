# Elbalang Orchestration
Experiment data processing orchestration

This is a pipline to handle the processing of logs from an Elba experiment.

## Pipeline Deployment
1. [Install the Google Cloud SDK](https://cloud.google.com/sdk/downloads)
2. Create a project in GCP (referred to as [PROJECT])
2. Create Cloud Storage Buckets  
  You will need 3 buckets:  
    * Input Bucket (referred to as [INPUT_BUCKET])
    * Output Bucket (referred to as [OUTPUT_BUCKET])
    * Credentials & Configs Bucket (referred to as [CONFIG_BUCKET])

  From the command line:  
  `gsutil mb -p [PROJECT_NAME] -c [STORAGE_CLASS] -l [BUCKET_LOCATION] gs://[BUCKET_NAME]/`

  More info on Google's Documentation [here](https://cloud.google.com/storage/docs/).

3. Build the Elba-api container and upload to Google Container Registry:  
    * Unzip the log-file-analyzer to `infrastructure/flask/src/elbalang`
    * [Make a service account for Cloud Storage](https://cloud.google.com/storage/docs/access-control/using-iam-permissions) and download the credentials JSON to `infrastructure/flask/src` (creds.json)
    * Make the following modifications to the Dockerfile:  
      * Change `INPUT_BUCKET` value to `[INPUT_BUCKET]`
      * Change `INPUT_BUCKET` value to `[INPUT_BUCKET]`
      * Change `GOOGLE_APPLICATION_CREDENTIALS` value to `/src/creds.json`
    * From `infrastructure/flask` run `docker build -t us.grc.io/[PROJECT]/elba-applet:latest`
    * `docker push us.grc.io/[PROJECT_NAME]/elba-applet:latest`
4. [Create a GCP Kubernetes cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-container-cluster)
5. [Deploy a workload consisting of the container from step 3 to said cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/stateless-apps)
6. [Expose the application to external traffic](https://cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps)  
    * You will want to set up the port mapping from 80 on the outside to 5000 inside
7. Note the external IP address the cluster's loadbalancer receives
8. Configure the Cloud Function environment before deployment  
    * In `infrastructure/cloud_functions` create a file `.env`
    * Set the value of `ELBA_API_ENDPOINT` to `http://$K8s-IP-addr/process`
9. From `infrastructure/cloud_functions` run `gcloud beta functions deploy postLog --trigger-resource [INPUT_BUCKET] --trigger-event google.storage.object.finalize --stage-bucket [CONFIG_BUCKET]`

All set! Any files you upload to [INPUT_BUCKET] will be processed and automatically deposited with the same key in [OUTPUT_BUCKET]
