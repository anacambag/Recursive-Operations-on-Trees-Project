
# Name: Ana Camba Gomes


from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation

tree1 = Node(8, Node(2, Node(1), Node(6)),Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    
    if tree.get_left_child() == None and tree.get_right_child() == None: #if there is no child there tree hight 0
        return 0
        
    
    else:
        if tree.get_right_child():
            right_child= find_tree_height(tree.get_right_child()) #recursive step to find height of right child
        else: 
            right_child= 0 
        
        if tree.get_left_child(): #recursive step to find height of left child
            left_child = find_tree_height(tree.get_left_child())   
        else: 
            left_child = 0 
            
    
    return max(left_child,right_child) + 1 #the max will be the right child height + left child height plus the height of the beggining
        

def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    if find_tree_height(tree) == 0: # if height is zero the compare function is true for both max and min
        return True
    
    else:
        if tree.get_right_child() != None and tree.get_left_child() != None: # if there is right and left child evaluate the values for both sides and we compare them with the function
            child_right = tree.get_right_child().get_value()
            child_left = tree.get_left_child().get_value()
            parent = tree.get_value() #value of node of parent to determine if there is a max or min
            return compare_func(child_right, parent) and compare_func(child_left, parent) and is_heap(tree.get_right_child(), compare_func) and is_heap(tree.get_left_child(), compare_func)
        
        elif tree.get_right_child() != None: #if there is only right child, use the compare function and is heap function on parent and right child values
            child_right = tree.get_right_child().get_value()
            parent = tree.get_value()
            return compare_func(child_right, parent) and is_heap(tree.get_right_child(), compare_func) #evaluates max and min value if they are true or false
        
        elif tree.get_left_child() != None: #if there is only left child, use the compare function and is heap function on parent and right child values
            child_left = tree.get_left_child().get_value()
            parent = tree.get_value()
            return compare_func(child_left, parent) and is_heap(tree.get_left_child(), compare_func)
    
    
        



if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass