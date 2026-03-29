---
name: multimodal-creation-expert
description: >
  多模态内容创作专家技能。生成文生图、文生视频提示词，优化AI生成内容质量。
  触发关键词：生成图片提示词、分镜提示词、文生图、Midjourney、DALL-E、Stable Diffusion、Sora
version: 1.0.0
agent_type: multimodal_creator
capabilities: [text-to-image, video-generation, cinematic-prompts, negative-prompts, style-transfer]
---

# 多模态创作专家 Skill

## 文生图提示词规范

### 通用结构（优先级从高到低）
```
[主体描述] + [环境/背景] + [光线/色调] + [构图/视角] + [风格/质感] + [质量词]
```

### 质量增强词（根据工具调整）

**写实摄影风格**：
- `电影感摄影, 35mm胶片, HDR, 高对比度`
- `RAW photo, 8k, ultra realistic, photorealistic`
- `cinematic lighting, dramatic shadows`
- `shot on ARRI Alexa, anamorphic lens`

**插画/概念艺术风格**：
- `concept art, digital painting, artstation`
- `illustration style, detailed linework`
- `by [艺术家名], inspired by [作品风格]`

**赛博朋克专用**：
- `cyberpunk, neon-lit, rain-soaked streets`
- `blade runner aesthetic, neo-noir`
- `volumetric fog, god rays, lens flare`
- `blue-purple color palette, high contrast`

### 负面提示词（通用）
```
模糊, 变形, 低质量, 水印, 文字, 多余肢体, 不自然光线
blurry, deformed, low quality, watermark, text, extra limbs, unnatural lighting
```

### 各平台最佳实践

#### Midjourney
- 支持 `--ar 16:9`（宽屏）、`--ar 9:16`（竖屏）
- `--style raw` 减少风格化
- `--v 6` 最新版本
- 重要词放前面

#### DALL-E 3
- 中文/英文均可
- 描述要详细具体
- 指定艺术风格效果好

#### Stable Diffusion
- 需要负面提示词（negative prompt）
- `masterpiece, best quality` 作为开头
- CFG Scale: 7-12

### 分镜单帧提示词专项规范

**核心原则**：
> 图片是**凝固的一帧**，提示词只描述这一刻，不描述"正在做"

❌ 错误："林深慢慢走向废墟，脚步越来越重"
✅ 正确："林深站在废墟入口，背影对着镜头，肩膀微沉，脚尖踏在碎石上"

**情绪传递方法**：
- 通过**具体细节**传递情绪（不说"悲伤"，说"眼眶泛红，睫毛挂着水珠"）
- 通过**色调**传递情绪（暖黄=希望，冷蓝=压迫，暗红=危险）
- 通过**姿态**传递情绪（握拳=克制，垂肩=疲惫，抬头=坚定）

### 视频生成提示词（Sora/Kling）
```
[镜头运动] + [场景] + [主体动作] + [时长/节奏] + [氛围]
```
镜头运动词：推镜（push in）、拉镜（pull back）、摇镜（pan）、跟镜（follow shot）
