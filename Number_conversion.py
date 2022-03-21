import math

def con(n):
   
   x,y = 0,0
   yr , m ,wk  = 365 , 30 , 7 
   
   if n > yr :
    num_of_years = math.floor(n/yr)
    x = n%yr 
   else:
      if n < yr :
        num_of_years = 0
        x = n
      else:
         num_of_years = 1
   if x > m :
    num_of_months = math.floor(x/m)
    y = x%m
   else:
      if x < m :
          num_of_months = 0
          y = x
      else:
         num_of_months =1 

   if y > wk:
     num_of_wks = math.floor(y/wk)
     num_of_days = y%wk
   else:
      if y < wk :
          num_of_wks = 0
          num_of_days = y
      else:
         num_of_wks =1 

   print(num_of_years,  num_of_months , num_of_wks, num_of_days)    

con(500)