"""
John Burris:

Today’s date is the beginning of the Fibonacci sequence. 1/1/23

I think everyone on the server should use this as incentive to practice coding before you return to school.

Write both a recursive function solution and an iterative (simple for loop) solution that produces the first 100 Fibonacci numbers

Reminder:
Fib(1) = 1
Fib(2) = 1
Fib(n) = Fib(n-2) + Fib(n-1)
Sequence: 1, 1, 2, 3, 5, 8, 13, 21,…
"""


#GLOABL VARIABLE FOR STARTING FIBONACCI SEQEUNCE
F0 = 0
F1 = 1


#How many iterations to run
iteration_amount = int(input("How many iterations of the Fibonacci Sequence would you like to do? "))
fib_sequence = []


#Do Recursively
fib_sequence.clear()
def recursive_fib(iteration_amount) -> int:
    if iteration_amount in {0, 1}:
        return iteration_amount
    else:
        return recursive_fib(iteration_amount - 1) + recursive_fib(iteration_amount - 2)

for i in range(iteration_amount):
    fib_sequence.append(recursive_fib(i))

print(fib_sequence)


#Do Iteratively
fib_sequence.clear()
for i in range(iteration_amount):
    if i == 0:
        fib_sequence.append(F0)
    elif i < 2:
        fib_sequence.append(F1)
    else:
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

print(fib_sequence)