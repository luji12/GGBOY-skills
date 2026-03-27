#!/usr/bin/env python3
"""
动态多智能体协作系统 - 主入口

使用方式:
1. 直接运行进行测试: python multi_agent_system.py
2. 作为模块导入使用:
   from multi_agent_system import MultiAgentSystem
   system = MultiAgentSystem()
   result = system.execute("你的任务")
"""

import sys
from typing import Dict, List, Optional
from orchestrator import Orchestrator
from agent_team import AgentTeam, MessageType


class MultiAgentSystem:
    """
    动态多智能体系统的主接口
    
    整合了:
    - Orchestrator: 任务分析和调度
    - AgentTeam: Agent团队管理
    """
    
    def __init__(self):
        self.orchestrator = Orchestrator()
        self.agent_team = AgentTeam()
        self.execution_mode = "simulate"  # simulate 或 real
    
    def execute(self, task: str, verbose: bool = True) -> Dict:
        """
        执行用户任务的主入口
        
        Args:
            task: 用户输入的任务描述
            verbose: 是否打印详细日志
            
        Returns:
            执行结果字典
        """
        if verbose:
            print(f"\n{'='*70}")
            print(f"🚀 多智能体系统启动")
            print(f"{'='*70}\n")
        
        # 1. 分析任务
        analysis = self.orchestrator.analyze_task(task)
        
        if verbose:
            print(f"📋 任务分析:")
            print(f"   意图: {analysis['intent'] or '未明确'}")
            print(f"   复杂度: {analysis['complexity']}")
            print(f"   领域: {', '.join(analysis['domains']) if analysis['domains'] else '通用'}")
            print()
        
        # 2. 拆解任务
        subtasks = self.orchestrator.decompose_task(task, analysis)
        
        if verbose:
            print(f"🔨 任务拆解为 {len(subtasks)} 个子任务:")
            for i, st in enumerate(subtasks, 1):
                deps = f" [依赖: {', '.join(st.dependencies)}]" if st.dependencies else ""
                print(f"   {i}. [{st.required_capability}] {st.description}{deps}")
            print()
        
        # 3. 创建/获取agent团队
        if verbose:
            print("👥 组建专业团队:")
        
        agents_created = []
        for st in subtasks:
            agent_profile = self.orchestrator.find_or_create_agent(st.required_capability)
            
            # 检查是否已有相同类型的agent
            existing = self.agent_team.find_agents_by_capability(st.required_capability)
            if not existing:
                agent = self.agent_team.create_agent(agent_profile)
                agents_created.append(agent)
                if verbose:
                    print(f"   ✨ 新创建: {agent.name}")
            else:
                agent = existing[0]
                if verbose:
                    print(f"   ♻️  复用: {agent.name}")
            
            st.assigned_agent = agent.id
        
        if verbose:
            print(f"\n   团队规模: {len(self.agent_team.agents)} 个agent\n")
        
        # 4. 执行任务（模拟）
        if verbose:
            print("⚙️  开始执行:")
            print("-" * 70)
        
        results = []
        completed_tasks = set()
        
        # 按依赖顺序执行
        pending = set(st.id for st in subtasks)
        
        while pending:
            progress = False
            
            for st in subtasks:
                if st.id in pending:
                    # 检查依赖是否完成
                    deps_satisfied = all(d in completed_tasks for d in st.dependencies)
                    
                    if deps_satisfied:
                        if verbose:
                            print(f"\n   ▶️  执行: {st.description[:50]}...")
                            print(f"      负责人: {st.assigned_agent}")
                        
                        # 模拟执行
                        st.status = "completed"
                        st.result = self._simulate_execution(st)
                        completed_tasks.add(st.id)
                        pending.remove(st.id)
                        results.append(st.result)
                        progress = True
                        
                        if verbose:
                            print(f"      ✅ 完成")
                        
                        # 如果有后续任务，通知相关agent
                        self._notify_dependent_tasks(st, subtasks)
            
            if not progress and pending:
                # 依赖循环或无法完成
                if verbose:
                    print(f"   ⚠️  警告: 部分任务因依赖问题无法执行: {pending}")
                break
        
        if verbose:
            print("\n" + "-" * 70)
        
        # 5. 整合结果
        final_result = {
            "success": len(completed_tasks) == len(subtasks),
            "task": task,
            "analysis": analysis,
            "subtasks_total": len(subtasks),
            "subtasks_completed": len(completed_tasks),
            "agents_involved": [a.name for a in self.agent_team.agents.values()],
            "results": results,
            "summary": self._generate_summary(task, subtasks, results)
        }
        
        if verbose:
            print(f"\n📦 结果整合完成")
            print(f"\n{'='*70}")
            print(f"✅ 任务执行完毕")
            print(f"{'='*70}\n")
            print(f"📊 执行摘要:")
            print(f"   完成度: {final_result['subtasks_completed']}/{final_result['subtasks_total']}")
            print(f"   参与agent: {', '.join(final_result['agents_involved'])}")
            print(f"\n📝 {final_result['summary']}\n")
        
        return final_result
    
    def _simulate_execution(self, subtask) -> str:
        """模拟子任务执行"""
        agent = self.agent_team.get_agent(subtask.assigned_agent)
        agent_name = agent.name if agent else "Unknown"
        
        # 模拟不同类型的任务输出
        capability = subtask.required_capability
        
        outputs = {
            "architecture": f"[{agent_name}] 已完成架构设计，包含模块划分和接口定义",
            "coding": f"[{agent_name}] 已完成代码实现，包含单元测试",
            "design": f"[{agent_name}] 已完成设计方案，包含视觉稿和规范",
            "writing": f"[{agent_name}] 已完成文档编写，包含使用说明",
            "analysis": f"[{agent_name}] 已完成分析报告，包含数据洞察",
        }
        
        return outputs.get(capability, f"[{agent_name}] 已完成任务")
    
    def _notify_dependent_tasks(self, completed_task, all_tasks):
        """通知依赖于此任务的其他任务"""
        for st in all_tasks:
            if completed_task.id in st.dependencies:
                self.agent_team.send_message(
                    from_agent=completed_task.assigned_agent,
                    to_agent=st.assigned_agent,
                    msg_type=MessageType.RESULT,
                    content=f"前置任务已完成: {completed_task.description}",
                    context={"completed_task_id": completed_task.id}
                )
    
    def _generate_summary(self, task: str, subtasks: List, results: List) -> str:
        """生成任务执行摘要"""
        agent_names = set()
        for st in subtasks:
            agent = self.agent_team.get_agent(st.assigned_agent)
            if agent:
                agent_names.add(agent.name)
        
        return (
            f"任务『{task[:30]}...』已完成。"
            f"共协调 {len(agent_names)} 个专业agent，"
            f"完成 {len(subtasks)} 个子任务。"
        )
    
    def chat_between_agents(self, agent1_id: str, agent2_id: str, topic: str):
        """
        触发两个agent之间的协作对话
        """
        agent1 = self.agent_team.get_agent(agent1_id)
        agent2 = self.agent_team.get_agent(agent2_id)
        
        if not agent1 or not agent2:
            print("❌ Agent不存在")
            return
        
        print(f"\n💬 启动协作对话: {agent1.name} ↔ {agent2.name}")
        print(f"   主题: {topic}\n")
        
        # 模拟对话
        self.agent_team.send_message(
            from_agent=agent1_id,
            to_agent=agent2_id,
            msg_type=MessageType.COLLABORATION,
            content=f"关于『{topic}』，我需要你的专业意见..."
        )
        
        self.agent_team.send_message(
            from_agent=agent2_id,
            to_agent=agent1_id,
            msg_type=MessageType.ANSWER,
            content=f"根据我的经验，建议..."
        )
        
        # 显示对话记录
        conversation = self.agent_team.get_conversation_between(agent1_id, agent2_id)
        for msg in conversation:
            print(f"   [{msg.from_agent[:15]}]: {msg.content}")
    
    def get_system_info(self) -> Dict:
        """获取系统信息"""
        return {
            "orchestrator_stats": self.orchestrator.get_stats(),
            "team_status": self.agent_team.get_team_status(),
            "available_templates": list(self.orchestrator.AGENT_TEMPLATES.keys()),
            "custom_templates": list(self.orchestrator.custom_templates.keys()),
        }
    
    def print_system_info(self):
        """打印系统信息"""
        info = self.get_system_info()
        
        print(f"\n{'='*70}")
        print(f"🤖 动态多智能体系统信息")
        print(f"{'='*70}\n")
        
        print("📊 Orchestrator统计:")
        for key, value in info["orchestrator_stats"].items():
            print(f"   {key}: {value}")
        
        print("\n👥 团队状态:")
        for key, value in info["team_status"].items():
            print(f"   {key}: {value}")
        
        print("\n📚 内置Agent模板:")
        for template in info["available_templates"]:
            print(f"   • {template}")
        
        if info["custom_templates"]:
            print("\n🔧 自定义Agent模板:")
            for template in info["custom_templates"]:
                print(f"   • {template}")
        
        # 打印专业skills信息
        from agent_skills_config import get_all_skills_summary
        skills_summary = get_all_skills_summary()
        print(f"\n🎓 专业Skills库:")
        print(f"   总Skills数: {skills_summary['total_skills']} 个")
        print(f"   覆盖领域: {len(skills_summary['by_category'])} 个类别")
        print(f"   来源: Vercel Labs, Anthropic, Microsoft, Trail of Bits等")
        
        print()


def demo():
    """
    演示多智能体系统的各种能力
    """
    system = MultiAgentSystem()
    
    print("\n" + "🎯" * 35)
    print("\n   动态多智能体协作系统演示\n")
    print("🎯" * 35)
    
    # 演示1: 简单任务
    print("\n" + "="*70)
    print("演示 1/4: 简单任务 - 编写一个函数")
    print("="*70)
    system.execute("写一个Python函数，计算列表的平均值")
    
    # 演示2: 中等复杂度任务
    print("\n" + "="*70)
    print("演示 2/4: 中等复杂度 - 开发一个功能模块")
    print("="*70)
    system.execute("设计并实现一个用户注册功能，包含前端表单和后端验证")
    
    # 演示3: 复杂任务
    print("\n" + "="*70)
    print("演示 3/4: 复杂任务 - 完整系统开发")
    print("="*70)
    result = system.execute(
        "开发一个完整的博客系统，包含文章管理、用户认证、评论功能，"
        "需要美观的界面设计和完整的技术文档"
    )
    
    # 演示4: Agent协作
    print("\n" + "="*70)
    print("演示 4/4: Agent间协作")
    print("="*70)
    
    # 获取两个agent进行协作演示
    agents = list(system.agent_team.agents.values())
    if len(agents) >= 2:
        system.chat_between_agents(
            agents[0].id,
            agents[1].id,
            "优化系统性能"
        )
    
    # 显示系统信息
    system.print_system_info()
    
    print("\n" + "="*70)
    print("✨ 所有演示完成!")
    print("="*70 + "\n")


if __name__ == "__main__":
    # 如果带参数运行，执行指定任务
    if len(sys.argv) > 1:
        task = " ".join(sys.argv[1:])
        system = MultiAgentSystem()
        system.execute(task)
    else:
        # 否则运行演示
        demo()
