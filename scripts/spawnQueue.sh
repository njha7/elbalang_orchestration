gcloud compute instances create workqueue \
    --image cos-stable-64-10176-62-0 \
    --image-project cos-cloud \
    --zone us-east1-b \
    --machine-type f1-micro \
    --metadata=startup-script=configs/elbaQueue.sh \
    --tags=elba