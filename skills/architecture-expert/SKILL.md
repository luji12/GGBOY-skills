---
name: architecture-expert
description: >
  架构专家技能。系统设计、技术选型、微服务架构、API设计、数据库设计。
  触发关键词：系统设计、架构设计、技术选型、数据库设计、API设计、扩展性
version: 1.0.0
agent_type: architect
capabilities: [system-design, microservices, api-design, database-design, cloud-architecture, scalability]
---

# 架构专家 Skill

## 系统设计方法论

### 1. 需求澄清（先问再设计）
- 日活用户规模？读写比例？
- 数据量级？增长速度？
- 可用性要求（99.9% vs 99.99%）？
- 延迟要求？
- 是否需要全球分布？

### 2. 容量估算
- QPS = DAU × 操作次数 / 86400
- 存储 = 每条记录大小 × 日增量 × 365天
- 带宽 = QPS × 平均请求大小

### 3. 高层设计
- 客户端 → CDN → 负载均衡 → 应用层 → 缓存层 → 数据层
- 读多写少 → 读写分离 + 缓存
- 写多读少 → 消息队列 + 异步处理

### 4. 深入关键组件

#### 数据库选型
| 场景 | 推荐方案 |
|------|---------|
| 结构化数据，ACID事务 | PostgreSQL / MySQL |
| 高频读写，缓存 | Redis |
| 文档型，灵活Schema | MongoDB |
| 时序数据 | InfluxDB / TimescaleDB |
| 全文搜索 | Elasticsearch |
| 图数据 | Neo4j |

#### API设计原则（RESTful）
- 资源名用名词复数：`/users`, `/orders`
- HTTP动词：GET（查）/ POST（创建）/ PUT（全量更新）/ PATCH（部分更新）/ DELETE
- 版本化：`/api/v1/...`
- 错误码规范：4xx（客户端错误）/ 5xx（服务端错误）

#### 缓存策略
- **Cache-aside**：先查缓存，miss了查DB写缓存
- **Write-through**：写DB同时写缓存
- **Write-behind**：先写缓存，异步写DB（高性能但有数据丢失风险）
- TTL设置：热数据短TTL，冷数据长TTL

### 5. 扩展性设计
- **垂直扩展**：升级硬件（有上限）
- **水平扩展**：加机器（需要无状态设计）
- **数据分片**：按用户ID、地区、时间分片
- **读写分离**：主库写，从库读

### 6. 故障处理
- 熔断器模式（Circuit Breaker）
- 限流（Rate Limiting）
- 降级（Graceful Degradation）
- 重试（Exponential Backoff）

## 常用架构模式

| 模式 | 适用场景 |
|------|---------|
| 微服务 | 大团队、独立部署、高扩展需求 |
| 单体应用 | 小团队、快速迭代、低复杂度 |
| 事件驱动 | 异步处理、解耦、高吞吐 |
| CQRS | 读写分离、复杂查询 |
| Serverless | 低频触发、弹性伸缩 |
