

'''def s(n):
    while n > 0:
        print(n , end=' ')
        n -= 5
    
a = s(30)
print(a)'''

    
        

'''def q1(l):
    ans = set()
    for i in l:
        ans.add(i)
    l = list(ans)
    l.sort(reverse=True)
    print(l)
    max_num = 0
    second_max = 0
    for i in range(len(l) - 1):
        if l[i] > max_num:
            second_max = l[i]
            if second_max < max_num:
                print(second_max)
            max_num = l[i]
            
            
    print(f"second largest :- {second_max}")
nums = [4, 2, 9, 2, 4, 7]
q1(nums) '''     
'''
Write a function count_even() that accepts any 
number of numeric arguments and returns the number of even numbers among them.

def count_even(*nums):
    count = 0
    if len(nums) == 0:
        return 0
    else:
        for i in nums:
            if i % 2 == 0:
                count += 1
    return count

print(count_even(2, 5, 8, 11, 14))
print(count_even(3, 7, 9))
print(count_even())
'''
'''
def s():
    numbers = [1, 2, 3, 4, 5]

    result = list(map(lambda x: x * x, numbers))

    print(result)
s()
'''
'''
2 Coding Questions

Coding Q1 (Easy to Medium)
Write a function stats(*numbers) that uses built-in functions (sum, min, max, len) and prints the sum, 
minimum, maximum and average of any number of arguments. Call it as stats(4, 8, 15, 16).

Expected output:

Sum: 43
Min: 4
Max: 16
Average: 10.75
'''
'''
Coding Q2 (Hard)
This one has two parts.

Part A: Write a function make_counter(start=0, step=1) that returns an inner function. Each 
time the inner function is called, it adds step to the count (using nonlocal) and returns the new value.
python
counter = make_counter(10, 5)
print(counter(), counter(), counter())   # expected: 15 20 25
Part B: Given students = [("Ravi", 82), ("Anu", 91), ("Meet", 75)], sort it by marks in 
descending order using sorted() with a lambda.
[('Anu', 91), ('Ravi', 82), ('Meet', 75)]

def make_counter(start=0 , step = 1):
    def inner():
        nonlocal start
        nonlocal step
        start += step
        
        print(start)
        print(step)
    inner()
counter = make_counter(10 , 5)
print(counter())
 '''   
'''
def stats(*numbers):
    print(f"Sum: {sum(numbers)}")
    print(f"Min: {min(numbers)}")
    print(f"Max: {max(numbers)}")
    print(f"Average: {sum(numbers) // float(len(numbers))}")

stats(4, 8, 15, 16)
'''