import base64
from sagemaker.serializers import IdentitySerializer
from sagemaker.predictor import Predictor

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2024-05-02-16-03-16-221"

def lambda_handler(event, context):
    # Decode the image data
    image = base64.b64decode(event['image_data'])

    # Instantiate a Predictor
    predictor = Predictor(endpoint_name=ENDPOINT)

    # For this model the IdentitySerializer needs to be "image/png"
    predictor.serializer = IdentitySerializer("image/png")

    # Make a prediction:
    inferences = predictor.predict(
        image,
        {
            "ContentType": "application/x-image",
            "Accept": "application/json"
        }
    )

    # We return the data back to the Step Function
    event["inferences"] = inferences

    return {
        'statusCode': 200,
        'body': event
    }