word = "aaaaaaabcda"
start = int(0)
end = int(0)
max_len = int(0)
ls = set({})

while(end < len(word)):
    if not(word[end] in ls):
        ls.add(word[end])
        end+=1
        max_len = max(len(ls),end - start)
    
    else:
        ls.discard(word[end])
        start+=1
        
        
print(max_len)
