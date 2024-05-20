import json
from dataclasses import dataclass
import dt_utils

@dataclass
class Input:
    pass

@dataclass
class Output:
    message: str


def lambda_handler(event, context):
    
    message = dt_utils.hello_from_layer()

    return {
        "statusCode": 200,
        "body": json.dumps({"message": message}),
        "headers": {"Access-Control-Allow-Origin": "*"}
    }

lambda_handler(None, None)