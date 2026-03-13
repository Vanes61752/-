def fibonacci(n):
   
    fib_numbers = [1, 1]
    
  
    for i in range(2, n):
        next_fib = fib_numbers[i-1] + fib_numbers[i-2]
        fib_numbers.append(next_fib)
    
    return fib_numbers[:n]


result = fibonacci(100)


for i, num in enumerate(result):
    print(f"{i+1}-е число: {num}")