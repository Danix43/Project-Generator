from github import Github
import argparse
import os.path
import venv
import shutil


class Creator():
    """
    TODO:
        - Create a nicer README
        !!! TBD: - Add integration with 174
        - Add windows notifications for creating and created
    """

    def __init__(self, name_p, language):
        self._name = name_p

        if language == None:
            self._language = ""
        else:
            self._language = language

        with open("./access_token.txt", "r") as token:
            tk = token.read()
        self._github = Github(tk).get_user()
        self._repo = self._github.create_repo(self._name, private=True, license_template="gpl-3.0")

        self._script_path = os.path.dirname(os.path.abspath(__file__))
        self._path = os.path.join(self._script_path, self._name)


    def create_directories(self, already_exists=False):
        print("Creating file structure")
        exists = already_exists
        try:
            os.makedirs(self._path, exist_ok=exists)

            git_ignore_path = shutil.copy2(self._script_path + os.path.sep +
                                           ".gitignore", self._path)

            with open(git_ignore_path, "r") as git_ignore:
                self._repo.create_file(".gitignore", "Initial commit", git_ignore.read())


            with open("./template.md", "r") as template:
                content = template.read()

            with open(self._path + os.path.sep + "README.md", "w") as readme:
                readme.write(content.format(self._name))

            with open(self._path + os.path.sep + "README.md", "r") as readme:
                self._repo.create_file("README.md", "Initial commit", readme.read())

        except FileExistsError:
            print("An folder with this name already exits")

            choise = input(
                "Do you want to continue with the project creation\nUse Y or N: ")
            if choise.lower() == "y":
                self.create_directories(already_exists=True)
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

    def create_project(self):
        if self._language.lower() == "python":
            print("Creating a python project")
            self.create_python()
        else:
            print("Unknown language, creating a generic project")
            self.create_directories()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "projectname", help="The string that will be use for anything related to this project")
    parser.add_argument("--languageused", "-lu",
                        help="The programming language used for this project")

    args = parser.parse_args()

    creator = Creator(args.projectname, args.languageused)
    creator.create_project()
