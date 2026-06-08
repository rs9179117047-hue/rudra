import json
import boto3
import logging
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

bedrock_runtime = boto3.client("bedrock-runtime", region_name="us-east-1")

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}")) if isinstance(event.get("body"), str) else event.get("body", {})
        user_message = body.get("message", "").strip()
        conversation_history = body.get("history", [])
        
        if not user_message:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Message cannot be empty"})
            }
        
        conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        response = bedrock_runtime.invoke_model(
            modelId="anthropic.claude-3-sonnet-20240229-v1:0",
            contentType="application/json",
            accept="application/json",
            body=json.dumps({
                "anthropic_version": "bedrock-2023-06-01",
                "max_tokens": 1024,
                "messages": conversation_history
            })
        )
        
        response_body = json.loads(response.get("body").read())
        assistant_message = response_body["content"][0]["text"]
        
        conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "message": assistant_message,
                "history": conversation_history[-6:],
                "timestamp": datetime.utcnow().isoformat()
            })
        }
        
    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=True)
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal server error"})
        }
