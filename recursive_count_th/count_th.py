'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
''' 
def count_th(word):
    length1 = len(word)  
    length2 = len("th")  
    if (length1 == 0 or length1 < length2):   #Base Case
        return 0  
    if (word[0 : length2] == "th"): #Recursive Case 
        return count_th(word[length2 - 1:]) + 1  
    return count_th(word[length2 - 1:])  

count = count_th("abcthefthghin"), count_th("thick than thin THon"), count_th("ththththt"), count_th('abcthxyz')
print(count)
count2 = count_th("THtHThthn")
print(count2)  
count3 = count_th("abcthefthghithn")
print(count3)  
count4 = count_th("ththththt")
print(count4)  