#Important:-
#  Page to Find details of how to do - https://www.tutorialspoint.com/python/python_command_line_arguments.htm
#  Page to Find details of how to do - https://gist.github.com/AtmaMani/4cdda473f02d70ed26035a3f191d5b73
from model.config import Config
import argparse

# TODO: in v2
#   Get Language or Framework of Project
#   Store language
parser = argparse.ArgumentParser(description="Project Management Tool")

parser.add_argument('proj_name', help="Enter the Name of the Project")

parser.add_argument('-d','--delete', help='Delete the Project', action='store_true')
parser.add_argument('-a','--alter', help='Alter the Project', action='store_true')

parser.add_argument('-u','--username', help='Username for Version Control')
parser.add_argument('-p','--password', help='Password for Version Control')
parser.add_argument('-v','--vcs', help='Version Control: \n1.Github', type=int)

parser.add_argument('--path', help='Project Path')

parser.add_argument('-s','--save', help='Save current Settings and Default', action='store_true')

class Options:
    project_name = ""
    action=""
    def __init__(self):
        self.load()
        self.__args = parser.parse_args()
        self.setProjectName()
        self.setOptions()
        if self.__args.save:
            self.config.save()

    def setProjectName(self):
        self.project_name = self.__args.proj_name

    #TODO:Get Options
    def setOptions(self):
        self.action = ALTER if self.__args.alter else DELETE if self.__args.delete else CREATE


    def load(self):
        self.config = Config.load()

    def save(self):
        self.config.save()

#TODO:Display Help Menu For Options
def help():
    pass

CREATE = 'PROJECT_CREATE'
DELETE = 'PROJECT_DELETE'
ALTER = 'PROJECT_ALTER'
HELP = 'PROJECT_HELP'
