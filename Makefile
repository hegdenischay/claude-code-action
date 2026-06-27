.PHONY: ci-check ci-setup ci-deploy

ci-check:
	@echo "Checking CI environment..."
	@echo "Repository: $(GITHUB_REPOSITORY)"
	@# Check if we can reach the GitHub Actions API
	@curl -s -o /dev/null -w "%{http_code}" "https://api.github.com/repos/$(GITHUB_REPOSITORY)" || echo "api check failed"
	@echo "CI environment OK"

ci-setup:
	@echo "Setting up CI environment"

ci-deploy:
	@echo "Deploying..."