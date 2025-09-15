import json
import boto3
import base64

s3 = boto3.client('s3')

def serialize_lambda(event, context):
    """A function to serialize target data from S3"""

    key = event["s3_key"]
    bucket = event["s3_bucket"]

    # Download the data from s3 to /tmp/image.png
    download_path = "/tmp/image.png"
    s3.download_file(bucket, key, download_path)

    # Read the file
    with open(download_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")

    return {
        "image_data": image_data,
        "s3_bucket": bucket,
        "s3_key": key,
        "inferences": []
    }


ENDPOINT = "image-classification-2025-09-13-23-33-13-283"
runtime = boto3.client("sagemaker-runtime")

def predict_lambda(event, context):
    """Lambda to invoke SageMaker image classifier"""

    # Decode image
    image = base64.b64decode(event["image_data"])

    # Call endpoint
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType="image/png",
        Body=image
    )

    # Predictions (string → list)
    inferences = json.loads(response["Body"].read().decode("utf-8"))

    event["inferences"] = inferences
    return event


THRESHOLD = 0.93

def filter_lambda(event, context):
    """Lambda to filter predictions by confidence threshold"""

    inferences = event["inferences"]
    meets_threshold = max(inferences) >= THRESHOLD

    if not meets_threshold:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")

    return event
