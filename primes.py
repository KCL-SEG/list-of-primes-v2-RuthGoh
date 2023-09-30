"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError
    list = [2]
    number_done = 1
    current_num = 3
    while number_done < number_of_primes:
        prime = True
        for p in list:
            if current_num%p == 0:
                prime = False
                break
        
        if prime:
            list.append(current_num)
            number_done += 1
        
        current_num += 1
    return list
