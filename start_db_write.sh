#!/bin/bash

bash_scripts_path="./bash_scripts/start_python_env_and_run.sh"

start_script () {
    echo "Starting script..."
    source $1
    echo "Script started."
}

start_script $bash_scripts_path