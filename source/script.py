import requests
import config
from getpass import getpass
import sys
import json

# function to authenticate and create git repo
def create():
    username = config.username
    password = config.password
    with requests.Session() as session:
        if password:
            session.auth = (username, password)
        else:
            session.auth = (username, getpass())
        response = session.get('https://api.github.com/user')

        status = response.status_code
        if (status == 200):
            print("User Authenticated")
            repo_name = sys.argv[1]
            payload = {
                "name": repo_name,
                "description": "This project was created via GitHub APIs",
                "private": False,
                "has_issues": True,
                "has_projects": True,
                "has_wiki": True
            }
            repo = session.post('https://api.github.com/user/repos', data=json.dumps(payload))
            if repo.status_code == 201:
                print("Repository successfully created!")
            else:
                print("Something went wrong!")
        elif (status == 401):
            print("Bad Credentials")
        elif (status == 403):
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
