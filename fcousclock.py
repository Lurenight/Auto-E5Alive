import time

def focus_timer(minutes):
    print("开始专注：")
    for i in range(minutes*60, 0, -1):
        minutes, seconds = divmod(i, 60)
        print(f"{minutes:02}:{seconds:02}", end="\r")
        time.sleep(1)
    print("专注结束！")

focus_timer(120) 
