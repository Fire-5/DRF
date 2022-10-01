#!/bin/bash

if [[ -e "venv-linux" ]]; then
  echo "[+] - Virtual environment is installed aready, skipping."
else
  echo "[!] - Doing virtual environment installation."
  python -m venv venv-linux
fi

source venv-linux/bin/activate

if [[ -e "venv-linux/dimasflag.txt" ]]; then
  echo "[+] - Libraries are installed aready, skipping."
else
  echo "[!] - Installing libraries."
  pip install -r requirements.txt
#   pip install -r requirements_dev.txt
#   pip install pytest

#  if !errorlevel! neq 0 exit /b !errorlevel!
  echo "[+] - requirements.txt requirements are installed" > ./venv-linux/dimasflag.txt
fi

echo "[+] Project already!"