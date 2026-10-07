print(455//2)# it sends round out value of the numerator 

"""Loops in python while loop """

# n=1
# while n<=10:
#     if n==5: 
#         n+=1
#         continue
#     print(n)
#     n+=1

# """Loops in python For Loop"""

# for i in range(1,10):print(i)

# for i in range(1,10,2):print(i)

# """String in loops"""

# for ch in 'Python':
#     if ch == 'h':
#         break
#     print(ch)


# """For loop example """

# for hours in range(8,17,2):
#     if hours<12:
#         print(f'it is {hours} AM !')
#     elif hours ==12:
#         print(f'It is noon')
#     else:
#         print(f'It is {hours} PM')


"""Else statement in for loop"""

# for i in range(5):
#     print(i)
# else:
#     print("The for loop has finished")


# for i in range(5):
#     print(i)
#     if i == 3: break
# else:
#     print('The for loop has finished executing.')

"""Nested for Loop"""

rows = 6
columns = 6

for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        print(str(i * j), end = ' ')
    print()