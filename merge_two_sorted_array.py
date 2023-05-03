def list_apppend(a,b):
     res = []
     i = j = 0
     while i < len(a) and j < len(b):
         print(res)
         if a[i] <= b[j]:
             res.append(a[i])
             i+=1
         elif b[j] <= a[i]:
             res.append(b[j])
             j+=1
     while i < len(a):
         res.append(a[i])
         i+=1
     while j < len(b):
         res.append(b[j])
         j+=1
     print(res)
     return res
            
a= [2,4,5,6,8,9]
b = [1,3,4,5,7,9,9]
print(li_append(a,b))
#op [1,2,3,4,4,5,5,6,7,8,9,9,9]
