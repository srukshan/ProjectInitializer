import helper.FileHelper as FileHelper
import handler.LoginHandler as LoginHandler
import setting
import json
from getpass import getpass
import model.config

class InitConfig:
    def __init__(self):
        self._intro()
        self._getProjectPath()
        self._getVCS()
        if self._saveCredentials():
            self._login()
        self._save()
    def _intro(self):
        print("Welcome To Project Intializer!")
        print()
        print("Lets First Setup the Settings For you.")
        print()
    def _getVCS(self):
        print("First Lets Find your Favorite Version Control System")
        print("\t1. Github")
        print()
        var = input("Select your preference : ")
        print()
        try:
            var = int(var)
            if var==1:
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
    def _saveCredentials(self):
        prompt = input("Do you want to save your login Credentials? (y/n) ")
        return prompt=="y"
    def _login(self):
        print("Please Enter your Login Credentials")
        username = input("Username\t:\t")
        password = getpass(prompt="Password\t:\t")
        if self._vcs==1:
            if LoginHandler.GithubLogin(username, password).verify():
                self._username = username
                self._password = password
            else:
                print("Invalid Credentials!")
                return self._login()
        else:
            pass
    def _save(self):
        my_settings = {}
        my_settings['vcs'] = {
            "type":self._vcs
        }
        try:
            my_settings['vcs']["username"]=self._username
            my_settings['vcs']["password"]=self._password
        except:
            pass
        my_settings['path'] = self._projectPath
        model.config.Config(my_settings).save()