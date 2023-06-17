import boto3

s3 = boto3.resource("s3")
s3 = boto3.client("s3")
s3.download_file(
    Bucket="landbaytechnicaltask", Key="data_task_part_1.csv", Filename="/Users/og/Documents/landbay_tech_task/data/data_task_part_1.csv"
)