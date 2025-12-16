def analyze_numbers(num):
    even_count = 0
    odd_count = 0
    total = 0 

    max_val = num[0]
    min_val = num[0]


    for i in num:
        total +=i

        if i%2==0:
            even_count +=1
        else:
            odd_count +=1

        if i >max_val:
            max_val = i
        if i < min_val:
            min_val =i 

    print("sum of  :",total)
    print("Max :",max_val)
    print("Min :",min_val)
    print("Even count :",even_count)
    print("Odd count :",odd_count)
# ------user input--------
M =int(input("Enter no of element : "))
num =[]
for i in range (M):
    n = int(input(f"Enter number {i+1}: "))
    num.append(n)

analyze_numbers(num)