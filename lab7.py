#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist 
import math

loc = {
	'right': 0,
	'front': 0,
	'left': 0,
}

def laser(msg):
	global loc
	loc = {
		'right': min(msg.ranges[0:7]),
		'front': min(msg.ranges[8:12]),
		'left': min(msg.ranges[13:19]),
    }

rospy.init_node('reading_laser')
sub = rospy.Subscriber('/base_scan', LaserScan, laser)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
while not rospy.is_shutdown():
	msg = Twist() 		
	if loc['right']>1 and loc['right']<1.5 and loc['left']>1 and loc['front']>1: 
		msg.linear.x = 1
		msg.angular.z = 0	
	if loc['left']<=1:
		msg.linear.x = 0.5
		msg.angular.z = -0.7
	if loc['right']<=1:
		msg.linear.x = 0.5
		msg.angular.z = 0.7 
	if loc['right']>=1.5:
		msg.linear.x = 0.5
		msg.angular.z = -0.7 
	if loc['front']<=1:
		msg.linear.x = 0.1
		msg.angular.z = 0.7       
	pub.publish(msg)  	
