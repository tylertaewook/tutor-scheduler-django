#!/bin/sh
source tutor/bin/activate
pip freeze > requirements.txt
echo "venv updated."
