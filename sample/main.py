import sys
from behaviortree.tree import Tree

def ACommand():
    print(sys._getframe().f_code.co_name)
    return True

def ACommand3():
    print(sys._getframe().f_code.co_name)
    return True

def ACommand1():
    print(sys._getframe().f_code.co_name)
    return True

def CGetFactorGraph():
    print(sys._getframe().f_code.co_name)
    return False

def ASensorException():
    print(sys._getframe().f_code.co_name)
    return True

def CGetFactorGraph1():
    print(sys._getframe().f_code.co_name)
    return False

def ACommand4():
    print(sys._getframe().f_code.co_name)
    return True

def ACommand5():
    print(sys._getframe().f_code.co_name)
    return True

def ACommand2():
    print(sys._getframe().f_code.co_name)
    return True

xmlfile = "./sample.xml"

bt_tree = Tree()
func_list = bt_tree.get_func_name(xmlfile)
eval_func = list(map(eval, func_list))
print("------gen_tree-----")
bt_tree.gen_tree(xmlfile, eval_func)
print("------dump-----")
bt_tree.dump()
print("------run-----")
bt_tree.run()