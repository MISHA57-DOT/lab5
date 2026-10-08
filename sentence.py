sentence=input("enter your sentence:")
print("characters in sentence:",len(sentence))
words=sentence.split()
print("words in sentence is:",len(words))
vowel_count=0
space_count=0
digit_count=0
for i in sentence:
    if i=="a"or i=="e"or i=="i"or i=="o"or i=="u":
        vowel_count=vowel_count+1
    elif i==" ":
        space_count=space_count+1
    elif i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
        digit_count=digit_count+1
print("vowels in sentence:",vowel_count)
print("spaces in sentence:",space_count)
print("digit_counts in sentence:",digit_count)
