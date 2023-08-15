import boto3
import json
secret_name = "week-1-rds"
region_name = "ap-south-1"
client=boto3.client("secretsmanager", region_name=region_name)
response=client.get_secret_value(SecretId="week-1-rds")
secret_dict=json.loads(response['SecretString'])

customhost = secret_dict['host']
customuser = secret_dict['username']
custompass = secret_dict['password']
customdb = secret_dict['dbInstanceIdentifier']
customregion = "ap-south-1"
print("customhost",secret_dict['host'])
print("customuser",secret_dict['username'])
print("custompass",secret_dict['password'])
print("customdb",secret_dict['dbInstanceIdentifier'])
customregion = "ap-south-1"
