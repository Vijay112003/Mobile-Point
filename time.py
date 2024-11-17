from datetime import datetime




def time():
    now = datetime.now()
    nowtime=str(now.hour)+":"+str(now.minute)+":"+str(now.second)
    print("Current Time =", nowtime)
for i in range(100):
    time()
