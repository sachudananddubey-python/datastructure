def RepeatCh(ch):
  
  freq = {}
  
  if len(ch) == 1:
    freq[ch] = 1
    return freq
  
  for i in ch:
    if i in freq:
      freq[i] += 1
    
    else:
      freq[i] = 1
  max_char = max(freq, key=freq.get)

  return max_char
  

freq = "programming"
print(RepeatCh(freq))