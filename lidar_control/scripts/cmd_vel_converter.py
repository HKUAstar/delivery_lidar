#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import TwistStamped

lin_x = 0
lin_y = 0
lin_z = 0
ang_x = 0
ang_y = 0
ang_z = 0

def GetVel(msg):
    global lin_x
    global lin_y
    global lin_z
    global ang_x
    global ang_y
    global ang_z
    
    lin_x = msg.twist.linear.x
    lin_y = msg.twist.linear.y
    lin_z = msg.twist.linear.z
    ang_x = msg.twist.angular.x
    ang_y = msg.twist.angular.y
    ang_z = msg.twist.angular.z

if __name__=="__main__":
    rospy.init_node("cmd_vel_converter")
    sub = rospy.Subscriber("new_vel", TwistStamped, GetVel, queue_size=100)
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=100)
    rate = rospy.Rate(100)

    msg = Twist()

    while not rospy.is_shutdown():
        msg.linear.x = round(lin_x, 2)
        msg.linear.y = round(lin_y, 2)
        msg.linear.z = round(lin_z, 2)
        msg.angular.x = round(ang_x,2)
        msg.angular.y = round(ang_y,2)
        msg.angular.z = round(ang_z/2,2)
        pub.publish(msg)
        rate.sleep()
