def is_anagram(word1, word2):
  list_word1 = list(word1)
  list_word2 = list(word2)
  list_word1.sort()
  list_word2.sort()
  return ((list_word1 == list_word2) and "Anagram!") or "Not an Anagram"

# 
word1 = raw_input("Input 1st word: ")
word2 = raw_input("Input 2nd word: ")
print(is_anagram(word1, word2))
