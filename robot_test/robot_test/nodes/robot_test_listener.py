#!/usr/bin/env python
#coding=utf-8

import rospy
import math
from std_msgs.msg import String, Int32, Float64

DEFINE_PARAMETER =   1.5   #预定以的参数，车辆的固定参数可方这里

def callback(This):
    rospy.loginfo("I heard %s \n", This.data)

if __name__ == '__main__':
    rospy.init_node('Listener_test', anonymous=True)
    rospy.Subscriber('chatter', String, callback)
    pub1 = rospy.Publisher('number1', Float64, queue_size=10)
    pub2 = rospy.Publisher('number2', Int32, queue_size=10)
    count = 0
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        count = count + 1
        if count % 50 == 0:
            num = math.cos(count * DEFINE_PARAMETER)
            rospy.loginfo("I Send %f \n", num)
            pub1.publish(num)
            pub2.publish(count)
        rate.sleep()
    rospy.spin()
        
        