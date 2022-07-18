import sys
from behaviortree.tree import Tree

def CAmIHungry():
    print(sys._getframe().f_code.co_name)
    return True

def CDoIHaveFood():
    print(sys._getframe().f_code.co_name)
    return True

def AEnemiesNotAround():
    print(sys._getframe().f_code.co_name)
    return True

def AEatFood():
    print(sys._getframe().f_code.co_name)
    return True

xmlfile = "sample/EatFood/tree.xml"

bt_tree = Tree()
func_list = bt_tree.get_func_name(xmlfile)
eval_func = list(map(eval, func_list))
# Generate behavior tree。
bt_tree.gen_tree(xmlfile, eval_func)
# Print the structure of the tree。
bt_tree.dump()
# Execution tree。
bt_tree.run()