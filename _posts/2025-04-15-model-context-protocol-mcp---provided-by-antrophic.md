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

⇒ 각 api마다 프로토콜을 개발해줘야했음 (예를 들어, 날씨검색을 위한 api call full pipeline을 api 제공자마다 설계해줘야 했음)

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_000.png" class="img-fluid rounded z-depth-1" %}

### MCP란?

- Model Context Protocol(MCP)은 LLM(Large Language Model) 애플리케이션과 외부 데이터 소스 및 도구들 (api call/function call) 간의 원활한 통합을 가능하게 하는 개방형 프로토콜이다.

> **Protocol:** 서로 다른 시스템 간 상호작용을 위해 정의된 규칙과 절차

⇒ api call/function call마다 개발하는걸 일종의 ‘abstraction’화 하여, LLM 사용자/개발자들에게 확장성을 키워줌

⇒ 여러 api call들을 제공하는 tool provider로 존재하는 github이 MCP server를 개발하면, LLM이 protocol에 맞게 통신만 해주면 손쉽게 api call하고 response를 받아 실행가능해짐!

- MCP 구조는 아래와 같음

  - **MCP Hosts**:
Claude Desktop, IDE 또는 AI 도구와 같이 사용자가 직접 사용하는 프로그램. MCP를 통해 데이터에 접근하고자 하는 최종 사용자 애플리케이션.

⇒ 가장 상위 레벨의 어플리케이션으로 사용자가 prompt 날리는 대상 (`Claude Desktop, Cursor`)

  - **MCP Clients**:
호스트 내부에서 서버와의 1:1 통신을 담당하는 기술적 구성요소. 프로토콜 규칙에 따라 메시지를 주고받는 통신 관리자 역할을 담당.

⇒ Host 내부에서 작동하는 구성 요소

    - 메시지 변환 및 처리

    - 프로토콜에 맞게 요청을 포맷팅

    - 서버와의 통신 관리 (연결 유지, 오류 처리 등)

  - **MCP Servers**:
특정 기능을 표준화된 Model Context Protocol을 통해 제공하는 경량 프로그램.

⇒ 각 서버는 특정 기능(`api call/function call`)이나 데이터 접근을 담당.

  - **Local Data Sources (로컬 데이터 소스)**:
사용자 컴퓨터에 있는 파일, 데이터베이스, 서비스 등으로 MCP 서버가 안전하게 접근할 수 있는 정보 저장소 (`local database`)

  - **Remote Services (원격 서비스)**:
인터넷을 통해 접근 가능한 외부 시스템(API 등)으로, MCP 서버가 연결하여 정보를 가져올 수 있는 외부 자원 (`web search results`)

  - **MCP Protocol**:
클라이언트와 서버 간의 표준화된 통신 방식으로, 데이터 형식, 요청/응답 구조, 오류 처리 등을 정의 (`pip install mcp` 로 설치되는 것)

### **MCP 통신 흐름**

1. 초기화 (Initialization)

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_001.png" class="img-fluid rounded z-depth-1" %}

  - 능력 협상 (Capability Negotiation)

  - 버전 확인

  - 서버 정보 교환

1. 일반 통신

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_002.png" class="img-fluid rounded z-depth-1" %}

  - 요청/응답 (Request/Response)

  - 알림 (Notification)

  - 에러 처리

1. 종료

  - 정상 종료

  - 에러 복구

  - 리소스 정리

- Protocol까보면 사실상 client ↔ server는 json 구조로 통신함

```json
// 기본 JSON-RPC 2.0 메시지 형식
interface JSONRPCMessage {
    jsonrpc: "2.0";
    id?: string | number;  // 요청/응답 식별자
    method?: string;       // 메서드 이름
    params?: object;       // 매개변수
    result?: object;       // 응답 결과
    error?: {
        code: number;
        message: string;
        data?: unknown;
    };
}
```

- 그렇다면 Model Context Protocol은 왜 각광을 받을까?

  - 대 AI-Agent시대에 모델만으로 구현할 수 있는 action의 정교함에는 한계가 있고, 외부 툴을 활용하는건 어느정도 필연적.

  - `**모듈성과 호환성의 압도적 향상**`

    - 프로토콜에 맞게 개발된 모든 모델과 서버/도구는 서로 쉽게 교체가 가능해짐!

(LLM / MCP server의 자유로운 플러그인 아웃)

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_003.png" class="img-fluid rounded z-depth-1" %}

    - USB 규격만 맞추면 어떤 USB 장치든 어떤 컴퓨터에도 연결할 수 있는 것처럼, Model Context Protocol을 따르는 모든 모델과 도구는 서로 원활하게 연결될 수 있음!

    - 그만큼 보안을 보다 더 신경써서 client/server side를 개발해야한다고 함.

## 2. Practical Information

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_004.png" class="img-fluid rounded z-depth-1" %}

### MCP Marketplace

→MCP client나 Server를 open src로 베포해놓는 platform

https://mcp.so/

https://smithery.ai/

### MCP Client

⇒ claude가 어떻게 MCP로 server랑 통신할 것인가, 이런거를 정의해주는 건데

(이미 cursor등등에는 알아서 잘 정의가 되어있음)

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_005.png" class="img-fluid rounded z-depth-1" %}

### MCP Servers

⇒ 여러가지 tool들을 사용하게 해놓은 Server (MCP를 따름)

https://github.com/smithery-ai/reference-servers/tree/main/src/github

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_006.png" class="img-fluid rounded z-depth-1" %}

## 3. Examples

### Cursor - Github MCP Server

1. Github Token 발급 후 각 권한들 (Tool들)에 대한 권한 부여

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_007.png" class="img-fluid rounded z-depth-1" %}

⇒ Issues & PR 권한 부여한 Token

1. 1.에서 입력한 token을 기반으로 지정해준 MCP client에서 MCP server를 사용하기 위해 추가적인 configuration을 전달

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_008.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_009.png" class="img-fluid rounded z-depth-1" %}

1. Cursor > MCP > add to MCP > github json을 추가하면 아래와 같이 MCP server가 추가됨

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_010.png" class="img-fluid rounded z-depth-1" %}

1. Cursor (AI agent)에게 Github Token의 권한 아래 있는 repo에 대해서 tool 실행 (e.g., issue를 실행해줘)를 요청하면, (1) LLM이 특정 MCP server가 필요하다고 판단 → 특정 Tool 실행이 필요하다고 판단  (2) MCP에 맞는 입력 생성

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_011.png" class="img-fluid rounded z-depth-1" %}

1. Agent를 통해 성공적으로 Tool 실행 (`Run tool`)

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_012.png" class="img-fluid rounded z-depth-1" %}

### Cursor - Personal MCP Server (MCP Market Place에 내가 원하는 MCP Server가 없는 경우)

⇒ `pip install mcp`

- 수동으로 MCP Server 생성: https://modelcontextprotocol.io/quickstart/server

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_013.png" class="img-fluid rounded z-depth-1" %}

  - FactMCP 인스턴스 생성

  - decorator를 활용해 `@mcp.tool()`을 활용해 tool 정의

  - server가 independent하게 동작하는지 확인

```json
if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
```

  - 서버의 경로를 `mcp.json` 에 추가해주면 됨

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_014.png" class="img-fluid rounded z-depth-1" %}

  - AI Agent (LLM)에게 prompt를 날리면 추가된 mcp server를 쓴다고 요청이 옴.

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_015.png" class="img-fluid rounded z-depth-1" %}

  - `Run tool` 실행하면 tool 실행하고, 그 결과를 LLM result에 통합해서 최종 chat completion을 반환

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_016.png" class="img-fluid rounded z-depth-1" %}

- LLM으로 MCP Server 생성: https://modelcontextprotocol.io/tutorials/building-mcp-with-llms

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-15-model-context-protocol-mcp---provided-by-antrophic/image_017.png" class="img-fluid rounded z-depth-1" %}

**⇒ Example**

  - **https://modelcontextprotocol.io/llms-full.txt** 사이트를 방문하여 전체 문서 내용을 복사

  - **MCP TypeScript SDK** 또는 **Python SDK 저장소**로 이동

> **SDK**:  특정 플랫폼, 프레임워크 또는 시스템을 위한 개발 도구 모음

  - README 파일과 기타 관련 문서들을 복사 (e.g., mcp-python-sdk readme)

  - 해당 문서를 이 문서들을 Claude(AI Agent)와의 대화창에 복붙

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

- 비동기 프로그래밍을 위해

- **동시성 처리**: 여러 작업을 동시에 처리할 수 있다. 한 작업이 I/O 작업(네트워크 요청, 파일 읽기 등)으로 대기하는 동안 다른 작업을 수행이 가능.

- **블로킹 방지**: 서버가 한 클라이언트 요청을 처리하느라 다른 요청을 처리하지 못하는 상황을 방지

→ 여러 클라이언트를 타고 들어오는 요청이 엄청 많을텐데 비동기 처리를 해놔야 MCP 서버가 안정적으로 돌아감

## 4. Conclusion

- MCP) 이전에 사용되던 여러 방식들에 비해 확실한 장점이 존재

  - 커스텀 API 통합 (일회성 커넥터)

    - 서비스마다 별도의 커스텀 코드나 SDK를 개발하는 방식 (AI가 Google Drive와 SQL 데이터베이스에 접근하려면 각각 다른 API와 데이터베이스 드라이버를 통합)

⇒ 제일 노동력 많음

  - 언어 모델 플러그인 (OpenAI Plugins)

    - 모델이 외부 API를 쉽게 호출할 수 있게 해주는 프레임워크

⇒ 대부분의 플러그인은 모델이 API를 호출할 형태를 만드는 방식에 초점

  - 프레임워크 기반 도구 사용 (LangChain의 Tools, Agents)

    - LLM에 "도구"를 설명하고 모델이 상황에 맞게 도구를 호출하는 방식

⇒ 개발자가 각 도구를 자신의 요구에 맞게 연결하거나 수정해야 함

→ **MCP는 모델이 직접 관련된 도구를 발견하고 사용하는 프로토콜**

→ **필요한 도구를 위해 에이전트 코드를 작성하지 않아도 모델이 MCP를 통해 해당 도구를 실시간으로 발견하고 사용 가능**

→ **MCP를 통해 data provider와 지속적인 양방향 통신이 가능**

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
