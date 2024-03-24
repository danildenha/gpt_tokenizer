#Listing assigned char values
print([ord(x)for x in "Hey"])

#listing values using utf8
print(list("привіт, how are you?😁".encode("utf-8")))

text = "ＵＵＵｎｉｃｏｄｅ!𝔥𝔢𝔱 𝔥𝔬𝔴  𝔞𝔯𝔢 𝔶𝔬𝔲. As of Unicode version 15.1, there are 149,878 characters with code points, covering 161 modern and historical scripts, as well as multiple symbol sets - this is example of unicode values"
tokens = text.encode("utf-8") # raw bytes
tokens = list(map(int, tokens)) # convert to a list in range 0-255
print('-------------')
print(text)
print('-------------')
print("length: ", len(text))
print('-------------')
print(tokens)
print("length of tokens: ", len(tokens)) #proving that tokens are longer than text
print('-------------')

#Pair bitwyse encoding of tokens 
def getPairs(tokens):
    count = {}
    for pair in zip(tokens, tokens[1:]):
        count[pair] = count.get(pair,0) + 1
    return count

pairs = getPairs(tokens)
#print(sorted(((i,j) for j,i in pairs.items()), reverse=True))

#maxPair = max(pairs, key = pairs.get)
#print(maxPair)

def merge(tokens, pair, newId):
    newIds = []
    i = 0
    while i < len(tokens):
        if i < len(tokens) - 1 and tokens[i] == pair[0] and tokens[i+1] == pair[1]:
            newIds.append(newId)
            i += 2
        else:
            newIds.append(tokens[i])
            i += 1
    return newIds

updatedTokens = merge(tokens, maxPair, 256)
print(updatedTokens)



