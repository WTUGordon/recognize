#!/usr/bin/env python
#coding=utf-8


import rospy  #导入包
from std_msgs.msg import String, Int32, Float64

def talker():  #发送函数
    pub = rospy.Publisher('chatter', String, queue_size=10) #定义对象，发布接口
    rospy.init_node('Broadcaster_test', anonymous=True) #定义节点
    rate = rospy.Rate(1) #设置频率
    while not rospy.is_shutdown():
        test_str = "robot test %s" % rospy.get_time() #字符串
        pub.publish(test_str) #发布数据
        rospy.loginfo("I Send %s \n", test_str) #终端打印
        rate.sleep() #睡眠等待

if __name__ == '__main__':
    talker()
    rospy.spin()
