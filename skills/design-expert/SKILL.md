---
name: design-expert
description: >
  设计专家技能。UI/UX设计、视觉规范、用户体验、品牌设计、原型设计。
  触发关键词：UI设计、界面设计、用户体验、配色方案、视觉规范、品牌风格
version: 1.0.0
source_refs:
  - https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
agent_type: designer
capabilities: [ui-design, ux-design, visual-design, brand-guidelines, accessibility, design-system]
---

# 设计专家 Skill

## Web 界面设计规范

获取最新 Vercel Web 界面指南：
```
fetch: https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

## 核心设计原则

### 视觉层次
1. **尺寸对比**：重要内容更大
2. **颜色权重**：主要操作用强调色
3. **留白**：给内容呼吸空间（最常被忽视）
4. **对齐**：建立视觉秩序感

### 色彩规范
```
主色（Brand Color）：用于CTA、重要强调
辅色（Secondary）：用于次要操作
中性色（Neutral）：文本、背景、边框
语义色：Success(绿) / Warning(黄) / Error(红) / Info(蓝)
```

**色彩可访问性**：
- 文本与背景对比度 ≥ 4.5:1（普通文字）
- 大文字 ≥ 3:1
- 不能仅用颜色传达信息（色盲用户）

### 排版规范
- **字号层级**：H1(32px) → H2(24px) → H3(20px) → Body(16px) → Caption(12px)
- **行高**：正文 1.5-1.7，标题 1.2-1.3
- **字重**：Regular(400)/Medium(500)/SemiBold(600)/Bold(700)
- **每行字符**：40-80字符最佳阅读范围

### 间距系统（8px基准）
```
4px  - 极小间距（标签内边距）
8px  - 小间距（相关元素间）
16px - 基准间距（一般间距）
24px - 中等间距（组件间）
32px - 大间距（区块间）
48px - 超大间距（章节间）
```

### 组件设计规范

#### 按钮
- 主按钮：填充色，用于主要操作（每页最多1个）
- 次按钮：描边或幽灵，用于次要操作
- 尺寸：Small(32px) / Medium(40px) / Large(48px)
- 状态：默认/悬停/按下/禁用/加载中

#### 表单
- 标签在输入框上方（不用placeholder替代标签）
- 错误信息在输入框下方，红色，具体说明问题
- 必填字段明确标注

#### 交互反馈
- 操作响应时间 < 100ms 感觉即时
- 100-300ms 需要视觉反馈（如按钮状态变化）
- > 1s 需要进度指示器

### 响应式断点
```
Mobile:  < 768px
Tablet:  768px - 1024px
Desktop: > 1024px
Wide:    > 1440px
```

## 可访问性检查清单
- [ ] 所有图片有 alt 文字
- [ ] 颜色对比度达标
- [ ] 键盘可导航
- [ ] 焦点状态可见
- [ ] 表单有关联标签
