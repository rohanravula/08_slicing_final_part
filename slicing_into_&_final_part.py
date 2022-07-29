"example"

# c="python"
# print(c[5]) #n
# print(c[3]) #h
# print(c[2]) #t
# print(c[4]) #o
# print(c[0]) #p
# print(c[1]) #y
# print(c[6]) #IndexError : string index is out of range.

# print(c[0:]) #python
# print(c[1:]) #ython
# print(c[2:]) #thon
# print(c[3:]) #hon
# print(c[4:]) #on
# print(c[5:]) #n

"in this we are going with left side to right side i,e positive terms"
x="python"
# print(x[:]) #it shows the full word python
# print(x[:3]) #pyt 
# print(x[2:5]) #tho
# print(x[4:1]) #the left side value is greter than the right side value so it shows blank line.
 
"now in this we are going form right side to left side i,e. negitive terms"
"012345" "left to right"
"python"
"-6-5-4-3-2-1" "this from right to left"
k="python"
# print(k[-2]) #o
# print(k[-4]) #t
# print(k[-1]) #n
# print(k[-3]) #h
# print(k[-5]) #y
# print(k[-6]) #p

g="python"
# print(g[-6]+g[-1]) #pn
# "or"
# print(g[0]+g[-1]) #pn 

"programe to find the sum of  first and  last digit "
# a=1234567
# print(a,type(a)) #it is in type of integer
# print(a[0]) # it can't show the output coz the index value can be only shown for only the string type

"programe to find the sum of  first and  last digit "
a="12345"
# print(a[0]+a[-1]) #15. but insted of 5 we need to get at last 6 i,e is known as finding of first and last digit number.
#first we need to convert the str to int the we can get the 6. this process is known as the type convertion and the typ casting.
# print(int(a[0])+int(a[-1])) #6 .we got 6 by adding the first number and the last number i,e. 1+5=6
b="648399"
# print(int(b[0])+int(b[-1])) #15.. we got 15 by adding the first and the last dingit number i,e 6+9=15
# print(int(b[1])+int(b[-2])) #4+9=13 

f="python"
# print(f[2:7]) #thon. con their are only 5 index vlaue if their is more it will print till end.
g="rohankumar"
# print(g[3:12]) #ankumar

'this is the combanation of  "+"(plus) & "-"(negitive)'
h="python"
# print(h[1:-2]) #yth
# print(h[-4:0]) #now -4 is at index position at 2.(2<1) 2 is not lees than 1. the statement is false. so it shows blank line
# print(h[-1:1]) #now -1 is at index position at 5. (5<1) 5 is not less then 1. the statement is false. so it shoes blank line.

"in reverse order. this programe is called as reverse order of string"
x="water" # we need the water in reverse order i,e. retaw
# print(x[::-1]) #(::) dubble collan is used for reverse order.#retaw
y="rohankumar" #ramuknahor
# print(y[::-1])
# z="python"
# print(z[::-2]) #ohtyp
# print(z[::-3]) #htyp
# print(z[::-4]) #typ
# print(z[::-5]) #yp
# print(z[::-6]) #p #this answers are not matcing this is called skipping.

c="python"
# print(c[::]) #python
"or"
# print(c[0::1]) #python
# print(c[0::2]) #pto

n="ravula" #r=0,a=1 ,v=2 ,u=3 ,l=4 ,a=5
# print(n[0::3]) #ru. [0:5:3] 0=r,0+3=3(u),3+3=6(wrong statement).

o="kishore" #k=0 ,i=1 ,s=2,h=3 , o=4 ,r=5 ,e=6
print(o[::4])