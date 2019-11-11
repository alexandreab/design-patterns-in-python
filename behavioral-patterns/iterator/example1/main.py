from iterator import Fibonacci

if __name__ == '__main__':
    fibo = Fibonacci()
    fibo_iter = iter(fibo)

    for n in range(0, 20):
        print(next(fibo_iter))
