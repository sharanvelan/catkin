#!/usr/bin/env python3 

import rospy 

from turtlesim.msg import Pose 
from geometry_msgs.msg import Twist 
from turtlesim.srv import SetPen

prev=0
def call_service(r,g,b,width,off):
    try:
        ser=rospy.ServiceProxy("/turtle1/set_pen",SetPen)
        ser(r,g,b,width,off)

    except rospy.ServiceException as e:
        rospy.logerr(e)


def getdata(msg:Pose):
    rospy.loginfo(msg.x)
    put_data=Twist()

    if msg.x > 9.0 or msg.x<2.0:
        put_data.linear.x=1 
        put_data.angular.z=2
    else:
        put_data.linear.x=2
        
    pub.publish(put_data)
    global prev

    if msg.x>=5.5 and prev<5.5:
        prev=msg.x
        call_service(0,0,200,5,0)
    else:
        prev=msg.x
        call_service(0,200,0,5,0)
if __name__=="__main__":
    rospy.init_node("controller")
    rospy.wait_for_service("/turtle1/set_pen")
    call_service(200,0,0,3,0)
   
    sub=rospy.Subscriber("turtle1/pose",Pose,callback=getdata)
    pub=rospy.Publisher("turtle1/cmd_vel",Twist,queue_size=10)

    rospy.spin()

