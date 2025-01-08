#! /usr/bin/python

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped

# AMCL_received = False
odom_x = odom_y = odom_z = amcl_x = amcl_y = amcl_z = 0


def difference():
    global odom_x, odom_y, odom_z, amcl_x, amcl_y, amcl_z

    dif_x = odom_x - amcl_x
    dif_y = odom_y - amcl_y
    dif_z = odom_z - amcl_z

    print("Difference: x = {}  y = {}  z = {}".format(dif_x, dif_y, dif_z))


def callback_odom(odom_pose):
    global odom_x, odom_y, odom_z
    odom_x = round(odom_pose.pose.pose.position.x, 3)
    odom_y = round(odom_pose.pose.pose.position.y, 3)
    odom_z = round(odom_pose.pose.pose.position.z, 3)

    global AMCL_received
    # if AMCL_received:
    print("Odom: x = {}  y = {}  z = {}".format(odom_x, odom_y, odom_z))
    # difference()
    # AMCL_received = False


def callback_amcl(amcl_pose):
    global amcl_x, amcl_y, amcl_z
    amcl_x = round(amcl_pose.pose.pose.position.x, 3)
    amcl_y = round(amcl_pose.pose.pose.position.y, 3)
    amcl_z = round(amcl_pose.pose.pose.position.z, 3)

    global AMCL_received
    # if amcl_pose:
    print("Amcl: x = {}  y = {}  z = {}".format(amcl_x, amcl_y, amcl_z))
    # AMCL_received = True


def listener():
    rospy.init_node("get_pose", anonymous=True)
    rospy.Subscriber("/odom", Odometry, callback_odom)
    rospy.Subscriber("/amcl_pose", PoseWithCovarianceStamped, callback_amcl)

    rospy.spin()


if __name__ == "__main__":
    listener()
