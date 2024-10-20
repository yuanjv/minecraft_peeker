from os import system,popen

def getRandId():
    return popen('date +%s%N').read().strip('\n')

'''
class Tmux:
    
    @staticmethod
    def create(id=getRandId(),command:str="clear"):
        system("tmux new -d -s "+id)
        #system(f'tmux send-keys -t {self.id} "export DISPLAY=:1.0" ENTER')
        system(f"tmux send-keys -t {id} '{command}' ENTER")
        print(f"NEW TMUX {id}: {command}")
    
    @staticmethod
    def send(id:str,command:str):
        system(f"tmux send-keys -t {id} '{command}' ENTER")
        print(f"TMUX {id}: {command}")
'''
'''
The syntax for a specific pane is tmux send-keys -t {session}:{window}. {pane} , so tmux send-keys -t Test:Test1. 1 "TEST" C-m would send that to the first pane. 
'''

def setup(id:str=getRandId(),commands:list=["clear"]):
    system("tmux new -d -s "+id)
    system(f"tmux send-keys -t {id} '{commands[0]}' ENTER")
    #system(f"tmux rename-window -t {id} 0")
    system(f"tmux rename-window -t {id} 0")

    for i,c in enumerate(commands[1:]):
        system(f"tmux split-window -h -t {id}")
        #system(f"tmux rename-window -t {id} {i+1}")
        system(f"tmux send-keys -t {id} '{c}' ENTER")

def send(id:str,command:str):#,panel_id:int=None):
    #if panel_id:
    #    system(f"tmux select-pane -t {id}.{panel_id}")
    system(f"tmux send-keys -t {id} '{command}' ENTER")
    #print(f"TMUX {id}: {command}")