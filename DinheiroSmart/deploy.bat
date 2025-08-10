@echo off
echo ========================================
echo    DEPLOY AUTOMATICO - DINHEIRO SMART
echo ========================================
echo.
echo Abrindo sites de deploy...
echo.

start https://share.streamlit.io/signup
timeout /t 2 /nobreak >nul

start https://render.com/register
timeout /t 2 /nobreak >nul

start https://railway.app/login
timeout /t 2 /nobreak >nul

echo.
echo ========================================
echo SITES ABERTOS:
echo 1. Streamlit Cloud (RECOMENDADO)
echo 2. Render.com
echo 3. Railway.app
echo ========================================
echo.
echo DADOS PARA DEPLOY:
echo Repository: leandrovcorrea/Dinheiro-mart
echo Branch: main
echo Main file: app.py
echo ========================================
echo.
pause