import datetime as dt
import os
import time
from pathlib import Path

import boto3  # type: ignore
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Let's use Amazon S3
s3 = boto3.resource("s3")
s3_bucket = os.getenv("s3_bucket")


def generate_s3_filename(local_file: Path) -> str:
    timenow = dt.datetime.now()

    # Append the time now, to make the target file unique, otherwise we risk overwriting an existing file
    hour_string = timenow.strftime("%Y%m%d_%H%M%S")
    s3_filename = local_file.stem + "_uploaded_" + hour_string + ".csv"

    return s3_filename


# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

print("Uploading temperature logs")
p = Path("./output")
for file in p.glob("*.csv"):
    with open(file, "rb") as data:
        try:
            filename = generate_s3_filename(file)
            response = s3.Bucket(s3_bucket).put_object(Key=str(filename), Body=data)
            # print(response)

            destination = Path(str(file).replace("output", "archive"))
            file.rename(destination)

        except Exception as e:
            print("Upload failed")
            print(e)

    time.sleep(1)

print("Uploading weather logs")
p = Path("./weather")
for file in p.glob("**/*.json"):
    print(file)
    with open(file, "rb") as data:
        try:
            response = s3.Bucket(s3_bucket).put_object(Key=str(file), Body=data)
            # print(response)

            destination = Path(
                "./archive/weather_" + str(file.parts[-2]) + "_" + str(file.name)
            )
            file.rename(destination)

        except Exception as e:
            print("Upload failed")
            print(e)

    time.sleep(1)
