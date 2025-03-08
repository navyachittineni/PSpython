def remove_dups(arr):
    seen=set()
    result=[]
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
print(remove_dups([1,0,1,0]))
#no.of occurences in dict format


#quick sort
def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quicksort(left)+middle+quicksort(right)
print(quicksort([3,1,6,2,8]))
#full pyramid
def full_pyramid(n):
    for i in range(1,n+1):
        for j in range(0,n-i):
            print(" ",end=" ")
        for k in range(1,2*i):
            print("*",end=" ")
        print()
full_pyramid(5)
#half pyramid
def half_pyramid(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
half_pyramid(5)
#reverse case
def reverse_case(string):
    if not isinstance(string,str):
        return "Invalid Input: Input must be string"
    reversed_string=" "
    for char in string:
        if char.isalpha():
            if char.islower():
               reversed_string+=char.upper()
            elif char.isupper():
               reversed_string+=char.lower()
            else:
               reversed_string+=char
    return reversed_string
print(reverse_case("Yamini_Navya"))
#char count
def char_count(char,string):
    if not isinstance(char,str) and len(char)!=1 and string is None:
        return 0
    count=0
    for c in string:
        if c==char:
            count+=1
    return count
print(char_count("c","chamber of secrets")) 
#count of vowels
def vowels_count(string):
    if not isinstance(string,str):
        return "Invalid Input"
    vowels="aeiouAEIOU"
    count=0
    for char in string:
        if char in vowels:
            count+=1
    return count
print(vowels_count("Adam"))
#count vowel and consonant count
s=str(input("Enter a string:")).lower()
vowel_count=0
consonant_count=0
vowels="aeiou"
for char in s:
    if char in vowels:
       vowel_count+=1
    else:
       consonant_count+=1
print(f"{vowel_count} vowels and {consonant_count} consonants")
#data type
def determine_datatype(data):
    if isinstance(data,int):
        return "Integer"
    elif isinstance(data,float):
        return "float"
    elif isinstance(data,str):
        return "string"
    elif isinstance(data,bool):
        return "boolean"
    elif data is None:
        return "Nonetype"
    else:
        return "Unknown"
print(determine_datatype(500))
#fibonacci
def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        print(a,end=" ")
        a,b=b,a+b
    print()
fibonacci(10)
#palindrome number
num=123
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
if num==rev:
    print("Not palindrome")
else:
    print("Palindrome")

    




        
    

