.PHONY: linux_venv windows_venv gen freeze install gen_test run

path_linux_venv = ./venv/bin/activate
path_windows_venv = venv\Scripts\activate

# Detect the operating system
OS := $(shell uname)
ifeq ($(OS), Linux)
    activate_venv = . $(path_linux_venv)
else
    activate_venv = .\\venv\\Scripts\\activate
endif

linux_venv:
	rm -rf venv && python3 -m venv venv

windows_venv:
	rm -rf venv && python3 -m venv venv

gen:
	cp .env.example .env

freeze:
	rm -f requirements.txt && $(activate_venv) && python3 -m pip freeze > requirements.txt

install:
	$(activate_venv) && python3 -m pip install -r requirements.txt

gen_test:
	cp .env test/.env

run:
	$(activate_venv) && python3 app.py
