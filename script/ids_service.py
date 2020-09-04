#!/usr/bin/env python

import rospy
from HomeRobotRosFsmIds import HomeRobotRosFsmIds
from ros_ids.srv import ids_service, ids_serviceResponse


def ids_service_callback(req):
    ids= HomeRobotRosFsmIds()
    return ids_serviceResponse(ids.submit_test_action(req))


rospy.init_node('ids_node')
service=rospy.Service('ids_service', ids_service, ids_service_callback)
rospy.spin()

