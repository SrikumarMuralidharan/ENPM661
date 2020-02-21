import copy

# Getting input from user
def zero_coord(node_i):
    for i in range(3):
        for j in range(3):
            if (node_i[i][j]==0):
                return i,j

def Arr_to_str(a):
    b=""
    for i in range(3):
        for j in range(3):
            b+=str(a[i][j])
    return b

def Solvable(Inp_node):
    b=[]
    inversion=0
    for i in range(3):
        for j in range(3):
            if (Inp_node[i][j]!=0):
                b.append(Inp_node[i][j])            
    for i in range(7):
        j=i+1
        while(j<8):
            if b[i]>b[j]:
                inversion+=1
            j+=1
    if inversion%2:
        print("\nPuzzle is unsolvable")
        return 0
    else:
        print("\nPuzzle is solvable\n")
        return 1
    
    
#checking if new node configuration already exists; if not appending the same onto the parent node:
def check_and_append(Parent_node, new_string, count, Goal):
    temp_1=copy.deepcopy(Parent_node)
    c=copy.deepcopy(count)
    breaker=1
    Goal_num=0
    for i in range(c):
        if temp_1[i]==new_string:
            breaker=0
            break
    if breaker==1:
        temp_1.append(new_string)
        c+=1
    if (new_string==Goal):
        Goal_num=1
    return temp_1, c, Goal_num, breaker

#defining function to swap the zero left
def left_slide(node_i, Row, Col):
    temp = copy.deepcopy(node_i)
    if Col!=0:
        swap = temp[Row][Col-1]
        temp[Row][Col-1]=0
        temp[Row][Col]=swap
    return temp

#defining function to swap the zero right
def right_slide(node_i, Row, Col):
    temp = copy.deepcopy(node_i)
    if Col!=2:
        temp[Row][Col] = temp[Row][Col+1]
        temp[Row][Col+1]=0
    return temp

#defining function to swap the zero up
def up_slide(node_i, Row, Col):
    temp = copy.deepcopy(node_i)
    if Row!=0:
        temp[Row][Col] = temp[Row-1][Col]
        temp[Row-1][Col]=0
    return temp

#defining function to swap the zero down
def down_slide(node_i, Row, Col):
    temp = copy.deepcopy(node_i)
    if Row!=2:
        temp[Row][Col] = temp[Row+1][Col]
        temp[Row+1][Col]=0
    return temp
           
# main code
    
Orig_P_node=[]
print("Enter entries row-wise")
Input_node = []
for i in range(3):    
    element_val = []
    for j in range(3):
        element_val.append(int(input()))
    Input_node.append(element_val)

Count = 1
Goal_state= [[1,2,3],
              [4,5,6],
              [7,8,0]]

Address=[]
Address.append(-1)
Orig_P_node.append(Input_node)
Orig_P_str=[]
Orig_P_str.append(Arr_to_str(Input_node))
G_count=0
Node_index_i=0
Goal=Arr_to_str(Goal_state)

if (Solvable(Input_node)):
    while(Node_index_i<Count):
        P_node= copy.deepcopy(Orig_P_node[Node_index_i])
        Row, Col=zero_coord(P_node)
    
        if not(G_count):
            Node_state_i = down_slide(P_node, Row, Col)
            Node_str=Arr_to_str(Node_state_i)
            Orig_P_str, Count, G_count, Did_append = check_and_append(Orig_P_str, Node_str, Count, Goal)
            if Did_append:
                Address.append(Node_index_i)
                Orig_P_node.append(Node_state_i)
        else:
            print("Goal reached!")
            break
    
        if not(G_count):
            Node_state_i = up_slide(P_node, Row, Col)
            Node_str=Arr_to_str(Node_state_i)
            Orig_P_str, Count, G_count, Did_append = check_and_append(Orig_P_str, Node_str, Count, Goal)
            if Did_append:
                Address.append(Node_index_i)
                Orig_P_node.append(Node_state_i)
        else:
           print("Goal reached!")
           break
    
        if not(G_count):
            Node_state_i = left_slide(P_node, Row, Col)
            Node_str=Arr_to_str(Node_state_i)
            Orig_P_str, Count, G_count, Did_append = check_and_append(Orig_P_str, Node_str, Count, Goal)
            if Did_append:
                Address.append(Node_index_i)
                Orig_P_node.append(Node_state_i)
        else:
            print("Goal reached!")
            break
    
        if not(G_count):
            Node_state_i = right_slide(P_node, Row, Col)
            Node_str=Arr_to_str(Node_state_i)
            Orig_P_str, Count, G_count, Did_append = check_and_append(Orig_P_str, Node_str, Count, Goal)
            if Did_append:
                Address.append(Node_index_i)
                Orig_P_node.append(Node_state_i)
        else:
            print("Goal reached!")
            break
    
    
        print("count of unique configs:" + str(Count))
        Node_index_i+=1
    #End of while loop

    print("Total number of unique configurations")
    print(Count)

    print("Address of the goal object")
    Add=[]
    inc= Count - 1
    while(inc>=0):
        Add.append(inc)
        inc=Address[inc]
        Add.reverse()
        
    for i in range(len(Add)):
        print(str(Add[i]))    

    print("shortest sequence from start to end")
    for i in range(len(Add)):
        l=Add[i]
        for j in range(3):
            for k in range(3):
                print(Orig_P_node[l][j][k], end=' ')
            print('')
        print('')
   