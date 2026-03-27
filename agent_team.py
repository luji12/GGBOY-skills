#!/usr/bin/env python3
"""
动态Agent团队管理器

负责：
1. 创建和管理专业agent团队
2. 协调agent间的通信
3. 处理agent的生命周期
"""

import json
from typing import Dict, List, Optional, Callable
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import uuid


class MessageType(Enum):
    """消息类型"""
    TASK = "task"           # 任务分配
    RESULT = "result"       # 任务结果
    QUESTION = "question"   # 询问
    ANSWER = "answer"       # 回答
    COLLABORATION = "collab"  # 协作请求
    BROADCAST = "broadcast"  # 广播


@dataclass
class Message:
    """Agent间通信消息"""
    id: str
    from_agent: str
    to_agent: str  # "all" 表示广播
    type: MessageType
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    context: Dict = field(default_factory=dict)


@dataclass
class Agent:
    """Agent实例"""
    id: str
    name: str
    profile: "AgentProfile"
    status: str = "idle"  # idle, busy, offline
    current_task: Optional[str] = None
    message_history: List[Message] = field(default_factory=list)
    capabilities_used: List[str] = field(default_factory=list)


class AgentTeam:
    """
    Agent团队管理器
    管理多个agent的协作
    """
    
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.message_log: List[Message] = []
        self.message_handlers: Dict[str, Callable] = {}
    
    def create_agent(self, profile: "AgentProfile") -> Agent:
        """
        创建一个新的agent实例
        """
        agent_id = f"{profile.name}_{uuid.uuid4().hex[:8]}"
        agent = Agent(
            id=agent_id,
            name=profile.name,
            profile=profile
        )
        self.agents[agent_id] = agent
        print(f"   🆕 创建agent: {profile.name} (ID: {agent_id})")
        return agent
    
    def get_agent(self, agent_id: str) -> Optional[Agent]:
        """获取agent实例"""
        return self.agents.get(agent_id)
    
    def find_agents_by_capability(self, capability: str) -> List[Agent]:
        """根据能力查找agent"""
        return [
            agent for agent in self.agents.values()
            if capability in agent.profile.capabilities
        ]
    
    def send_message(
        self,
        from_agent: str,
        to_agent: str,
        msg_type: MessageType,
        content: str,
        context: Dict = None
    ) -> Message:
        """
        发送消息
        to_agent: "all" 表示广播给所有agent
        """
        msg = Message(
            id=str(uuid.uuid4()),
            from_agent=from_agent,
            to_agent=to_agent,
            type=msg_type,
            content=content,
            context=context or {}
        )
        
        self.message_log.append(msg)
        
        # 如果是广播，发送给所有agent（除了发送者）
        if to_agent == "all":
            for agent in self.agents.values():
                if agent.id != from_agent:
                    agent.message_history.append(msg)
        else:
            # 发送给特定agent
            target = self.agents.get(to_agent)
            if target:
                target.message_history.append(msg)
        
        # 触发消息处理器
        self._handle_message(msg)
        
        return msg
    
    def _handle_message(self, msg: Message):
        """处理消息"""
        handler = self.message_handlers.get(msg.type.value)
        if handler:
            handler(msg)
    
    def register_handler(self, msg_type: MessageType, handler: Callable):
        """注册消息处理器"""
        self.message_handlers[msg_type.value] = handler
    
    def get_conversation_between(self, agent1: str, agent2: str) -> List[Message]:
        """获取两个agent之间的对话历史"""
        return [
            msg for msg in self.message_log
            if (msg.from_agent == agent1 and msg.to_agent == agent2) or
               (msg.from_agent == agent2 and msg.to_agent == agent1)
        ]
    
    def broadcast(self, from_agent: str, content: str, context: Dict = None):
        """广播消息给所有agent"""
        return self.send_message(from_agent, "all", MessageType.BROADCAST, content, context)
    
    def request_collaboration(
        self,
        from_agent: str,
        capability: str,
        task_description: str
    ) -> Optional[Agent]:
        """
        请求具有特定能力的agent协作
        """
        available_agents = [
            agent for agent in self.find_agents_by_capability(capability)
            if agent.status == "idle" and agent.id != from_agent
        ]
        
        if available_agents:
            # 选择第一个可用的agent
            collaborator = available_agents[0]
            self.send_message(
                from_agent=from_agent,
                to_agent=collaborator.id,
                msg_type=MessageType.COLLABORATION,
                content=f"请求协作: {task_description}",
                context={"requested_capability": capability}
            )
            return collaborator
        
        return None
    
    def get_team_status(self) -> Dict:
        """获取团队状态"""
        return {
            "total_agents": len(self.agents),
            "idle_agents": len([a for a in self.agents.values() if a.status == "idle"]),
            "busy_agents": len([a for a in self.agents.values() if a.status == "busy"]),
            "total_messages": len(self.message_log),
        }
    
    def print_conversation_log(self):
        """打印对话日志"""
        print(f"\n📨 Agent通信记录 ({len(self.message_log)} 条消息):")
        print("-" * 60)
        for msg in self.message_log:
            arrow = "→" if msg.to_agent != "all" else "⇢"
            target = "所有人" if msg.to_agent == "all" else msg.to_agent[:20]
            print(f"[{msg.timestamp.strftime('%H:%M:%S')}] {msg.from_agent[:15]} {arrow} {target}")
            print(f"   [{msg.type.value}] {msg.content[:60]}...")
        print("-" * 60)


# 协作场景示例
if __name__ == "__main__":
    from orchestrator import Orchestrator, AgentProfile
    
    # 创建团队
    team = AgentTeam()
    orchestrator = Orchestrator()
    
    # 创建几个专业agent
    coder_profile = orchestrator.find_or_create_agent("coding")
    designer_profile = orchestrator.find_or_create_agent("design")
    writer_profile = orchestrator.find_or_create_agent("writing")
    
    coder = team.create_agent(coder_profile)
    designer = team.create_agent(designer_profile)
    writer = team.create_agent(writer_profile)
    
    print("\n" + "="*60)
    print("模拟协作场景: 开发一个带界面的应用")
    print("="*60 + "\n")
    
    # 场景1: 架构师分配任务
    print("1️⃣ 架构师分配任务给设计师和程序员\n")
    team.send_message(
        from_agent="architect_001",
        to_agent=designer.id,
        msg_type=MessageType.TASK,
        content="请设计一个简洁的用户登录界面"
    )
    
    team.send_message(
        from_agent="architect_001",
        to_agent=coder.id,
        msg_type=MessageType.TASK,
        content="请实现用户登录的后端API"
    )
    
    # 场景2: 程序员向设计师询问UI细节
    print("2️⃣ 程序员询问设计师UI细节\n")
    team.send_message(
        from_agent=coder.id,
        to_agent=designer.id,
        msg_type=MessageType.QUESTION,
        content="登录按钮的颜色和尺寸是什么？"
    )
    
    # 场景3: 设计师回复
    print("3️⃣ 设计师回复\n")
    team.send_message(
        from_agent=designer.id,
        to_agent=coder.id,
        msg_type=MessageType.ANSWER,
        content="主按钮: 蓝色 #1890ff, 尺寸 120x40px; 次要按钮: 灰色"
    )
    
    # 场景4: 程序员请求写作专家协助编写文档
    print("4️⃣ 程序员请求写作专家协助\n")
    collaborator = team.request_collaboration(
        from_agent=coder.id,
        capability="writing",
        task_description="为登录API编写技术文档"
    )
    
    if collaborator:
        print(f"   ✅ 找到协作者: {collaborator.name}\n")
    
    # 场景5: 广播通知
    print("5️⃣ 项目经理广播进度更新\n")
    team.broadcast(
        from_agent="pm_001",
        content="第一阶段开发完成，准备进入测试阶段",
        context={"phase": "development", "status": "completed"}
    )
    
    # 打印团队状态
    print("\n" + "="*60)
    print("团队状态:")
    status = team.get_team_status()
    for key, value in status.items():
        print(f"   {key}: {value}")
    
    # 打印通信记录
    team.print_conversation_log()
