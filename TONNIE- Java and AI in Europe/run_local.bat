@echo off
echo Instalando dependencias...
pip install -r requirements.txt

echo.
echo Iniciando aplicativo Streamlit...
streamlit run app.py

pause