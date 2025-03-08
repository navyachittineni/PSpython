num=int(input("Enter a no: "))
flag=False
if num==0 or num==1:
    print("Not a prime")
elif num>1:
    for i in range(2,num):
        if num%i==0:
            flag=True
            break
    if flag:
           print(num,"is not prime")
    else:
           print(num,"is a prime")


#@2nd approach
import math

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

print(is_prime(29))  # True
print(is_prime(10))  # False

#counting occurences of all numbers in an array
def count_occurrences_dict(arr):
    """Counts the occurrences of each number in an array using a dictionary.

    Args:
        arr: The input array (list) of numbers.

    Returns:
        A dictionary where keys are the numbers and values are their counts.
    """
    if not isinstance(arr, list):
        return "Input must be a list."

    counts = {}  # Initialize an empty dictionary to store counts

    for num in arr:
        if not isinstance(num, (int, float)):
            return "Array must contain numbers"

        if num in counts:
            counts[num] += 1  # Increment count if number is already in the dictionary
        else:
            counts[num] = 1  # Add number to dictionary with count 1 if it's new
    return counts
print(count_occurrences_dict([1,2,2,3,3,3,4,4,4,4]))
#anagram check
def are_anagrams(str1, str2):
    """
    Checks if two strings are anagrams of each other (case-insensitive).

    Args:
        str1: The first string.
        str2: The second string.

    Returns:
        True if the strings are anagrams, False otherwise.
    """

    # Normalize strings: lowercase and remove non-alphanumeric characters
    str1 = "".join(char.lower() for char in str1 if char.isalnum())
    str2 = "".join(char.lower() for char in str2 if char.isalnum())

    if len(str1) != len(str2):
        return False  # Anagrams must have the same length

    # Method 1: Using a dictionary to count characters
    char_counts = {}

    for char in str1:
        char_counts[char] = char_counts.get(char, 0) + 1

    for char in str2:
        char_counts[char] = char_counts.get(char, 0) - 1
        if char_counts[char] < 0: # early exit optimisation
            return False

    return all(count == 0 for count in char_counts.values()) #check if all count values are zero

    #Method 2: using sorted.
    #return sorted(str1) == sorted(str2)
print(are_anagrams("listen","silent"))


# 7) longest word in arr

def longestStr(arr):
    longest=""
    for word in arr:
        count=0
        for char in word:
            count+=1
        longest_count=0
        for char in longest:
            longest_count+=1
        if count>longest_count:
            longest=word
    return longest
print(longestStr(['ant','elephant','cow']))

# 8) Most commonly used two chars in a string

def most_common_chars(s):
    freq={}
    for char in s:
        if char!='':
            freq[char]=freq.get(char,0)+1
    sorted_freq=sorted(freq.items(),key=lambda item:item[1],reverse=True)
    for i in range(min(2,len(sorted_freq))):
        print(sorted_freq[i][0],end=" ")
most_common_chars('Hii iam navya')

# 9) remove dups and sort the arr

def remove_dups_and_sort(arr):
    unique_elements=[]
    for num in arr:
        if num not in unique_elements:
            unique_elements.append(num)

    n=len(unique_elements)
    for i in range(n):
        for j in range(0,n-i-1):
            if unique_elements[j]<unique_elements[j+1]:
               unique_elements[j],unique_elements[j+1]=unique_elements[j+1],unique_elements[j]
    return unique_elements
print(remove_dups_and_sort([2,3,4,2,6,1,7,7,9]))

# 10) Eliminating braces

def removing_braces(expression):
    result=" "
    for char in expression:
        if char not in '()[]{}':
            result+=char
    return result
print(removing_braces("a+b-[9+c]"))

# 11) If subseq arr is subsequential to the array

def is_subseq(arr,subseq):
    i,j=0,0
    while i<len(arr) and j<len(subseq):
        if arr[i]==subseq[j]:
            j+=1
        i+=1
    return j==len(subseq)
arr=[5,7,3,2,2,7,-1,5,-3,13,4] 
subseq=[7,-1,5,-3]
print(is_subseq(arr,subseq))

# 12) uniques_sum

def uniques_sum(arr):
    uniques=[]
    for num in arr:
        if num not in uniques:
            uniques.append(num)
    sum=0
    for num in uniques:
        sum+=num
    return sum
print(uniques_sum([3,1,4,2,3]))

