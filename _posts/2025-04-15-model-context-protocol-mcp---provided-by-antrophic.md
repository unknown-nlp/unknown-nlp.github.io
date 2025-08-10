---
categories:
- paper-reviews
date: '2025-04-15 00:00:00'
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
tags:
- language-model
- llm
- paper-review
thumbnail: assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/thumbnail.jpg
title: Model Context Protocol (MCP) - provided by Antrophic
---

**논문 정보**
- **Date**: 2025-04-15
- **Reviewer**: 준원 장

## 1. What is MCP

### MCP가 왜 필요한가?

- Agent 논문 (Self-Reflection/React)를 보면 LLM이 api call/function call을 통해 response의 정확도를 높히곤 하는데, 여러 api call/function call와 통신하는데 있어 ‘규격화된 프로토콜’이 존재하지 않았음

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_000.png" class="img-fluid rounded z-depth-1" %}

### MCP란?

- Model Context Protocol(MCP)은 LLM(Large Language Model) 애플리케이션과 외부 데이터 소스 및 도구들 (api call/function call) 간의 원활한 통합을 가능하게 하는 개방형 프로토콜이다.

⇒ api call/function call마다 개발하는걸 일종의 ‘abstraction’화 하여, LLM 사용자/개발자들에게 확장성을 키워줌

⇒ 여러 api call들을 제공하는 tool provider로 존재하는 github이 MCP server를 개발하면, LLM이 protocol에 맞게 통신만 해주면 손쉽게 api call하고 response를 받아 실행가능해짐!

- MCP 구조는 아래와 같음

### **MCP 통신 흐름**

1. 초기화 (Initialization)

1. 일반 통신

1. 종료

- Protocol까보면 사실상 client ↔ server는 json 구조로 통신함

- 그렇다면 Model Context Protocol은 왜 각광을 받을까?

## 2. Practical Information

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_001.png" class="img-fluid rounded z-depth-1" %}

### MCP Marketplace

→MCP client나 Server를 open src로 베포해놓는 platform

https://mcp.so/

https://smithery.ai/

### MCP Client

⇒ claude가 어떻게 MCP로 server랑 통신할 것인가, 이런거를 정의해주는 건데

(이미 cursor등등에는 알아서 잘 정의가 되어있음)

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_002.png" class="img-fluid rounded z-depth-1" %}

### MCP Servers

⇒ 여러가지 tool들을 사용하게 해놓은 Server (MCP를 따름)

https://github.com/smithery-ai/reference-servers/tree/main/src/github

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_003.png" class="img-fluid rounded z-depth-1" %}

## 3. Examples

### Cursor - Github MCP Server

1. Github Token 발급 후 각 권한들 (Tool들)에 대한 권한 부여

1. 1.에서 입력한 token을 기반으로 지정해준 MCP client에서 MCP server를 사용하기 위해 추가적인 configuration을 전달

1. Cursor > MCP > add to MCP > github json을 추가하면 아래와 같이 MCP server가 추가됨

1. Cursor (AI agent)에게 Github Token의 권한 아래 있는 repo에 대해서 tool 실행 (e.g., issue를 실행해줘)를 요청하면, (1) LLM이 특정 MCP server가 필요하다고 판단 → 특정 Tool 실행이 필요하다고 판단  (2) MCP에 맞는 입력 생성

1. Agent를 통해 성공적으로 Tool 실행 (`Run tool`)

### Cursor - Personal MCP Server (MCP Market Place에 내가 원하는 MCP Server가 없는 경우)

⇒ `pip install mcp`

- 수동으로 MCP Server 생성: https://modelcontextprotocol.io/quickstart/server

- LLM으로 MCP Server 생성: https://modelcontextprotocol.io/tutorials/building-mcp-with-llms

### Cursor - Client Server

```python
async def connect_to_server(self, server_script_path: str):
    """Connect to an MCP server

    Args:
        server_script_path: Path to the server script (.py or .js)
    """
    is_python = server_script_path.endswith('.py')
    is_js = server_script_path.endswith('.js')
    if not (is_python or is_js):
        raise ValueError("Server script must be a .py or .js file")

    command = "python" if is_python else "node"
    server_params = StdioServerParameters(
        command=command,
        args=[server_script_path],
        env=None
    )

    stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
    self.stdio, self.write = stdio_transport
    self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

    await self.session.initialize()

    # List available tools
    response = await self.session.list_tools()
    tools = response.tools
    print("\nConnected to server with tools:", [tool.name for tool in tools])
```

- MCP server 동작에 필요한 parameter를 준비하는 과정

- MCP server initializer

- MCP server내 tool들 load

```python
async def process_query(self, query: str) -> str:
    """Process a query using Claude and available tools"""
    messages = [
        {
            "role": "user",
            "content": query
        }
    ]

    response = await self.session.list_tools()
    available_tools = [{
        "name": tool.name,
        "description": tool.description,
        "input_schema": tool.inputSchema
    } for tool in response.tools]

    # Initial Claude API call
    response = self.anthropic.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        messages=messages,
        tools=available_tools
    )

    # Process response and handle tool calls
    final_text = []

    assistant_message_content = []
    for content in response.content:
        if content.type == 'text':
            final_text.append(content.text)
            assistant_message_content.append(content)
        elif content.type == 'tool_use':
            tool_name = content.name
            tool_args = content.input

            # Execute tool call
            result = await self.session.call_tool(tool_name, tool_args)
            final_text.append(f"[Calling tool {tool_name} with args {tool_args}]")

            assistant_message_content.append(content)
            messages.append({
                "role": "assistant",
                "content": assistant_message_content
            })
            messages.append({
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": content.id,
                        "content": result.content
                    }
                ]
            })

            # Get next response from Claude
            response = self.anthropic.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1000,
                messages=messages,
                tools=available_tools
            )

            final_text.append(response.content[0].text)

    return "\n".join(final_text)
```

⇒ tool results를 통합해 최종 chat completion를 도출

⇒ `async` 로 정의하는 이유?

## 4. Conclusion

- MCP) 이전에 사용되던 여러 방식들에 비해 확실한 장점이 존재

- MCP가 사실상 Tool Usage의 표본으로 자리 잡아 가는중

- 앞으로 단기의 미래는 MCP Server내의 필요한 모든 기능을 Tool로 때려넣고 LLM Response에 통합시키는 방향으로 발전하지 않을까?

- 하지만, 미래에는 인간이 컴퓨터와의 I/O를 키보드&모니터로만 스마트폰과의 I/O를 화면&손가락으로 하지만 그 안의 수많은 tool들을 제어할 수 있듯이.. 궁극에는 가장 상위-level의 tool들만 남고, 나머지 기능들은 현재처럼 완전 세부적으로 호출을 요구하진 않지 않을까? (여러분의 생각이 궁금합니다!)

## References

https://www.anthropic.com/news/model-context-protocol

https://modelcontextprotocol.io/introduction

https://wikidocs.net/book/17027

https://www.youtube.com/watch?v=zVSZ2gXvhVE

https://www.youtube.com/watch?v=0f3fTTXqTps

**Model Context Protocol (MCP) - provided by Antrophic**
