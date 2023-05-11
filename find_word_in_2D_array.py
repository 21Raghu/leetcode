m = [['A','B','C','E'],
     ['S','F','C','S'],
     ['A','D','E','E']]
word= "ABCCED"
word_i = 0

def helper(m,i,j,word,word_i):
    if i > -1 and i < len(m) and j > -1 and len(m[0]):
        if word_i == len(word):
            return True
        elif m[i][j]!=word[word_i]:
            return False
        elif m[i][j]==word[word_i]:
            word_i+=1
            return helper(m,i,j+1,word,word_i) or helper(m,i+1,j,word,word_i) or helper(m,i-1,j,word,word_i) or helper(m,i,j-1,word,word_i)


    
f = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == word[word_i]:
            x= helper(m,i,j,word,word_i)
            print("status of word found of not:",x)
            f = 1
            break
    if f==1:break
            
