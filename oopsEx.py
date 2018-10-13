'''
OOPS : Object oriented programing structure
Advantage:
-Reusability of source code
-Support to modular programing , large
task can be written in small set of code
-Easy to manage the source code 

THere are following fundamental of oops:
-class: is wrapper of data member and function
-object   : is an instance of class
-encapsulation
-abstraction
-constructor
-deconstructor

'''
#create class
class calc:
     #functions / methods
     def add(s,a,b):# first argument will take ref of bject
          print(a+b)
          
     def sub(s,a,b):
          print(a-b)
     def mul(s,a,b):
          print(a*b)


#create object of class
o = calc()
print(o)
o.add(11,2)
o.sub(333,4)
o.mul(33,3)









          



          



