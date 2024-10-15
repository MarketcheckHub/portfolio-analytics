SHELL := /bin/zsh
include .env

create.apikey-config:
	@echo "Creating apikey-config"
	kubectl create configmap apikey-config-portfolio-analysis --from-file=config/build/api_keys.json --namespace=$(NAMESPACE)

