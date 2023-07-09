import time

def pomodoro_timer(total_time, break_time):
    while True:
        print("工作时间倒计时开始！")
        for i in range(total_time, 0, -1):
            minutes = i // 60
            seconds = i % 60
            print("{:02d}:{:02d}".format(minutes, seconds))
            time.sleep(1)
        
        print("休息时间！")
        for i in range(break_time, 0, -1):
            minutes = i // 60
            seconds = i % 60
            print("{:02d}:{:02d}".format(minutes, seconds))
            time.sleep(1)

# 设置工作时间为25分钟，休息时间为5分钟
pomodoro_timer(1500, 300)
