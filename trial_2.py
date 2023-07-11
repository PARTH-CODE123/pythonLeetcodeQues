# def isAnagram( s, t):
#     dic = {}
#     for i in s:
#         if i in dic:
#             dic[i]+=1
#         else:
#             dic[i]=1
#     print(dic)
#     for j in t:
#         if j not in dic:
#             return False
#         else:
#             dic[j]-=1
#     print(dic)
#     for key in dic:
#         if dic[key]!= 0:return False
#     return True

# isAnagram("anagram","nagaram")

word = "letsthisis"
print("".join(sorted(word)))