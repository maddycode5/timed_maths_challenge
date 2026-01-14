import random
import time

OPERATORS=["+","-","*"]
MIN_OPERAND=2
MAX_OPERAND=15
TOTAL_PROBLEMS=[5,10,15,20,25]

while True:
    problems=input(f"Chose how many problems you wan to solve {TOTAL_PROBLEMS} :")
    if problems.isdigit() and int(problems) in TOTAL_PROBLEMS:
        problem = int(problems)
        break
    print("Please chose a valid number from the list!")

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right= random.randint(MIN_OPERAND,MAX_OPERAND)
    operators=random.choice(OPERATORS)

    exp=str(left) + " " + operators + " " + str(right)

    answer=eval(exp)
    return exp,answer

wrong=0
input("PRESS ENTER TO START !!")
print(" ------------------------- ")

start_time =time.time()

for i in range(problem):
    exp ,answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) + ":  " + exp + " = ")    
        if guess == str(answer):
            break
        wrong+=1

end_time=time.time()
total_time = end_time - start_time
print("NICE WORK!,You finished in " , total_time , "seconds")
