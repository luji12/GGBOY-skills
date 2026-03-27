#!/usr/bin/env python3
"""
专业Agent Skills配置

为每个agent类型配置来自GitHub高星项目的专业skills
这些skills会增强agent的专业能力
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional


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


# 专业Skills库 - 来自GitHub高星项目
PROFESSIONAL_SKILLS = {
    # ========== 提示词工程专家 (新增) ==========
    "prompt_engineer": [
        Skill(
            name="prompt-engineering-guide",
            source="dair-ai/Prompt-Engineering-Guide",
            description="全面的提示词工程指南，涵盖Chain-of-Thought、Few-shot等核心技术",
            category="prompt-engineering",
            capabilities=["prompt-design", "chain-of-thought", "few-shot", "prompt-optimization"],
            priority=1
        ),
        Skill(
            name="dspy-framework",
            source="stanfordnlp/dspy",
            description="斯坦福声明式框架，自动提示优化（20k+ stars）",
            category="prompt-engineering",
            capabilities=["dspy", "automatic-optimization", "prompt-tuning"],
            priority=1
        ),
        Skill(
            name="automatic-prompt-engineer",
            source="keirp/automatic_prompt_engineer",
            description="自动提示工程师，通过LLM生成和优化提示",
            category="prompt-engineering",
            capabilities=["ape", "auto-prompt", "prompt-generation"],
            priority=2
        ),
        Skill(
            name="prompt-optimization-research",
            source="malteos/awesome-prompt-optimization",
            description="提示词优化研究资源汇总，包含最新论文和方法",
            category="prompt-engineering",
            capabilities=["prompt-research", "optimization-methods", "best-practices"],
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
    
    # ========== 图片分析专家 (新增) ==========
    "image_analyst": [
        Skill(
            name="llava-vision",
            source="haotian-liu/LLaVA",
            description="视觉指令调优框架，理解图像内容并生成描述",
            category="computer-vision",
            capabilities=["image-understanding", "visual-qa", "image-description"],
            priority=1
        ),
        Skill(
            name="clip-multimodal",
            source="openai/CLIP",
            description="OpenAI CLIP模型，图像-文本对齐理解",
            category="computer-vision",
            capabilities=["clip", "image-text-alignment", "zero-shot-classification"],
            priority=1
        ),
        Skill(
            name="vision-language-prompting",
            source="JindongGu/Awesome-Prompting-on-Vision-Language-Model",
            description="视觉语言模型提示方法综述，CLIP、BLIP、GPT-4V等",
            category="computer-vision",
            capabilities=["vlm-prompting", "visual-prompts", "multimodal"],
            priority=2
        ),
        Skill(
            name="vip-llava",
            source="WisconsinAIVision/ViP-LLaVA",
            description="理解视觉提示（矩形、箭头等）的多模态框架",
            category="computer-vision",
            capabilities=["visual-prompts", "spatial-understanding", "image-annotation"],
            priority=2
        ),
        Skill(
            name="bagel-multimodal",
            source="bytedance-seed/bagel",
            description="统一多模态理解和生成模型",
            category="computer-vision",
            capabilities=["multimodal", "image-generation", "image-understanding"],
            priority=3
        ),
        Skill(
            name="image-evaluation",
            source="microsoft/promptbench",
            description="图像提示评估和优化框架",
            category="computer-vision",
            capabilities=["image-evaluation", "prompt-testing", "quality-metrics"],
            priority=3
        ),
    ],
    
    # ========== 多模态内容生成专家 (新增) ==========
    "multimodal_creator": [
        Skill(
            name="text-to-image-prompting",
            source="letsenhance.io",
            description="文本到图像提示优化指南，涵盖DALL-E、Midjourney、Stable Diffusion",
            category="multimodal",
            capabilities=["text-to-image", "dalle", "midjourney", "stable-diffusion"],
            priority=1
        ),
        Skill(
            name="sora-video-generation",
            source="openai/sora",
            description="OpenAI Sora视频生成官方指南",
            category="multimodal",
            capabilities=["video-generation", "sora", "cinematic-prompts"],
            priority=2
        ),
        Skill(
            name="negative-prompt-optimization",
            source="NegOpt-research",
            description="自动负面提示优化，提升图像生成质量",
            category="multimodal",
            capabilities=["negative-prompts", "image-optimization", "quality-improvement"],
            priority=2
        ),
    ],
    # ========== 代码专家 Skills ==========
    "coder": [
        Skill(
            name="vercel-react-best-practices",
            source="vercel-labs/agent-skills",
            description="React和Next.js性能优化指南，包含40+条规则",
            category="frontend",
            install_command="npx skills add vercel-labs/agent-skills --skill react-best-practices",
            capabilities=["react", "nextjs", "performance", "optimization"],
            priority=1
        ),
        Skill(
            name="react-composition-patterns",
            source="vercel-labs/agent-skills",
            description="React组合模式，避免布尔属性泛滥",
            category="frontend",
            install_command="npx skills add vercel-labs/agent-skills --skill composition-patterns",
            capabilities=["react", "architecture", "patterns"],
            priority=2
        ),
        Skill(
            name="code-review",
            source="awesome-agent-skills",
            description="代码审查最佳实践，自动检查代码质量",
            category="quality",
            capabilities=["review", "quality", "best-practices"],
            priority=1
        ),
        Skill(
            name="unit-test-generator",
            source="awesome-agent-skills",
            description="单元测试自动生成，支持多种测试框架",
            category="testing",
            capabilities=["testing", "unittest", "jest", "pytest"],
            priority=2
        ),
        Skill(
            name="python-testing-patterns",
            source="wshobson/agents",
            description="Python测试模式，pytest、mock、TDD",
            category="testing",
            capabilities=["python", "testing", "pytest", "mock", "tdd"],
            priority=2
        ),
        Skill(
            name="trailofbits-security",
            source="trailofbits/skills",
            description="安全审计技能，由Trail of Bits提供",
            category="security",
            capabilities=["security", "audit", "vulnerability"],
            priority=1
        ),
        Skill(
            name="api-doc-generator",
            source="awesome-agent-skills",
            description="API文档自动生成",
            category="documentation",
            capabilities=["api", "documentation", "openapi"],
            priority=3
        ),
    ],
    
    # ========== 设计专家 Skills ==========
    "designer": [
        Skill(
            name="web-design-guidelines",
            source="vercel-labs/agent-skills",
            description="Web界面最佳实践，包含100+条规则，覆盖可访问性和性能",
            category="ui/ux",
            install_command="npx skills add vercel-labs/agent-skills --skill web-design-guidelines",
            capabilities=["ui", "ux", "accessibility", "performance", "design-system"],
            priority=1
        ),
        Skill(
            name="frontend-design",
            source="anthropics/skills",
            description="前端UI设计最佳实践",
            category="ui/ux",
            capabilities=["frontend", "ui", "css", "responsive"],
            priority=2
        ),
        Skill(
            name="brand-guidelines",
            source="anthropics/skills",
            description="品牌设计指南",
            category="branding",
            capabilities=["branding", "logo", "visual-identity"],
            priority=2
        ),
        Skill(
            name="algorithmic-art",
            source="anthropics/skills",
            description="算法艺术生成",
            category="creative",
            capabilities=["generative-art", "creative", "visualization"],
            priority=3
        ),
        Skill(
            name="d3-visualization",
            source="awesome-claude-skills",
            description="D3.js数据可视化",
            category="data-viz",
            capabilities=["d3", "visualization", "charts", "data"],
            priority=2
        ),
    ],
    
    # ========== 写作专家 Skills ==========
    "writer": [
        Skill(
            name="doc-coauthoring",
            source="anthropics/skills",
            description="文档协作写作",
            category="documentation",
            capabilities=["writing", "documentation", "collaboration"],
            priority=1
        ),
        Skill(
            name="technical-writing",
            source="microsoft/agent-skills",
            description="技术文档写作规范",
            category="documentation",
            capabilities=["technical-writing", "docs", "api-docs"],
            priority=1
        ),
        Skill(
            name="academic-writing",
            source="best-skills",
            description="高质量学术论文写作",
            category="academic",
            capabilities=["academic", "research", "paper"],
            priority=2
        ),
        Skill(
            name="readme-generator",
            source="awesome-agent-skills",
            description="README文档自动生成",
            category="documentation",
            capabilities=["readme", "markdown", "github"],
            priority=2
        ),
        Skill(
            name="changelog-generator",
            source="awesome-agent-skills",
            description="Changelog自动生成",
            category="documentation",
            capabilities=["changelog", "git", "release"],
            priority=3
        ),
    ],
    
    # ========== 分析专家 Skills ==========
    "analyst": [
        Skill(
            name="data-analysis",
            source="awesome-claude-skills",
            description="数据分析和洞察提取",
            category="data",
            capabilities=["data-analysis", "statistics", "insights"],
            priority=1
        ),
        Skill(
            name="context-engineering",
            source="muratcankoylan/Agent-Skills-for-Context-Engineering",
            description="上下文工程和多智能体架构",
            category="ai",
            capabilities=["context", "prompt-engineering", "llm"],
            priority=1
        ),
        Skill(
            name="performance-analysis",
            source="vercel-labs/agent-skills",
            description="性能分析和优化建议",
            category="performance",
            capabilities=["performance", "profiling", "optimization"],
            priority=2
        ),
    ],
    
    # ========== 架构专家 Skills ==========
    "architect": [
        Skill(
            name="system-design",
            source="awesome-agent-skills",
            description="系统设计和架构模式",
            category="architecture",
            capabilities=["system-design", "architecture", "patterns"],
            priority=1
        ),
        Skill(
            name="microservices-patterns",
            source="awesome-agent-skills",
            description="微服务架构模式",
            category="architecture",
            capabilities=["microservices", "distributed", "scalability"],
            priority=2
        ),
        Skill(
            name="cloud-architecture",
            source="microsoft/agent-skills",
            description="云架构设计，Azure最佳实践",
            category="cloud",
            capabilities=["cloud", "azure", "aws", "gcp"],
            priority=2
        ),
        Skill(
            name="vercel-deploy",
            source="vercel-labs/agent-skills",
            description="Vercel部署最佳实践",
            category="deployment",
            install_command="npx skills add vercel-labs/agent-skills --skill vercel-deploy-claimable",
            capabilities=["deployment", "vercel", "ci-cd"],
            priority=3
        ),
    ],
    
    # ========== DevOps专家 (可动态创建) ==========
    "devops": [
        Skill(
            name="docker-management",
            source="claudebox",
            description="Docker环境管理",
            category="devops",
            capabilities=["docker", "containers", "devops"],
            priority=1
        ),
        Skill(
            name="kubernetes-patterns",
            source="devops-claude-skills",
            description="Kubernetes部署模式",
            category="devops",
            capabilities=["kubernetes", "k8s", "orchestration"],
            priority=2
        ),
        Skill(
            name="ci-cd-pipelines",
            source="claudekit-skills",
            description="CI/CD流水线设计",
            category="devops",
            capabilities=["ci-cd", "github-actions", "automation"],
            priority=1
        ),
    ],
    
    # ========== 安全专家 (可动态创建) ==========
    "security": [
        Skill(
            name="security-audit",
            source="trailofbits/skills",
            description="安全审计和漏洞检测",
            category="security",
            capabilities=["security", "audit", "vulnerability-scanning"],
            priority=1
        ),
        Skill(
            name="secure-coding",
            source="awesome-agent-skills",
            description="安全编码实践",
            category="security",
            capabilities=["secure-coding", "owasp", "best-practices"],
            priority=1
        ),
    ],
    
    # ========== 移动端专家 (可动态创建) ==========
    "mobile": [
        Skill(
            name="react-native-guidelines",
            source="vercel-labs/agent-skills",
            description="React Native最佳实践，16条规则",
            category="mobile",
            install_command="npx skills add vercel-labs/agent-skills --skill react-native-guidelines",
            capabilities=["react-native", "mobile", "ios", "android"],
            priority=1
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
    
    Args:
        agent_type: agent类型
        
    Returns:
        增强后的system prompt
    """
    skills = get_skills_for_agent(agent_type)
    
    if not skills:
        return ""
    
    prompt_parts = ["\n📚 你已装备以下专业技能:\n"]
    
    for i, skill in enumerate(skills[:5], 1):  # 最多显示前5个
        prompt_parts.append(f"{i}. **{skill.name}** - {skill.description}")
        prompt_parts.append(f"   来源: {skill.source}")
        prompt_parts.append(f"   能力: {', '.join(skill.capabilities[:3])}\n")
    
    prompt_parts.append("\n在工作中请优先应用这些专业技能的最佳实践。\n")
    
    return "\n".join(prompt_parts)


# 导出配置
__all__ = [
    'PROFESSIONAL_SKILLS',
    'get_skills_for_agent',
    'get_skill_by_capability',
    'get_all_skills_summary',
    'generate_skill_prompt',
    'Skill',
]


if __name__ == "__main__":
    # 打印skills摘要
    print("=" * 60)
    print("🎓 专业Agent Skills配置")
    print("=" * 60)
    
    summary = get_all_skills_summary()
    print(f"\n📊 统计摘要:")
    print(f"   Agent类型: {summary['total_agent_types']} 种")
    print(f"   总Skills数: {summary['total_skills']} 个")
    
    print(f"\n📁 按Agent类型分布:")
    for agent_type, count in summary['by_agent_type'].items():
        print(f"   • {agent_type}: {count} 个skills")
    
    print(f"\n🏷️ 按类别分布:")
    for category, count in sorted(summary['by_category'].items(), key=lambda x: -x[1]):
        print(f"   • {category}: {count} 个")
    
    print("\n" + "=" * 60)
    print("示例: 代码专家的Skills")
    print("=" * 60)
    
    coder_skills = get_skills_for_agent("coder")
    for skill in coder_skills:
        print(f"\n🔧 {skill.name}")
        print(f"   描述: {skill.description}")
        print(f"   来源: {skill.source}")
        print(f"   能力: {', '.join(skill.capabilities)}")
        if skill.install_command:
            print(f"   安装: {skill.install_command}")
