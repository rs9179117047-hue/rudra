#!/bin/bash

# Joke Generator Testing Script

ENDPOINT=${1:-"http://localhost:3000"}

echo "🎭 Testing Joke Generator API..."
echo "Endpoint: $ENDPOINT"
echo ""

# Test 1: Get Random Joke
echo "Test 1: Get Random Joke"
curl -s "$ENDPOINT/joke" | jq . || echo "Error"
echo ""

# Test 2: Get Programming Joke
echo "Test 2: Get Programming Joke"
curl -s "$ENDPOINT/joke?type=programming" | jq . || echo "Error"
echo ""

# Test 3: Get Knock-Knock Joke
echo "Test 3: Get Knock-Knock Joke"
curl -s "$ENDPOINT/joke?type=knock-knock" | jq . || echo "Error"
echo ""

# Test 4: Health Check
echo "Test 4: Health Check"
curl -s "$ENDPOINT/health" | jq . || echo "Error"
echo ""

echo "✅ Testing complete!"
