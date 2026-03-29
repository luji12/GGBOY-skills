#!/usr/bin/env python3
"""
动态多智能体协作系统 - 总代理 (Orchestrator)

核心能力：
1. 分析用户指令，理解意图
2. 将复杂任务拆解为子任务
3. 按需创建专业agent执行子任务
4. 协调agent间通信与协作
5. 整合结果返回给用户
"""

import json
import re
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

from agent_skills_config import (
    get_skills_for_agent,
    get_skill_by_capability,
    generate_skill_prompt,
    get_skill_content,
    Skill
)


class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    BLOCKED = "blocked"  # 借鉴ClawTeam：依赖未满足时阻塞


@dataclass
class SubTask:
    """子任务定义（借鉴ClawTeam任务管理机制）"""
    id: str
    description: str
    required_capability: str  # 所需能力，如 "coding", "design", "writing"
    dependencies: List[str] = field(default_factory=list)  # 依赖的其他子任务ID
    status: TaskStatus = TaskStatus.PENDING
    result: Any = None
    assigned_agent: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    completed_at: Optional[str] = None
    skill_content: Optional[str] = None  # 注入的实际Skill知识内容

    def can_start(self, completed_ids: List[str]) -> bool:
        """检查依赖是否满足，可以开始执行"""
        return all(dep in completed_ids for dep in self.dependencies)

    def mark_completed(self, result: Any = None):
        self.status = TaskStatus.COMPLETED
        self.result = result
        self.completed_at = datetime.now().isoformat()

    def mark_blocked(self):
        self.status = TaskStatus.BLOCKED


@dataclass
class AgentProfile:
    """Agent档案"""
    name: str
    capabilities: List[str]
    description: str
    system_prompt: str


class Orchestrator:
    """
    总代理 - 动态多智能体系统的核心
    """
    
    # 预定义的agent模板库 - 可动态扩展
    AGENT_TEMPLATES = {
        "prompt_engineer": AgentProfile(
            name="提示词工程师",
            capabilities=["prompt-engineering", "prompt-optimization", "chain-of-thought", "few-shot", "dspy"],
            description="专业的提示词工程师，装备斯坦福DSPy、LangChain等顶级框架",
            system_prompt="""你是一名专业的提示词工程师，擅长：
- 设计和优化LLM提示词
- Chain-of-Thought思维链设计
- Few-shot示例工程
- 自动提示优化（DSPy、APE）
- 多模态提示设计
- 提示词评估和测试

工作时请：
1. 深入理解任务需求和模型能力
2. 应用最新的提示工程技术
3. 设计可复用的提示模板
4. 进行系统性的提示优化
5. 评估提示效果和鲁棒性

参考框架：
- Stanford DSPy（声明式提示优化）
- LangChain（提示模板和链）
- Chain-of-Thought Prompting
- Automatic Prompt Engineer
""" + generate_skill_prompt("prompt_engineer")
        ),
        "image_analyst": AgentProfile(
            name="图像分析专家",
            capabilities=["image-analysis", "computer-vision", "multimodal", "visual-understanding", "clip", "llava"],
            description="专业的计算机视觉专家，装备LLaVA、CLIP等顶级视觉模型技能",
            system_prompt="""你是一名专业的图像分析专家，擅长：
- 图像内容理解和描述
- 视觉问答（Visual QA）
- 图像-文本对齐分析
- 多模态内容理解
- 视觉提示设计
- 图像质量评估

工作时请：
1. 仔细观察图像细节
2. 提供准确、全面的图像描述
3. 理解图像中的空间关系和语义
4. 结合文本提示进行深度分析
5. 使用视觉语言模型最佳实践

参考技术：
- LLaVA（视觉指令调优）
- OpenAI CLIP（图像-文本对齐）
- ViP-LLaVA（视觉提示理解）
- GPT-4V多模态能力
""" + generate_skill_prompt("image_analyst")
        ),
        "multimodal_creator": AgentProfile(
            name="多模态内容创作者",
            capabilities=["multimodal", "text-to-image", "video-generation", "content-creation", "prompt-crafting"],
            description="专业的多模态内容创作者，精通DALL-E、Midjourney、Sora等生成工具",
            system_prompt="""你是一名专业的多模态内容创作者，擅长：
- 文本到图像的提示词设计（DALL-E、Midjourney、Stable Diffusion）
- 视频生成提示词优化（Sora）
- 负面提示词优化
- 多模态内容策划
- 视觉叙事和创意表达
- 生成内容质量优化

工作时请：
1. 理解创意意图和目标受众
2. 设计精准的生成提示词
3. 优化负面提示以提升质量
4. 考虑美学和构图原则
5. 迭代优化生成结果

参考工具：
- DALL-E 3
- Midjourney
- Stable Diffusion
- OpenAI Sora
- PromptHero提示库
""" + generate_skill_prompt("multimodal_creator")
        ),
        "coder": AgentProfile(
            name="代码专家",
            capabilities=["coding", "programming", "development", "debugging", "refactoring", "react", "nextjs", "testing", "security"],
            description="专业的软件开发工程师，精通多种编程语言和框架，装备Vercel、Trail of Bits等顶级skills",
            system_prompt="""你是一名资深软件工程师，擅长：
- 编写高质量、可维护的代码
- 代码审查和重构
- 解决复杂的技术问题
- 遵循最佳实践和设计模式
- React/Next.js性能优化（40+条规则）
- 安全编码实践（Trail of Bits标准）
- 自动化测试（pytest、jest、TDD）

工作时请：
1. 先理解需求和约束
2. 提供清晰的实现方案
3. 编写完整可运行的代码
4. 添加必要的注释和文档
5. 应用React最佳实践避免性能陷阱
6. 进行安全审查防止常见漏洞
""" + generate_skill_prompt("coder")
        ),
        "designer": AgentProfile(
            name="设计专家",
            capabilities=["design", "ui", "ux", "visual", "creative", "accessibility", "responsive"],
            description="专业的UI/UX设计师，装备Vercel Web Design Guidelines等顶级设计skills",
            system_prompt="""你是一名专业设计师，擅长：
- UI/UX设计
- 视觉创意和美学
- 设计系统和规范
- 用户体验优化
- Web可访问性（100+条规则）
- 响应式设计
- 品牌设计

工作时请：
1. 理解设计目标和用户群体
2. 提供美观实用的设计方案
3. 考虑可用性和可访问性（WCAG标准）
4. 输出清晰的设计规范
5. 确保设计在不同设备上的适配性
""" + generate_skill_prompt("designer")
        ),
        "writer": AgentProfile(
            name="写作专家",
            capabilities=["writing", "content", "documentation", "copywriting", "technical-writing", "academic"],
            description="专业的内容创作者，装备Anthropic和Microsoft官方文档skills",
            system_prompt="""你是一名专业写作者，擅长：
- 技术文档编写（Microsoft标准）
- 营销文案创作
- 内容结构和逻辑
- 清晰准确的表达
- 学术论文写作
- README和API文档自动生成

工作时请：
1. 理解目标读者和写作目的
2. 组织清晰的结构
3. 使用恰当的语言风格
4. 确保内容准确完整
5. 遵循技术文档最佳实践
""" + generate_skill_prompt("writer")
        ),
        "analyst": AgentProfile(
            name="分析专家",
            capabilities=["analysis", "data", "research", "evaluation", "visualization"],
            description="专业的数据分析师，装备上下文工程和数据可视化skills",
            system_prompt="""你是一名专业分析师，擅长：
- 数据分析和可视化（D3.js）
- 信息收集和研究
- 逻辑推理和评估
- 提供有价值的洞察
- 上下文工程
- 性能分析

工作时请：
1. 明确分析目标和范围
2. 系统地收集和处理信息
3. 使用适当的分析方法
4. 提供清晰、有依据的结论
5. 创建直观的数据可视化
""" + generate_skill_prompt("analyst")
        ),
        "architect": AgentProfile(
            name="架构专家",
            capabilities=["architecture", "system_design", "planning", "strategy", "microservices", "cloud"],
            description="专业的系统架构师，装备系统设计、微服务和云架构skills",
            system_prompt="""你是一名系统架构师，擅长：
- 系统架构设计
- 技术方案规划
- 模块划分和接口设计
- 可扩展性和性能考虑
- 微服务架构模式
- 云架构（Azure/AWS/GCP最佳实践）
- CI/CD流水线设计

工作时请：
1. 理解业务需求和技术约束
2. 设计合理的系统架构
3. 考虑可维护性和扩展性
4. 提供清晰的架构文档
5. 评估技术选型的利弊
""" + generate_skill_prompt("architect")
        ),
    }
    
    def __init__(self):
        self.active_agents: Dict[str, Any] = {}  # 当前活跃的agent
        self.task_history: List[Dict] = []  # 任务历史
        self.custom_templates: Dict[str, AgentProfile] = {}  # 用户自定义的agent模板
    
    def analyze_task(self, user_input: str) -> Dict:
        """
        分析用户指令，提取关键信息
        """
        analysis = {
            "raw_input": user_input,
            "intent": None,
            "complexity": "simple",  # simple, medium, complex
            "domains": [],  # 涉及的领域
            "estimated_subtasks": 1,
        }
        
        # 简单的意图识别逻辑（实际可用LLM增强）
        input_lower = user_input.lower()
        
        # 检测复杂度
        complexity_indicators = {
            "complex": ["系统", "平台", "完整", "全套", "架构", "设计"],
            "medium": ["功能", "模块", "页面", "接口", "优化"],
        }
        
        for level, indicators in complexity_indicators.items():
            if any(ind in input_lower for ind in indicators):
                analysis["complexity"] = level
                break
        
        # 检测领域
        domain_keywords = {
            "coding": ["代码", "程序", "开发", "实现", "函数", "api", "数据库"],
            "design": ["设计", "界面", "ui", "样式", "美观", "布局"],
            "writing": ["文档", "文章", "文案", "写作", "内容", "报告"],
            "analysis": ["分析", "数据", "研究", "评估", "对比"],
        }
        
        for domain, keywords in domain_keywords.items():
            if any(kw in input_lower for kw in keywords):
                analysis["domains"].append(domain)
        
        # 估算子任务数量
        if analysis["complexity"] == "complex":
            analysis["estimated_subtasks"] = 3 + len(analysis["domains"])
        elif analysis["complexity"] == "medium":
            analysis["estimated_subtasks"] = 2
        
        return analysis
    
    def decompose_task(self, user_input: str, analysis: Dict) -> List[SubTask]:
        """
        将任务拆解为子任务
        """
        subtasks = []
        
        # 根据复杂度决定拆解策略
        if analysis["complexity"] == "simple":
            # 简单任务 - 直接执行
            capability = analysis["domains"][0] if analysis["domains"] else "coding"
            subtasks.append(SubTask(
                id="task_001",
                description=user_input,
                required_capability=capability,
                dependencies=[]
            ))
        
        elif analysis["complexity"] == "medium":
            # 中等复杂度 - 拆分为2-3个子任务
            if "coding" in analysis["domains"]:
                subtasks.extend([
                    SubTask(
                        id="task_001",
                        description=f"设计实现方案: {user_input}",
                        required_capability="architecture",
                        dependencies=[]
                    ),
                    SubTask(
                        id="task_002",
                        description=f"编写代码实现: {user_input}",
                        required_capability="coding",
                        dependencies=["task_001"]
                    ),
                ])
            elif "design" in analysis["domains"]:
                subtasks.extend([
                    SubTask(
                        id="task_001",
                        description=f"设计概念和方案: {user_input}",
                        required_capability="design",
                        dependencies=[]
                    ),
                    SubTask(
                        id="task_002",
                        description=f"细化设计并输出规范: {user_input}",
                        required_capability="design",
                        dependencies=["task_001"]
                    ),
                ])
            else:
                subtasks.append(SubTask(
                    id="task_001",
                    description=user_input,
                    required_capability=analysis["domains"][0] if analysis["domains"] else "coding",
                    dependencies=[]
                ))
        
        else:  # complex
            # 复杂任务 - 完整的工作流
            subtasks.extend([
                SubTask(
                    id="task_001",
                    description=f"需求分析和架构设计: {user_input}",
                    required_capability="architecture",
                    dependencies=[]
                ),
                SubTask(
                    id="task_002",
                    description=f"详细设计和技术方案: {user_input}",
                    required_capability="design" if "design" in analysis["domains"] else "architecture",
                    dependencies=["task_001"]
                ),
                SubTask(
                    id="task_003",
                    description=f"核心功能实现: {user_input}",
                    required_capability="coding",
                    dependencies=["task_002"]
                ),
                SubTask(
                    id="task_004",
                    description=f"代码审查和优化: {user_input}",
                    required_capability="coding",
                    dependencies=["task_003"]
                ),
            ])
            
            # 如果有写作需求，添加文档任务
            if "writing" in analysis["domains"]:
                subtasks.append(SubTask(
                    id="task_005",
                    description=f"编写文档和使用说明: {user_input}",
                    required_capability="writing",
                    dependencies=["task_004"]
                ))
        
        return subtasks
    
    def find_or_create_agent(self, capability: str) -> AgentProfile:
        """
        根据能力需求查找或创建agent
        """
        # 1. 先在模板库中查找匹配的agent
        for template in {**self.AGENT_TEMPLATES, **self.custom_templates}.values():
            if capability in template.capabilities:
                return template
        
        # 2. 如果没有匹配的，动态创建一个新agent
        return self._create_dynamic_agent(capability)
    
    def _create_dynamic_agent(self, capability: str) -> AgentProfile:
        """
        动态创建一个通用agent来处理特定能力需求
        会尝试从skills库中查找匹配的专业skill
        """
        # 尝试查找匹配的专业skill
        matched_skill = get_skill_by_capability(capability)
        
        if matched_skill:
            # 使用专业skill创建agent
            agent_name = matched_skill.name.replace('-', ' ').title() + "专家"
            skill_prompt = f"""
📚 你已装备专业Skill: {matched_skill.name}
来源: {matched_skill.source}
描述: {matched_skill.description}
能力: {', '.join(matched_skill.capabilities)}

请在工作中充分应用此skill的最佳实践。
"""
        else:
            # 创建通用agent
            agent_name = f"{capability.capitalize()}专家"
            skill_prompt = ""
        
        new_agent = AgentProfile(
            name=agent_name,
            capabilities=[capability] + (matched_skill.capabilities if matched_skill else []),
            description=f"专业的{capability}领域agent，按需创建" + (f"，装备{matched_skill.name} skill" if matched_skill else ""),
            system_prompt=f"""你是一名{capability}领域的专家。

你的职责是：
1. 深入理解用户的{capability}相关需求
2. 运用你的专业知识提供最佳解决方案
3. 确保输出质量符合专业标准
4. 如有需要，主动寻求其他agent的协助

请始终保持专业、高效、可靠的工作态度。
{skill_prompt}
"""
        )
        
        # 保存到自定义模板库
        template_id = f"dynamic_{capability}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.custom_templates[template_id] = new_agent
        
        if matched_skill:
            print(f"🆕 动态创建了新agent: {agent_name} (ID: {template_id})")
            print(f"   ✨ 已装备专业skill: {matched_skill.name} ({matched_skill.source})")
        else:
            print(f"🆕 动态创建了新agent: {agent_name} (ID: {template_id})")
        
        return new_agent
    
    def execute_task(self, user_input: str) -> Dict:
        """
        执行用户任务的完整流程
        """
        print(f"\n{'='*60}")
        print(f"🎯 收到任务: {user_input}")
        print(f"{'='*60}\n")
        
        # 1. 分析任务
        print("📊 正在分析任务...")
        analysis = self.analyze_task(user_input)
        print(f"   复杂度: {analysis['complexity']}")
        print(f"   涉及领域: {', '.join(analysis['domains']) if analysis['domains'] else '通用'}")
        print(f"   预估子任务: {analysis['estimated_subtasks']}个\n")
        
        # 2. 拆解任务
        print("🔨 正在拆解任务...")
        subtasks = self.decompose_task(user_input, analysis)
        print(f"   已拆解为 {len(subtasks)} 个子任务:\n")
        for st in subtasks:
            deps = f" (依赖: {', '.join(st.dependencies)})" if st.dependencies else ""
            print(f"   • [{st.required_capability}] {st.description}{deps}")
        print()
        
        # 3. 为每个子任务分配agent
        print("👥 正在分配agent...")
        agent_assignments = {}
        for st in subtasks:
            agent = self.find_or_create_agent(st.required_capability)
            st.assigned_agent = agent.name
            if agent.name not in agent_assignments:
                agent_assignments[agent.name] = agent
                print(f"   ✅ {agent.name} - 负责 {st.required_capability} 相关任务")
        print(f"\n   共启动 {len(agent_assignments)} 个专业agent\n")
        
        # 4. 模拟执行（实际实现中这里会调用真实的agent）
        print("⚙️  正在执行子任务...\n")
        results = []
        for st in subtasks:
            print(f"   📝 执行: {st.description}")
            print(f"      执行者: {st.assigned_agent}")
            
            # 检查依赖是否完成
            pending_deps = [d for d in st.dependencies if not any(
                t.id == d and t.status == TaskStatus.COMPLETED for t in subtasks
            )]
            
            if pending_deps:
                print(f"      ⏳ 等待依赖: {', '.join(pending_deps)}")
            else:
                st.status = TaskStatus.COMPLETED
                st.result = f"[{st.assigned_agent}] 已完成: {st.description}"
                print(f"      ✓ 完成\n")
                results.append(st.result)
        
        # 5. 整合结果
        print("📦 正在整合结果...")
        final_result = {
            "task": user_input,
            "analysis": analysis,
            "subtasks_completed": len([s for s in subtasks if s.status == TaskStatus.COMPLETED]),
            "total_subtasks": len(subtasks),
            "agents_involved": list(agent_assignments.keys()),
            "results": results,
            "summary": f"任务已完成，共使用{len(agent_assignments)}个专业agent，完成{len(subtasks)}个子任务。"
        }
        
        # 记录历史
        self.task_history.append({
            "timestamp": datetime.now().isoformat(),
            "input": user_input,
            "result": final_result
        })
        
        print(f"\n{'='*60}")
        print(f"✅ 任务完成!")
        print(f"{'='*60}\n")
        
        return final_result
    
    def get_stats(self) -> Dict:
        """
        获取系统统计信息
        """
        return {
            "total_tasks": len(self.task_history),
            "built_in_agents": len(self.AGENT_TEMPLATES),
            "custom_agents": len(self.custom_templates),
            "total_agents": len(self.AGENT_TEMPLATES) + len(self.custom_templates),
        }


# 使用示例
if __name__ == "__main__":
    orchestrator = Orchestrator()
    
    # 测试不同复杂度的任务
    test_tasks = [
        "写一个Python函数计算斐波那契数列",  # 简单任务
        "设计一个用户登录功能",  # 中等任务
        "开发一个完整的任务管理系统，包含前端界面和后端API",  # 复杂任务
    ]
    
    for task in test_tasks:
        result = orchestrator.execute_task(task)
        print(f"\n结果摘要: {result['summary']}\n")
        print("-" * 60)
    
    # 显示统计
    stats = orchestrator.get_stats()
    print(f"\n📈 系统统计:")
    print(f"   完成任务: {stats['total_tasks']}")
    print(f"   内置agent模板: {stats['built_in_agents']}")
    print(f"   动态创建agent: {stats['custom_agents']}")
