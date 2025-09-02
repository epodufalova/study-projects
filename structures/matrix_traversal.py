import numpy as np 

def about():
    print('This program traverses the right quarter-triangle of the matrix. The dimension of matrix is set by the user.')

def input_n():
    n = int(input('Enter the dimension of matrix: '))
    if n <= 0: 
       raise ValueError
    return n

def create(n):
    inf=0.25
    sup=0.75
    return np.random.uniform(inf, sup, size=(n, n)) 
def _f1(matrix, start, interval, d):
    '''ф-ція, що рухається вправо й вгору, перпендикулярно головній діагоналі'''
    while interval[0] <= start[1] < interval[1]:
        start += d
        print(f'{matrix[*start]:.1f}', end=' ')
def _down(matrix, start, interval, d):
    if start[0] < interval[1]  and start[1]<= interval[1]:
        start += d
    print(f'{matrix[*start]:.1f}', end=' ') 

def _f2(matrix, start, interval, d): 
    '''ф-ція, що рухається вліво й вниз, перпендикулярно головній діагоналі'''
    while interval[0] < start[1] <= interval[1]: 
        start += d
        print(f'{matrix[*start]:.1f}', end=' ') 

def _side(matrix, start, interval, d):
    if start[0] < interval[1] and start[1] < interval[1]:
        start += d
    print(f'{matrix[*start]:.1f}', end=' ')

def traversal(a): 
    n = a.shape[0]
    n2 = n // 2
    p = (n + 1) % 2
    i, j = n2 - p, n2
    point = np.array([i, j])
    vector_d1 = np.array([1, -1])
    vector_d2 = np.array([-1, 1])
    vector1 = np.array([1, 0])
    vector2 = np.array([0, 1])

    print(f'{a[point[0], point[1]]:.1f}', end=' ')

    for k in range(n2):
        interval = np.array([n2 + k, n - 1])
        _f1(a, point, interval, vector_d2)
        _down(a, point, interval, vector1)
        if n%2 == 1:
            interval = np.array([n2 + k + 1, n - 1])
            _f2(a, point, interval, vector_d1)
        else:
            _f2(a, point, interval, vector_d1)
        if n%2 == 0: 
            if k < n2-1:
                _side(a, point, interval, vector2)
        else: 
            _down(a, point, interval, vector1)

def main():
    try:
        about()
        n = input_n()
        matrix = create(n)
        print(matrix)
        print("TRAVERSAL")
        traversal(matrix)
    except ValueError as e:
        print('\n***** error \nWrong input, must be > 0', e)
    except (EOFError) as e:
        print('\n***** error\nCtrl-Z was pressed')
    except MemoryError as e:
        print('\n***** error\n', e)
try:    
    main()
except KeyboardInterrupt: 
    print('\nprogram aborted \nCtrl-C was pressed.')
          

input()
