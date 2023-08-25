#!/usr/bin/env python3
from geometry_msgs.msg import Twist 

import rospy 


if __name__=='__main__':
    rospy.init_node("draw_circle")
    
    rate=rospy.Rate(2)

    pub=rospy.Publisher("turtle1/cmd_vel",Twist,queue_size=10)

    while not rospy.is_shutdown():
        msg=Twist()
        msg.angular.z=1
        msg.linear.x=2
        pub.publish(msg)
        rate.sleep()

    
