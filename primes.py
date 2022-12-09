

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    
    list = [] 
    prime = True 
    base_number = 2
    while len(list) != number_of_primes:
      
        for divisor in range(2,base_number):
            prime = True
            if(base_number % divisor) == 0:
                prime = False
                break
            
        if prime == True:
            list.append(base_number)
    
        
        
        base_number +=1
    
    return list
