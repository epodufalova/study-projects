
"""
The author of this program is Yelyzaveta Podufalova
This program calculates the value of the expression by given x.
"""

import math
def f(x): 
    """
    This function calculates the value of expression
    """
    result = math.sin(14/68) - (5 * math.e) / (59 * math.pi) * (7 / ((x + 3) * (x - 10))) - 14 * math.cos(x + 13) - (12 + math.sqrt(x + 15)) / (x - 11)
    return result

def domain_check(value):
    """
    This function checks the domain
    """
    return value != 10 and value != 11 and value != -3 and value >= -15

def main(): 
    print(__doc__) 
    try:
        x = float(input("Enter x (x!=-3 x!=11 x!=10): ")) 
        print("***** do calculations ...", end=" ") 
        domain = domain_check(x) 

        if domain:
            result = f(x)
        else:
            result = "undefined"
        print("done") 
        print(f"for x = {x:.6f}") 
        if domain:
            print(f"result = {result:.8f}") 
        else:
            print("result = undefined")  
    except ValueError: 
        print("wrong input")
    except KeyboardInterrupt: 
        print("aborted")
    except EOFError: 
        print("wrong input")
    except ZeroDivisionError: 
        print("result = undefined")

main() 







