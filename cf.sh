#! /bin/bash

script_dir="$(dirname "$0")"
source $script_dir/.venv/bin/activate
python3 $script_dir/main.py "$1" "$2"
