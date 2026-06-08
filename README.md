# 大萝卜 API：低价 AI API 中转站接入示例

![大萝卜 Logo](https://daluobo.cc.cd/daluobo-logo.png)

大萝卜 API 是一个面向开发者、个人用户和小团队的低价 AI API 中转站。

它支持支付宝小额充值、OpenAI 兼容接口、API Key 管理、用量日志、模型价格展示、文本模型和图片生成。你只需要把 OpenAI SDK 的 Base URL 改成大萝卜地址，就可以低成本跑通模型 API 调用。

官网：<https://daluobo.cc.cd>

新手入口：<https://daluobo.cc.cd/start>

API Base URL：

```text
https://api.daluobo.cc.cd/v1
```

## 核心卖点

| 卖点 | 说明 |
| --- | --- |
| 低价调用 | 适合日常开发、脚本、自动化、小项目测试和图片生成。 |
| 支付宝充值 | 国内用户可以小额充值，不用折腾海外卡。 |
| OpenAI 兼容 | OpenAI SDK 改 `base_url` / `baseURL` 就能接。 |
| 用量透明 | 控制台可看余额、令牌、调用日志和模型价格。 |
| 统一入口 | 文本、代码、图片生成走同一个 API Base URL。 |
| 新手友好 | curl、Python、Node.js、图片生成示例都已整理。 |

## 当前低门槛套餐

| 套餐 | 价格 | 周重置额度 | 适合 |
| --- | ---: | ---: | --- |
| 先试一下 | ¥1/月 | 100 配额 | 跑通第一次调用 |
| 慢慢来嘛 | ¥6/月 | 300 配额 | 低频测试 |
| 够用就行 | ¥15/月 | 1000 配额 | 日常轻量使用 |
| 每周够用 | ¥22/月 | 1500 配额 | 稍高频使用 |

订阅额度按周期重置，未用完不结转。真实可用模型和价格以控制台为准。

模型价格页：<https://daluobo.cc.cd/pricing>

## 适合谁

- 个人开发者
- 小团队
- 自动化脚本用户
- 图片生成用户
- 想低成本接入模型 API 的项目
- 不想折腾海外支付，只想支付宝小额测试的用户

## 当前主推模型

| 场景 | 模型 |
| --- | --- |
| 文本和代码 | `gpt-5.5` |
| 轻量文本 | `gpt-5.4-mini` |
| 高强度代码辅助 | `gpt-5.3-codex-spark` |
| 图片生成 | `gpt-image-2` |

## 1. 创建 API Key

1. 注册并登录：<https://daluobo.cc.cd>
2. 进入控制台里的令牌管理。
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

## 5. 图片生成示例

```bash
curl https://api.daluobo.cc.cd/v1/images/generations \
  -H "Authorization: Bearer sk-你的令牌" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-image-2",
    "prompt": "一个干净明亮的萝卜形状 API 控制台图标",
    "size": "1024x1024"
  }'
```

图片模型消耗通常高于普通文本模型，建议先小额测试。

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

可以到控制台支付宝充值，也可以关注红包广场活动额度。

### 模型不可用怎么办？

先查看模型价格页和公告，再用 `gpt-5.5` 做最小请求测试。

### 适合生产唯一依赖吗？

大萝卜当前主打低价、小额测试、开发者日常使用和小团队接入。不承诺无限稳定，不承诺无限额度，不宣传绕过限制。重要业务建议保留备用方案。

## 关键词

AI API, API 中转站, OpenAI API, OpenAI 兼容 API, 大模型 API, 低价 API, 支付宝充值, Python OpenAI SDK, Node.js OpenAI SDK, gpt-image-2, 大萝卜 API

