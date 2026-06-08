import "dotenv/config";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.DALUOBO_API_KEY,
  baseURL: process.env.DALUOBO_BASE_URL || "https://api.daluobo.cc.cd/v1",
});

const response = await client.chat.completions.create({
  model: "gpt-5.5",
  messages: [
    { role: "user", content: "用一句话介绍大萝卜 API" },
  ],
});

console.log(response.choices[0].message.content);

