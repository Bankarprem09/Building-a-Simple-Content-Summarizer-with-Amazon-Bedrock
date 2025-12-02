import boto3

def get_summary(text):
    # Initialize the Bedrock client
    bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

    # Payload for Claude 3 Sonnet
    messages = [{
        "role": "user",
        "content": [{"text": f"Summarize the following text concisely:\n\n{text}"}]
    }]

    # Call the Converse API
    response = bedrock.converse(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        messages=messages,
        inferenceConfig={"maxTokens": 512, "temperature": 0.5}
    )

    return response['output']['message']['content'][0]['text']
