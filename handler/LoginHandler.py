from github import Github

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def verify(self):
        pass
    def getUser(self):
        pass

class GithubLogin(Login):
    def verify(self):
        self.github = Github(self.username, self.password)
        try:
            self.github.get_user().login
        except:
            return False
        return True
    def getUser(self):
        if self.verify():
            return self.github.get_user()
        else:
            return None
