---
name: multi-agent-orchestrator
description: 动态多智能体协作系统 - 智能任务分析、自动Agent调度、专业Skills装备
category: architecture
version: 1.0.0
author: Multi-Agent System
tags: [multi-agent, orchestration, collaboration, ai-system]
---

# 动态多智能体协作系统

一个灵活的多智能体系统，能够智能分析任务、自动拆解子任务、按需创建专业Agent，并协调Agent间协作完成任务。

## 核心能力

- **🎯 智能任务分析** - 自动识别任务复杂度和所需能力
- **🔨 动态任务拆解** - 将复杂任务分解为可执行的子任务
- **🤖 按需创建Agent** - 没有合适的Agent时自动创建新的专业Agent
- **💬 Agent间协作** - 支持Agent之间的消息传递和协作
- **🎓 专业Skills装备** - 44个来自GitHub高星项目的专业Skills

## 使用方法

### 方式1: 直接执行Python脚本

```bash
# 运行演示
python multi_agent_system.py

# 执行特定任务
python multi_agent_system.py "开发一个用户登录系统"
```

### 方式2: 作为Python模块导入

```python
from multi_agent_system import MultiAgentSystem

# 创建系统实例
system = MultiAgentSystem()

# 执行任务
result = system.execute("你的任务描述")

# 查看结果
print(result['summary'])
print(f"完成度: {result['subtasks_completed']}/{result['subtasks_total']}")
print(f"参与Agent: {', '.join(result['agents_involved'])}")
```

### 方式3: 高级用法 - Agent协作

```python
# 获取Agent进行协作对话
agents = list(system.agent_team.agents.values())
system.chat_between_agents(
    agents[0].id,
    agents[1].id,
    "讨论技术方案"
)

# 查看系统信息
system.print_system_info()
```

## 内置Agent类型（11种）

| Agent | 能力 | 装备Skills |
|-------|------|-----------|
| 提示词工程师 | prompt-engineering | Stanford DSPy、LangChain、APE |
| 图像分析专家 | image-analysis | LLaVA、CLIP、ViP-LLaVA |
| 多模态创作者 | multimodal | DALL-E、Midjourney、Sora |
| 代码专家 | coding | Vercel React、Trail of Bits安全 |
| 设计专家 | design | Vercel Web Design、品牌指南 |
| 写作专家 | writing | Anthropic文档、Microsoft技术写作 |
| 分析专家 | analysis | 数据分析、上下文工程 |
| 架构专家 | architecture | 系统设计、微服务、云架构 |
| DevOps专家 | devops | Docker、Kubernetes、CI/CD |
| 安全专家 | security | Trail of Bits安全审计 |
| 移动端专家 | mobile | React Native |

## 专业Skills库（44个）

### 提示词工程
- prompt-engineering-guide (dair-ai, 40k+ ⭐)
- dspy-framework (Stanford NLP, 20k+ ⭐)
- automatic-prompt-engineer (APE)
- prompt-optimization-research
- langchain-prompts (90k+ ⭐)

### 图像分析
- llava-vision、clip-multimodal (OpenAI)
- vision-language-prompting
- vip-llava、bagel-multimodal (ByteDance)
- image-evaluation (Microsoft)

### 多模态生成
- text-to-image-prompting
- sora-video-generation (OpenAI)
- negative-prompt-optimization

### 更多...
详见 `agent_skills_config.py`

## 系统架构

```
用户任务
    ↓
Orchestrator (总代理)
    - 任务分析
    - 任务拆解
    - Agent调度
    ↓
AgentTeam (Agent团队)
    - Agent生命周期管理
    - 消息通信协调
    - Skills增强
    ↓
专业Agent们 (11种类型)
    - 执行子任务
    - 互相协作
    ↓
结果整合
```

## 任务复杂度自动识别

系统根据任务描述自动判断复杂度：

- **简单任务** - 直接执行，单Agent处理
- **中等任务** - 拆分为2-3个子任务
- **复杂任务** - 完整工作流：架构 → 设计 → 开发 → 审查 → 文档

## 文件结构

```
.
├── SKILL.md                    # 本文件
├── README.md                   # 详细文档
├── multi_agent_system.py       # 主入口
├── orchestrator.py             # 总代理核心
├── agent_team.py               # Agent团队管理
├── agent_skills_config.py      # 专业Skills配置
├── test_new_skills.py          # 新Skills测试
└── test_skills_system.py       # 系统测试
```

## 示例

### 示例1: 简单任务
```python
system.execute("写一个Python函数计算斐波那契数列")
# 输出: 1个代码专家Agent完成
```

### 示例2: 中等复杂度
```python
system.execute("设计并实现一个用户注册功能")
# 输出: 架构专家 → 设计专家 → 代码专家协作完成
```

### 示例3: 复杂项目
```python
system.execute("开发一个完整的博客系统，包含前端、后端、文档")
# 输出: 5个子任务，4个专业Agent协作完成
```

### 示例4: 提示词优化
```python
system.execute("优化一个情感分析提示词，使用Chain-of-Thought")
# 输出: 提示词工程师Agent自动装备DSPy等Skills
```

### 示例5: 图像分析
```python
system.execute("设计图像分析工作流，识别产品特征")
# 输出: 图像分析专家Agent装备LLaVA、CLIP等Skills
```

## 扩展开发

### 添加新的Agent类型

```python
from orchestrator import Orchestrator, AgentProfile

orchestrator = Orchestrator()
orchestrator.AGENT_TEMPLATES["data_scientist"] = AgentProfile(
    name="数据科学家",
    capabilities=["ml", "statistics", "modeling"],
    description="专业的数据科学家",
    system_prompt="你是一名数据科学家..."
)
```

### 添加新的Skill

```python
from agent_skills_config import Skill, PROFESSIONAL_SKILLS

PROFESSIONAL_SKILLS["coder"].append(Skill(
    name="new-skill",
    source="github-owner/repo",
    description="新技能描述",
    category="category",
    capabilities=["capability1", "capability2"],
    priority=1
))
```

## 依赖

- Python 3.8+
- 无外部依赖（纯Python实现）

## 许可证

MIT License

## 参考资源

- [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills)
- [Awesome Agent Skills](https://github.com/JackyST0/awesome-agent-skills)
- [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)
- [Stanford DSPy](https://github.com/stanfordnlp/dspy)
- [LLaVA](https://github.com/haotian-liu/LLaVA)
