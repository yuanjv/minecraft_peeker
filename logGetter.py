from os import listdir,path
#while it's true that minecraft write the log into logs/latest.log,
#when amount of logs reached a certain threshold, it will create a new one regardless the session
'''
class LogGetter:
    def __init__(self):
        #self.pos=pos
        self.f=open(path.join(path.dirname(path.dirname(__file__)),"logs/latest.log"),'r')
    def getInfo(self):
        #self.f.seek(self.pos)
        #return self.f.read().split('\n')[:-1]
        #self.pos=self.f.tell()
        #new_log.pop()
        return [x.strip('\n').split("thread/INFO]: ",1)[1] for x in self.f.readlines() if x.split()[2]=="thread/INFO]:"]
'''
LOG_PATH=path.join(path.dirname(path.dirname(__file__)),"logs")
LATEST_LOG_PATH=path.join(LOG_PATH,"latest.log")

WANTED_LOG_HEADER="thread/INFO]:"

class LogGetter:
    def __init__(self):
        self.log_ls_count=0
        self.posResetter()
        self.f=open(LATEST_LOG_PATH,'r')
    def posResetter(self):
        #if ls returns a different value, it usually .gz ed the lastest.log and made a new one
        new_log_ls_count=len(listdir(LOG_PATH))
        if self.log_ls_count!=new_log_ls_count:
            self.log_ls_count=new_log_ls_count
            self.pos=0

    def getInfo(self):
        self.posResetter()
        self.f.seek(self.pos)
        #return self.f.read().split('\n')[:-1]
        #new_log.pop()
        ret=[x.strip('\n').split(WANTED_LOG_HEADER+" ",1)[1] for x in self.f.readlines() if x.split()[2]==WANTED_LOG_HEADER]
        self.pos=self.f.tell()
        return ret
