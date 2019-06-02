#!/bin/bash

# script directory path
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# to change path where you want to create the project edit the value below
# default = new project is created outside the directory containing the repo
DIR=0              # eg: DIR = $HOME/projects/

function forge() {
    PROJECT_DIR=$1
    if [ $1 ]; then
        if [ $DIR == 0 ]; then
            cd $SCRIPT_DIR/../..
        else
            cd $DIR
        fi
        if [ -d "$PROJECT_DIR" ]; then
            # Control will enter here if $DIRECTORY exists.
            echo "Project Already Exists!"
        else
            echo "Creating New Project..."
            mkdir $PROJECT_DIR
            echo "CREATED "$PROJECT_DIR
            cd $PROJECT_DIR
            python3 $SCRIPT_DIR/script.py "$1" "$PWD"
        fi
    else
        echo "Missing Argument -- [ forge <project-name> ]"
    fi
}

# python3 script.py
