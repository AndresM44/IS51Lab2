
"""
start
get the numbers of sheets
sheets/5
round answer to next number
output the result to the user
end
"""
import math

# input: sheet
def calculate(sheet):
    # step 1
    answer = sheet / 5
    # step 2
    rounded = math.ceil(answer)
    print("sheet is: ", sheet)
    print("the answer is: ", answer)
    print("rounded is: ", rounded)
    print("==================================")
    # output: numberof stamps needed 
    return rounded

output = calculate(16)

print("The number of stamps needed is: ", output)

