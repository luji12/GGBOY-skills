#!/usr/bin/env python3
"""
专业Agent Skills配置

为每个agent类型配置来自GitHub高星项目的专业skills
这些skills会增强agent的专业能力
"""

import os
from dataclasses import dataclass, field
from typing import List, Dict, Optional

# Skills本地文件根目录
SKILLS_DIR = os.path.join(os.path.dirname(__file__), "skills")


@dataclass
class Skill:
    """Skill定义"""
    name: str
    source: str  # GitHub仓库或来源
    description: str
    category: str
    install_command: Optional[str] = None
    capabilities: List[str] = field(default_factory=list)
    priority: int = 1  # 优先级，1-5，数字越小越优先
    local_skill_path: Optional[str] = None  # 本地SKILL.md路径

    def load_skill_content(self) -> Optional[str]:
        """加载本地Skill文件内容，供Agent实际读取使用"""
        if self.local_skill_path and os.path.exists(self.local_skill_path):
            with open(self.local_skill_path, "r", encoding="utf-8") as f:
                return f.read()
        return None

    def has_local_content(self) -> bool:
        """检查是否有本地Skill内容"""
        return (self.local_skill_path is not None and 
                os.path.exists(self.local_skill_path))


# 专业Skills库 - 来自GitHub高星项目，配有本地实际内容文件
PROFESSIONAL_SKILLS = {
    # ========== 提示词工程专家 ==========
    "prompt_engineer": [
        Skill(
            name="prompt-engineering-guide",
            source="dair-ai/Prompt-Engineering-Guide",
            description="全面的提示词工程指南，涵盖Chain-of-Thought、Few-shot等核心技术",
            category="prompt-engineering",
            capabilities=["prompt-design", "chain-of-thought", "few-shot", "prompt-optimization"],
            priority=1,
            local_skill_path=os.path.join(SKILLS_DIR, "prompt-engineering", "SKILL.md")
        ),
        Skill(
            name="dspy-framework",
            source="stanfordnlp/dspy",
            description="斯坦福声明式框架，自动提示优化（20k+ stars）",
            category="prompt-engineering",
            capabilities=["dspy", "automatic-optimization", "prompt-tuning"],
            priority=2
        ),
        Skill(
            name="langchain-prompts",
            source="langchain-ai/langchain",
            description="LangChain提示模板和链系统（90k+ stars）",
            category="prompt-engineering",
            capabilities=["langchain", "prompt-templates", "chains"],
            priority=3
        ),
    ],

    # ========== 图像分析专家 ==========
    "image_analyst": [
        Skill(
            name="image-analysis-expert",
            source="haotian-liu/LLaVA + openai/CLIP",
            description="视觉要素提取、画面构成分析、分镜单帧描述",
            category="computer-vision",
            capabilities=["image-understanding", "visual-qa", "image-description", "spatial-understanding"],
            priority=1,
            local_skill_path=os.path.join(SKILLS_DIR, "image-analysis", "SKILL.md")
        ),
        Skill(
            name="vision-language-prompting",
            source="JindongGu/Awesome-Prompting-on-Vision-Language-Model",
            description="视觉语言模型提示方法综述，CLIP、BLIP、GPT-4V等",
            category="computer-vision",
            capabilities=["vlm-prompting", "visual-prompts", "multimodal"],
            priority=2
        ),
    ],

    # ========== 多模态内容创作专家 ==========
    "multimodal_creator": [
        Skill(
            name="multimodal-creation-expert",
            source="DALL-E/Midjourney/StableDiffusion/Sora Best Practices",
            description="文生图、文生视频提示词生成，分镜单帧提示词规范",
            category="multimodal",
            capabilities=["text-to-image", "video-generation", "cinematic-prompts", "negative-prompts"],
            priority=1,
            local_skill_path=os.path.join(SKILLS_DIR, "multimodal-creation", "SKILL.md")
        ),
    ],

    # ========== 代码专家 Skills ==========
    "coder": [
        Skill(
            name="code-expert",
            source="vercel-labs/agent-skills + trailofbits/skills",
            description="代码审查、安全审计、React/Python最佳实践，含OWASP检查清单",
            category="coding",
            capabilities=["coding", "debugging", "security-audit", "performance", "testing", "code-review"],
            priority=1,
            local_skill_path=os.path.join(SKILLS_DIR, "code-expert", "SKILL.md")
        ),
        Skill(
            name="react-composition-patterns",
            source="vercel-labs/agent-skills",
            description="React组合模式，避免布尔属性泛滥",
            category="frontend",
            capabilities=["react", "architecture", "patterns"],
            priority=2
        ),
    ],

    # ========== 设计专家 Skills ==========
    "designer": [
        Skill(
            name="design-expert",
            source="vercel-labs/web-interface-guidelines",
            description="Web界面最佳实践，色彩/排版/间距/组件/可访问性完整规范",
            category="ui/ux",
            capabilities=["ui", "ux", "accessibility", "design-system", "visual-design"],
            priority=1,
            local_skill_path=os.path.join(SKILLS_DIR, "design-expert", "SKILL.md")
        ),
    ],

    # ========== 写作专家 Skills ==========
    "writer": [
        Skill(
            name="writing-expert",
            source="Microsoft Technical Writing + Anthropic Docs",
            description="技术文档、报告、文案、脚本写作全流程规范",
            category="documentation",
            capabilities=["technical-writing", "documentation", "copywriting", "storytelling"],
            priority=1,
            local_skill_path=os.path.join(SKILLS_DIR, "writing-expert", "SKILL.md")
        ),
    ],

    # ========== 分析专家 Skills ==========
    "analyst": [
        Skill(
            name="analysis-expert",
            source="Context Engineering + Data Analysis Best Practices",
            description="数据分析、竞品分析、研究报告、MECE/金字塔原理等分析框架",
            category="analysis",
            capabilities=["data-analysis", "competitive-analysis", "research", "context-engineering"],
            priority=1,
            local_skill_path=os.path.join(SKILLS_DIR, "analysis-expert", "SKILL.md")
        ),
    ],

    # ========== 架构专家 Skills ==========
    "architect": [
        Skill(
            name="architecture-expert",
            source="System Design Best Practices + Cloud Architecture",
            description="系统设计、数据库选型、API设计、微服务、扩展性设计完整指南",
            category="architecture",
            capabilities=["system-design", "microservices", "api-design", "database-design", "scalability"],
            priority=1,
            local_skill_path=os.path.join(SKILLS_DIR, "architecture-expert", "SKILL.md")
        ),
    ],

    # ========== DevOps专家 ==========
    "devops": [
        Skill(
            name="devops-expert",
            source="Docker/Kubernetes/GitHub Actions Best Practices",
            description="Docker优化、K8s部署、CI/CD流水线、监控告警完整指南",
            category="devops",
            capabilities=["docker", "kubernetes", "ci-cd", "monitoring", "automation"],
            priority=1,
            local_skill_path=os.path.join(SKILLS_DIR, "devops-expert", "SKILL.md")
        ),
    ],

    # ========== 安全专家 ==========
    "security": [
        Skill(
            name="security-expert",
            source="OWASP Top 10 + Trail of Bits",
            description="OWASP Top 10审查清单、安全编码规范、漏洞检测方法",
            category="security",
            capabilities=["security-audit", "owasp", "secure-coding", "vulnerability-scanning"],
            priority=1,
            local_skill_path=os.path.join(SKILLS_DIR, "security-expert", "SKILL.md")
        ),
    ],

    # ========== 移动端专家 ==========
    "mobile": [
        Skill(
            name="mobile-expert",
            source="vercel-labs/agent-skills react-native-guidelines",
            description="React Native最佳实践，性能优化、平台差异处理、状态管理",
            category="mobile",
            capabilities=["react-native", "mobile", "ios", "android", "performance"],
            priority=1,
            local_skill_path=os.path.join(SKILLS_DIR, "mobile-expert", "SKILL.md")
        ),
    ],
}


def get_skills_for_agent(agent_type: str) -> List[Skill]:
    """
    获取指定agent类型的所有skills
    
    Args:
        agent_type: agent类型，如 "coder", "designer", "writer"等
        
    Returns:
        Skill列表，按优先级排序
    """
    skills = PROFESSIONAL_SKILLS.get(agent_type, [])
    return sorted(skills, key=lambda s: s.priority)


def get_skill_by_capability(capability: str) -> Optional[Skill]:
    """
    根据能力查找最合适的skill
    
    Args:
        capability: 能力关键词
        
    Returns:
        最匹配的Skill或None
    """
    best_match = None
    best_priority = float('inf')
    
    for agent_skills in PROFESSIONAL_SKILLS.values():
        for skill in agent_skills:
            if capability.lower() in [c.lower() for c in skill.capabilities]:
                if skill.priority < best_priority:
                    best_match = skill
                    best_priority = skill.priority
    
    return best_match


def get_all_skills_summary() -> Dict[str, int]:
    """
    获取所有skills的统计摘要
    
    Returns:
        统计信息字典
    """
    summary = {
        "total_agent_types": len(PROFESSIONAL_SKILLS),
        "total_skills": sum(len(skills) for skills in PROFESSIONAL_SKILLS.values()),
        "by_category": {},
        "by_agent_type": {k: len(v) for k, v in PROFESSIONAL_SKILLS.items()},
    }
    
    # 按类别统计
    category_count = {}
    for skills in PROFESSIONAL_SKILLS.values():
        for skill in skills:
            category_count[skill.category] = category_count.get(skill.category, 0) + 1
    summary["by_category"] = category_count
    
    return summary


def generate_skill_prompt(agent_type: str) -> str:
    """
    为指定agent类型生成包含skills的system prompt
    优先读取本地SKILL.md文件内容，让Agent真正掌握专业知识
    
    Args:
        agent_type: agent类型
        
    Returns:
        增强后的system prompt（含实际知识内容）
    """
    skills = get_skills_for_agent(agent_type)
    
    if not skills:
        return ""
    
    prompt_parts = [f"\n# 📚 {agent_type} 专业技能包\n"]
    
    for i, skill in enumerate(skills[:3], 1):  # 最多加载前3个skill的完整内容
        content = skill.load_skill_content()
        if content:
            # 有本地内容，直接注入完整知识
            prompt_parts.append(f"\n## Skill {i}: {skill.name}\n")
            prompt_parts.append(content)
            prompt_parts.append("\n---\n")
        else:
            # 没有本地内容，只显示元信息
            prompt_parts.append(f"\n## Skill {i}: {skill.name}")
            prompt_parts.append(f"- 描述: {skill.description}")
            prompt_parts.append(f"- 来源: {skill.source}")
            prompt_parts.append(f"- 能力: {', '.join(skill.capabilities[:3])}\n")
    
    prompt_parts.append("\n> 以上是你的专业技能知识库，执行任务时请严格按照这些规范和方法操作。\n")
    
    return "\n".join(prompt_parts)


def get_skill_content(agent_type: str, skill_name: str) -> Optional[str]:
    """
    直接获取指定skill的完整内容（供Agent读取使用）
    
    Args:
        agent_type: agent类型
        skill_name: skill名称
        
    Returns:
        Skill的完整Markdown内容
    """
    skills = get_skills_for_agent(agent_type)
    for skill in skills:
        if skill.name == skill_name:
            return skill.load_skill_content()
    return None


def list_available_skills() -> Dict[str, List[Dict]]:
    """
    列出所有可用的Skills及其状态（是否有本地内容）
    
    Returns:
        按agent类型分组的skill状态信息
    """
    result = {}
    for agent_type, skills in PROFESSIONAL_SKILLS.items():
        result[agent_type] = []
        for skill in skills:
            result[agent_type].append({
                "name": skill.name,
                "description": skill.description,
                "has_content": skill.has_local_content(),
                "capabilities": skill.capabilities,
            })
    return result


# 导出配置
__all__ = [
    'PROFESSIONAL_SKILLS',
    'SKILLS_DIR',
    'get_skills_for_agent',
    'get_skill_by_capability',
    'get_all_skills_summary',
    'generate_skill_prompt',
    'get_skill_content',
    'list_available_skills',
    'Skill',
]


if __name__ == "__main__":
    # 打印skills摘要及本地内容状态
    print("=" * 60)
    print("🎓 专业Agent Skills配置")
    print("=" * 60)
    
    available = list_available_skills()
    for agent_type, skills in available.items():
        has_content = sum(1 for s in skills if s["has_content"])
        print(f"\n🤖 {agent_type}: {len(skills)} 个Skills，{has_content} 个有本地内容")
        for skill in skills:
            status = "✅" if skill["has_content"] else "📋"
            print(f"   {status} {skill['name']}")
    
    print("\n" + "=" * 60)
    print("示例: 加载多模态创作者的完整Skill内容")
    print("=" * 60)
    content = get_skill_content("multimodal_creator", "multimodal-creation-expert")
    if content:
        print(content[:500] + "...")
    else:
        print("未找到本地内容")
