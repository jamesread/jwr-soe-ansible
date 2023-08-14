build:
	ansible-galaxy collection build .

yamlfix:
	yamlfix roles

lint:
	ansible-lint roles/

publish:
	ansible-galaxy collection publish
