class nArry:
    """
class of the narry tree (the node itself and its children)
    """
    def __init__(self,val):
        """
        Ctor of the the class resets all the values

        :param val: value of the node itself
        """
        self.val = val
        left =middleLeft=middleRight=right=None
        self.nodes=[left,middleLeft,middleRight,right]

    def __str__(self):
        """
        prints the tree

        :return: space string
        """
        PrintTheTree(self)
        return " "
    def __repr__(self):
        """
        prints how the class looks to the program

        :return: string of how the class looks to the program
        """
        return f'nArry({self.val})'
    def getVal(self):
        """
        gets the value of the node

        :return: value of the root
        """
        return self.val
    def AddValue(self,newNode):
        """
        adds a value to the tree

        :return: function that adds a value to the tree
        """
        return insert(tree, newNode)
    def DeleteValue(self,value):
        """
        removes a value from the tree

        :param value: value of the root
        :return: function that removes a value from the tree
        """
        return(RemoveValue(self, value,self))

class TreeError(Exception):
    """
    base Exception class
    """
    def __init__(self):
        """
        Ctor that resets the tree

        """
        self.tree = tree

class TreeValueDoesNotExist(TreeError):
    """
    exception class that except exceptions of values that does not exist
    """
    def __init__(self,value):
        """
        Ctor that reset the value and the tree

        :param value: value of the root
        """
        self.tree = tree
        self.value=value
    def returnMistake(self):
        """
        returns why the exception happened

        :return: string of why the exception happened
        """
        return f"TreeValueDoesNotExist: this value does not exist in the tree, in order do delete a value you must enter an existing node, the value that wasn't deleted is: {self.value}"


class TreeIllegalValue(TreeError):
    """
        exception class that except exceptions of value that is not a leaf
    """
    def __init__(self,value):
        """
        Ctor that reset the value and the tree

        :param value: value of the root
        """
        self.tree = tree
        self.value=value
    def returnMistake(self):
        """
        returns why the exception happened

        :return: string of why the exception happened
        """
        return f"TreeIllegalValue: this value is illegal, in order do delete a node you must enter a value of a leaf, the value that wasn't deleted is: {self.value}"


def iter_improve(tree, value):
    """
    catches the exceptions of the deleting errors

    :param tree: the root node
    :param value: value of the root
    :return: function that deletes the node from the tree
    """
    try:
        return tree.DeleteValue(value)
    except AttributeError as error:
        TreeValueDoesNotExist(value).returnMistake()
        raise TreeValueDoesNotExist(value)

def preorderTraversal(root):
    """
    finds all the nodes in the tree

    :param root: the root node
    :return: list of all the nodes in the tree
    """
    answer = []
    preorderTraversalUtil(root, answer)
    return answer

def preorderTraversalUtil(root, answer):
    """
    collects all the nodes in the tree to a list

    :param root: the root node
    :param answer: list of all the nodes in the tree
    """
    if root is None:
        return
    answer.append(root)
    preorderTraversalUtil(root.nodes[0], answer)
    preorderTraversalUtil(root.nodes[1], answer)
    preorderTraversalUtil(root.nodes[2], answer)
    preorderTraversalUtil(root.nodes[3], answer)
    return

def rtraverse(seq, i=0):
    """
    prints every node and its 4 children

    :param seq: list of all the nodes in the tree
    :param i: index
    :return: space string
    """
    if i < len(seq):
        answer=[]
        if seq[i].nodes[0]!=None:
            answer.append(seq[i].nodes[0])
        if seq[i].nodes[1] != None:
            answer.append(seq[i].nodes[1])
        if seq[i].nodes[2]!=None:
            answer.append(seq[i].nodes[2])
        if seq[i].nodes[3]!=None:
            answer.append(seq[i].nodes[3])

        nodesVals = list(map(lambda x:x.getVal(), answer))
        nodesVals = list(map(lambda x: f'<{x.getVal()}>', answer))
        print (f'<{seq[i].getVal()}>',end=" " )
        print('[',*nodesVals, sep=";",end="")
        print("]")
        rtraverse(seq, i+1)
        return " "

def insert(root, key):
    """
    adds a new node to the tree

    :param root: the root node
    :param key: value of root
    :return: the tree after there was an insert of new node
    """
    if root is None:
        return nArry(key)

    if (root.nodes[0] != None and root.nodes[1]!= None and key<root.val) or (root.nodes[2] != None and root.nodes[3]!= None and key>root.val):
        if key < root.val:
            if root.nodes[0]!= None:
                if root.nodes[0].getVal() < key:
                    leftRight = insert(root.nodes[1], key)
                    root.nodes[1]=leftRight
                else:
                    left = insert(root.nodes[0], key)
                    root.nodes[0]=left
            else:
                left = insert(root.nodes[0], key)
                root.nodes[0]=left
        else:
            if root.nodes[2]!= None:
                if root.nodes[2].getVal() < key:
                    right = insert(root.nodes[3], key)
                    root.nodes[3]=right
                else:
                    rightLeft = insert(root.nodes[2], key)
                    root.nodes[2]=rightLeft
            else:
                rightLeft = insert(root.nodes[2], key)
                root.nodes[2]=rightLeft
    else:
        newNode=nArry(key)
        if key < root.val:
            if root.nodes[0]!= None:
                if root.nodes[0].getVal() < key:
                    root.nodes[1]=newNode
                else:
                    root.nodes[1]=root.nodes[0]
                    root.nodes[0]=newNode
            else:
                root.nodes[0]=newNode
        else:
            if root.nodes[2]!= None:
                if root.nodes[2].getVal() < key:
                    root.nodes[3]=newNode
                else:
                    root.nodes[3] = root.nodes[2]
                    root.nodes[2]=newNode
            else:
                root.nodes[2]=newNode
    return root

def CreateTree():
    """
    creates a new tree

    :return: the tree
    """
    try:
        head=int(input("please enter the value of the head of the new tree (only numbers):"))
        tree=nArry(head)
        return tree
    except ValueError as error:
        print("GENERAL ERROR: oops.. you did something wrong. GOODBYE! ")
        return False
def RemoveValue(root,key,originalRoot):
    """
    removes a value from the tree

    :param root: the root node
    :param key: value of the root
    :param originalRoot: the root node that will not be changed (to print the full tree in case of an error)
    :return: the tree after a node has been removed
    """
    try:
        if root.getVal()==key:
            if root.nodes[0]==None and root.nodes[1]==None and root.nodes[2]==None and root.nodes[3]==None:
                root=None
                return root
            else:
                raise TreeIllegalValue(value)

        for i in range(3):
            if root.nodes[i]!=None:
                if root.nodes[i].getVal()==key:
                    root.nodes[i]=None
                    return root

        if key < root.val:
            if root.nodes[0] != None:
                if root.nodes[0].getVal() < key:
                    RemoveValue(root.nodes[1], key,originalRoot)
                else:
                    RemoveValue(root.nodes[0], key,originalRoot)
            else:
                RemoveValue(root.nodes[1], key,originalRoot)
        else:
            if root.nodes[2] != None:
                if root.nodes[2].getVal() < key:
                    right = RemoveValue(root.nodes[3], key,originalRoot)
                else:
                    rightLeft = RemoveValue(root.nodes[2], key,originalRoot)
            else:
                rightLeft = RemoveValue(root.nodes[3], key,originalRoot)
        return root
    except TreeIllegalValue as err:
        print(TreeIllegalValue(value).returnMistake())
        print(str(originalRoot))

def PrintTheTree(tree):
    """
    prints the tree

    :param tree: the root node
    :return: space string
    """
    answer = preorderTraversal(tree)
    rtraverse(answer, i=0)
    return " "

def printGeneralOptions():
    """
    prints the main options
    """
    print("Please choose one of the following options:\n Press:\n")
    print("----------------------------------------------------------------------\n")
    print("1- Create a new tree\n")
    print("2- Add a new node to the tree\n")
    print("3- Remove a node from the tree\n")
    print("4- Print the tree\n")
    print("5- Exit\n")
    print("----------------------------------------------------------------------\n")

allNodes=[]
tree=None
GeneralRun = True
while GeneralRun:
    try:
        printGeneralOptions()
        option = input("Your choice is: ")
        if option == '1':
            tree=CreateTree()
            allNodes.append(tree.val)
            if tree==False:
                GeneralRun=False

        elif option=='2':
            try:
                if tree==None:
                    raise UnboundLocalError('tree does not exist. Please create a tree')

                newNode = int(input("please enter value new node (only numbers that does not exist in the tree): "))
                if newNode in allNodes:
                    raise ValueError
                tree.AddValue(newNode)
                allNodes.append(newNode)
            except UnboundLocalError as err:
                print(f"UnboundLocalError: {err}.")
            except ValueError as error:
                print("GENERAL ERROR: oops.. you did something wrong. GOODBYE! ")
                GeneralRun=False

        elif option == '3':
            try:
                if tree==None:
                    raise UnboundLocalError('tree does not exist. Please create a tree')
                value = int(input("please enter the value of node you wish to remove (only numbers):"))
                tree = iter_improve(tree, value)
            except TreeValueDoesNotExist as e:
                print (TreeValueDoesNotExist(value).returnMistake())
                print(str(tree))
            except ValueError as error:
                print("GENERAL ERROR: oops.. you did something wrong. GOODBYE! ")
                GeneralRun = False
            except UnboundLocalError as err:
                print(f"UnboundLocalError: {err}")

        elif option == '4':
            PrintTheTree(tree)
        elif option == '5':
            GeneralRun = False
            print("The system closed successfully\n")
        else:
            raise UnboundLocalError('Wrong option, you must insert a number between 1-5. Please try again!')

    except UnboundLocalError as err:
        print(f"UnboundLocalError: {err}.")



