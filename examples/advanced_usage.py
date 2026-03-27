#!/usr/bin/env python3
"""
多智能体协作系统 - 高级使用示例
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from multi_agent_system import MultiAgentSystem
from orchestrator import Orchestrator, AgentProfile
from agent_skills_config import Skill, PROFESSIONAL_SKILLS


def example_1_custom_agent():
    """示例1: 创建自定义Agent"""
    print("="*70)
    print("示例1: 创建自定义Agent类型")
    print("="*70)
    
    orchestrator = Orchestrator()
    
    # 添加自定义Agent模板
    orchestrator.AGENT_TEMPLATES["data_scientist"] = AgentProfile(
        name="数据科学家",
        capabilities=["ml", "statistics", "modeling", "data-analysis"],
        description="专业的数据科学家，擅长机器学习和统计分析",
        system_prompt="""你是一名数据科学家，擅长：
- 机器学习模型设计和训练
- 统计分析和假设检验
- 数据预处理和特征工程
- 模型评估和优化
- Python数据科学生态（pandas, scikit-learn, PyTorch）

工作时请：
1. 理解业务问题和数据特点
2. 选择合适的算法和模型
3. 进行严谨的数据分析
4. 提供可解释的结果
"""
    )
    
    print("✅ 已添加自定义Agent: 数据科学家")
    print(f"   当前Agent模板数: {len(orchestrator.AGENT_TEMPLATES)}")


def example_2_custom_skill():
    """示例2: 添加自定义Skill"""
    print("\n" + "="*70)
    print("示例2: 添加自定义Skill")
    print("="*70)
    
    # 为代码专家添加新的skill
    PROFESSIONAL_SKILLS["coder"].append(Skill(
        name="custom-ml-skill",
        source="your-org/custom-ml",
        description="自定义机器学习编码规范",
        category="machine-learning",
        capabilities=["ml", "pytorch", "tensorflow"],
        priority=2
    ))
    
    print("✅ 已为代码专家添加自定义Skill: custom-ml-skill")
    print(f"   代码专家当前skills数: {len(PROFESSIONAL_SKILLS['coder'])}")


def example_3_task_analysis():
    """示例3: 任务分析详情"""
    print("\n" + "="*70)
    print("示例3: 查看任务分析详情")
    print("="*70)
    
    system = MultiAgentSystem()
    
    tasks = [
        "写一个Python函数",
        "开发一个用户登录系统",
        "构建一个完整的电商平台，包含前后端、支付、物流跟踪",
    ]
    
    for task in tasks:
        analysis = system.orchestrator.analyze_task(task)
        print(f"\n📝 任务: {task[:40]}...")
        print(f"   复杂度: {analysis['complexity']}")
        print(f"   领域: {', '.join(analysis['domains']) if analysis['domains'] else '通用'}")
        print(f"   预估子任务: {analysis['estimated_subtasks']}个")


def example_4_agent_communication():
    """示例4: 查看Agent通信"""
    print("\n" + "="*70)
    print("示例4: 查看Agent间通信记录")
    print("="*70)
    
    system = MultiAgentSystem()
    
    # 执行任务产生通信
    result = system.execute("开发一个博客系统", verbose=False)
    
    # 打印通信记录
    print(f"\n📨 Agent通信记录:")
    print(f"   总消息数: {len(system.agent_team.message_log)}")
    
    for msg in system.agent_team.message_log[:5]:  # 显示前5条
        print(f"\n   [{msg.type.value}] {msg.from_agent[:20]} → {msg.to_agent[:20]}")
        print(f"   内容: {msg.content[:50]}...")


def example_5_skills_inspection():
    """示例5: 查看Skills详情"""
    print("\n" + "="*70)
    print("示例5: 查看专业Skills详情")
    print("="*70)
    
    from agent_skills_config import get_skills_for_agent, get_all_skills_summary
    
    # 总体统计
    summary = get_all_skills_summary()
    print(f"\n📊 Skills库统计:")
    print(f"   Agent类型: {summary['total_agent_types']} 种")
    print(f"   总Skills: {summary['total_skills']} 个")
    
    # 查看特定Agent的skills
    print(f"\n🔍 提示词工程师的Skills:")
    skills = get_skills_for_agent("prompt_engineer")
    for skill in skills:
        print(f"   • {skill.name} ({skill.source})")
        print(f"     能力: {', '.join(skill.capabilities)}")


def example_6_batch_tasks():
    """示例6: 批量处理任务"""
    print("\n" + "="*70)
    print("示例6: 批量处理多个任务")
    print("="*70)
    
    system = MultiAgentSystem()
    
    tasks = [
        "设计一个数据库schema",
        "优化前端性能",
        "编写API文档",
    ]
    
    results = []
    for task in tasks:
        print(f"\n🚀 执行任务: {task}")
        result = system.execute(task, verbose=False)
        results.append(result)
        print(f"   ✅ 完成 - Agent: {', '.join(result['agents_involved'])}")
    
    # 统计
    print(f"\n📈 批量处理统计:")
    print(f"   总任务数: {len(results)}")
    print(f"   总Agent参与: {sum(len(r['agents_involved']) for r in results)}")
    print(f"   总子任务: {sum(r['subtasks_total'] for r in results)}")


def example_7_system_extension():
    """示例7: 系统扩展"""
    print("\n" + "="*70)
    print("示例7: 扩展现有Agent能力")
    print("="*70)
    
    system = MultiAgentSystem()
    
    # 修改现有Agent的system prompt
    coder_profile = system.orchestrator.AGENT_TEMPLATES["coder"]
    coder_profile.system_prompt += """

额外专长：
- 代码性能分析
- 内存优化
- 并发编程
"""
    
    print("✅ 已为代码专家添加额外专长")
    
    # 执行任务验证
    result = system.execute("编写高性能数据处理函数", verbose=False)
    print(f"   任务完成，使用Agent: {', '.join(result['agents_involved'])}")


def main():
    """运行所有高级示例"""
    print("\n" + "🚀" * 35)
    print("\n   多智能体协作系统 - 高级使用示例\n")
    print("🚀" * 35)
    
    # 运行示例
    example_1_custom_agent()
    example_2_custom_skill()
    example_3_task_analysis()
    example_4_agent_communication()
    example_5_skills_inspection()
    example_6_batch_tasks()
    example_7_system_extension()
    
    print("\n" + "="*70)
    print("✅ 所有高级示例运行完成!")
    print("="*70)
    print("\n💡 高级用法提示:")
    print("   • 可以通过修改AGENT_TEMPLATES自定义Agent")
    print("   • 可以通过PROFESSIONAL_SKILLS添加自定义Skills")
    print("   • 可以查看agent_team.message_log分析协作过程")
    print("   • 可以批量处理任务提高效率")
    print("   • 可以动态扩展Agent的system prompt")
    print()


if __name__ == "__main__":
    main()
