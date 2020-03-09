import timeit
from itertools import product

def palindrom_test(string):
    start, end = 0, len(string)-1
    while(start <=end):
        if (string[start] != string[end]):
            return False
        start = start + 1
        end = end - 1
    return True

def longest_palindrome(s):
    returnstr = ''
    def search_for_palindrom(s,i,j):
        while (i >= 0 and j <len(s) and s[i]==s[j] ):
            i += -1
            j += 1
        return s[i+1:j]
    for i in range(len(s)-1):
        firststr = search_for_palindrom(s,i,i+1)
        secondstr = search_for_palindrom(s,i-1,i+1)
        returnstr = max(returnstr, firststr,secondstr, key=len)
    return returnstr
    

def shortestPalindrome(s: str) -> str:
    i,l = 0,len(s)
    for j in range(l-1,-1,-1):
        if s[i]==s[j]: i+=1
    if i==l: return s
    return s[i:][::-1] + shortestPalindrome(s[:i]) + s[i:]
        
#        prx = ''
#        
#        while (s != '' and s != s[::-1]):
#            prx =  s[-1:] + prx
#            s = s[:-1]
#        
#        return prx[::-1]+s+prx

def fib(n):
    a,b = 0,1
    lst = [a,b]

    for i in range(2,n+1):
        lst.append(a+b)
        a,b = b, a+b
    return lst

def palindromePairs(words):
    empty_idx = None
    word_dict = {}
    for idx, w in enumerate(words):
        if w != '':
            word_dict[w] = idx
        else:
            empty_idx = idx
    res = []
    for w, idx in word_dict.items():
        w_reverse = w[::-1]
        if w == w_reverse and empty_idx != None:
            res += [(idx, empty_idx), (empty_idx, idx)]
        if w != w_reverse and word_dict.get(w_reverse, -1) != -1:
            res += [(idx, word_dict[w_reverse])]
        for i in range(1, len(w)):
            pre, pos = w[:i], w[i:]
            pre_reverse, pos_reverse = pre[::-1], pos[::-1]
            if pre == pre_reverse and word_dict.get(pos_reverse, -1) != -1:
                res += [(word_dict[pos_reverse], idx)]
            if pos == pos_reverse and word_dict.get(pre_reverse, -1) != -1:
                res += [(idx, word_dict[pre_reverse])]
    return res
def palindromePairs1(words):
    pl = product(enumerate(words), enumerate(words))
    reslt = []
    for pair in pl:
        if pair[0][0] == pair[1][0]:
            continue
        contstr = pair[0][1] + pair[1][1]
        if contstr == contstr[::-1]:
            reslt.append((pair[0][0], pair[1][0]))
    return reslt
def reverse(x: int) -> int:
    if x ==0:
        return x
    rev = 0 
    ml = 1
    if x<0:
        x=abs(x)
        ml = -1
        
    while x != 0:
        rmdr, x = x%10, x//10
        rev = (rev*10)+rmdr
    if rev*ml >= 2**31 or rev*ml <= -2**31:
        return 0    
    return rev*ml
        

if __name__ == "__main__":
    print(palindrom_test("aba"))
    print(fib(10))
    print(longest_palindrome("babad"))
    print(longest_palindrome("cbbd"))
    print(shortestPalindrome("aacecaaa"))
    print(palindromePairs(['lls','sl']))
    print(palindromePairs1(["abcd","dcba","lls","s","sssll"]))
    print(timeit.timeit(stmt='palindromePairs1(["babababbbaaa","bbaabbbaabbbbba","abbbbbbbbbbbb","bbabaaababb","aabbbaaaababbbbba","aabbababbab","abaaa","aba","abaab","aabbbababa","aabbaabbbaaabaa","abbbbababbbbaaa","bbabbbaababbab","a","bb","ababbaa","baaba","b","bbaabaabaa","abbaaabbbbabbaabaabb","aabbbbaaaa","aabbbbaaaaab","abbaaababbaaa","abaaaaaabbabbaa","baaaabaaabaaa","aaaabaabbabaababaab","aaabbbbaaaaabbb","babaabbbababbb","babbbb","bababaabbbbababaaba","aaaaa","baabbaabbbabb","baaabababbb","bbbabbaaaabaaabbbba","aaabbbabbaaababaa","babaaa","baabbabbbaabbaba","bbb","baabaababba","baabaaaabaaababababa","bbbbbaaabaaabaab","abba","baaaaaababbbb","bbabbbbbaaaaaababa","aaaaabbababbbba","abaabbbaabbabaabba","babbaabbaabbbbaa","aabbabba","abababababaabaabab","baab","baabaaaaaaaa","baaabababbbbbabba","bbaaabbaa","bbabba","bbbabbaab","baa","ab","baaaa","aaa","abbaabab","aabbbbbbaaaaa","aaaab","bbabaaab","bbaabaabababaaaaabb","aaaaaab","aabbbb","baaabbabaab","abaa","bbabbaabbabbbbbbb","aabbabbbabbab","abbbbbba","bbbbbaabaab","bbbbbaabbbbb","abbbbbbbabbbabb","aaaaaaababb","bababbbbbabbabb","aabababbabaaababaa","bababa","baabbabaabb","babbbbaabab","aabbbaaabbbbabaabb","abaabbbaaaaabababbab","abb","bbaab","abbaaa","abbbbaba","bbaabaa","bbbabbaabbaaa","bababab","baaaabbbb","abbbbaaaaaba","aaabaaabbaabaaabbaab","bababbaababb","aaaaab","aababbbbbababbbaab","aa","bbaaa","baaababaab","aabbaaabba","abbaabbaaaababbaaaaa","babaabaabbabbaaaaabb","bbabaabbaababaabbaaa","abbba","aaab","baabab","bbbbbbaabbaabbb","bbbabbabbaabbbabbab","bbabbabbbabbabbbba","abaabaabbabbabab","abbbbbaaababbbbbbbb","aaaaababbaaaaa","bbaababa","aabbbbbaba","baabababbbaba","aaabbbbba","aab","baaabbbbaabb","bbaaba","abaaaaaba","bba","bbabaaaab","abbabaaabba","abbabbb","baaabbaaabbbbbbaabb","aaababbb","aabbbbabaabaa","baaaaaaabab","baaaabbaaabbb","abbaaaabbbbbbb","bbaabbabbaabbaa","baababbbbabaababbaa","bbababbbbbab","baabbbabbbabab","aabaaabababaaa","bbbbaaabaaa","bbbabbabb","abababbaa","abbbbbbaababab","aabbbbabaa","abbabaabbaaababbbba","baabbabbbaaabbbbbbba","bbbb","aababbbabaabbaab","abbab","babb","aabaabbaabbababaa","aabbbbaaa","bbbab","baabbabbabab","baabbbabababba","abaaabbaababbabb","aababbaaabbbbbbbaaaa","aaabaabbbbbbbbaaa","baaabbbbaa","babaabaabbabaabbb","aaaabaaaba","bbababbbbbba","bbaaabaa","bbbaabbabaaaa","babbbab","abbaabbabababbbaa","bab","aabababbabbbbab","abbbabababb","baaabbaaab","babbbaab","baaabbbbbbbaab","abbbaaaaaab","aababbba","bbbababbbbaabaaabba","babbaabbb","bbaaabaabbb","baaabaabbbbbaa","baaaaaab","babbaabbbaabba","aabbbbaaabbabbbb","baaababaabbbabab","aaaabaab","baabbaaabbaaabb","aabaabaababbabaab","aabbaba","baaababbabbaaabbabb","aabaababaaaaabbbabaa","ababa","babbbbbbabaaabaabb","babbaaaabbbbaab","abbbabaababa","aabaaaaabbbbabab","aaabbbaabaaab","aababbaaaaaaaabbb","aaaabbababaab","aabababbabbbbbb","bbbbbabbbabbb","aabbaaaaaabbbba","abbabaababba","aaaaabbba","baaaaaaaabbbbbbbb","aaaabbbabb","abbbabaaa","aaabbabbabaabbaaa","bbaabaabbbbbbbbbaba","bbaaabbababaaba","baaabbaaaaaabbbbba","bbabbabbabbbbaab","aaabaaa","bababaaabaa","aabab","babbaba","aabbabbbaab","aaaabaaabbaaaabaa","bbaba","bbabbbaabbbbbabb","bbaabbaaaaabaab","ababbbaababbab","babaaab","babababba","abaaaaaaaaaab","aabbb","abababbbaabbaabaa","aaaabbaaabbbbaabaab","aababababbaababbb","babbaaaababaa","aabbabbaababbaaaba","aabbbabaababbab","abaaaab","babbbbbaaaababaaabba","bbbbababaabaaabaaba","aaabaabbbaabaabab","aaababbbaba","aabaaabba","aabbaabb","aaabbbabbabaaaabbbb","baabbbaabaabaabb","aaaabbbbababbabbabb","abbaabb","baaaabaaababababbba","aabababba","baaaaaabbbabbbbaa","babbab","aaabaaaaabbaaaaaba","aabbaaa","aaba","aababbababab","baabaabbaababbab","abaaaabba","bbaaaabbaabaaa","babbaaaabbbaaabaa","bbaaabbabaaa","abbabbaaabbabbbabba","aaabab","baaa","ba","bababbaab","aabaababb","bbabaaaaaaabbabb","aaaabbaaaaaabbbababb","aabbabbba","abbaaba","ababbaababbbbaaab","aabbabbaabba","aaaaabaabababbbabbb","bbaababbabaabbb","babbabaaaa","abbbbabaabb","bbaaaabaabbbbbb","abaaaaaaababbaaab","abbaaaabaaababba","ababbaabbaa","bbabaabbaaa","aababaaabab","ababaaabbabaabbbab","bbbaaa","aababbbabab","aaabaab","bbbbbbaaabbabbb","baaaabb","abaaabb","bbabbabbb","bbbbba","bbababaaababbbbaa","bbabaaba","bbaabaabaabbba","bbababaaabaaaba","bbbbbaabbaaaaaab","babaabaaaaaabaabaaab","baabbababa","bbaabbaaabbbbb","baabbaaabbabba","babbababaaaba","babbbbbbababbbabbbb","ababaabaaabbbb","aabbbaabaabbabb","bbabbababbabbabb","bbaabaaaabbbbb","bababba","aaaaababbbab","bbabbbaaababa","abbababbaabaabba","abaabaabbba","babbbbaaab","bbbbabbaababbabbbaab","ababaabababa","ababaaa","abbbaabaaaabaaaaab","aaaabbabbbaaaa","abaabaaaabbabb","bbbabaaab","bbaa","bbbaaababbabbbaabbbb","abbababbbbaabaaabb","babaa","bbababaaaababb","aaaaaabbbbbbbaabbb","bbbbabbab","aabbababa","babbbabbaab","bbbababababbbab","baaaabbaaaabbabbba","baaaaaa","abbbbaaaaaaaabbb","aabaaaab","aabb","bbaaab","abaabba","bbabbbbbaaaaabaaab","bbabbb","baabaaabbbbabaaabb","aaabababaabababbaaba","abab","babbabababbbabab","abbabbbbaabbaab","aaaabbbabaaba","babaaabababbaabaaabb","babaab","bbabbbbba","abbaabbbbaab","baaaaaaa","baaaab","bbbabaababbabaab","abaaaaaabababbab","aaaaaababbbaaaaabbb","baaaababaabaaabbbabb","abbaabbaabbb","bbaaaabbaabbaaabab","abaaaaba","abbbabbbabbaba","bbaabbabbabababbbaab","baabaabbbab","bbaabababbaaaaabaaa","aabaab","abbabab","bbabbbbbabb","baaabaaaabaabaaba","babba","aaaaaaabaaaaaabb","aabaa","aabaaabaaa","baaabaabbbbaabbaa","bbaabbbbbabbbababb","bbabbabaaa","bbabaaaabbaaaa","ababbb","aaabaaabbabaaaabaaaa","baba","aabbabbbaa","bbabaababbb","aaabb","aababaabababbbaba","bbabbbbbabba","baaabbbab","aaabbbbbbba","baabbbaababb","aabababa","aababaab","aabaaab","bbbabba","babaaabaaaaabbba","baabbaabbaabb","aaabaaababbbabaa","babaabaaabaaabba","bbbbabaaaaabbbab","aababaabaaaa","abaabbbbaababaaaabb","abbbabaa","abbbbbbbbbbbbbbbab","abbabbabbabbb","baaaabaab","bbabababababb","baabb","abbabaaabbabaaabbbaa","aaaabbababaaaabba","babaaaaa","abbabbbb","aabbaa","babaabbabbbabaabaaab","abbaaaa","baaab","bbbbbbbaba","babaabbabaaab","baaaabbbbbb","bbbbbbbaabbbbaaaaaa","bbbbabbba","aaababbbbaabaaaba","babbbbb","bbabab","baaabaabbbababb","baabbaaaaaaa","bbabaaaabbaa","baabbbbbaa","bbababbbbaabababa","aaabababb","bbaaaabbbbbabbbabab","aaabbbab","aaaaaaaaabbbbbaaaba","aaabaaabbababa","abaabbaabbabaabbab","aababbaaaaaaabbabb","aabbbbabba","bbababaaaaababbab","bbbbaaabbaa","aaaabaa","aaabaaaaaababbbba","bbbaaaaabbbbbabbabaa","baababaabaabbbb","abbbaaabaabaaab","aabaaabbbbaaabbaab","aabaabbaaaaaaaaaaa","baabababbb","bbbbbaabaaaabaababbb","abbaabbaba","babbbaaabbaab","baaaabaaa","aababbbaabba","bbbabaaa","aabbaaaaaaaaab","baaaaabbaaabaa","bababbbbabbaaaaa","bbbabbabaabaaaaabb","aaaaaaaaabbaababbb","aaaabb","bbbbaaabaabbbbaab","bbbaabbabbbbbbbbabb","abbaaaaaaaabba","abbaaaaaabbbbbb","aababbbbbaabaabbbb","aaaaababaabaab","baaababbabbba","bbbbbabaabbbaa","aaaaabaabbbbbbbab","aabbbbbb","abbb","bbbaaaabbababbabbb","bbabaabaabba","abaaabbbaaaabbb","ababbbbabbb","aaaabbbaaaaaabb","bbaabbbaaaaab","abbaabbabaab","babbba","abababbabbaabba","aabbababbbaabba","abbbabaabaabbbaa","baaaabbaaaa","baabaa","abaabbabbbaabbaaab","bbbbaabbbaabbbbab","abbbbbbaaabaababb","bbbaaababbaabb","bbaaabaabaabbbaaabb","babab","abbbbbbbbbbbbb","abaaba","bbabbababbbbbbaab","baabababbbb","abaababbabaa","aaaaaabbaab","babbbbbbbbbbbaaa","aabbba","babaaababbbbbbbaa","ababaaababbaba","bbaaababbbaababa","aaaabaaaaaaaab","bbababba","abaaababbb","bbabbabbbab","bbbbabbabb","babbabbaaabbbbaa","bbbbabaaaab","aaabbaaaabbb","baaabaab","aabaabbbbbaaba","baabbabaabba","abbbbaabababaabaaab","aabbabaab","aaabbbbb","bbbabbbbbabb","abbbb","baaababa","babababbbb","bbabbbbbaabbab","abbabaabaaaa","bbbaa","ababbbb","aabbbaab","aaabaaaabbbbaabab","abbbbbbabaabaababaaa","bbaabbba","babbababaaab","bbaabababbabbbbbbab","ababbbabbabaabaa","aabbaabbb","aaabbbbabaabaabb","babbaaaaaababb","abaaaabaaaabbaab","aaabaababaabbaabbaab","aaabbbbbbbbaabbbaab","aaababababaabaaa","aaabbababbaaaaaababb","baabbb","abaabaaaabb","abbabbaabaabbb","baaaaaabbbbbab","aabbabaabab","bbaaaaaaaaabaaaaaabb","abaabbbaaabaaababb","babbaaabbbb","bbabb","babaababbaaabbaaaba","babbbabaaaab","abaabbababababbaaaaa","abbaabaabababbb","aabbbabb","aabbbaabbbbaaaabba","babbabbbaaaababaabba","bbbbbbaabbabbbbabba","bababaaababbbababaa","bbaababbabaaaa","bbba","abababaabaababaabb","aabbbbabaababbab","abbaba","babaaaabbbababa","abbbaab","ababaaaaabbabbb","bbabbbbbabaabaabbbba","aababab","abaaaabbababbaab","bbaaabbbbabaab","aababbbaa","aababbbabbababbbbaba","baabaaaaaabab","bbbababbbbab","baaabbbaabaabbb","aaaaabababaaaaabb","abababbbaaaabbab","bbbabaa","abaaabbbabbaaaabbbbb","bbbbbbbab","bbbabbbbaababba","abbbabababab","abbbbbbbaaaaaabbabbb","aaaaaabaaabbbabab","abbaaaabbbababbbaa","bbbbbbaabbbaababaa","baabababababbbaaba","baaaaaabbabbaabbbaba","aaabaaabababbabaaaab","aababbababbabab","abaaababa","bbababaabbbabb","abbbababbb","bbabbabbaabab","aabbaabaabbbabb","bbbabab","baaaaabba","aaaabbabbbb","babbbaaaaa","babbaaa","baaababbaab","abaaabbaaaaabaab","abbbaaabaabaabaa","baababbbbaaaba","aaaaabbbbaababaa","babbbaabbbbabbbbabaa","bbaabaabbaabbbb","aaaaaabaaaaaaabbaa","abbbbbaaba","bbaaaaabbabaabba","aaabbbaababaaaabbbbb","bbabbababaaababaa","bbbabbaaabaaababaa","babbabbbb","abbbaabb","aabbbaabbbbbbaa","aabbbbbaabbbbaaaaba","baababbbbabbaa","abbabb","baabaaabbabbbabaa","aaaaababab","aaabbbbbbbbbb","bbaaaabbbabbbba","aaaabababab","abaaaabaaab","bababbbaa","abbbbbabaa","bababbababbabbbbb","aabbaaaa","abbbbbaab","aaaabbbaabbbab","aaabaaaabaa","ababbbbbbaababbabba","baabbabbaaba","abaabbaaab","aaabbaabbaabbaaaaba","baabba","aabbbaababbaaabaaaba","babaaaabbbab","aaaaabbbbbaaaa","bbbabbaabbb","bbbbaabbabbaababbbbb","baabbaa","aaaaba","aabaabaaababbbaa","bbaaaaabab","ababbababbabbaaa","ababbbaaaab","babbaababaaaabbabb","aabaaaabaabbabaaa","abbabaaabbabb","abbbbabbbbbb","babaabaa","bbabbaabbabb","baabbabbbaba","bbab","bbababaabb","bbabbaaabbaaa","ababbabbabaaaab","bbabababaaaabababb","baaababbbababbbbba","bbbaabaabbaabbaba","aabababbaaaba","bbbaaaabaabbaababaab","bbbaaaabbbabababa","bbaabab","baaabbaabbaaaababba","aaaabbbbbaaab","baabbbabbab","abbaaabaaab","baabaaa","bbbbb","aaaaabbabaaaaaabbbba","aaabbababbbaabbaaab","aababbaabaaabbbbaba","bbbbbbbaaaabbbbabbbb","abaabbabbaaa","baabaaaabbbabb","baabbaabbabbbbabbaba","aaabbabaa","bbaabb","babaaba","bbababaaaaaabbbaab","abababbba","bababbaaabbabbab","bbbbbaabab","bababbaababbaaababaa","bbbbaab","aaabababaa","abbaaaabbbaaab","aabbaaaabbaba","aaababbaababbbaabbbb","ababba","bbbababbabababba","abbbabaabbaabaab","aaabbba","bbbbababbaaaababa","aababababba","bbaabbbbabbaaa","aaaaaaabbbba","bbaabbbbabaaaaaaa","bababaaaabaab","aaaa","abbabaaabbbaabbb","baabbbabbaa","bbbabbbbaaabababaa","bababbbbbaaababb","bbbbbb","abbbbbbbaaabbaaab","abbbaaab","bbaaaababa","bbabaabbbababbbbbb","baabbbbbbaaabbab","abbbbbabbabaaaba","baabaabab","bbbababbbbbabaaaaaaa","abbaabbbbbabaaaab","abbbaabbabbabbbaab","bbbbbbabbbbaaaaab","abababababa","babaaaaaaaaaa","aababbbaabbb","abbabbbaaaabbbbbbbb","baaababbbbaaabaababa","baaabaabaababaaabba","bababbababbbaabb","abbabbaabba","babaabbaaaaabbb","abbabbbbab","abbbba","abababaaabaabbaa","bbbba","bbabbbbaaaabbbaaba","aabaabb","ababbbaabbbaaababba","bbaaabaaaaabaabbbaa","babaaabbaaaabbbba","aaaabaabbbabbbbaba","aaaabbaaaabab","aaaabbabbaabaabaaab","bbabbabbaaab","babbbbaaaaaabbba","aabbabb","bbbbaa","baabbbaabaaaa","aababbbaabaabab","aabbbbbababba","bbbbbbabbbbbb","babaabbbaaaaabbbaa","bbbabaabbaa","bbbbaaabaaaba","abbbaabaaaabab","aabbbabbb","aaaabaaabbabbbbbbbaa","bbabaaaababaabaaaab","aabaaaabaaabbbaabbab","baabbbbabba","bbbaaababbbbabbaaaaa","aabbbaaaaa","bbaaaa","bbbabaaababaaaababa","aaabbbbaaabbbabba","aabaaabab","abbaabaaaabbbab","abbababbbbabbab","aaabbaaaaaaaba","aaaabab","aaaababa","aabbbbbbbba","bbbbbbbbaabbabaabb","bbaababaaabbaabab","abaabb","bbabaab","aaabaabbbababbb","bababbaaaa","aabbbbaabbababababbb","baabaabaabaaaab","babbaabaaaa","bbbaaabaabbbaaaabb","bbaabbbb","aaaaaa","abbaabbbbbbaaaaba","abbaabaab","abbbabbaaaaabaa","babaabaaaabbab","bbaabbaaababababbabb","baaabaaaab","babaaabbabaabbaabb","bbbbaaba","abbbaa","aaaabaabbba","aabbbbbabaa","bababaaaaaabba","baaabbabaabb","bababbbaabbabb","bbaabbbaaba","aaabaa","bbababbb","abaabbbbaaabaa","bbbaabbbab","babababbbaabba","bbabaaaaabaaa","abbbbbbb","bbbabababa","babbbbbababbabbbbab","baabbabaabbbbbbababb","baabbabbbabbaaaaa","abbbaabaab","baabbaabbabbbaabbba","aaabbbbbb","abbabbabbbbaabbaaba","ababaabbbbbaaa","aaaaabbabaaaababb","aabababaaaabb","bbbaaababbbbabbaa","bbababbaaa","aabbbabbbabbbbb","babababbabab","aabbbabababbbabbaa","abaaaa","bbaaabaaabbbabb","baabbbbbbabbbbbbaab","babbabababaabbaabaaa","ababb","bbbaabbaabbabaaba","aaaaaabbbbabaaaab","bbbbabaababbababab","bbaabaababbbbbaaabb","abaababbab","bbbbaaabbbabaababba","bbbbaababbbaaa","abaaaabbbabbaa","babbaaaaabb","bbaaababbab","aabbabbbaabaaaaab","bababaa","aaaaaaaaa","ababababb","bbaababab","abbabbaaabbbb","abbbaaaa","abaabbbaba","abbbbabaabbababbbb","baababbbabaaaaa","baaababaaaaaba","abaaabaaaa","ababbbbaabbaaaaaa","babaaabbba","aababbbaaabbabaabab","ababbbbaba","aababaaabbaaab","aaaaaaabb","ababaabaabb","bababbbaabbabba","abaaaba","bbbbaaaabbababbbb","abaaabbabbaabba","abaabaabaaabbbaba","bababababbb","abbaaabaaaabaaaabaaa","abbbababa","bbaabbaaaaaaaabbbbba","abbaaabbba","bbabbabbbaa","baababaaabaaaba","baabbaaabbabaaaabab","bababbabbbaaaabbaba","aaabaaba","aabbab","baababbbb","babbbbbabbabaa","aababaabaabbaabba","babaaabbbb","aaaabbaaabbabb","abaabaaaaababba","aaaababbabbbaaba","abaaabbaabbb","aabbbbbaabbaab","bbabbaa","abaaababbbbbbbaaabaa","aaaaabababaabaa","aabbbbaababaaabaaba","bbababaabbabbaaabbbb","aabaaaabbaaba","bbaabbabbbaaaab","baabaabbbbbbbbbaab","bbaaabbbbaabaaaa","abbbbbbabbababb","aababbbabbbbaa","bbaaaaa","ababbbaaababbababb","abaabbaabbabbb","aabbaab","aababbabaaabbbbab","baaaababaaab","babbbbbbabbab","abbbbbabaaababbaa","babbbaaaba","baabbbaaab","abababaaaabbbbbaab","bababababaa","bbabbaabbbbaaa","bbbabbab","aaaaaabbab","bbabaababaabbb","aaaaaaabbababbaabba","abbabaaaaaab","aabaaaa","abbaabbb","abaaabaabaaa","aababbbbbbaabaabbabb","bbbaaaaaabbab","aabbbbabababb","baabaaaabbabaabb","aaaaabbb","abbabbbbbba","bbbbbabbaaaabaabaaa","ababbaaaababaa","baaabab","aabbababbaababbb","baabbabbaaaaaa","babbbabbbaabbaba","aaabaabababaababa","babaabbaaaba","aaabbbabaaaaa","abbaaaabaabbbaa","bbaabbababbaaabb","aaaaabababaa","bbaabbababbbbb","abbbabbbbabaaaba","bbbaababaabaaaabaaaa","bbaaaababbbbba","abbbabaaabb","aababbbbabbaaa","abababaaaabbab","bbbbbbbbaaaaaaaa","aaaabbaaaabbbaabbb","aaaabababb","abbbbbabab","ababbbaaaaababaaaaab","babaaaa","babbabbbbbbbb","bbbabbaaabbbbbbba","abbbabbbaaaaaabbb","bbaabbbbbbbababab","bbabaaabbbbb","aaaaaabb","aaaabaaabbba","abbbaaababbaababaaab","aaaababaabbabbaab","aaababbbbbabbbabbba","aabababbbbbbbaababa","ababaabbabbbbabba","aabbabbabaaa","bbbababb","aabbaaabbabaaa","abaabbaabbbbbababb","aaaaababbaaabbaaaaba","bbbbaabaaabaaababb","bbbaba","abbabbbaabbabbbbaba","aaaababbaaaaabb","aabbbbababaabbbbaab","abbababba","abbbaaabaabbbabaaaab","bbbbbaabaaabaabb","aabbaabbaaaaabaaaaaa","abbabaaaaaaaba","bbababbbbbababaab","bbabababa","babbababaababbabbb","bbbbbbba","bbababbabbbabbabbaba","bbbbbaabbbabaaba","aaaababbababbabaabaa","bababaabbba","ababbbbbabbbaaa","abbbabbaaab","bbbabaaaa","bbbabbb","baaababbabaaabbaaba","bbbabaabbaaaabb","aabbbabaabaaabb","aabbabbbabbbabaa","bbbaaba","aabbabaabbababbaa","bbaabbabbab","bbaabaaaaabaabbaaaab","abbabbabbabbaba","abbabbbabaababbb","baabbbaabaa","aababaabaabbaaabb","babbbababbabbaab","aaabbaaaaabaab","aaaabbbabaaabaabaaa","bbabbbbbba","ababbbbaabaaaaaaaa","babbbbbbbbaab","bbbbbaabaaba","aababaaaabaaaaaba","babaaabababbaabbaabb","ababbabbaaabbbabbbaa","aabaaaaabba","bbbbabbabbababbb","ababaababbbbaaa","bbbbbbaaabaaa","babbabbbababaaaabbbb","bbabbbbb","abaaabbababbaaabbb","bbbaaabaaab","bbabaabbaba","bbbbababbbbbbbbab","baaaaaaaaabbabababab","babbbbabbaaabb","bbbaabb","babbaa","aabbabbaabbb","aabba","bbabbbbaabbbbbb","aababbbbbababbaabb","aaaabbbababbaaaaaaba","babbaabaaabbaaa"])',
    setup="from __main__ import palindromePairs1", 
    number=5))
    print(reverse(1534236469))