# your code goes here!
class Anagram:
    def __init__(self, original_word):
        self.original_word = original_word 
        
    def match(self, words):
        anagrams = []
        for potential_anagram in words:
            if(sorted(potential_anagram) == sorted(self.original_word)):
                anagrams.append(potential_anagram)
        return anagrams
                
        