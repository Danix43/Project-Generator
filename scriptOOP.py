import argparse
import os.path
import venv

class Creator():
    """
    TODO: - implement reading command line arguments for project nameing and folder generation
            - the folder creation should be made based on the script's current location and the name provided by the user
        - implement venv creation from script 
        - implement repository creation from script
            - create the readme, .gitignore and LICENCE from the script
        !!! - Add integration with 174
        - Add windows notifications for creating and created
    """

    def __init__(self, name_p, language):
        self._name = name_p
        
        if language == None:
            self._language = ""
        else:
            self._language = language
        
        self._script_path = os.path.dirname(os.path.abspath(__file__))
        self._path = os.path.join(self._script_path, self._name)


    def create_project(self):
        if self._language.lower() == "python":
            # create_python()
            print("Creating a python project")
        else:
            create_directories()
            print("Unknown language, creating a generic project")


    def create_directories(self):
        print("Creating file structure")
        try:
            os.makedirs(self._path)
        except FileExistsError:
            print("An folder with this name already exits")
            choise = input("Do you want to continue with the project creation\nUse Y or N: ")
            if choise.lower() == "y":
                os.makedirs(_path, exist_ok=True)
            elif choise.lower() == "n":
                exit()
            else:
                print("Unknown command, exiting...")
                exit()


    def create_python(self):
        print("Creating a python specific project")
        self.create_directories()
        pathVenv = os.path.join(self._path, self._name + "Env")
        print("Creating virtual enviroment...")
        venv.create(pathVenv, with_pip=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("projectname", help="The string that will be use for anything related to this project")
    parser.add_argument("--languageused", "-lu", help="The programming language used for this project")

    args = parser.parse_args()

    creator = Creator(args.projectname, args.languageused)
    creator.create_project()
    

