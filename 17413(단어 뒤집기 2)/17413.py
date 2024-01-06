import sys

s = list(sys.stdin.readline().strip())
tag = False
word = ''
result = ''
for i in s:
  if tag == False:
    if i == '<':
      tag = True
      word = word + i
    
    elif i == ' ':
      word = word + i
      result = result + word
      word = ''
    else :
      word = i + word

  elif tag == True :
    word = word + i
    if i == '>' :
      tag = False
      result = result + word
      word = ''

print(result+word)
