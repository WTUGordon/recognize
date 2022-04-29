#!/usr/bin/env python
#coding=utf-8

import rospy
import math
from std_msgs.msg import String, Int32, Float32, Float64MultiArray
import threading

CAR_D = 5     #预定以的参数，车辆的固定参数可方这里,注意不要重名

##每个预警内容对应一个fun
def thread1_fun():
    while not rospy.is_shutdown():
        msg1 = rospy.wait_for_message('/chatter/array1', Float64MultiArray, timeout=None)
        rospy.loginfo("thread1 heard %s \n", msg1.data) #终端打印
        mu = rospy.wait_for_message('/chatter/mu', Float32, timeout=None)
        rospy.loginfo("Mu heard %f \n", mu.data) #终端打印
        #下面写你的预警算法


        warning1 = 1.0     #预警仪
        warning1 = warning1 * CAR_D
        pub1.publish(warning1)

def thread2_fun():
    while not rospy.is_shutdown():
        msg2 = rospy.wait_for_message('/chatter/array2', Float64MultiArray, timeout=None)
        rospy.loginfo("thread2 heard %s \n", msg2.data) #终端打印
        ##下面写你的预警算法


        warning2 = 1.0    #预警仪
        pub2.publish(warning2)

def thread3_fun():
    while not rospy.is_shutdown():
        msg3 = rospy.wait_for_message('/chatter/array3', Float64MultiArray, timeout=None)
        rospy.loginfo("thread3 heard %s \n", msg3.data) #终端打印
        ##下面写你的预警算法


        warning3 = 1.0   #预警仪
        pub3.publish(warning3)

def thread4_fun():
    while not rospy.is_shutdown():
        msg4 = rospy.wait_for_message('/chatter/array4', Float64MultiArray, timeout=None)
        rospy.loginfo("thread4 heard %s \n", msg4.data) #终端打印
        ##下面写你的预警算法


        warning4 = 1.0   #预警仪
        pub4.publish(warning4)

if __name__ == '__main__':
    rospy.init_node('Warning', anonymous=True) #定义节点
    
    thread1 = threading.Thread(target = thread1_fun)
    thread2 = threading.Thread(target = thread2_fun)
    thread3 = threading.Thread(target = thread3_fun)
    thread4 = threading.Thread(target = thread4_fun)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    pub1 = rospy.Publisher("/chatter/Warning1", Float32, queue_size=1)
    pub2 = rospy.Publisher("/chatter/Warning2", Float32, queue_size=1)
    pub3 = rospy.Publisher("/chatter/Warning3", Float32, queue_size=1)
    pub4 = rospy.Publisher("/chatter/Warning4", Float32, queue_size=1)
    
    rate = rospy.Rate(0.2)
    while not rospy.is_shutdown():
        rospy.loginfo("The warning node is running \n") #终端打印
        rate.sleep()
