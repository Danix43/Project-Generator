# from github import Github
import argparse
import os
import venv

"""
TODO: - implement reading command line arguments for project nameing and folder generation
        - the folder creation should be made based on the script's current location and the name provided by the user
      - implement venv creation from script 
      - implement repository creation from script
        - create the readme, .gitignore and LICENCE from the script
     !!! - Add integration with 174
      - Add windows notifications for creating and created
"""

script_path = os.path.dirname(os.path.abspath(__file__))

def create_dir(name_used):
    path = os.path.join(script_path, name_used)
    try:
        os.makedirs(path)
    except FileExistsError:
        print("An folder with this name already exits")
        choise = input("Do you want to continue with the project creation\nUse Y or N: ")
        if choise.lower() == "y":
            os.makedirs(path, exist_ok=True)
        elif choise.lower() == "n":
            exit()
        else:
            print("Unknown command, exiting...")
            exit()

    # For creating a python project
    # pathVenv = os.path.join(path, name_used + "Env")
    # print("Creating ")
    # venv.create(pathVenv, with_pip=True)




argsParser = argparse.ArgumentParser()
argsParser.add_argument("projectname", help="The string that will be use for anything related to this project")
argsParser.add_argument("--languageused", "-lu", help="The programming language used for this project")
args = argsParser.parse_args()

project_name = args.projectname
project_language = args.languageused


print("The name that will be used is: " + args.projectname)
if args.languageused is None:
    create_dir(project_name)
