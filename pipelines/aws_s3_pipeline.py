from etls.aws_etl import connect_to_s3,create_bucket_if_not_exist,upload_to_s3
from utils.constants import AWS_BUCKET_NAME

def upload_s3_pipeline(ti):
    file_path = ti.xcom_pull(task_ids='reddit_extract', key='return_value')

    if not file_path:
        raise ValueError("No file_path found from XCom. Ensure the previous task returns the correct path.")

    s3 = connect_to_s3()
    if not s3:
        raise ConnectionError("Failed to connect to S3")

    create_bucket_if_not_exist(s3, AWS_BUCKET_NAME)
    upload_to_s3(s3, file_path, AWS_BUCKET_NAME, file_path.split('/')[-1])