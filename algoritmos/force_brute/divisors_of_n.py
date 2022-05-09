def divisores (n_param):
    n = n_param
    divisores_list =[]

    for num in range (1, n + 1):
        if n % num == 0:
            # num es divisor
            divisores_list. append(num)

    return divisores_list
n = 9282312
result = divisores (n)
print ("N: "+ str(n)+ " Divisores: "+ str (result))