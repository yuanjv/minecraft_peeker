import sys
from json import load
from time import sleep
import re
from os import path
from datetime import datetime as dt
import pytz


from logGetter import LogGetter
from userCommands import UserCommands
from offHours import OffHours
from tmuxAPI import send

whitelist_path=path.join(path.dirname(path.dirname(__file__)),"whitelist.json")
def getWhiteList():
    with open(whitelist_path,"r") as f:
        return [x["name"] for x in load(f)]

def main():
    #load config to dic
    with open(sys.argv[1],"r") as f:
        conf=load(f)
    
    peeker_settings=conf["peeker_settings"]

    timezone=pytz.timezone(peeker_settings["timezone"])

    # .1 is the reference to the 2nd panel where minecraft server was in
    # somehow commands doesnt work when people restart the peeker but not mc server
    # server command line have the commands but no responds
    # i guess just dont touch tmux after server started then...
    sendServerCommmand=lambda command:send(conf["tmux_session_settings"]["tmux_session_name"],command)
    
    log=LogGetter()

    off_hours=OffHours(getWhiteList,peeker_settings["off_hours"],int(dt.now(timezone).strftime("%H%M")),sendServerCommmand)

    user_commands=UserCommands(conf,sendServerCommmand)

    


    while True:
        sleep(peeker_settings["loop_interval"])
        infos=log.getInfo()
        cur_time=int(dt.now(timezone).strftime("%H%M"))
        off_hours.sync(cur_time)


        for info in infos:
            #print(info)
            head_split=info.split(" ",1)
            #if any player tryed to send command, send username and command to UserCommands
            #<[username]> !XXX
            if re.match(r'<(' + '|'.join(map(re.escape, getWhiteList())) + ')>',head_split[0]):
                if head_split[1][0]==peeker_settings["user_command_starting_sign"]:
                    user_commands.execute(head_split[0][1:-1],head_split[1][1:])
            
            #if player joined the game, send username and time to the OffHours
            #[username] XXX
            if head_split[0] in getWhiteList():
                if head_split[1]=="joined the game":
                    off_hours.enforce(head_split[0])
                    #sendServerCommmand('title '+head_split[0]+' subtitle ["",{"selector":"no player will allowed to join the server between ","color":"#CE9178"},{"selector":"11:30 p.m.","color":"red"},{"selector":" and ","color":"#CE9178"},{"selector":"9:00 a.m","color":"red"},{"selector":".","color":"#CE9178"}]')
                    #sendServerCommmand("say thank you for your understanding")
                    sendServerCommmand(f'tellraw {head_split[0]} "Welcome {head_split[0]}"')
                    sendServerCommmand(f'tellraw {head_split[0]} "no player will allowed to join the server between 11:30 p.m. and 9:00 a.m."')
                    sendServerCommmand(f'tellraw {head_split[0]} "thank you for your understanding"')


                if "has made the advancement" in head_split[1]:
                    sendServerCommmand(f'tellraw {head_split[0]} "great i guess. i tried to put something here but u know how this went"')

            
            
            

            
            



if __name__ == "__main__":
    #make sure the minecraft server started
    print("DO NOT TOUCH THIS TMUX PANEL")
    print("TOUCHING IT BREAKS THE MINECRAFT SERVER AND I DON'T KNOW WHY")
    sleep(10)

    main()
    