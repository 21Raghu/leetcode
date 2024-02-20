
num = 883
res = ''

def convert_num(num):
     d = {1: " one", 2: " two", 3: " three", 4: " four", 5: " five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
          11: " eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fiftieen", 16: "sixteen", 17: "seventeen",
          18: " eighteen", 19: " ninteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
          70: "seventy", 80: "eighty", 90: "ninty", 100: "hundred", 1000: "thousand"}
     if num <=0 : return ''
     if num%10 in d:
         return convert_num(num - num%10) + d[num%10]
     elif num%100 in d:
          return convert_num(num - num%100) + d[num%100]
     elif num%1000==0:
          num/=1000
          return convert_num(num) +" thousand"
     else:
          num/=100
          return convert_num(num) + " Hundrad"



print(convert_num(num))
print(res)
