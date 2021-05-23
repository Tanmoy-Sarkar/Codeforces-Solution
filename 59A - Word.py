word = input()
count = 0
for i in word:
      if(i.islower()):
            count=count+1

if count >= len(word)/2:
    print(word.lower())
else:
    print(word.upper()) 