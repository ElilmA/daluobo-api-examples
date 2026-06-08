# 大萝卜 API 快速开始

![大萝卜 Logo](https://daluobo.cc.cd/daluobo-logo.png)

大萝卜 API 是面向开发者和小团队的 OpenAI 兼容 API 服务，支持支付宝充值、API Key 管理、用量日志、文本模型、Responses API 和图片生成。

官网：<https://daluobo.cc.cd>

新手入口：<https://daluobo.cc.cd/start>

API Base URL：

```text
https://api.daluobo.cc.cd/v1
```

## 适合谁

- 想用 OpenAI SDK 快速跑通模型调用的开发者
- 想用支付宝小额充值测试 API 的个人和小团队
- 想在一个控制台里看清令牌、余额、调用日志和模型价格的用户
- 想统一调用文本模型和图片模型的自动化脚本用户

## 当前主推模型

| 场景 | 模型 |
| --- | --- |
| 文本和代码 | `gpt-5.5` |
| 轻量文本 | `gpt-5.4-mini` |
| 高强度代码辅助 | `gpt-5.3-codex-spark` |
| 图片生成 | `gpt-image-2` |

实际可用模型和价格以控制台为准：<https://daluobo.cc.cd/pricing>

## 订阅套餐

当前先开放低风险周重置套餐：

| 套餐 | 价格 | 周重置额度 |
| --- | ---: | ---: |
| 先试一下 | ¥1/月 | 100 配额 |
| 慢慢来嘛 | ¥6/月 | 300 配额 |
| 够用就行 | ¥15/月 | 1000 配额 |
| 每周够用 | ¥22/月 | 1500 配额 |

订阅额度按周期重置，未用完不结转。图片和高价模型请按控制台实际扣费理解。

## 1. 创建令牌

1. 注册并登录：<https://daluobo.cc.cd>
2. 进入控制台：`令牌管理`
3. 创建一个 API Key
4. 调用时使用：

```text
Authorization: Bearer sk-你的令牌
```

不要把 API Key 提交到公开仓库。

## 2. curl 跑通 Chat

```bash
curl https://api.daluobo.cc.cd/v1/chat/completions \
  -H "Authorization: Bearer sk-你的令牌" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.5",
    "messages": [
      {"role": "user", "content": "用一句话介绍大萝卜 API"}
    ]
  }'
```

## 3. Python 示例

安装依赖：

```bash
pip install openai python-dotenv
```

运行：

```bash
python examples/python_chat.py
```

## 4. Node.js 示例

安装依赖：

```bash
npm install openai dotenv
```

运行：

```bash
node examples/node_chat.mjs
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

## 常见问题

### Base URL 应该填什么？

填：

```text
https://api.daluobo.cc.cd/v1
```

不要填主站域名，也不要少写 `/v1`。

### 401 Invalid token 怎么办？

通常是令牌复制错、缺少 `sk-` 前缀、令牌被禁用，或者把登录密码当成 API Key。重新到控制台复制完整令牌。

### 余额不足怎么办？

可以到控制台充值，也可以关注红包广场活动额度。

### 模型不可用怎么办？

先查看模型价格页和公告，再换 `gpt-5.5` 做最小请求测试。

## 关键词

OpenAI API, OpenAI 兼容 API, AI API, API 中转站, 大模型 API, 支付宝充值, gpt-5.5, gpt-image-2, Responses API, Python OpenAI SDK, Node.js OpenAI SDK

