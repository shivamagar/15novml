## ques. 2
## 1.
5**9
print(5**9)
## 2.
3//2
print(3//2)
## 3.
7//3
print(7//3)
## 4.
7/3
print(7/3)
## 5.
6 == 6
print(6 == 6)
## 6.
a = 20;
a+=30;
a%=3;
print(a)
## 7.
True * False
print(True * False)
## 8.
True & False
print(True & False)
## 9.
True and False
print(True and False)
## 10.
print((6>3) and (7<4) or (18==3)) and (9>3)
## 11.
print(True is False)
##  12.
print('False' in 'False')
## 13.
print((True == False) or (False > True)) and (False <= True)
## ques. 3
s1 = 'nice to have it '
s2 = 'here'
print(s1 + s2)
## ques. 4
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])
## ques. 5
a.insert(0,s1)
a.insert(7,s2)
print(a)
## ques. 6
##numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
##953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
##687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
##742, 717, 958,743, 527]
##for x in numbers:
  ##  if x==237:
  ##     print(x)
  ##     break;
  ##  elif x%2==0 :
  ##     print(x)
##ques. 7
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1-color_list_2)
## ques.8
#string = input("enter a string")
#string = set(string)
#alpha = list('abcdefghijklmnopqrstuvwxyz')
#i=0
#for word in string:
#   if(word in alpha):
#      i+=1
# if(i==26):
#       print('string is pangram')
#   else:
#        print('string is not a pangram')
## ques. 9
#c = int(input('enter a number'))
#y = c*100+c*10+c
#z = c*10+c
#print(c+y+z)
## ques .10
#s = input("enter a string")
#l = s.split('#')
#list1 = l[0].split(' ')
#for i in range(len(list1)):
#    list1[i]=(list1[i])
#list2 = l[i].split(' ')
#for i in range (len(list2)):
 #   list2[i]=(list2[i])
#print(list1)
#print(list2)
## ques. 11
#print("enter the string")
#s = input().split(',')
#print(s)
#s.sort()
#print(s)
## ques. 12
#d = {'student':['Rahul','Kishore','vidhya','Raakshi'],'Marks':[57,87,67,79]}
#marks_list = d.get('Marks')
#student_list = d.get('Student')
#num = marks_list.index(max(marks_list))
#print(student_list[num])
## ques. 13
s = input("enter a string:")
letter = 0
digit = 0
for i in s:
    if i.isalpha():
        letter = letter+1
    if i.isdegit():
        digit = digit +1
print("LETTERS",letter)
print("DIGITS",digit)
# ques. 14
subject = input('Enter the subject')
d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'], 'Subject': ['Python', 'Java', 'Python', 'C','Python', 'Java'], 'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
name_list1 = d.get('Name')
name_list2 = []
sub_list1 = d.get('Subject')
sub_list2 = []
rate_list1 = d.get('Ratings')
rate_list2 = []
newData = {}
n = sub_list1.count(subject)
for i in range(0,n):
    a = sub_list1.index(subject)
    name = name_list1.pop(a)
    name_list2.append(name)
    sub = sub_list1.pop(a)
    sub_list2.append(sub)
    rate = rate_list1.pop(a)
    rate_list2.append(rate)
    

newData.update({'Name':name_list2})
newData.update({'Subject':sub_list2})
newData.update({'Ratings':rate_list2})
print(newData)

#ques. 16
up = eval(input("UP "))
down = eval(input("DOWN "))
left = eval(input("LEFT "))
right = eval(input("RIGHT "))
print(int((((up-down)**2)+((left-right)**2))**0.5))
