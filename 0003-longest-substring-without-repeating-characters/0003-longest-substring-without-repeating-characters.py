class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s) #length of the string
        maxLength = 0  #current longest unique substring
        charSet = set() #stores characters in current window to check of dups
        x = 0 #left pointer
        
        for y in range(n): #y right pointer, moves from left to right accross string
            if s[y] not in charSet:
                charSet.add(s[y])
                maxLength = max(maxLength, y - x + 1)
                #if y[s] is not in window, add to set, compute legth, update max length
            else:
                while s[y] in charSet: #move left side foward until dup character is gone
                    charSet.remove(s[x]) #remove the character at left edge
                    x += 1 #move left edge right by 1
                charSet.add(s[y]) #adds to set once dup is gone
        
        return maxLength #Returns longest unique string

#len(s): returns number of characters
#set(): creates and empty set(an unordered collection of unique, immutable elements)
#s[x] checks left most character
#s[y] checks rightmost character