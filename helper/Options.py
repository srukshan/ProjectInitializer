#Important:-
#  Page to Find details of how to do - https://www.tutorialspoint.com/python/python_command_line_arguments.htm
#  Page to Find details of how to do - https://gist.github.com/AtmaMani/4cdda473f02d70ed26035a3f191d5b73

import argparse

parser = argparse.ArgumentParser(description="Project Management Tool")

parser.add_argument('proj_name', help="Enter the Name of the Project")

parser.add_argument('-d','--delete', help='Delete the Project', action='store_true')
parser.add_argument('-a','--alter', help='Alter the Project', action='store_true')

parser.add_argument('-u','--username', help='Username for Version Control')
parser.add_argument('-p','--password', help='Password for Version Control')
parser.add_argument('-v','--vcs', help='Version Control: \n1.Github', type=int)

parser.add_argument('--path', help='Project Path')

parser.add_argument('-s','--save', help='Save current Settings and Default')

class Options:
    project_name = ""
    action=""
    options = {}
    def __init__(self):
        self.__args = parser.parse_args()
        self.setProjectName()
        self.setOptions()

    #TODO:Get Project Name
    def setProjectName(self):
        self.project_name = self.__args.proj_name

    #TODO:Get Options
    def setOptions(self):
        pass

#TODO:Display Help Menu For Options
def help():
    pass

CREATE = 'PROJECT_CREATE'
DELETE = 'PROJECT_DELETE'
ALTER = 'PROJECT_ALTER'
HELP = 'PROJECT_HELP'
