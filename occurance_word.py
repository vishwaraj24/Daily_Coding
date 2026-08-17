# 1.	Count Occurrences of a Word 
# a.	Count how many times a specific word appears in a sentence. 
sen=input("Enter the sentence:")
word=input("Enter the word you want to count:")
count=sen.count(word)
if count==0:
    print("No word in sentence")
else:
    print(count,"times it appeared.")
