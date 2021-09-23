import boto3
from sagemaker import get_execution_role

def get_remote_s3_files(remote_file_location, dest_location):


    '''
    
    This function get the dataset, files, compressions from given remote_file_location
    and it saved on given UNIX/WIN valid dest_location

    >> get_remote_s3_files('s3://aws/location','/User/downloads')
    
    
    '''

    remote_file='adl-ai-summit-2021-prehackathon.zip'
    dest_file='/home/ec2-user/SageMaker/output.zip'

    s3=boto3.resource('s3')
    s3.Bucket(s3_bucket).download_file(remote_file, dest_file)
    print('file downloaded .: '+dest_file)
