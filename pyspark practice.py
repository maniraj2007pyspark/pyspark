'''# #1. Write a Python program to calculate the length of a string. 
x = "maniraj"
print("length of string x is:",len(x))

# #Write a Python program to sum all the items in a list.
maniraj=[25,69,35,71,50]
print("sum all the items:",sum(maniraj))

# Write a Python program to multiplies all the items in a list. 

maniraj =[10,20,30,40,50]
n = 1
for i in maniraj:
    n =n*i
print("multiplies all the items in a list:",n)

#Write a Python program to get the largest number from a list.
maniraj=[25,69,35,71,50]
print("the largest number from a list is:",max(maniraj))

#Write a Python program to get the smallest number from a list.  
maniraj=[25,-3,2,6,350,71,-50]
print("the smallest number from a list is:",min(maniraj))
'''
'''
#Write a Python program to count the number of characters in a string\Sample String : 'google.com'
#Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
str = "google.com"
dict={}
for x in str:
    keys=dict.keys()
    if x in keys:
        dict[x] += 1
    else:
        dict[x] = 1
print(dict)

#7. Write a Python program to count the number of characters (character frequency) in a string.  Sample String : google.com'
def char(str):
    dict={}
    for x in str:
        keys = dict.keys()
        if x in keys:
            dict[x] += 1
        else:
            dict[x] = 1
    return dict
print(char("google.com")) 
'''

'''8.Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.  
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2'''

# x = ['abc', 'xyz', 'aba', '1221']
# str=0
# for word in x:
#     if len(word)>1 and word[0]==word[-1]:
#         str += 1
# print(str)


# class tester:
#     def _init_(self,id):
#         self.id=str(id)
#         id="224"
# temp=tester(12)
# print(temp.id)

# i = 0
# while i < 5:
#     print(i)
#     i +=1
#     if i == 3:
#         break
# else:
#     print(0)

# i = "abcd"
# for x in range(len(i)):
#     print(x)

# def additem(listparam):
#     listparam += [1]
# mylist = [1,2,3,4]
# additem(mylist)
# print(len(mylist))

# def example(a):
#     a = a + "2"
#     a = a * 2
#     return a
# example("hello")


# i = 1
# while True:
#     if i%3 == 0:
#         break
#     print(i)
#     i +=1


# def reverse(string):
#     reversed_string =""
#     for i in string:
#         reversed_string = i+reversed_string
#     print("reversed_string is:",reversed_string)

# string = input("Enter the string:")
# print("entered string:",string)
# reverse(string)


# . Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.  
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# def last(n):
#     return n[-1]

# def sort(tubles):
#     return sorted(tubles,key = last)

# a =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# print("sorted:")
# print(sort(a))

# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead the empty string.  
# Sample String : 'w3resource'
# Expected Result : 'w3ce'

# inputString = "w3resource"
  
# l = len(inputString)
# newString = ""
  
# for i in range(0, len(inputString)):
#     if l < 3:
#         break
#     else:
#         if i in (0, 1, l-2, l-1):
#             newString = newString + inputString[i]
#         else:
#             continue
  
# print("Input string : " + inputString)
# print("New String : " + newString)

# or Using list slicing
# inputString = "w3resource"
  
# count = 0
  

# for i in inputString:
#       count = count + 1
# newString = inputString[ 0:2 ] + inputString [count - 2: count ] 
  
# print("Input string = " + inputString)
# print("New String = "+ newString)

# def strings(str):
#   if len(str) < 2:
#     return ''

#   return str[0:2] + str[-2:]

# print(strings('w3resource'))
# print(strings('w3'))
# print(strings('w'))

# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.  
# Sample String : 'restart'
# Expected Result : 'resta$t'

# def change_char(str1):
#   char = str1[0]
#   str1 = str1.replace(char, '$')
#   str1 = char + str1[1:]

#   return str1

# print(change_char('restart'))

#or

# e = "test String"
# f = e[0]
# for char in e[1:]:
#     if char == e[0]:
#         f+="$"
#     else:
#         f+=char

# print(f)
 
# def reverse(string):
#     rev_string=""
#     for i in string:
#         rev_string = i+rev_string
#     print("rev_string:",rev_string)
# string=input("enter a string:")
# print("entered string",string)
# reverse(string)

    
