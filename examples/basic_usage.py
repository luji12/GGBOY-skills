#!/usr/bin/env python3
"""
多智能体协作系统 - 基础使用示例
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from multi_agent_system import MultiAgentSystem


def example_1_simple_task():
    """示例1: 简单任务"""
    print("="*70)
    print("示例1: 简单任务 - 编写函数")
    print("="*70)
    
    system = MultiAgentSystem()
    result = system.execute("写一个Python函数，计算列表的平均值和中位数")
    
    print(f"\n✅ 任务完成!")
    print(f"   参与Agent: {', '.join(result['agents_involved'])}")
    print(f"   子任务数: {result['subtasks_total']}")


def example_2_medium_task():
    """示例2: 中等复杂度任务"""
    print("\n" + "="*70)
    print("示例2: 中等复杂度 - 开发功能模块")
    print("="*70)
    
    system = MultiAgentSystem()
    result = system.execute("设计并实现一个用户注册功能，包含前端表单和后端验证")
    
    print(f"\n✅ 任务完成!")
    print(f"   参与Agent: {', '.join(result['agents_involved'])}")
    print(f"   子任务数: {result['subtasks_total']}")


def example_3_complex_task():
    """示例3: 复杂任务"""
    print("\n" + "="*70)
    print("示例3: 复杂任务 - 完整系统开发")
    print("="*70)
    
    system = MultiAgentSystem()
    result = system.execute(
        "开发一个完整的博客系统，包含：\n"
        "- 文章管理功能\n"
        "- 用户认证系统\n"
        "- 评论功能\n"
        "- 响应式前端界面\n"
        "- 后端API\n"
        "- 技术文档"
    )
    
    print(f"\n✅ 任务完成!")
    print(f"   参与Agent: {', '.join(result['agents_involved'])}")
    print(f"   子任务数: {result['subtasks_total']}")
    print(f"   完成度: {result['subtasks_completed']}/{result['subtasks_total']}")


def example_4_prompt_engineering():
    """示例4: 提示词工程任务"""
    print("\n" + "="*70)
    print("示例4: 提示词工程 - 优化LLM提示词")
    print("="*70)
    
    system = MultiAgentSystem()
    result = system.execute(
        "优化一个情感分析提示词：\n"
        "1. 使用Chain-of-Thought方法\n"
        "2. 设计3个few-shot示例\n"
        "3. 针对中文评论优化\n"
        "4. 提供评估方法"
    )
    
    print(f"\n✅ 任务完成!")
    print(f"   参与Agent: {', '.join(result['agents_involved'])}")
    print(f"   提示词工程师已装备DSPy、LangChain等专业skills")


def example_5_image_analysis():
    """示例5: 图像分析任务"""
    print("\n" + "="*70)
    print("示例5: 图像分析 - 电商产品分析")
    print("="*70)
    
    system = MultiAgentSystem()
    result = system.execute(
        "设计图像分析工作流：\n"
        "1. 识别产品类别和主要特征\n"
        "2. 提取颜色、材质、风格\n"
        "3. 生成电商商品描述\n"
        "4. 使用CLIP验证图像-文本对齐"
    )
    
    print(f"\n✅ 任务完成!")
    print(f"   参与Agent: {', '.join(result['agents_involved'])}")
    print(f"   图像分析专家已装备LLaVA、CLIP等专业skills")


def example_6_agent_collaboration():
    """示例6: Agent间协作"""
    print("\n" + "="*70)
    print("示例6: Agent间协作对话")
    print("="*70)
    
    system = MultiAgentSystem()
    
    # 先执行一个任务创建Agent
    result = system.execute("设计一个Web应用架构", verbose=False)
    
    # 获取Agent进行协作
    agents = list(system.agent_team.agents.values())
    if len(agents) >= 2:
        print(f"\n💬 启动 {agents[0].name} 和 {agents[1].name} 的协作对话\n")
        system.chat_between_agents(
            agents[0].id,
            agents[1].id,
            "讨论系统性能优化方案"
        )


def main():
    """运行所有示例"""
    print("\n" + "🎯" * 35)
    print("\n   多智能体协作系统 - 基础使用示例\n")
    print("🎯" * 35)
    
    # 运行示例
    example_1_simple_task()
    example_2_medium_task()
    example_3_complex_task()
    example_4_prompt_engineering()
    example_5_image_analysis()
    example_6_agent_collaboration()
    
    print("\n" + "="*70)
    print("✅ 所有示例运行完成!")
    print("="*70)
    print("\n💡 提示:")
    print("   • 系统会自动根据任务复杂度选择合适的Agent")
    print("   • 复杂任务会自动拆解为多个子任务")
    print("   • Agent会自动装备相关的专业skills")
    print("   • 可以通过 system.agent_team 查看Agent间通信")
    print()


if __name__ == "__main__":
    main()
