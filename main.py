number = int(input('Digite um número: '))

if number < 0:
    print ('Número inválido.')
else: 
    if number >= 1:
        print ('2')
        p = 1 
        y = 3
        while p < number:
            x = 3
            while(x < y):
                if y % x == 0:
                    break
                x = x + 2
            if x == y:
                print(x)
                p = p + 1
            y = y + 2

        