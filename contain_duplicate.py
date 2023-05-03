
def contain_duplicate(v):
  xor=0
  for num in v:
    newx=xor^(2**num)
    if newx<xor:
      print("Duplicate number found:",num)
      return True
    else:
      xor=newx
  return False

v = [2,1,4,2]    
#funtion return true if duplicate is there else return false
print(contain_duplicate(v))
