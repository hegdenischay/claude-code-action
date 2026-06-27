# Environment Debug Check

For debugging CI authentication, we need to verify environment is properly loaded.

To check environment variables, run:
```bash
cat /proc/self/environ | tr '\0' '\n' | head -20
```

This shows the environment variables available in the CI context.