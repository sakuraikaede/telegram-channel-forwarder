import os

def main():
    os.system("(pip3 list | grep pyTelegramBotAPI) > tmpString")
    FileName = "tmpString"
    File = open(FileName, "r")
    
    Package_curr = False
    while 1:
        FileLine = File.readline()
        print(FileLine[0: 16])
        if not FileLine:
            break

        if FileLine[0: 16] == "pyTelegramBotAPI":
            Package_curr = True
            break
        else:
            continue
    
    if not Package_curr:
        print("You may installed wrong package, please uninstall 'telebot' and install 'pyTelegramBotAPI'")
        return
    if os.path.exists("/etc/systemd/system/tcfbot.service"):
        print("Server file exists, use 'sudo systemctl [start/stop] tcfbot.service' to control it." )
        return 

    string = "[Unit]\nDescription=tcfbot\nAfter=network.target\nWants=network.target\n\n[Service]\nWorkingDirectory="
    string += os.getcwd()
    string += "\nType=forking\nExecStart=/usr/bin/python3 "
    string += os.path.join(os.getcwd(), "main.py")
    string += "\nKillMode=process\nRestart=always\n\n[Install]\nWantedBy=multi-user.target"
    print(string)
    
    FileName = "/etc/systemd/system/tcfbot.service"
    File = open(FileName, "w")
    File.write(string)
    File.close()

    os.system("sudo systemctl enable tcfbot.service")
    os.system("sudo systemctl start tcfbot.service")

    return



if __name__ == '__main__':
    main()
