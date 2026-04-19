#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
LongRiver 环境验证和修复脚本
用于检查依赖版本兼容性和环境问题
"""

import sys
import subprocess
from typing import Tuple, List, Dict

class Colors:
    """ANSI 颜色代码"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

def print_status(status: str, message: str):
    """打印带颜色的状态信息"""
    if status == "✅":
        print(f"{Colors.GREEN}{status} {message}{Colors.RESET}")
    elif status == "❌":
        print(f"{Colors.RED}{status} {message}{Colors.RESET}")
    elif status == "⚠️":
        print(f"{Colors.YELLOW}{status} {message}{Colors.RESET}")
    else:
        print(f"{Colors.BLUE}ℹ️  {message}{Colors.RESET}")

def check_python_version() -> bool:
    """检查Python版本"""
    version = sys.version_info
    min_version = (3, 8)
    
    if version >= min_version:
        print_status("✅", f"Python 版本: {version.major}.{version.minor}.{version.micro} (支持)")
        return True
    else:
        print_status("❌", f"Python 版本: {version.major}.{version.minor} (需要3.8+)")
        return False

def get_installed_packages() -> Dict[str, str]:
    """获取已安装的包及版本"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list", "--format", "json"],
            capture_output=True,
            text=True,
            timeout=30
        )
        import json
        packages = json.loads(result.stdout)
        return {pkg['name'].lower(): pkg['version'] for pkg in packages}
    except Exception as e:
        print_status("❌", f"无法获取包列表: {e}")
        return {}

def check_critical_packages(packages: Dict[str, str]) -> Tuple[bool, List[str]]:
    """检查关键包的兼容性"""
    critical_checks = {
        'flask': ('3.0.0', '3.0.1'),
        'numpy': ('1.24.0', '1.26.4'),
        'pandas': ('2.0.0', '2.1.3'),
        'tensorflow': ('2.13.0', '2.14.0'),
        'scikit-learn': ('1.0.0', '1.3.2'),
    }
    
    issues = []
    all_ok = True
    
    # 检查可能的问题包
    problematic = ['pathlib', 'keras==2.4', 'autokeras==1.0']
    
    for name in packages:
        for prob in problematic:
            if prob.split('==')[0].lower() in name:
                version = packages[name]
                print_status("❌", f"找到问题包: {name}=={version} (应删除)")
                issues.append(name)
                all_ok = False
    
    for package, (min_ver, recommended) in critical_checks.items():
        if package in packages:
            print_status("✅", f"{package}: {packages[package]}")
        else:
            print_status("⚠️", f"{package}: 未安装")
            all_ok = False
    
    return all_ok and len(issues) == 0, issues

def check_database_modules() -> bool:
    """检查数据库相关模块"""
    try:
        import sqlite3
        print_status("✅", "sqlite3: 内置模块可用")
        return True
    except ImportError:
        print_status("❌", "sqlite3: 未找到")
        return False

def check_flask_app() -> bool:
    """检查Flask应用文件"""
    import os
    
    required_files = [
        'app.py',
        'requirements.txt',
        'requirements_fixed.txt',
        'Builder/__init__.py',
        'Controller/Controller.py',
        'Database/ProjectsSQL.py',
        'Tools/__init__.py',
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print_status("✅", f"文件存在: {file}")
        else:
            print_status("❌", f"文件缺失: {file}")
            all_exist = False
    
    return all_exist

def main():
    """主检查流程"""
    print(f"\n{Colors.BLUE}{'='*60}")
    print("LongRiver 0.4.3 - 兼容性检查工具")
    print(f"{'='*60}{Colors.RESET}\n")
    
    # 1. Python版本
    print(f"{Colors.BLUE}📋 检查 1: Python 版本{Colors.RESET}")
    py_ok = check_python_version()
    print()
    
    # 2. 获取已安装包
    print(f"{Colors.BLUE}📋 检查 2: 获取已安装的包{Colors.RESET}")
    packages = get_installed_packages()
    print_status("✅", f"找到 {len(packages)} 个已安装包")
    print()
    
    # 3. 检查关键包
    print(f"{Colors.BLUE}📋 检查 3: 关键包兼容性{Colors.RESET}")
    pkg_ok, issues = check_critical_packages(packages)
    if issues:
        print_status("⚠️", "检测到以下问题包需要移除:")
        for issue in issues:
            print(f"   - {issue}")
        print(f"\n建议: pip uninstall -y {' '.join(issues)}")
    print()
    
    # 4. 数据库模块
    print(f"{Colors.BLUE}📋 检查 4: 数据库模块{Colors.RESET}")
    db_ok = check_database_modules()
    print()
    
    # 5. Flask应用文件
    print(f"{Colors.BLUE}📋 检查 5: 应用文件{Colors.RESET}")
    app_ok = check_flask_app()
    print()
    
    # 最后建议
    print(f"{Colors.BLUE}{'='*60}")
    print("🎯 修复建议")
    print(f"{'='*60}{Colors.RESET}\n")
    
    if not py_ok:
        print_status("❌", "需要升级 Python 到 3.8+")
    
    if issues:
        print_status("❌", f"移除问题包: pip uninstall -y {' '.join(issues)}")
        print_status("✅", "然后安装新的依赖: pip install -r requirements_fixed.txt")
    elif not pkg_ok:
        print_status("⚠️", "某些包版本不匹配")
        print_status("✅", "建议重新安装: pip install -r requirements_fixed.txt --force-reinstall")
    else:
        print_status("✅", "所有关键包版本兼容!")
    
    if not app_ok:
        print_status("⚠️", "某些应用文件缺失，请检查项目结构")
    
    # 最后确认
    print(f"\n{Colors.BLUE}{'='*60}{Colors.RESET}")
    if py_ok and pkg_ok and db_ok and app_ok:
        print_status("✅", "✨ 环境检查完全通过！可以运行应用了。")
        print("\n启动应用: python app.py")
    else:
        print_status("⚠️", "环境检查发现问题，请按照上述建议进行修复。")
    print(f"{Colors.BLUE}{'='*60}{Colors.RESET}\n")

if __name__ == "__main__":
    main()
