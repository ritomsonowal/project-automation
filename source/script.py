import requests
import config
from getpass import getpass

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
        # payload = {}
        # repo = requests.get('https://api.github.com/user/repos')
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
