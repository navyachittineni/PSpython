#Time and space complexities
#sum of n natural no's:

#Approach 1:
n=10
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

#Approach 2:
print((n*(n+1))/2)   #Better approach as it has efficient time and space complexity
"""
only raw time is not a metric to determine how much the code efficiency, there are other metrics
like no.of operations,h/w,...etc
TO estimate roughly how many operations are taking place in the code is known as time complexity
Constant Time Complexity or O(1) ---a straight line parallel to x-axis is formed ,y=c for #2 w.r.t input time is constant
with respect to input the time taken is increasing linearly---Linear T.C or O(n) time complexity

"""

n=11
for i in range(1,n+1):
    for j in range(1,n):
        print(i,j)

#input 10 - operations 100
#input 100 - operations 10000
#T.C - O(n square)

"""
O(1) < O(logn) < O(n) < O(nlogn) < O(n square) < O(n cube)
Binary search: O(logn)
Bubble Sort,Insertion Sort,...: O(nlogn)

"""

num1=17 #no.of iterations- O(n), we go for worst case time complexity in case of ambiguiity
num1=16 #no.of iterations- O(1)
for i in range(2,num): #except 1 and 17 ,it runs 15 times
    if num1%i==0:
        print("Not prime")
        break

### we can choose highest degree complexity among two different time complexities



# Memory complexity or space complexity
#O(1) S.C
#O(n) S.c

lst=[1,2,1,2,5,5,7,55]
dup_lst=[] #Max-n size => O(n) extra space

#Min - 1
lst=[1,1,1,1,1,1] #=> O(1)
for i in list1:
    if i not in dup_lst:
        dup_lst.append(i)
    else:
        print('i',"repeated")

#if-else conditions O(1) Time coplexity


    


    