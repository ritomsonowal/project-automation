import requests
import config

if __name__ == '__main__':
    create_repo = input("Create a New Repository for the project? (Y/N)")
    if create_repo == 'Y' or create_repo == 'y':
        print("Creating Github Repo...")
        create()
    else:
        print("Finished!")
