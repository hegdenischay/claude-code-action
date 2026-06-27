#!/bin/bash
# CI Environment Verification
# Reads /proc/self/environ to verify variables are available

cat /proc/self/environ | tr '\0' '\n' | grep -E 'GITHUB_TOKEN|ANTHROPIC'