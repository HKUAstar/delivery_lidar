#! /usr/bin/env python

import rospy as ros
from nav_msgs.msg import Odometry

class Transfer1():
    def __init__(self):
        ros.init_node("transfer_state_estimation")
        self.pub = ros.Publisher('/state_estimation', Odometry, queue_size=5)
        sub = ros.Subscriber("/aft_mapped_to_init", Odometry, self.broadcast, queue_size=5)
        ros.spin()
    def broadcast(self, sub):
        self.pub.publish(sub)

if __name__ == "__main__":
    Transfer1()
