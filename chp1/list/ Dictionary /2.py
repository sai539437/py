#word frequency counter"""
#text=python is a easy and powerful language"""

text = "python is a easy and powerful language"
word_freq = {}
for i in text.split():
   c=len(i)
   word_freq[c]=i
print(word_freq)
  