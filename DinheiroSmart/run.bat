@echo off
echo Iniciando Dinheiro Smart...
echo Abrindo navegador em http://localhost:8503
start http://localhost:8503
python -m streamlit run app.py --server.port 8503
pause