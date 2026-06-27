#!/usr/bin/env python3
"""
CI Debug Logger
Writes environment information to a log file for troubleshooting.
This helps debug token and configuration issues in CI.
"""

import os

# Write debug info to file
with open('debug-info.txt', 'w') as f:
    f.write(f"Repository: {os.environ.get('GITHUB_REPOSITORY', 'local')}\n")
    f.write(f"Run ID: {os.environ.get('GITHUB_RUN_ID', 'local')}\n")
    github_token = os.environ.get('GITHUB_TOKEN', '')
    if github_token:
        f.write(f"GITHUB_TOKEN length: {len(github_token)}\n")
    anthropic_key = os.environ.get('ANTHROPIC_API_KEY', '')
    if anthropic_key:
        f.write(f"ANTHROPIC_API_KEY length: {len(anthropic_key)}\n")

print("Debug info written to debug-info.txt")