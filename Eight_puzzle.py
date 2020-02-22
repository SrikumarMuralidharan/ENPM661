'''
ENPM 661 
Planning for Autonomous Robots
Project-1
8 Puzzle problem solution using BFS algorithm
Author: Srikumar Muralidharan
UID: 116950572
'''

import time
import copy

# Function to find location of zero at that node
def zero_coord(node_i):
    for i in range(3):
        for j in range(3):
            if (node_i[i][j]==0):
                return i,j

# Function to convert a 2D array to string
def Arr_to_str(a):
    b=""
    for i in range(3):
        for j in range(3):
            b+=str(a[i][j])
    return b

# Function to check if Input is solvable for given goal state
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
    
    
# Function to check if new node configuration already exists; 
# If not, appending the same onto the parent node
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

# Function to slide the zero left
def left_slide(node_i, Row, Col):
    temp = copy.deepcopy(node_i)
    if Col!=0:
        temp[Row][Col] = temp[Row][Col-1]
        temp[Row][Col-1]=0
    return temp

# Function to slide the zero right
def right_slide(node_i, Row, Col):
    temp = copy.deepcopy(node_i)
    if Col!=2:
        temp[Row][Col] = temp[Row][Col+1]
        temp[Row][Col+1]=0
    return temp

# Function to slide the zero up
def up_slide(node_i, Row, Col):
    temp = copy.deepcopy(node_i)
    if Row!=0:
        temp[Row][Col] = temp[Row-1][Col]
        temp[Row-1][Col]=0
    return temp

# Function to slide the zero down
def down_slide(node_i, Row, Col):
    temp = copy.deepcopy(node_i)
    if Row!=2:
        temp[Row][Col] = temp[Row+1][Col]
        temp[Row+1][Col]=0
    return temp
           
# Main code
    
Orig_P_node=[]             #Parent Matrix to which unique configs get appended
# Accepting input from user
print("Enter entries row-wise")
Input_node = []
for i in range(3):    
    element_val = []
    for j in range(3):
        element_val.append(int(input()))
    Input_node.append(element_val)

start_time=time.time()      #Starting clock for computation
Count = 1                   #Count to keep track of unique configurations
Goal_state = [[1,2,3],      #If we change goal state, we have to change solvability criteria as well
              [4,5,6],
              [7,8,0]]

Address=[]                  #Keeps track of address of its parent element
Address.append(0)           #For the first element
Orig_P_node.append(Input_node)  #Appending input to parent node
Orig_P_str=[]               #Parent Matrix used to store string equalent of unique configs
Orig_P_str.append(Arr_to_str(Input_node))   #Appending input to parent node as a string
G_count=0                   #Variable that is updated when goal is reached
Node_index_i=0              #Iterand that keeps track of node that is being operated on
Goal=Arr_to_str(Goal_state) #Goal matrix as a string

if (Solvable(Input_node)):  #Checking if input is solvable
    while(Node_index_i<Count):  #start of iterations
        P_node= copy.deepcopy(Orig_P_node[Node_index_i]) #Taking node at iterand's address
        Row, Col=zero_coord(P_node) #Obtaining zero at that position
    
        if not(G_count):    #if we havent reached the goal
            Node_state_i = down_slide(P_node, Row, Col) #tries to do slide down operation
            Node_str=Arr_to_str(Node_state_i)   #converting new/original node to string to be used below
            Orig_P_str, Count, G_count, Did_append = check_and_append(Orig_P_str, Node_str, Count, Goal)
            if Did_append:  #If appended
                Address.append(Node_index_i+1)  #Appending address
                Orig_P_node.append(Node_state_i)    #Appending node to parent matrix
        else:               #if we have reached the goal
            print("Goal reached!")
            break
    
        if not(G_count):
            Node_state_i = up_slide(P_node, Row, Col)   #tries to do slide down operation
            Node_str=Arr_to_str(Node_state_i)   
            Orig_P_str, Count, G_count, Did_append = check_and_append(Orig_P_str, Node_str, Count, Goal)
            if Did_append:
                Address.append(Node_index_i+1)
                Orig_P_node.append(Node_state_i)
        else:
           print("Goal reached!")
           break
    
        if not(G_count):
            Node_state_i = left_slide(P_node, Row, Col) #tries to do slide down operation
            Node_str=Arr_to_str(Node_state_i)   
            Orig_P_str, Count, G_count, Did_append = check_and_append(Orig_P_str, Node_str, Count, Goal)
            if Did_append:
                Address.append(Node_index_i+1)
                Orig_P_node.append(Node_state_i)
        else:
            print("Goal reached!")
            break
    
        if not(G_count):
            Node_state_i = right_slide(P_node, Row, Col)    #tries to do slide down operation
            Node_str=Arr_to_str(Node_state_i)  
            Orig_P_str, Count, G_count, Did_append = check_and_append(Orig_P_str, Node_str, Count, Goal)
            if Did_append:
                Address.append(Node_index_i+1)
                Orig_P_node.append(Node_state_i)
        else:
            print("Goal reached!")
            break
    
    
        print("count of unique configs:" + str(Count))  #Prints number of unique configurations till then
        Node_index_i+=1 #incrementing iterand
    #End of while loop

    print("\nTotal number of unique configurations")
    print(Count)    #Total number of unique configurations

    print("Shortest path to reach goal operation is to follow these configurations:") 
    Add=[]
    inc= Count - 1
    while(inc>=0):
        Add.append(inc)
        inc=Address[inc]-1
    Add.reverse()
        
    for i in range(len(Add)):
        print(str(Add[i]))    #Prints Address of path to goal

    #Printing matrices that form the sequence from input to goal
    print("shortest sequence from start to end")
    for i in range(len(Add)):
        l=Add[i]
        for j in range(3):
            for k in range(3):
                print(Orig_P_node[l][j][k], end=' ')
            print('')
        print('')
    
    #Creating File_1 nodePath.txt that stores configs in the shortest path
    #Column wise
    File_1=open("nodePath.txt", "w+")
    for i in range(len(Add)):
        l=Add[i]
        for j in range(3):
            for k in range(3):
                File_1.write(str(Orig_P_node[l][k][j]))
                File_1.write(str(" "))
        File_1.write(str("\n"))
    File_1.close()
    
    #Creating File_2 NodesInfo.txt that stores the values of all configurations and 
    #their parents and the third column is the cost associated with it
    File_2=open("NodesInfo.txt", "w+")
    for i in range(len(Address)):
        File_2.write(str(i+1))
        File_2.write(" ")
        File_2.write(str(Address[i]))
        File_2.write(" ")
        File_2.write("0")
        File_2.write("\n")
    File_2.close()
    
    #Creating File_3 Nodes.txt that store all unique configurations recorded 
    #Column wise
    File_3=open("Nodes.txt", "w+")
    for i in range(Count):
        for j in range(3):
            for k in range(3):
                File_3.write(str(Orig_P_node[i][k][j]))
                File_3.write(str(" "))
        File_3.write(str("\n"))
    File_3.close()

# Function to record operation time
print("total time:")
print(time.time()-start_time)        