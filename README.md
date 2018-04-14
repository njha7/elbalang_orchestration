# Elbalang Orchestration
Experiment data processing orchestration

This is a RESTful API to handle the processing of logs from an Elba experiment.

## Prerequisite Setup
1. [Install the Google Cloud SDK](https://cloud.google.com/sdk/downloads)
2. Create Cloud Storage Buckets

...You will need 3 buckets.
..* Input Bucket
..* Output Bucket
..* Credentials & Configs Bucket

..From the command line:..
..`gsutil mb -p [PROJECT_NAME] -c [STORAGE_CLASS] -l [BUCKET_LOCATION] gs://[BUCKET_NAME]/`..
..More info on Google's Documentation [here](https://cloud.google.com/storage/docs/).

## API Endpoints

### GET

### POST

#### Process Log

##### Endpoint
```
/process
```

##### Parameters


| Param | Description |
| ------| ----------- |
|  key  | Authentication key |
|  log  | File to process |

##### Returns