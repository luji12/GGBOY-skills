---
name: security-expert
description: >
  安全专家技能。安全审计、漏洞检测、渗透测试思路、安全编码实践。
  触发关键词：安全审计、漏洞、SQL注入、XSS、CSRF、安全加固、权限控制
version: 1.0.0
agent_type: security
capabilities: [security-audit, vulnerability-scanning, secure-coding, owasp, penetration-testing]
---

# 安全专家 Skill

## OWASP Top 10 审查清单

### 1. 注入攻击（SQL/Command注入）
检查点：
- 用户输入是否直接拼接SQL？
- 是否使用参数化查询/预处理语句？
- 命令执行是否过滤特殊字符？

### 2. 认证与会话管理
- 密码是否使用强哈希（bcrypt/argon2）？
- 会话Token是否足够随机（≥128bit）？
- 是否实现了登录失败限速？
- HTTPS是否强制？

### 3. XSS（跨站脚本）
- 输出到HTML时是否转义 `< > & " '`？
- 是否使用 CSP（Content Security Policy）？
- innerHTML 是否使用了不受信任的数据？

### 4. 不安全的直接对象引用（IDOR）
- API 是否验证当前用户有权访问该资源？
- 是否用可猜测的ID（如递增整数）暴露资源？

### 5. 安全配置错误
- 是否暴露了详细错误信息？
- 是否存在默认密码？
- 不需要的端口/服务是否关闭？

### 6. 敏感数据泄露
- API Key/密码是否硬编码在代码中？
- 日志是否打印了敏感信息？
- Git 历史是否有意外提交的密钥？

### 7. CSRF（跨站请求伪造）
- 状态变更操作是否有 CSRF Token？
- SameSite Cookie 是否设置？

## 安全编码规范

### 输入验证
```python
# 白名单验证（推荐）
ALLOWED_CHARS = re.compile(r'^[a-zA-Z0-9_-]+$')
if not ALLOWED_CHARS.match(user_input):
    raise ValueError("Invalid input")
```

### 密码存储
```python
import bcrypt
# 存储
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))
# 验证
bcrypt.checkpw(password.encode(), hashed)
```

### 环境变量管理
- 使用 `.env` 文件 + `.gitignore`
- 生产环境用密钥管理服务（AWS Secrets Manager等）
- 代码中只读取环境变量，不硬编码

## 审计输出格式
```
[严重程度] 文件:行号
问题描述：xxx
风险：xxx
修复建议：xxx
```
严重程度：CRITICAL / HIGH / MEDIUM / LOW / INFO
