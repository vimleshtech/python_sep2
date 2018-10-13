class emp:
     #first argument will take add of object
     #at least one argument need to recieve
     def newEmp(self):
          #print(self)
          self.sid  =input('etner data :')
          self.name =input('enter name :')          

     def show(a):
          #print(a)
          print(a.sid)
          print(a.name)
#
elist=[] #declare empty list 
while True:
     op = input('press 1 for add, 2 for show 3 for exit ')
     if op =='1':
          o = emp();
          o.newEmp()
          elist.append(o)
     elif op =='2':
          for ol in elist:
               ol.show()
     elif op =='3':
          break #terminate the loop

     else:
          print('invalid choice ')



          

     



          



     
