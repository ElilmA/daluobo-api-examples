# 大萝卜 API：低价 AI API 中转站接入示例

> Daluobo API — low-cost OpenAI-compatible AI API relay (GPT / Claude / Gemini / DeepSeek / Grok).

![大萝卜 Logo](https://daluobo.cc.cd/daluobo-logo.png)

大萝卜 API 是一个面向个人开发者、自动化脚本用户和小团队的 OpenAI 兼容 API 中转站，覆盖 GPT / Claude / Gemini / DeepSeek / Grok / Qwen 等 30 个主流模型。注册即送体验额度，支持每日签到、邀请奖励，微信/支付宝小额充值即可长期使用。

链接：

- 官网：<https://daluobo.cc.cd>
- 新手入口：<https://daluobo.cc.cd/start>
- 模型与价格：<https://daluobo.cc.cd/pricing>
- 国际用户充值（GGsel 10 USD 兑换码）：<https://ggsel.net/catalog/product/openai-compatible-api-balance-10-usd-gpt-5-6-gpt-5-5-instant-code-102585713>

API Base URL：

```text
https://api.daluobo.cc.cd/v1
```

## 核心卖点

| 卖点 | 说明 |
| --- | --- |
| 注册送额度 | 新用户注册即得 $0.5 体验额度，先跑通接入再决定是否充值。 |
| 每日签到 | 登录后在「个人中心」签到，每天随机领取约 $0.004–$0.02 额度。 |
| 邀请奖励（限时双倍） | 好友注册并完成首次充值后，双方各得 $1；双倍活动至 10-28，之后恢复 $0.5/人。 |
| 低价调用 | 按量计费，适合日常开发、脚本自动化、小项目测试。 |
| OpenAI 兼容 | OpenAI SDK 只改 `base_url` / `baseURL`；兼容 Cherry Studio、Lobe Chat、Continue、Codex 等客户端。 |
| 多渠道充值 | 微信/支付宝小额充值（¥6.2 = $10，以站内「充值指南」为准）、GGsel 兑换码、USDT、国际卡。 |
| 用量透明 | 控制台可查看余额、令牌、调用日志和实时价格。 |

## 当前可用模型（30 个）

| 系列 | 模型 |
| --- | --- |
| GPT | `gpt-6-sol`, `gpt-6-astra`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.5` |
| Claude | `claude-opus-5-5`, `claude-opus-5`, `claude-opus-4-8`, `claude-opus-4-7`, `claude-opus-4-6`, `claude-sonnet-5`, `claude-sonnet-4-6`, `claude-haiku-4-5`, `claude-fable-5`, `claude-fable-5-1` |
| Gemini | `gemini-3.8-flash`, `gemini-3.7-flash`, `gemini-3.1-pro-preview` |
| DeepSeek | `deepseek-v4.1-flash`, `deepseek-flash` |
| Grok | `grok-4.6` |
| Qwen | `qwen3.7-plus` |
| GLM | `glm-5.3-flash` |
| Kimi | `kimi-k2.7-code`, `kimi-k2.6` |
| MiMo | `mimo-v2.6-flash`, `mimo-v2.5-pro`, `mimo-v2.5` |
| MiniMax | `minimax-m3` |
| 其他 | `codex-auto-review` |

完整列表和实时价格以 <https://daluobo.cc.cd/pricing> 为准。

## 1. 创建 API Key

1. 注册并登录：<https://daluobo.cc.cd>
2. 进入控制台的令牌管理。
3. 创建一个新的 API Key。
4. 调用时使用：

```text
Authorization: Bearer sk-你的令牌
```

不要把 API Key 提交到公开仓库，也不要把登录密码当成 API Key。

## 2. curl 跑通 Chat

```bash
curl https://api.daluobo.cc.cd/v1/chat/completions \
  -H "Authorization: Bearer sk-你的令牌" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.5",
    "messages": [
      {"role": "user", "content": "hello"}
    ]
  }'
```

## 3. Python 示例

安装依赖：

```bash
pip install openai python-dotenv
```

复制 `.env.example` 为 `.env`，填入你的 API Key：

```text
DALUOBO_API_KEY=sk-你的令牌
DALUOBO_BASE_URL=https://api.daluobo.cc.cd/v1
```

运行：

```bash
python examples/python_chat.py
```

## 4. Node.js 示例

安装依赖：

```bash
npm install
```

运行：

```bash
npm run chat
```

## 常见问题

### Base URL 应该填什么？

填：

```text
https://api.daluobo.cc.cd/v1
```

不要填主站域名，也不要漏掉 `/v1`。

### 401 Invalid token 怎么办？

通常是 API Key 复制错、缺少 `sk-` 前缀、令牌被禁用，或者把登录密码当成 API Key。重新到控制台复制完整令牌。

### 余额不足怎么办？

三种方式：

- 在「个人中心」每日签到，随机领取免费额度；
- 邀请好友注册并完成首次充值，双方各得奖励（限时双倍，详见站内公告）；
- 充值：微信/支付宝小额充值按站内「充值指南」操作；国际用户可在 GGsel 购买 10 USD 兑换码：<https://ggsel.net/catalog/product/openai-compatible-api-balance-10-usd-gpt-5-6-gpt-5-5-instant-code-102585713>。

### 模型不可用或报错怎么办？

先查看模型价格页和站内公告，再用 `gpt-5.5` 或 `deepseek-v4.1-flash` 做最小请求测试。

### 适合生产唯一依赖吗？

大萝卜当前主打低价、小额充值、开发者日常使用和小团队接入。不承诺无限稳定，不承诺无限额度，不宣传绕过限制。重要业务建议保留备用方案。

## 相关链接

- 官网：<https://daluobo.cc.cd>
- 新手入口：<https://daluobo.cc.cd/start>
- 模型价格：<https://daluobo.cc.cd/pricing>
- 控制台：<https://daluobo.cc.cd/console>
- GitHub 主仓库：<https://github.com/ElilmA/daluobo>

## 关键词

AI API, API 中转站, OpenAI API, OpenAI 兼容 API, 中转 API, 大模型 API, 低价 API, 免费 API 额度, 每日签到, 邀请奖励, 支付宝充值, DeepSeek API, Claude API, Gemini API, gpt-5.5 API, Python OpenAI SDK, Node.js OpenAI SDK, 大萝卜 API