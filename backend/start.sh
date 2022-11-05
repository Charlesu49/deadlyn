#!/usr/bin/env bash

echo "Hello Charles"
source ./venv/bin/activate
export FLASK_APP=run.py
export FLASK_DEBUG=True
export SECRET_KEY="somerandomsecretkey"
echo "environment activated and variables set! run 'flask run'"
