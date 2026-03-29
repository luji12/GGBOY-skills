---
name: code-expert
description: >
  代码专家技能。编写、审查、调试、重构代码，进行安全审计和性能优化。
  触发关键词：写代码、调试、重构、代码审查、安全漏洞、性能优化
version: 1.0.0
source_refs:
  - https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-best-practices/SKILL.md
  - https://raw.githubusercontent.com/trailofbits/publications/master/reviews/README.md
agent_type: coder
capabilities: [coding, debugging, security-audit, performance, testing, code-review]
---

# 代码专家 Skill

## 代码审查流程

### 1. 读取代码
使用工具读取相关文件，理解整体架构。

### 2. 应用审查维度

#### 安全性（最高优先级）
- SQL注入、XSS、CSRF 漏洞
- 敏感信息硬编码（API Key、密码）
- 不安全的依赖版本
- 输入验证缺失

#### 性能
- N+1 查询问题
- 不必要的重渲染（React）
- 内存泄漏
- 同步阻塞操作

#### 可维护性
- 函数单一职责
- 魔法数字/字符串
- 重复代码（DRY原则）
- 命名清晰度

#### 测试覆盖
- 边界条件
- 异常路径
- 关键业务逻辑

### 3. React/Next.js 最佳实践（Vercel Guidelines）

获取最新规则：
```
fetch: https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

核心原则：
- 使用 `React.memo()` 避免不必要重渲染
- `useMemo`/`useCallback` 用于昂贵计算
- 图片使用 `next/image` 自动优化
- 动态导入 `dynamic()` 代码分割
- Server Components 优先，减少客户端 Bundle

### 4. Python 代码规范
- 类型注解（Type Hints）
- 文档字符串（Docstring）
- 异常处理要具体，不用裸 `except:`
- 使用 `pathlib` 而非 `os.path`
- 上下文管理器处理资源

### 5. 输出格式
审查结果格式：
```
文件:行号 | 严重程度 | 问题描述 | 建议修复
```
严重程度：🔴 Critical | 🟡 Warning | 🔵 Info
