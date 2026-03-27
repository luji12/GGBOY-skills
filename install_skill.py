#!/usr/bin/env python3
"""
多智能体协作系统 - Skill安装脚本

安装方法:
1. 复制到目标项目的 .claude/skills/ 目录
2. 或复制到全局 ~/.claude/skills/ 目录
"""

import os
import shutil
import sys
from pathlib import Path


def install_skill(target_dir=None):
    """
    安装skill到指定目录
    
    Args:
        target_dir: 目标目录，默认为 ~/.claude/skills/multi-agent-orchestrator/
    """
    if target_dir is None:
        # 默认安装到用户目录
        home = Path.home()
        target_dir = home / ".claude" / "skills" / "multi-agent-orchestrator"
    else:
        target_dir = Path(target_dir)
    
    # 当前目录（skill所在目录）
    source_dir = Path(__file__).parent
    
    print(f"📦 安装多智能体协作系统Skill")
    print(f"   源目录: {source_dir}")
    print(f"   目标目录: {target_dir}")
    
    # 创建目标目录
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # 需要复制的文件
    files_to_copy = [
        "SKILL.md",
        "README.md",
        "multi_agent_system.py",
        "orchestrator.py",
        "agent_team.py",
        "agent_skills_config.py",
    ]
    
    # 复制文件
    for file_name in files_to_copy:
        source_file = source_dir / file_name
        target_file = target_dir / file_name
        
        if source_file.exists():
            shutil.copy2(source_file, target_file)
            print(f"   ✅ {file_name}")
        else:
            print(f"   ⚠️  跳过 {file_name} (不存在)")
    
    print(f"\n✅ 安装完成!")
    print(f"\n💡 使用方法:")
    print(f"   from multi_agent_system import MultiAgentSystem")
    print(f"   system = MultiAgentSystem()")
    print(f"   result = system.execute('你的任务')")
    
    return target_dir


def install_to_project(project_path):
    """安装到指定项目"""
    project_path = Path(project_path)
    skill_dir = project_path / ".claude" / "skills" / "multi-agent-orchestrator"
    return install_skill(skill_dir)


def main():
    """主函数"""
    if len(sys.argv) > 1:
        # 安装到指定项目
        project_path = sys.argv[1]
        install_to_project(project_path)
    else:
        # 安装到全局
        install_skill()


if __name__ == "__main__":
    main()
