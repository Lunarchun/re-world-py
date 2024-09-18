@echo off
rmdir /s /q dist
pyinstaller --noconsole --name "Re-world" --icon="RE-world.ico" main.py
"copy ressource.bat"
start dist