n= int(input())

for i in range(n):
    word_given = input()
    if len(word_given)>10:
        output = word_given[0] + str(len(word_given)-2) + word_given[-1]
        print(output)
    else:
        print(word_given)