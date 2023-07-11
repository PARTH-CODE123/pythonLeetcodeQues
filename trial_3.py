# def removeAnagrams(words):
#         """
#         :type words: List[str]
#         :rtype: List[str]
#         """
#         dic={}
#         for i in (words):
#             a="".join(sorted(i))
#             if a not in dic:
#                 dic[a]= i
            
#         arr = []
#         newarr=[]
#         for keys in dic:
#             arr.append(dic[keys])
#         return (arr)
# print(removeAnagrams(["a","b","c","d","e"]))
#  4 5 6 2 4 3 
# s = list(map(int,(input().split()))
# print(s)

# def digitCount(num):
#     """
#     :type num: str
#     :rtype: bool
#     """
#     flag=0
#     for i in range(len(num)):
#         a=num[i]
#         count=num.count(str(i))
#         if a!=count:
#             return False
#     return True

# digitCount("1210")






#           Input: answerKey = "TTFF", k = 2
#           Output: 4
#           Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
#           There are four consecutive 'T's.

# def maxConsecutiveAnswers(answerKey: str, k: int) -> int:
#         countF = 0
#         countT = 0
#         i = 0
#         j = 0
#         ans = 0
        
#         while j < len(answerKey):
#             if answerKey[j] == 'F':
#                 countF += 1
#             else:
#                 countT += 1
            
#             while min(countF, countT) > k:
#                 if answerKey[i] == 'F':
#                     countF -= 1
#                 else:
#                     countT -= 1
                
#                 i += 1
            
#             ans = max(ans, countF + countT)
#             j += 1
        
#         return ans
# print(maxConsecutiveAnswers("TFFT",1))

# def isValid(s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         arr=[]
        
#         for i in range(len(s)):
#             if s[i]=='(' or s[i]=='{' or s[i]=='[':
#                 arr.append(s[i])
#             elif (s[i]==')' or s[i]=='}' or s[i]==']'):
#                 if s[i]==')' and arr[-1]=='(':
#                     arr.pop()                    
#                 elif s[i]=='}' and arr[-1]=='{':
#                     arr.pop()                    
#                 elif s[i]==']' and arr[-1]=='[':
#                     arr.pop()
#                 else: return False    
#         print(len(arr))                   
#         if len(arr)==0:
#             return True
# isValid("()()()")  
# def strStr(haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         if needle in haystack:
#             return haystack.find(needle)
# print(strStr("sadbutsad","btt")) 

# # a=["hello"]
# # b=["hel"]
# # if b in a:
# #       print("yes")
# #       a.find(b)


# def removeElement(nums, val):
#     z=0   
#     for i in range(len(nums)):
        
#         if nums[z]==val:
#             a=nums[z]
#             nums.pop(z)
#             nums.append(-1)
#             z=z-1
#         z=z+1    
                
#     i=0
#     count=0        
#     for i in range(len(nums)):
#         if -1 < nums[i] < 10:
#             count=count+1
#     return count            
            
# print(removeElement([0,1,2,2,3,0,4,2],2))

# print(ord("A"))
# print(ord("Z"))


# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        
        print(s.count(" "))
lengthOfLastWord("   fly me   to   the moon  ")        