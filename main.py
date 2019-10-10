import setting
import helper.FileHelper as FileHelper
import helper.InitConfig as InitConfig

def init():
    if FileHelper.isFile(setting.CONFIG_FILE):
        print("has config")
    else:
        InitConfig.InitConfig()

if __name__ == "__main__":
    init()