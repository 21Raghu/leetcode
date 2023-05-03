def product_exp_self(ar):
    res = 1
    re = []
    for num in ar:
      res *= num

    for num in ar:
      re.append(res//num)
    return re

ar= [1,2,3,4,5]
print(product_exp_self(ar))
