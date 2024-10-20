from tmuxAPI import setup
from json import load
from os import path,chdir
#from time import sleep

CONF_PATH=path.join(path.dirname(__file__),"conf.json")
PEEKER_SESSION_PATH=path.join(path.dirname(__file__),"peekerSession.py")

if __name__ == "__main__":
    with open(CONF_PATH,"r") as f:
        conf_session_settings=load(f)["tmux_session_settings"]
    
    #assume peeker folder is in minecraft files
    #change dir to the minecraft folder
    chdir(path.dirname(path.dirname(__file__)))

    setup(
        conf_session_settings["tmux_session_name"],
        [
            f"python {PEEKER_SESSION_PATH} {CONF_PATH}",
            conf_session_settings["minecraft_start_command"]
        ]
        
    )
    #Tmux.create(conf["mc_server_settings"]["tmux_session"],conf["mc_server_settings"]["start_command"])
    #sleep(10)
    #chdir(path.dirname(__file__))
    #Tmux.create(conf["peeker_session_settings"]["tmux_session"],conf["peeker_session_settings"]["start_command"]+" "+CONF_PATH)

