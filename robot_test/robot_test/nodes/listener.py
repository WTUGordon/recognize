#!/usr/bin/env python
#coding=utf-8

import rospy
import math
from std_msgs.msg import String, Int32, Float64


def callback(This): #回调函数，每次话题有更新会执行此函数
    rospy.loginfo("I heard %s \n", This.data) #终端打印

if __name__ == '__main__':
    rospy.init_node('Listener', anonymous=True) #定义节点
    rospy.Subscriber('chatter', String, callback) #定义接受接口，包括话题名、数据类型、回调函数
    rospy.spin()
        
        