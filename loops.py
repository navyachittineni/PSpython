def check_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
num=2355
temp=num #should not effect the original value so work on the copy
sum=0
non_prime_sum=0
prime_sum=0
while temp>0:
    digit=temp%10
    print(digit)
    if not check_prime(digit):
        non_prime_sum+=digit
    else:
        prime_sum+=digit
    temp=temp//10
print(non_prime_sum)
print(prime_sum)

#even or odd check
#Armstrong number
#153- 3 digits
#1 + 125 + 27 =>153
#1634 -4 digits
#1 + 1206 + 81 + 256 =>1634
def is_armstrong(num):
    temp=num
    sum=0

    while temp>0:
        digit=temp%10
        sum+=digit**len(str(num)) # to make it work for all type digit numbers convert num to string and then find the length and raise the power to len of num1
        temp=temp//10  #temp value become 0 at last

    if sum==num:
       return True
    else:
       return False
    

min_num=300
max_num=10000

for i in range(min_num,max_num):
    if is_armstrong(i):
        print(i)

# Nearest prime

18- 17,19
26- 23,29
14- 13

num1 = 24
temp,temp2=num1,num1
right_side_prime = -1
left_side_prime = -1
while True:
    temp+=1
    if check_prime(temp):
        right_side_prime = temp
        break

print(right_side_prime)


while True:
    temp2 -= 1
    if temp2 <= 1:
        break
    if check_prime(temp2):
        left_side_prime = temp2
        break
print(left_side_prime)

if left_side_prime == -1: # Not found any prime
    print(right_side_prime)
elif num1 - left_side_prime > right_side_prime - num1:
    print(right_side_prime)
elif num1 - left_side_prime < right_side_prime - num1:
    print(left_side_prime)
else:
    print(left_side_prime,right_side_prime)
