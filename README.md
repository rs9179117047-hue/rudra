# AI Chatbot on AWS Lambda

Serverless LLM chatbot using AWS Lambda and Bedrock (Claude 3 Sonnet).

## Prerequisites

- AWS Account with Bedrock access
- AWS CLI configured
- SAM CLI (`pip install aws-sam-cli`)
- Python 3.11+

## Setup

### 1. Enable Bedrock in AWS Console

Go to: AWS Console → Bedrock → Model Access → Enable "Claude 3 Sonnet"

### 2. Deploy

```bash
git clone https://github.com/rs9179117047-hue/Rudra.git
cd Rudra
git checkout ai-chatbot-lambda

sam build
sam deploy --guided
```

### 3. Get Your API Endpoint

```bash
aws cloudformation describe-stacks \
  --stack-name ai-chatbot-lambda \
  --query 'Stacks[0].Outputs[0].OutputValue' \
  --output text
```

## Usage

### Send a Message

```bash
curl -X POST https://YOUR-ENDPOINT/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What is machine learning?",
    "history": []
  }'
```

### Response

```json
{
  "message": "Machine learning is...",
  "history": [...],
  "timestamp": "2024-06-08T12:34:56.789012"
}
```

### Multi-turn Conversation

```bash
curl -X POST https://YOUR-ENDPOINT/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Tell me more",
    "history": [{"role": "user", "content": "What is AI?"}, {"role": "assistant", "content": "..."}]
  }'
```

## Features

- Multi-turn conversations with context
- Powered by Claude 3 Sonnet
- Serverless (no servers to manage)
- Auto-scaling
- REST API via API Gateway

## Cleanup

```bash
sam delete --stack-name ai-chatbot-lambda
```

## Cost

- Lambda: Free tier covers 1M requests/month
- Bedrock: ~$0.003 per 1K input tokens, ~$0.015 per 1K output tokens
- API Gateway: $0.35 per million API calls
