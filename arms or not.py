m=int(input())  
s=0  
t= m
while t>0:  
       d=t% 10  
       s+= d**3  
       t//= 10        
if n==s:
  print("yes")  
else:  
  print("no")   
