def reverse_words(sentence: str) -> str:
   words = sentence.split()
   
   words.reverse()
   
   return " ".join(words)

print(reverse_words(" hello world "))
