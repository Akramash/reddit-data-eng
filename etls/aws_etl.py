import s3fs

from utils.constants import AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY, AWS_BUCKET_NAME


def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon=False,
                               key=AWS_ACCESS_KEY_ID,
                               secret=AWS_ACCESS_KEY)
        return s3
    except Exception as e:
        print(f"Failed to connect to S3: {e}")
        return None


def create_bucket_if_not_exist(s3: s3fs.S3FileSystem, bucket: str):
    try:
        if not s3.exists(bucket):
            s3.mkdir(bucket)
            print('Bucket created')
        else:
            print('Bucket already exists')
    except Exception as e:
        print(f"Failed to create bucket or bucket already exists: {e}")


def upload_to_s3(s3: s3fs.S3FileSystem, file_path: str, bucket: str, s3_file_name: str):
    if file_path is None:
        raise ValueError("file_path is None")

    try:
        s3.put(file_path, bucket + '/raw/' + s3_file_name)
        print('File uploaded to s3')
    except FileNotFoundError:
        print('The file was not found')
    except Exception as e:
        print(f"Failed to upload file to S3: {e}")


def upload_s3_pipeline(ti):
    file_path = ti.xcom_pull(task_ids='reddit_extract', key='return_value')

    if not file_path:
        raise ValueError("No file_path found from XCom. Ensure the previous task returns the correct path.")

    s3 = connect_to_s3()
    if not s3:
        raise ConnectionError("Failed to connect to S3")

    create_bucket_if_not_exist(s3, AWS_BUCKET_NAME)
    upload_to_s3(s3, file_path, AWS_BUCKET_NAME, file_path.split('/')[-1])