---
name: devops-expert
description: >
  DevOps专家技能。Docker、Kubernetes、CI/CD流水线、自动化运维、监控告警。
  触发关键词：Docker、K8s、CI/CD、部署、容器化、自动化运维、监控
version: 1.0.0
agent_type: devops
capabilities: [docker, kubernetes, cicd, monitoring, automation, infrastructure]
---

# DevOps专家 Skill

## Docker 最佳实践

### Dockerfile 规范
```dockerfile
# 使用精确版本，不用 :latest
FROM python:3.12-slim

# 使用非root用户
RUN useradd -m appuser
USER appuser

# 多阶段构建减小镜像体积
FROM node:20 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:20-slim
COPY --from=builder /app/node_modules ./node_modules
```

### 镜像优化
- 使用 `.dockerignore` 排除不必要文件
- 把变化少的层（依赖安装）放前面
- 合并 RUN 指令减少层数
- 使用多阶段构建

## Kubernetes 部署规范

### Deployment 最佳实践
```yaml
# 资源限制（必须设置）
resources:
  requests:
    memory: "64Mi"
    cpu: "250m"
  limits:
    memory: "128Mi"
    cpu: "500m"

# 健康检查
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10
```

## CI/CD 流水线设计

### GitHub Actions 模板
```yaml
name: Deploy
on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: npm test
  
  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Build & Push Docker
        run: |
          docker build -t app:${{ github.sha }} .
          docker push app:${{ github.sha }}
```

### 流水线阶段
1. **代码检查**：Lint + 格式化
2. **单元测试**：覆盖率要求
3. **构建**：编译/打包/镜像构建
4. **集成测试**：E2E测试
5. **安全扫描**：SAST/依赖漏洞检查
6. **部署**：蓝绿/金丝雀部署

## 监控告警

### 关键指标（四黄金指标）
- **延迟**（Latency）：请求响应时间
- **流量**（Traffic）：QPS/RPS
- **错误率**（Errors）：5xx 比例
- **饱和度**（Saturation）：CPU/内存使用率

### 告警阈值建议
- 错误率 > 1%：告警
- P99延迟 > 正常值3倍：告警
- CPU持续 > 80%（5分钟）：告警
- 内存 > 90%：告警
