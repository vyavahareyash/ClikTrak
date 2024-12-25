import os
import subprocess

def activate_venv_and_run_app():
    # Activate the virtual environment
    activate_script = os.path.join('.venv', 'Scripts', 'activate')
    subprocess.call(f'call {activate_script}', shell=True)

    # Install requirements
    subprocess.call('pip install -r requirements.txt', shell=True)

    # Run the Streamlit app
    subprocess.call('streamlit run app.py', shell=True)

if __name__ == "__main__":
    activate_venv_and_run_app()