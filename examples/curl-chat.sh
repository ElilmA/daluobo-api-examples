curl https://api.daluobo.cc.cd/v1/chat/completions \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.5",
    "messages": [
      {"role": "user", "content": "用一句话介绍大萝卜 API"}
    ]
  }'

