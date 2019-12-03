#https://adventofcode.com/2019/day/2

import math

#input program given by the problem
input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,2,9,19,23,1,9,23,27,2,27,9,31,1,31,5,35,2,35,9,39,1,39,10,43,2,43,13,47,1,47,6,51,2,51,10,55,1,9,55,59,2,6,59,63,1,63,6,67,1,67,10,71,1,71,10,75,2,9,75,79,1,5,79,83,2,9,83,87,1,87,9,91,2,91,13,95,1,95,9,99,1,99,6,103,2,103,6,107,1,107,5,111,1,13,111,115,2,115,6,119,1,119,5,123,1,2,123,127,1,6,127,0,99,2,14,0,0]

#The 'computer' run function. The input is a intcode program.
def run_program(current_input):
    position = 0

    #While the instruction is not 99 (99 means the end of the program)
    while (current_input[position] != 99):
        #1 is the add opcode.
        #Take the first int as a position of the first addened.
        #Take the second int as a position of the second addened.
        #Add them and put them in the position indicated by the 3rd int.
        if current_input[position] == 1:
            current_input[current_input[position + 3]] = current_input[current_input[position + 1]] + current_input[current_input[position + 2]]
        #2 is the Multiply opcode.
        #Take the first int as a position of the first multiplicand.
        #Take the second int as a position of the second multiplicand.
        #Multiply them and put them in the position of the 3rd int.
        elif current_input[position] == 2:
            current_input[current_input[position + 3]] = current_input[current_input[position + 1]] * current_input[current_input[position + 2]]
        
        #Add and Multiply each take 4 ints as a command so move the pointer 4 spaces ahead.
        position += 4
    
    #After the program is done return the results in the 0th postition per the task instructions.
    return current_input[0]

#The basic gist is raise the 1st index of the input (which multiplies the 1st input by some big number)
#and once we are within a 99 difference between the result and the target we set the second input
#(which multiplies the 2nd input by 1) and print the result '(100 * noun) + verb'
result = 0
while (result != 19690720):
    #get the result
    result = run_program(input[:])

    if result > 19690720:
        print("went over")
        break
    elif result < 19690720:
        if (19690720 - result) < 99:
            print(f"{str((100 * input[1]) + (19690720 - result))}")
            break

        input[1] += 1