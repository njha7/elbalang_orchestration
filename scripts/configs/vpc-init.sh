#A script to initialize a VPC for data processing in Google Cloud Platform
#This VPC is NOT addressable from the public internet, can reach Google services internally, and features a data-processing subnet in range 10.0.0.0/24
':
Args for the script are as follows
project-name : name of the project in GCP application is running in
region: desired region of the VPC
'
#Create the VPC and assign it a /24
gcloud compute --project=$1 networks create elba --subnet-mode=custom
gcloud compute --project=$1 networks subnets create data-processing --network=elba --region=$2 --range=10.0.0.0/24 --enable-private-ip-google-access

#Firewall rule to allow internal traffic within the subnet. By default VPCs disallow this
gcloud compute --project=$2 firewall-rules create elba-allow-internal --direction=INGRESS --priority=65534 --network=elba --action=ALLOW --rules=all --source-ranges=10.0.0.0/24