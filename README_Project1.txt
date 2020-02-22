# ENPM 661 
# Planning for Autonomous robots
# Project 1
# Eight piece puzzle using BFS algorithm
# Author: Srikumar Muralidharan
# UID: 116950572
# GITHUB link: https://github.com/SrikumarMuralidharan/ENPM661

This folder consists of the following files:
1. Eight_puzzle.py
2. plot_path.py
3. nodePath.txt
4. Nodes.txt
5. NodesInfo.txt

Eight_puzzle.py consists of the python code for running  Brute Force Search algorithm to find the path to reach goal state. The input is to be given by user in real-time, row-wise. Enter each number (from 0-8, only once) in any order and after each number press "enter key'. Once 9 inputs are received from the user, the output will either be that the code is solvable or not solvable. If the input is not solvable, the program ends there and a message is displayed. However, if the input is solvable, the code runs and shows the number of unique configurations generated per iteration and stops when goal configuration is reached. We have used 2 unique libraries "copy" and "time". I faced a lot of difficulties with the regular copy() function, so i had to use copy.deepcopy() to achieve better results. Also, i used the function time.time() to record how long the ccomputation was running. Once the goal is reached, prominent messages will be displayed and the shortest path to achieve goal state from input state will be displayed, along with addresses of each node involved in sequence. Also, we generate three text files:
	1. nodePath.txt - stores nodes involved in the sequence from input to goal configuration, column wise.
	2. Nodes.txt - stores all unique nodes generated from input to goal configuration, column wise.
	3. NodesInfo.txt - stores address of parent node for a particular node in the desired (shortest) sequence from input to goal

After obtaining these results, we can run plot_path.py file to get a visual representation of our algorithm to go from input to output.

