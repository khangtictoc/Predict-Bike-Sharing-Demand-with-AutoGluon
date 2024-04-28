import json
import ast 

THRESHOLD = .93


def lambda_handler(event, context):
    # Grab the inferences from the event
    inferences = event['inferences']

    inferences_lst = ast.literal_eval(inferences)

    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = True if max(inferences_lst) > THRESHOLD else False

    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': event
    }