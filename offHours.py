from multiprocessing import Process
from time import sleep
#from threading import Thread

class OffHours:
    def __init__(self,getWhiteList,conf,cur_time,send_command):
        
        self.getWhiteList=getWhiteList
        self.start=conf["start"]
        self.end=conf["end"]
        self.grace_peroid=conf["grace_peroid"]
        self.kick=lambda name:send_command("kick "+name)
        self.send_command=send_command
        #self.kick_players=False

        #check if the program is start on the off hours or not
        time_nodes=self.start+self.end
        if time_nodes:
            smaller_ls=[x for x in time_nodes if x<=cur_time]
            if smaller_ls:
                nearest_passed_node=max(smaller_ls)
            else:
                nearest_passed_node=max(time_nodes)
            
            self.kick_players=nearest_passed_node in self.start
        else:
            self.kick_players=False


    def sync(self,time:int):
        if self.kick_players:
            if time in self.end:
                self.kick_players=False
                #print("offHours OFF")
        else:
            if time in self.start:
                self.kick_players=True
                #print("offHours ON")

                self.send_command(f'tellraw @a "WARNING: TIME IS UP"')
                self.send_command(f'tellraw @a "ALL PLAYERS WILL BE KICKED IN {self.grace_peroid/60} MIN"')

                def graceKick():
                    sleep(self.grace_peroid)
                    for player in self.getWhiteList():
                        self.kick(player)
                
                Process(target=graceKick).start()
                '''
                Thread(target=graceKick).start()
                '''
                

    
    def enforce(self,name:str):
        if self.kick_players:
            self.kick(name)
