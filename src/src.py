#Listing assigned char values
print([ord(x)for x in "Hey"])

#listing values using utf8
print(list("привіт, how are you?😁".encode("utf-8")))

text = "ＵＵＵｎｉｃｏｄｅ!𝔥𝔢𝔱 𝔥𝔬𝔴  𝔞𝔯𝔢 𝔶𝔬𝔲 - this is example of unicode values"
tokens = text.encode("utf-8") # raw bytes
tokens = list(map(int, tokens)) # convert to a list in range 0-255
print('-------------')
print(text)
print('-------------')
print("length: ", len(text))
print('-------------')
print(tokens)
print("length of tokens: ", len(tokens)) #proving that tokens are longer than text
