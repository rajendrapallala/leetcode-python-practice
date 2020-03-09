def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]
    if strs:
        strs.sort(key=len)
        smallstr = strs[0]
    else:
        smallstr=''
    for j in range(len(smallstr), -1, -1):
        reslt = True
        for s in strs:
            if smallstr[0:j] != s[0:j]:
                reslt = False
        if reslt:
            return smallstr[0:j]
    return ''
        
if __name__ == "__main__":
    print(longestCommonPrefix(["abab","aba","abc"]))
