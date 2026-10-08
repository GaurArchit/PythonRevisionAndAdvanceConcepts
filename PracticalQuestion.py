print("Hello world")

"""Write a program to calculate the sum of all even numbers from 1 to N (inclusive)."""

# N=int(input("Enter a number"))
# sum=0
# while N>=0:
#     print(N)
#     if N %2==0:
#         sum+=N
#     N-=1
# else:
#     print(sum)



"""ite a program to count the number of digits in a given positive integer N. You need to repeatedly divide the number by 10 and count how many times you can do this before the number becomes zero. This simulates removing the last digit each time.
If the input number is zero, the count of digits should be 1, since zero itself is a single-digit number."""

NintoString=input("Enter a number")
count =0

for i in NintoString:
    count+=1
else:
    print(count)

"""Write a program to print numbers from 1 to n (inclusive), but skip any number that is a multiple of 3."""
n=int(input("Enter a number from 1 to n"))
for i in range(1,n+1):
    if i%3==0:
        continue
    print(i) 