#!/bin/bash


# Create python venv
# Activate venv
# Install requirements
# Run python script

current_script_path=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
base_path=$(dirname "$current_script_path")
python_scripts_path="$base_path/python_scripts"
python_filename="main.py"


install_python_venv () {
	python_project_files=$(ls $1)

	if [[ ! $python_project_files =~ "venv" ]]; then
		python3 -m venv "$1/venv"
		echo "Successfully installed python3 venv."
	else
		echo "Python3 venv already installed."
	fi 
}

activate_python_venv () {
	source "$1/venv/bin/activate"
	echo "Python3 venv successfully activated."
}

install_python_dependencies () {
	python3 -m pip install -r "$1/requirements.txt"
}

run_python_script () {
	python_file="$1/$2"
	python3 $python_file
}


install_python_venv $python_scripts_path
activate_python_venv $python_scripts_path
install_python_dependencies $python_scripts_path
run_python_script $python_scripts_path $python_filename