import setting
from helper import FileHelper, Options, InitConfig
import create
import delete
import alter

def init():
    if FileHelper.isFile(setting.CONFIG_FILE):
        pass
    else:
        InitConfig.InitConfig()
        return init()

def run():
    try:
        opts = Options.Options()
        if opts.action == Options.CREATE:
            create.run(opts)
        elif opts.action == Options.DELETE:
            delete.run(opts)
        elif opts.action == Options.ALTER:
            delete.run(opts)
        else:
            Options.help()
    except:
        Options.help()

if __name__ == "__main__":
    init()
    run()