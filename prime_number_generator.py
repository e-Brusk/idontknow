"""
   A simple home-made generator function for finding prime numbers between start and end args...
   """
def primenums(start,end):
    if end<2:
        raise ValueError
    number=start
    if start<=2:
        number=2
        yield 2
    while number < end:
        check = 1
        while True:
            check+=1
            if number%check==0:
                break
            elif check>number/2:
                yield number
                break
        number+=1

for i in iter(primenums(3,100)):
    print(i)

