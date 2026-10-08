numbers = (10, 15, 20, 25, 30, 35, 40)
even_count=0
odd_count=0
for i in numbers:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1

print(f"even count is,{even_count} odd count is,{odd_count}")