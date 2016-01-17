
#William's Fizzbuzz program
n = 100 #Hard coded upper line
# "fizz" Divisible by 3
# "buzz" #Divisible by 5
#"Fizzbuzz" Divisible by 3 and 5
c = 0 #Current number, Will hold the value in our while loop and be printed



    
for c in range(0,n): #Will run this loop from 0 to 100 then terminate

    if c <= n:
        
    
        if c%3 == 0 and c%5 == 0 :
         print("fizzbuzz")
    
        elif c%3 == 0:
         print("fizz")
    
        elif c%5 == 0:
         print("buzz")
        
        else:
         print(c)