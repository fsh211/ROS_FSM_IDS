import os.path
import datetime
import inspect
import sys
import pydoc

import rospy
from ros_ids.srv import ids_service,ids_serviceRequest,ids_serviceResponse
from src import ConfigFile
from std_msgs.msg import String


class Run:

    @classmethod
    def execute_operator_command(cls, commands_list):
        # we iterate command list and execute commands with or without ids

        startTime=datetime.datetime.now()
        for item in commands_list:
            # main_object = item.split('.', 2).__getitem__(0)
            main_work = item.split('.', 2).__getitem__(0).replace("\"", " ").strip()
            # detail_method = item.split('.', 2).__getitem__(1)
            detail_work = item.split('.', 2).__getitem__(1).replace("\"", " ").strip()
            # check validation of method
            if str(main_work) in ConfigFile.level1_behavior_defined and detail_work in ConfigFile.level2_behavior_defined:
                if ConfigFile.level1_ids_enabled == "true":
                    if ConfigFile.level2_ids_enabled == "true":
                        if cls.run_with_ids(main_work, detail_work)== False:
                            print ("IDS attack detection in level 2: command should not continue")
                            break
                    else:
                        if detail_work == "start" or detail_work == "end":
                            if cls.run_with_ids(main_work, detail_work) == False:
                                print("IDS attack detection in level 1: command should not continue")
                                break
                        else:
                            cls.run_without_ids(main_work, detail_work)
                else:
                    cls.run_without_ids(main_work,detail_work)
            else:
                print("command is not valid")
        exitTime = datetime.datetime.now()
        print("execution time="+ str(exitTime-startTime))

    @classmethod
    def run_with_ids(cls, main_work, detail_work):
        # construct messages and ids command object
        terminal_message = "behavior_" + main_work + "_" + detail_work
        ids_message = "fsm_ids_" + main_work + "_" + detail_work
        # get ids to check
        serv = rospy.ServiceProxy('ids_service', ids_service)
        resp = serv(ids_message)
        # started = HomeRobotRosFsmIds.get_instance().submit_test_action(inspect.getattr_static(ConfigFile, ids_message))
        # check ids result and print
        if resp.transition:
            print(inspect.getattr_static(ConfigFile, terminal_message) + " start at " + str(
                datetime.datetime.now()))
            cls.run_without_ids(main_work, detail_work)
            rospy.loginfo("Executed service")
            print(inspect.getattr_static(ConfigFile, terminal_message) + " end at " + str(
                datetime.datetime.now()))
        else:
            return False

    @classmethod
    def run_without_ids(cls, main_work, detail_work):
        main_object = pydoc.locate("home_robot_behavior."+main_work)
        method_call = getattr(getattr(main_object,main_work), detail_work)
        method_call()


if __name__ == '__main__':
    try:
        rospy.init_node('run_node', anonymous=False)
        if os.path.exists(sys.argv[1]):
            with open(sys.argv[1], "r") as my_file:
                Run.execute_operator_command(my_file.read().split("\n"))
        else:
            Run.execute_operator_command(str(sys.argv[1]).split("\\n"))

    except rospy.ROSInterruptException:
        pass
