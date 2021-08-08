import json

def lambda_handler(event: Dict[str, Any], context: LambdaContext) -> Dict[Str, Any]:
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        })
    }