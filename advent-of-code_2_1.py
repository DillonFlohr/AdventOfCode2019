#https://adventofcode.com/2019/day/2

import math

input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,2,9,19,23,1,9,23,27,2,27,9,31,1,31,5,35,2,35,9,39,1,39,10,43,2,43,13,47,1,47,6,51,2,51,10,55,1,9,55,59,2,6,59,63,1,63,6,67,1,67,10,71,1,71,10,75,2,9,75,79,1,5,79,83,2,9,83,87,1,87,9,91,2,91,13,95,1,95,9,99,1,99,6,103,2,103,6,107,1,107,5,111,1,13,111,115,2,115,6,119,1,119,5,123,1,2,123,127,1,6,127,0,99,2,14,0,0]

position = 0

#While the instruction is not 99 (99 means the end of the program)
while (input[position] != 99):
    #1 is the add opcode.
    #Take the first int as a position of the first addened.
    #Take the second int as a position of the second addened.
    #Add them and put them in the position indicated by the 3rd int.
    if input[position] == 1:
        input[input[position + 3]] = input[input[position + 1]] + input[input[position + 2]]
    #2 is the Multiply opcode.
    #Take the first int as a position of the first multiplicand.
    #Take the second int as a position of the second multiplicand.
    #Multiply them and put them in the position of the 3rd int.
    elif input[position] == 2:
        input[input[position + 3]] = input[input[position + 1]] * input[input[position + 2]]
    
    #Add and Multiply each take 4 ints as a command so move the pointer 4 spaces ahead.
    position += 4

#After the program is done return the results in the 0th postition per the task instructions.
print(input[0])