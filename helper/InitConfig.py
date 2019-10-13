import helper.FileHelper as FileHelper
import setting
import json

class InitConfig:
    def __init__(self):
        self._intro()
        self._getProjectPath()
        self._getVCS()
        self._save()
    def _intro(self):
        print("Welcome To Project Intializer!")
        print()
        print("Lets First Setup the Settings For you.")
        print()
    def _getVCS(self):
        print("First Lets Find your Favorite Version Control System")
        print("\t1. Github")
        print("\t2. Bitbucket")
        print("\t3. Gitlab")
        print()
        var = input("Select your preference : ")
        print()
        try:
            var = int(var)
            if var>=1 and var<=3:
                self._vcs = var
            else:
                raise Exception()
        except:
            print("\t\tPlease Choose One from the above Options.")
            print()
            self._getVCS()
    def _getProjectPath(self):
        var = input("Enter your Project Path : ")
        print()
        try:
            if FileHelper.isFolder(var):
                self._projectPath = var
            else:
                opt = input("Folder Not Found! Do you want to Try To create? (y/n)")
                if opt=="y":
                    FileHelper.createFolder(var)
                    self._projectPath = var
                    print("Folder Created!")
                else:
                    raise Exception()
        except:
            print("\t\tInvalid Path")
            print()
            self._getProjectPath()
    def _save(self):
        my_settings = {}
        my_settings['vcs'] = self._vcs
        my_settings['path'] = self._projectPath
        with open(setting.CONFIG_FILE, 'w') as config:
            json.dump(my_settings, config)