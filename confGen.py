import json

dic={
    "tmux_session_settings":{
        "tmux_session_name":"minecraft",
        "minecraft_start_command":
			"java -XX:+UseParallelGC -Xmx4G -Xms4G -Dsun.rmi.dgc.server.gcInterval=600000 -XX:+UnlockExperimentalVMOptions -jar fabric-server-mc.1.20.2-loader.0.14.22-launcher.0.11.2.jar nogui"
	},
    "peeker_settings":{
        "loop_interval":1,
        "timezone":"US/Pacific",
        "user_command_starting_sign":"!",
        "off_hours":{
            "grace_peroid":10*60,
            "start":[
                2330
            ],
            "end":[
                900
            ]
        }
    },

}
with open('conf.json', 'w') as f:
    json.dump(dic,f,indent="\t")
    pass

#from tmuxAPI import Tmux

#print(Tmux.getRecent("mc-1"))
#import os
#print(os.path.dirname(os.path.dirname(__file__)))
