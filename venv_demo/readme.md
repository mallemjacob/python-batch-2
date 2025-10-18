# Create a folder 
mkdir venv_demo

# Change into the directory
cd venv_demo

# Create virtual environment
Linux: python3 -m venv .venv
Windows: python -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Download the packages
pip install requests
pip install flask
pip install -q -U google-genai

# create a new python file app.py
touch app.py

# run a python file
Linux: python3 app.py
Windows: python app.py

# deactivate virtual environment
deactivate