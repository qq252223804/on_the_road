# -*- coding: utf-8 -*- 
# @Time : 2019/1/18 15:41 
# @Author : taojian 
# @File : launchTime.py
import csv
import os
import time


class App(object):
    '''
    运行类
    '''

    def __init__(self):
        self.content = ""
        self.startTime = 0

    # 启动APP
    def launchApp(self):
        # cmd1='adb connect 127.0.0.1:62001'
        # os.popen(cmd1)          #连接模拟器
        cmd2 = 'adb shell am start -W -n com.mfcar.dealer/.ui.splash.SplashActivity'
        self.content = os.popen(cmd2)  # 获取返回内容
        return self.content

    # 停止APP
    def StopApp(self):
        cmd = 'adb shell am force-stop com.mfcar.dealer'
        # cmd2="adb shell input keyevent 3 "   #back键退出
        os.popen(cmd)

    # 获取启动时间
    def GetLaunchedTime(self):
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.startTime = line.split(":")[1]
                break
        return self.startTime


class Controller(object):
    '''
    控制类
    '''

    def __init__(self, cont):
        """
        :param cont:执行次数
        """
        self.app = App()  # 获取运行类
        self.counter = cont
        # 定义手机数据的数组
        self.alldata = [("timestamp", "elapsedtime")]

    # 单次测试过程
    def testproces(self):
        self.app.launchApp()
        time.sleep(2)
        elapsedtime = self.app.GetLaunchedTime().replace('\n', '').lstrip()
        print(elapsedtime)
        self.app.StopApp()
        time.sleep(2)
        timestamp = self.timestamp()
        self.alldata.append((timestamp, elapsedtime))
        print(self.alldata)

    # 多次执行过程
    def run(self):
        while int(self.counter) > 0:
            self.testproces()
            self.counter = self.counter - 1

    # 获取当前时间戳
    def timestamp(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    # 存储数据
    def SaveDataToCSV(self):
        with open("strtTime.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.alldata)
            csvfile.close()


if __name__ == '__main__':
    controller = Controller(10)
    controller.run()
    controller.SaveDataToCSV()
