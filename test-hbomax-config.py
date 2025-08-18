#!/usr/bin/env python3
"""
HBO Max Config Validation Script
Validates the hbomax-2025.loli config file structure and syntax
"""

import re
import json
from pathlib import Path

def validate_config(config_path):
    """Validate the HBO Max config file structure"""
    print(f"Validating config: {config_path}")
    
    with open(config_path, 'r') as f:
        content = f.read()
    
    if '[SETTINGS]' not in content:
        print("❌ Missing [SETTINGS] section")
        return False
    
    if '[SCRIPT]' not in content:
        print("❌ Missing [SCRIPT] section")
        return False
    
    settings_match = re.search(r'\[SETTINGS\]\s*\n({.*?})\s*\n\[SCRIPT\]', content, re.DOTALL)
    if not settings_match:
        print("❌ Could not extract settings JSON")
        return False
    
    try:
        settings = json.loads(settings_match.group(1))
        print("✅ Settings JSON is valid")
    except json.JSONDecodeError as e:
        print(f"❌ Invalid settings JSON: {e}")
        return False
    
    required_settings = ['Name', 'NeedsProxies', 'Author', 'Version']
    for setting in required_settings:
        if setting not in settings:
            print(f"❌ Missing required setting: {setting}")
            return False
    
    script_section = content.split('[SCRIPT]')[1]
    
    required_placeholders = ['<USER>', '<PASS>']
    for placeholder in required_placeholders:
        if placeholder not in script_section:
            print(f"❌ Missing required placeholder: {placeholder}")
            return False
    
    required_blocks = [
        'REQUEST GET "https://auth.hbomax.com/login"',
        'REQUEST POST "https://auth.hbomax.com/api/login"',
        'REQUEST GET "https://play.hbomax.com/api/account/profile"'
    ]
    
    for block in required_blocks:
        if block not in script_section:
            print(f"❌ Missing required request block: {block}")
            return False
    
    essential_components = [
        '<USER>',
        '<PASS>',
        'PARSE "<SOURCE>" LR',
        'CAP "User ID: "',
        'CAP "Email: "'
    ]
    
    for component in essential_components:
        if component not in script_section:
            print(f"❌ Missing essential component: {component}")
            return False
    
    
    print("✅ All validation checks passed!")
    print("\n📋 Config Summary:")
    print(f"   Name: {settings.get('Name')}")
    print(f"   Author: {settings.get('Author')}")
    print(f"   Version: {settings.get('Version')}")
    print(f"   Needs Proxies: {settings.get('NeedsProxies')}")
    print(f"   Suggested Bots: {settings.get('SuggestedBots')}")
    
    return True

def main():
    config_path = Path(__file__).parent / "hbomax-2025.loli"
    
    if not config_path.exists():
        print(f"❌ Config file not found: {config_path}")
        return False
    
    return validate_config(config_path)

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
