def substring(s,k):
    n = len(s)
    vow = 0
    for i in range(k):
        if s[i] in 'aeiou':
            vow+=1

    max_vow = vow
    temp_str = s[:k]
    temp = vow
    for i in range(1 , n - k + 1) :
        if s[i-1] in 'aeiou':
            temp += 1
        if s[i+k-1] in 'aeiou' :
            temp += 1
        if max_vow < temp :
            max_vow = temp
            temp_str = s[i:i+k] 
    if max_vow == 0:
        return 'Not found!'
    return temp                           