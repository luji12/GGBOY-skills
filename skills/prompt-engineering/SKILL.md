---
name: prompt-engineering-guide
description: >
  提示词工程专家技能。当需要设计、优化或评估提示词时使用。
  触发关键词：优化提示词、设计prompt、Chain-of-Thought、Few-shot、提示词调优
version: 1.0.0
source: https://raw.githubusercontent.com/dair-ai/Prompt-Engineering-Guide/main/guides/prompts-intro.md
agent_type: prompt_engineer
capabilities: [prompt-design, chain-of-thought, few-shot, prompt-optimization, auto-prompt]
---

# 提示词工程专家 Skill

## 使用方法

当用户需要设计或优化提示词时，按以下步骤操作：

1. 使用 WebFetch 获取最新提示词工程指南：
   ```
   fetch: https://raw.githubusercontent.com/dair-ai/Prompt-Engineering-Guide/main/guides/prompts-intro.md
   fetch: https://raw.githubusercontent.com/dair-ai/Prompt-Engineering-Guide/main/guides/prompts-advanced-usage.md
   ```

2. 根据任务类型选择对应技术：
   - **分析/推理任务** → Chain-of-Thought (CoT) 提示
   - **少量示例** → Few-shot 提示
   - **复杂任务** → ReAct 框架（推理+行动）
   - **自动优化** → APE（自动提示工程师）方法

3. 提示词模板结构：
   ```
   角色定义 → 任务说明 → 约束条件 → 输出格式 → 示例（可选）
   ```

## 核心技术知识

### Zero-shot 提示
直接给出指令，不提供示例。适合简单、明确的任务。

### Few-shot 提示
提供2-5个高质量示例，引导模型理解预期格式和风格。

### Chain-of-Thought (CoT)
在提示中加入"让我们一步步思考"，引导模型展示推理过程。
适合：数学、逻辑、多步骤推理任务。

### ReAct 框架
结合推理（Reasoning）和行动（Acting）：
```
思考: [分析当前情况]
行动: [执行操作]
观察: [查看结果]
思考: [根据结果调整]
```

### 自我一致性
对同一问题生成多个推理路径，选择最一致的答案。

## 质量检查清单

- [ ] 指令是否清晰无歧义？
- [ ] 是否指定了输出格式？
- [ ] 是否包含必要的约束？
- [ ] Few-shot 示例是否具有代表性？
- [ ] 是否测试了边界情况？
