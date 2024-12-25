@echo off
REM Get the current directory
cd /d %~dp0

REM Activate the virtual environment
call .venv\Scripts\activate

REM Install requirements
pip install -r requirements.txt

REM Run the Streamlit app
streamlit run app.py