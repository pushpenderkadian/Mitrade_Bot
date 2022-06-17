@echo off
cd /d "C:\Program Files\Google\Chrome\Application"
start chrome.exe --remote-debugging-port=9000 --user-data-dir="C:/MiTrade Chrome-files/chrome"
timeout 1