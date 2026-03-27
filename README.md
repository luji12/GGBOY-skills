# 动态多智能体协作系统

一个灵活的多智能体系统，总代理按需创建专业agent来完成复杂任务。

## 🆕 最新更新：专业Skills增强

系统现已装备来自GitHub高星项目的**44个专业skills**，让agent们更加专业：

### 核心能力覆盖
- **提示词工程**: Stanford DSPy、LangChain、APE自动优化
- **图像分析**: LLaVA、CLIP、ViP-LLaVA、Bagel多模态
- **多模态生成**: DALL-E、Midjourney、Sora视频生成
- **前端开发**: Vercel React最佳实践、Web设计指南
- **代码质量**: Trail of Bits安全审计、代码审查
- **架构设计**: 系统设计、微服务、云架构

### 顶级来源
- **Stanford NLP**: DSPy框架（20k+ stars）
- **OpenAI**: CLIP多模态模型
- **Vercel Labs**: React/Next.js最佳实践
- **Anthropic**: 官方文档写作技能
- **Microsoft**: 技术写作、云架构
- **Trail of Bits**: 安全审计（权威）
- **社区精选**: 代码审查、测试模式等

## 核心特性

- **🎯 智能任务分析** - 自动识别任务复杂度和所需能力
- **🔨 动态任务拆解** - 将复杂任务分解为可执行的子任务
- **🤖 按需创建Agent** - 没有合适的agent时自动创建新的专业agent
- **💬 Agent间协作** - 支持agent之间的消息传递和协作
- **📊 执行过程可视化** - 清晰的执行日志和状态报告
- **🎓 专业Skills装备** - 每个agent都装备了来自顶级来源的专业skills

## 系统架构

```
┌─────────────────────────────────────────────┐
│           MultiAgentSystem                  │
│  ┌─────────────────────────────────────┐    │
│  │         Orchestrator                │    │
│  │  - 任务分析、拆解、调度              │    │
│  │  - 动态创建Agent                     │    │
│  │  - 自动匹配专业Skills                │    │
│  └──────────────────┬──────────────────┘    │
│                     │                        │
│  ┌──────────────────▼──────────────────┐    │
│  │           AgentTeam                 │    │
│  │  - Agent生命周期管理                │    │
│  │  - 消息通信协调                     │    │
│  │  - Skills增强的System Prompt        │    │
│  └─────────────────────────────────────┘    │
└─────────────────────────────────────────────┘
```

## 内置Agent类型（已装备专业Skills）

| Agent | 能力 | 描述 | 装备Skills |
|-------|------|------|-----------|
| **提示词工程师** ⭐新增 | prompt-engineering, optimization | 专业的LLM提示词优化师 | Stanford DSPy、LangChain、APE、Chain-of-Thought |
| **图像分析专家** ⭐新增 | image-analysis, computer-vision | 计算机视觉和多模态分析专家 | LLaVA、CLIP、ViP-LLaVA、Bagel |
| **多模态创作者** ⭐新增 | multimodal, text-to-image | AI生成内容创作者 | DALL-E、Midjourney、Sora、负面提示优化 |
| 代码专家 | coding, programming, development | 软件开发工程师 | Vercel React最佳实践、Trail of Bits安全审计、代码审查、测试模式 |
| 设计专家 | design, ui, ux, visual | UI/UX设计师 | Vercel Web设计指南、前端设计、品牌指南、D3可视化 |
| 写作专家 | writing, content, documentation | 内容创作者 | Anthropic文档写作、Microsoft技术写作、学术论文写作 |
| 分析专家 | analysis, data, research | 数据分析师 | 数据分析、上下文工程、性能分析 |
| 架构专家 | architecture, system_design, planning | 系统架构师 | 系统设计、微服务模式、云架构(Azure/AWS/GCP) |

## 专业Skills库（44个skills）

### 🆕 提示词工程（5个skills）⭐新增
- **prompt-engineering-guide** - 全面提示词工程指南（dair-ai，40k+ stars）
- **dspy-framework** - 斯坦福声明式提示优化框架（20k+ stars）
- **automatic-prompt-engineer** - 自动提示工程师（APE）
- **prompt-optimization-research** - 提示词优化研究资源汇总
- **langchain-prompts** - LangChain提示模板系统（90k+ stars）

### 🆕 图像分析（6个skills）⭐新增
- **llava-vision** - 视觉指令调优框架，图像理解
- **clip-multimodal** - OpenAI CLIP图像-文本对齐
- **vision-language-prompting** - 视觉语言模型提示方法
- **vip-llava** - 视觉提示理解（矩形、箭头等）
- **bagel-multimodal** - 字节跳动统一多模态模型
- **image-evaluation** - 图像提示评估框架

### 🆕 多模态生成（3个skills）⭐新增
- **text-to-image-prompting** - DALL-E/Midjourney/Stable Diffusion提示优化
- **sora-video-generation** - OpenAI Sora视频生成指南
- **negative-prompt-optimization** - 负面提示自动优化

### 前端开发
- **vercel-react-best-practices** - React/Next.js性能优化（40+规则）
- **react-composition-patterns** - React组合模式
- **web-design-guidelines** - Web界面最佳实践（100+规则）

### 代码质量
- **code-review** - 代码审查最佳实践
- **trailofbits-security** - 安全审计（权威来源）
- **unit-test-generator** - 单元测试自动生成
- **python-testing-patterns** - Python测试模式

### 架构设计
- **system-design** - 系统设计模式
- **microservices-patterns** - 微服务架构
- **cloud-architecture** - 云架构最佳实践

### DevOps
- **docker-management** - Docker环境管理
- **kubernetes-patterns** - Kubernetes部署
- **ci-cd-pipelines** - CI/CD流水线设计

### 更多...
查看 `agent_skills_config.py` 获取完整的44个skills列表

## 使用方法

### 1. 作为命令行工具使用

```bash
# 运行演示
python multi_agent_system.py

# 执行特定任务
python multi_agent_system.py "开发一个用户登录系统"
```

### 2. 作为Python模块使用

```python
from multi_agent_system import MultiAgentSystem

# 创建系统实例
system = MultiAgentSystem()

# 执行任务
result = system.execute("开发一个博客系统")

# 查看结果
print(result['summary'])
```

### 3. 高级用法 - Agent协作

```python
# 获取两个agent进行协作对话
agents = list(system.agent_team.agents.values())
system.chat_between_agents(
    agents[0].id,
    agents[1].id,
    "讨论技术方案"
)
```

## 任务复杂度自动识别

系统会根据任务描述自动判断复杂度：

- **简单任务** - 直接执行，单agent处理
- **中等任务** - 拆分为2-3个子任务
- **复杂任务** - 完整工作流：架构 → 设计 → 开发 → 审查 → 文档

## 动态Agent创建

当遇到系统没有预定义的agent类型时，会自动创建：

```
🆕 动态创建了新agent: 安全专家 (ID: dynamic_security_20260327140001)
```

## 文件说明

- `orchestrator.py` - 总代理核心，负责任务分析和调度
- `agent_team.py` - Agent团队管理，处理通信和协作
- `multi_agent_system.py` - 主入口和高级接口

## 扩展开发

### 添加新的Agent模板

```python
from orchestrator import Orchestrator, AgentProfile

orchestrator = Orchestrator()
orchestrator.AGENT_TEMPLATES["security"] = AgentProfile(
    name="安全专家",
    capabilities=["security", "audit", "vulnerability"],
    description="安全审计专家",
    system_prompt="你是一名安全专家..."
)
```

### 自定义消息处理器

```python
from agent_team import AgentTeam, MessageType

team = AgentTeam()

def handle_collaboration(msg):
    print(f"收到协作请求: {msg.content}")

team.register_handler(MessageType.COLLABORATION, handle_collaboration)
```

## 示例输出

```
======================================================================
🚀 多智能体系统启动
======================================================================

📋 任务分析:
   复杂度: complex
   领域: coding, design, writing

🔨 任务拆解为 5 个子任务:
   1. [architecture] 需求分析和架构设计
   2. [design] 详细设计和技术方案 [依赖: task_001]
   3. [coding] 核心功能实现 [依赖: task_002]
   4. [coding] 代码审查和优化 [依赖: task_003]
   5. [writing] 编写文档和使用说明 [依赖: task_004]

👥 组建专业团队:
   ✨ 新创建: 架构专家
   ✨ 新创建: 设计专家
   ✨ 新创建: 代码专家
   ✨ 新创建: 写作专家

⚙️  开始执行...

======================================================================
✅ 任务执行完毕
======================================================================

📝 任务已完成。共协调 4 个专业agent，完成 5 个子任务。
```
