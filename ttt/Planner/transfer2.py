#! /usr/bin/env python

import rospy as ros
from sensor_msgs.msg import PointCloud2

class Transfer2():
    def __init__(self):
        ros.init_node("transfer_registered_scan")
        self.pub = ros.Publisher('/registered_scan', PointCloud2, queue_size=5)
        sub = ros.Subscriber("/cloud_registered", PointCloud2, self.broadcast, queue_size=5)
        ros.spin()
    def broadcast(self, sub):
        self.pub.publish(sub)

if __name__ == "__main__":
    Transfer2()
