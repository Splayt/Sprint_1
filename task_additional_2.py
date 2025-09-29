def digit_root(num):
    if num < 10:
        return num
    else:
        digits = []
        for d in str(num):
            digit = int(d)
            digits.append(digit)
        
        sum_num = sum(digits) 
        return digit_root(sum_num) 

#для примера
print(digit_root(56786791)) 

