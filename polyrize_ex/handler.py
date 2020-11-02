import json


def main(event, context):
    json_body = json.loads(event['body'])
    if('data' in json_body):
        data = ['data']
    else:
        return {
            "statusCode": 201,
            "body": "no data supplied.."
        }

    normalized = {d['name']: d[[key for key in d.keys() if 'Val' in key][0]] for d in data}

    response = {
        "statusCode": 200,
        "body": json.dumps(normalized)
    }

    return response


if __name__ == "__main__":
    main('', '')
