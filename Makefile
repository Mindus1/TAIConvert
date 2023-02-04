build:
	pyinstaller -F -i "NONE" --paths="./.venv/Lib/site-packages" -n "TAIConvert" ./taiconvert/cli.py

.DEFAULT_GOAL := build
