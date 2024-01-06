import sys

dicA = {'CU' : 'see you', ':-)' : 'I’m happy', ':-(' : 'I’m unhappy', ';-)' : 'wink', ':-P' : 'stick out my tongue',
'(~.~)' : 'sleepy', 'TA' : 'totally awesome', 'CCC' : 'Canadian Computing Competition', 'CUZ' : 'because',
'TY' : 'thank-you', 'YW' : 'you’re welcome', 'TTYL' : 'talk to you later'}

while 1 :
    stringA = sys.stdin.readline().strip()
    if stringA == 'TTYL' :
        print(dicA['TTYL'])
        break
    else :
        if stringA not in dicA :
            print(stringA)
        else :
            print(dicA[stringA])
