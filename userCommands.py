from os import system
from time import sleep
class UserCommands:
    def __init__(self,conf,server_command):
        self.conf=conf
        self.server_command=server_command

    def execute(self,name:str,command:str):
        command=command.split(" ",1)
        match command[0]:
            case "espeak":
                system("espeak "+command[1])
            case "stop":
                self.server_command("stop")
                sleep(60)
                system("tmux kill-session -t"+self.conf["tmux_session_settings"]["tmux_session_name"])
