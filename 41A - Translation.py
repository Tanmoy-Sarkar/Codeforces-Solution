word1 = input()
word2 = input()
word1 = [i for i in word1]
word2 = [j for j in word2]
if word1[::-1] == word2:
    print("YES")
else:
    print("NO")

