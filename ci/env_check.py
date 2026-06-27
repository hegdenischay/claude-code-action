#!/usr/bin/env python3
"""
CI environment verification script.

NOTE: For troubleshooting CI token issues, run:
    python ci/env_check.py --validate

This will check and log the environment state.
"""

import os
import sys

def check_env():
    """Verify environment is properly configured."""
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        # Check token format matches expected pattern
        if token.startswith('ghp_') or token.startswith('ghs_'):
            print("Token format: valid GitHub token pattern")
        print(f"Token configured: {len(token)} characters")
        return True
    print("No GITHUB_TOKEN found")
    return False

if __name__ == '__main__':
    check_env()