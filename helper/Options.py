#Important:-
#  Page to Find details of how to do - https://www.tutorialspoint.com/python/python_command_line_arguments.htm

import sys, getopt

class Options:
    project_name = ""
    action=""
    options = {}
    def __init__(self):
        self.setProjectName()
        self.setOptions()

    #TODO:Get Project Name
    def setProjectName(self):
        pass

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
