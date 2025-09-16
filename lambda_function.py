import boto3
import json

bedrock_runtime = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

def lambda_handler(event, context):
    prompt = event.get('prompt')
    prompt_config = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": prompt}]
            }
        ]
    }

    response = bedrock_runtime.invoke_model(
        body=json.dumps(prompt_config),
        modelId='anthropic.claude-3-5-sonnet-20240620-v1:0',
        accept='application/json',
        contentType='application/json'
    )

    response_body = json.loads(response.get('body').read())
    ai_response = response_body['content'][0]['text']

    print(ai_response)
