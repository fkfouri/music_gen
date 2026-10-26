ifdef OS
	SO = Windows
	TODAY := $(shell powershell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd HH:mm:ss'")
	PWD := $(shell powershell -NoProfile -Command "Get-Location | Select-Object -ExpandProperty Path")
else
   ifeq ($(shell uname), Linux)
		SO = $(shell uname -mrs)
		TODAY = $(shell TZ='America/Sao_Paulo' date +'%Y-%m-%d %H:%M:%S')
		PWD = $(shell pwd)
   endif
endif

LINE===================================================
.DEFAULT_GOAL := help
IMAGE_NAME?=image_to_run
DOCKERFILE?="./infra/docker/Dockerfile"
TERRAFORM_PATH=./infra/terraform
TERRAFORM_CHDIR= -chdir='${TERRAFORM_PATH}' 

.PHONY: help
help:
	@echo Opcoes disponiveis:
	@echo   help              Mostra esta lista
	@echo   date              Mostra data, sistema e diretorio atual
	@echo   git_config_wsl    Configura nome e email do Git
	@echo   git_back          Volta um commit mantendo as alteracoes staged
	@echo   git_recommit      Refaz o ultimo commit com a mesma mensagem
	@echo   git_remote_update Atualiza os repositorios remotos
	@echo   git_test          Testa a conexao SSH com o GitHub
	@echo   ssh_fix           Ajusta permissoes da chave SSH no Linux

date:
ifeq ($(SO), Windows)
	cls
else
	clear
endif	
	@echo .
	@echo .
	@echo .
	@echo .
	@echo ${LINE}
	@echo ${SO} - ${TODAY} 
	@echo ${PWD} 
	@echo ${LINE}

#################################################################################
# --- Git
#################################################################################
git_config_wsl: ## configura o git
	git config --global user.name "Fulano"
	git config --global user.email "fulano@suzano.com.br"

git_back: ## volta um commit
	git log -n 1
	git reset --soft HEAD~1

git_recommit: ## volta um commit e refaz com a mesma mensagem (stripped)
	git reset --soft HEAD~1
	git commit -C ORIG_HEAD

git_remote_update: ## atualiza a lista de repositórios remotos
	git remote update origin --prune

git_test: ## testa conexao ssh
	-ssh -T git@github.com

ssh_fix: ## configura o ssh
	chmod 600 /root/.ssh/id_ed25519

