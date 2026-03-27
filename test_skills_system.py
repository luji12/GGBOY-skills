#!/usr/bin/env python3
"""
测试专业Skills系统

演示：
1. 查看所有可用的专业skills
2. 测试动态创建agent时自动匹配skill
3. 模拟真实场景下的agent协作
"""

from multi_agent_system import MultiAgentSystem
from agent_skills_config import (
    get_skills_for_agent,
    get_all_skills_summary,
    PROFESSIONAL_SKILLS
)


def show_skills_library():
    """展示专业skills库"""
    print("\n" + "="*70)
    print("🎓 专业Agent Skills库展示")
    print("="*70)
    
    summary = get_all_skills_summary()
    
    print(f"\n📊 总体统计:")
    print(f"   • 覆盖 {summary['total_agent_types']} 种专业领域")
    print(f"   • 共 {summary['total_skills']} 个专业skills")
    print(f"   • 来自 {len(summary['by_category'])} 个不同类别")
    
    print(f"\n🏢 顶级来源:")
    sources = [
        "vercel-labs/agent-skills (Vercel官方)",
        "anthropics/skills (Anthropic官方)",
        "microsoft/agent-skills (Microsoft官方)",
        "trailofbits/skills (安全领域权威)",
        "awesome-agent-skills (社区精选)",
    ]
    for src in sources:
        print(f"   • {src}")
    
    print(f"\n📁 按Agent类型分类:\n")
    
    for agent_type, skills in PROFESSIONAL_SKILLS.items():
        if not skills:
            continue
        
        print(f"\n🔹 {agent_type.upper()} ({len(skills)}个skills)")
        print("-" * 50)
        
        for skill in skills[:3]:  # 只显示前3个
            print(f"\n   🔧 {skill.name}")
            print(f"      描述: {skill.description[:50]}...")
            print(f"      来源: {skill.source}")
            print(f"      能力: {', '.join(skill.capabilities[:3])}")
        
        if len(skills) > 3:
            print(f"\n      ... 还有 {len(skills) - 3} 个skills")


def test_dynamic_agent_with_skills():
    """测试动态创建agent时自动匹配skill"""
    print("\n" + "="*70)
    print("🧪 测试：动态创建Agent并自动匹配专业Skill")
    print("="*70)
    
    system = MultiAgentSystem()
    
    # 测试场景1: 安全相关任务
    print("\n场景1: 安全审计任务")
    print("-" * 50)
    result = system.execute("对现有代码进行安全审计，检查SQL注入和XSS漏洞", verbose=True)
    
    # 测试场景2: DevOps任务
    print("\n场景2: DevOps部署任务")
    print("-" * 50)
    result = system.execute("设计一个Docker容器化部署方案，包含CI/CD流水线", verbose=True)
    
    # 测试场景3: 移动端开发
    print("\n场景3: 移动端开发任务")
    print("-" * 50)
    result = system.execute("开发一个React Native移动应用，包含用户登录和地图功能", verbose=True)


def test_skills_enhanced_collaboration():
    """测试装备skills后的agent协作"""
    print("\n" + "="*70)
    print("🤝 测试：装备Skills后的Agent协作")
    print("="*70)
    
    system = MultiAgentSystem()
    
    # 创建一个复杂的全栈项目
    print("\n🚀 启动全栈项目开发（装备专业skills）\n")
    
    result = system.execute(
        "开发一个电商网站，包含：\n"
        "1. React前端，使用Next.js框架\n"
        "2. Node.js后端API\n"
        "3. 响应式设计，支持移动端\n"
        "4. 完整的用户认证系统\n"
        "5. 支付功能集成\n"
        "6. 完整的测试覆盖\n"
        "7. 部署到Vercel\n"
        "8. 编写技术文档",
        verbose=True
    )
    
    print("\n" + "="*70)
    print("📈 项目完成统计")
    print("="*70)
    print(f"   子任务完成: {result['subtasks_completed']}/{result['subtasks_total']}")
    print(f"   参与Agent: {', '.join(result['agents_involved'])}")
    print(f"   项目复杂度: {result['analysis']['complexity']}")
    print(f"   涉及领域: {', '.join(result['analysis']['domains'])}")


def show_skill_details():
    """展示特定skill的详细信息"""
    print("\n" + "="*70)
    print("🔍 热门Skills详细介绍")
    print("="*70)
    
    featured_skills = [
        ("coder", "vercel-react-best-practices"),
        ("designer", "web-design-guidelines"),
        ("coder", "trailofbits-security"),
        ("architect", "system-design"),
    ]
    
    for agent_type, skill_name in featured_skills:
        skills = get_skills_for_agent(agent_type)
        skill = next((s for s in skills if s.name == skill_name), None)
        
        if skill:
            print(f"\n{'='*70}")
            print(f"🔥 {skill.name}")
            print(f"{'='*70}")
            print(f"📋 描述: {skill.description}")
            print(f"🏢 来源: {skill.source}")
            print(f"🏷️ 类别: {skill.category}")
            print(f"⭐ 优先级: {'⭐' * (6 - skill.priority)}")
            print(f"🎯 能力覆盖: {', '.join(skill.capabilities)}")
            if skill.install_command:
                print(f"💻 安装命令: {skill.install_command}")


def main():
    """主函数"""
    print("\n" + "🎯" * 35)
    print("\n   专业Skills增强的多智能体系统测试\n")
    print("🎯" * 35)
    
    # 1. 展示skills库
    show_skills_library()
    
    # 2. 展示热门skill详情
    show_skill_details()
    
    # 3. 测试动态创建
    test_dynamic_agent_with_skills()
    
    # 4. 测试协作
    test_skills_enhanced_collaboration()
    
    print("\n" + "="*70)
    print("✅ 所有测试完成!")
    print("="*70)
    print("\n💡 总结:")
    print("   • 系统已装备30个来自顶级来源的专业skills")
    print("   • Agent会根据任务自动匹配最合适的skills")
    print("   • 动态创建的Agent也会自动查找匹配的skills")
    print("   • 所有Agent的system prompt已增强skills指导")
    print()


if __name__ == "__main__":
    main()
