#!/usr/bin/env bash

echo "Initializing local git repo ..."

USER=$1
PROJECT=$2
DIR=$3

if [ -d "$DIR" ]; then
    cd $DIR
else
    echo "Something went wrong while Initializing local Repository"
fi

if [ $DIR == $PWD ]; then
    git init
    git remote add origin "https://github.com/$USER/$PROJECT"               # to use SSh: "git@github.com:$USER/$PROJECT"
    touch README.md
    git add .
    git commit -m "Initial Commit"
    git push origin master
fi

echo "--------------------------SUCCESSFULLY FORGED $PROJECT--------------------------"
