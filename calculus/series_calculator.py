"""
This program calculates the value of the series at given point by given epsilon and shows the result
"""
A = 0
B = 1

"""
The global variables A and B are the limits of the domain
"""

def author(): 
    print('The author of this program is Yelyzaveta Podufalova')


def about(): 
    print('This program calculates the value of the series')


def input_x(prompt):
    try:
        x = float(input(prompt))
        return x
    except ValueError as e:
        raise ValueError('It could not be converted to float', e)
    except EOFError as e:
        raise EOFError('There is no input', e)
  

def input_x_from_a_to_b(a, b): 
    try:
        x = input_x(f'Enter a real from [{a};{b}]: ')
        if a <= x <= b: 
            return x
        else:
            raise ValueError('Incorrect value of x') 
    except (ValueError, EOFError) as e:
        raise e.__class__('At time of getting x', e)  


def input_eps(prompt):
    try:
        eps = float(input(prompt))
        if eps > 0: 
            return eps
        else:
            raise ValueError('Incorrect value of eps')
    except (ValueError, EOFError) as e:
        raise e.__class__(f'At time of getting eps', e) 


def s(x, eps):
    """
    function s calculates the series by variables 'x' and 'eps'
    """

    a = 1
    s = a
    k = 1
    eps1 = -eps
    k3 = k * k * k
    while a <= eps1 or a >= eps: 
        a *= ((-4 * k + 2) * x) / k3 
        s += a
        k += 1
        k3 = k * k * k
    return s


def main():
    author()
    about()
    try:
        x = input_x_from_a_to_b(A, B)
        eps = input_eps('Enter epsilon > 0: ')
        print('\n***** do calculations ...', end=' ')
        res = s(x, eps)
        print('done')
        print(f'for x = {x:.8f}') 
        print(f'for eps = {eps:.7e}') 
        print(f'result ={res:.11f}') 
    except (ValueError, EOFError) as e: 
        print('***** error')
        print(e)


try:
    main()
except KeyboardInterrupt: 
    print('\nprogram aborted')

input()