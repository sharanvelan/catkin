#!/usr/bin/env python3

from turtlesim.msg import Pose 

from geometry_msgs.msg import Twist 


import rospy 


def call_this(msg:Pose):
    rospy.loginfo(msg.x)
 


if __name__=='__main__':

    rospy.init_node("get_data")
   
    sub=rospy.Subscriber("turtle1/pose",Pose,callback=call_this)
    
    
    rospy.spin()