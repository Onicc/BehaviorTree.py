from xml.etree.ElementTree import parse

key_list = ["Sequence", "Fallback"]
func_key_list = ["Action", "Condition"]

class Tree:
    """The basic node of tree structure"""
    def __init__(self, type="root", depth=1, index=0, id=None, func=None, parent=None):
        self.type_ = type
        self.depth_ = depth
        self.index_ = index
        self.id_ = id
        self.child_ = []
        self.parent_ = parent
        self.func_ = func

    def __copy(self, tree):
        self.type_ = tree.type_
        self.depth_ = tree.depth_
        self.index_ = tree.index_
        self.id_ = tree.id_
        self.child_ = tree.child_
        self.parent_ = tree.parent_
        self.func_ = tree.func_

    def __get_parent(self):
        return self.parent_

    def __add_child(self, type, depth=1, index=0, id=None, func=None):
        """add a child node to current node"""
        obj = Tree(type, depth, index, id, func)
        obj.parent_ = self
        self.child_.append(obj)
        return obj

    def dump(self, indent=0):
        """dump tree to string"""
        tab = '    '*(indent-1) + ' |- ' if indent > 0 else ''
        if(self.id_ != None):
            print('%s%s:%s %s %s' % (tab, self.type_, self.id_, self.depth_, self.index_))
        else:
            print('%s%s %s %s' % (tab, self.type_, self.depth_, self.index_))
        for child in self.child_:
            child.dump(indent+1)

    def run(self):
        if(self.id_ != None and self.func_ != None):
            return self.func_()

        for child in self.child_:
            status = child.run()
            if(status != None):
                if(self.type_ == "Sequence"):
                    if(not status):
                        return status
                if(self.type_ == "Fallback"):
                    if(child.type_ == "Condition"):
                        if(status == True):
                            return True
                        else:
                            continue
                    else:
                        return status
    
    def __get_func_name(self, root, name):
        if(root.tag in func_key_list):
            name.append(root.attrib["ID"])
            # print(root.attrib["ID"])

        if(len(root) != 0 and root.tag != "TreeNodesModel"):
            for child in root:
                self.__get_func_name(child, name)

    def __gen_tree(self, root, bt_tree, move_tree, index, index_in, first, func):
        if(root.tag in key_list):
            if(first):
                move_tree = bt_tree.__add_child(root.tag, index, index_in)
                first = 0
            else:
                move_tree = move_tree.__add_child(root.tag, index, index_in)
        else:
            if(move_tree != None and root.tag in func_key_list):
                move_tree.__add_child(root.tag, index, index_in, root.attrib["ID"], func[root.attrib["ID"]])

        if(len(root) != 0):
            index += 1
            for i, child in enumerate(root):
                index_in = i
                self.__gen_tree(child, bt_tree, move_tree, index, index_in, first, func)
            index -= 1
            if(move_tree != None):
                move_tree = move_tree.__get_parent()

    def get_func_name(self, xmlfile):
        tree = parse(xmlfile)
        root = tree.getroot()
        name = []
        self.__get_func_name(root, name)
        return name

    def gen_tree(self, xmlfile, funcs):
        func_dict = {str(func).split(" ")[1]:func for func in funcs}
        tree = parse(xmlfile)
        root = tree.getroot()
        bt_tree = Tree()
        move_tree = None
        index = 0
        index_in = 0
        first = 1
        self.__gen_tree(root, bt_tree, move_tree, index, index_in, first, func_dict)
        self.__copy(bt_tree)