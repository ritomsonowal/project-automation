import requests
import config
from getpass import getpass
import sys
import json
import os
import subprocess

# function to authenticate and create git repo
def create():
    # get the login credentials from config.py
    username = config.username
    password = config.password

    # start a session
    with requests.Session() as session:
        if password:            # if password is set in the config.py file, authenticate else ask for password in terminal
            session.auth = (username, password)
        else:
            session.auth = (username, getpass())

        response = session.get('https://api.github.com/user')           # authenticate

        login_status = response.status_code

        if (login_status == 200):               # check the response from GitHub
            print("User Authenticated")
            repo_name = sys.argv[1]

            # Repository Details
            payload = {
                "name": repo_name,
                "description": "This project was created via GitHub APIs",
                "private": False,
                "has_issues": True,
                "has_projects": True,
                "has_wiki": True
            }

            repo = session.post('https://api.github.com/user/repos', data=json.dumps(payload))              # create a new repo

            if repo.status_code == 201:
                print("Repository successfully created!")

                project_directory = sys.argv[2]

                # initialize git repo on local computer
                dir_path = os.path.dirname(os.path.realpath(__file__))
                subprocess.call(['./init.sh', username, repo_name, project_directory], cwd=dir_path)

            else:
                print("Something went wrong!")

        elif (login_status == 401):
            print("Bad Credentials")

        elif (login_status == 403):
            print("Max number of login attempts exceeded. Try again later...")

        else:
            print("Something went wrong! Please try again.")


#----------------------------MAIN---------------------------

if __name__ == '__main__':
    create_repo = input("Create a New Repository for the project? (Y/N)")
    if create_repo == 'Y' or create_repo == 'y':
        print("Creating Github Repo...")
        create()
    else:
        print("Finished!")
