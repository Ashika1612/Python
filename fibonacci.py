n = int(input ("ENTER THE NUMBER YOU WANT TO PRINT : "))   
n1 = 0  
n2 = 1  
count = 0   
if nterms <= 0:  
    print ("Please enter a positive integer, the given number is not valid")  
elif nterms == 1:  
    print ("The Fibonacci sequence of the numbers up to", n, ": ")  
    print(n1)   
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < n:  
        print(n1)  
        nth = n1 + n2    
        n1 = n2  
        n2 = nth  
        count += 1  
