#!/usr/bin/env python3
"""
测试新增的提示词工程和图片分析Skills
"""

from multi_agent_system import MultiAgentSystem
from agent_skills_config import get_skills_for_agent


def test_prompt_engineer():
    """测试提示词工程师"""
    print("\n" + "="*70)
    print("📝 测试：提示词工程师")
    print("="*70)
    
    system = MultiAgentSystem()
    
    # 显示提示词工程师的skills
    skills = get_skills_for_agent("prompt_engineer")
    print(f"\n✨ 提示词工程师装备了 {len(skills)} 个专业skills:\n")
    for skill in skills:
        print(f"   🔧 {skill.name}")
        print(f"      来源: {skill.source}")
        print(f"      能力: {', '.join(skill.capabilities)}\n")
    
    # 执行提示词优化任务
    print("-" * 70)
    print("\n🚀 执行任务：优化一个情感分析提示词\n")
    result = system.execute(
        "优化一个情感分析提示词，要求使用Chain-of-Thought方法，"
        "并设计3个few-shot示例，提升模型在中文评论上的准确率",
        verbose=True
    )


def test_image_analyst():
    """测试图像分析专家"""
    print("\n" + "="*70)
    print("🖼️ 测试：图像分析专家")
    print("="*70)
    
    system = MultiAgentSystem()
    
    # 显示图像分析专家的skills
    skills = get_skills_for_agent("image_analyst")
    print(f"\n✨ 图像分析专家装备了 {len(skills)} 个专业skills:\n")
    for skill in skills:
        print(f"   🔧 {skill.name}")
        print(f"      来源: {skill.source}")
        print(f"      能力: {', '.join(skill.capabilities)}\n")
    
    # 执行图像分析任务
    print("-" * 70)
    print("\n🚀 执行任务：分析电商产品图片并生成描述\n")
    result = system.execute(
        "设计一个图像分析工作流，能够：\n"
        "1. 识别图片中的产品类别和主要特征\n"
        "2. 提取颜色、材质、风格等视觉属性\n"
        "3. 生成适合电商平台的商品描述\n"
        "4. 使用CLIP模型进行图像-文本对齐验证",
        verbose=True
    )


def test_multimodal_creator():
    """测试多模态内容创作者"""
    print("\n" + "="*70)
    print("🎨 测试：多模态内容创作者")
    print("="*70)
    
    system = MultiAgentSystem()
    
    # 显示多模态创作者的skills
    skills = get_skills_for_agent("multimodal_creator")
    print(f"\n✨ 多模态内容创作者装备了 {len(skills)} 个专业skills:\n")
    for skill in skills:
        print(f"   🔧 {skill.name}")
        print(f"      来源: {skill.source}")
        print(f"      能力: {', '.join(skill.capabilities)}\n")
    
    # 执行多模态创作任务
    print("-" * 70)
    print("\n🚀 执行任务：为品牌生成视觉内容\n")
    result = system.execute(
        "为一家咖啡品牌生成视觉内容策略：\n"
        "1. 设计10个DALL-E提示词，生成不同风格的咖啡产品图\n"
        "2. 优化负面提示词以避免常见生成问题\n"
        "3. 设计视频生成提示词用于社交媒体广告\n"
        "4. 建立品牌视觉风格指南",
        verbose=True
    )


def test_collaboration_with_new_agents():
    """测试新agent与原有agent的协作"""
    print("\n" + "="*70)
    print("🤝 测试：跨领域Agent协作")
    print("="*70)
    
    system = MultiAgentSystem()
    
    print("\n🚀 启动复杂项目：AI驱动的电商视觉系统\n")
    print("这个项目需要提示词工程师、图像分析专家、设计师和代码专家协作\n")
    
    result = system.execute(
        "开发一个AI驱动的电商视觉系统：\n"
        "1. 提示词工程：设计图像识别和描述的提示词模板\n"
        "2. 图像分析：实现产品图片自动标注和分类\n"
        "3. 多模态生成：自动生成产品展示图和营销素材\n"
        "4. UI设计：设计分析结果展示界面\n"
        "5. 前端开发：实现交互式图像分析面板\n"
        "6. 后端开发：构建图像处理和API服务\n"
        "7. 编写完整的系统文档",
        verbose=True
    )
    
    print("\n" + "="*70)
    print("📊 协作统计")
    print("="*70)
    print(f"   参与Agent数量: {len(result['agents_involved'])}")
    print(f"   Agent列表: {', '.join(result['agents_involved'])}")
    print(f"   子任务总数: {result['subtasks_total']}")
    print(f"   任务复杂度: {result['analysis']['complexity']}")


def main():
    """主函数"""
    print("\n" + "🎯" * 35)
    print("\n   新增Skills测试：提示词工程 + 图像分析\n")
    print("🎯" * 35)
    
    # 测试各个新agent
    test_prompt_engineer()
    test_image_analyst()
    test_multimodal_creator()
    
    # 测试协作
    test_collaboration_with_new_agents()
    
    print("\n" + "="*70)
    print("✅ 所有测试完成!")
    print("="*70)
    print("\n💡 新增能力总结:")
    print("   • 提示词工程师: 5个skills (DSPy、APE、LangChain等)")
    print("   • 图像分析专家: 6个skills (LLaVA、CLIP、ViP-LLaVA等)")
    print("   • 多模态创作者: 3个skills (DALL-E、Midjourney、Sora等)")
    print("   • 系统总skills数: 44个")
    print()


if __name__ == "__main__":
    main()
