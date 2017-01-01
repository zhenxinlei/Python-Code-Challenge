import sys, re, string


data = sys.stdin.readlines()

tmp = []
findNonWord = False
wordList = []

for iLine in data:
	findNonWord = False
	for idx in range(len(iLine)):
		iChar = iLine[idx]

		if re.match("[a-z]", iChar) and not findNonWord:
			tmp.append(iChar)
		elif iChar == ' ':
			if not findNonWord and len(tmp)>0:
				wordList.append(''.join(tmp))
			tmp = []
			findNonWord = False
		else:
			findNonWord = True
			tmp = []

		if idx==len(iLine)-1:
			if not findNonWord and len(tmp)>0:

				wordList.append(''.join(tmp))
			tmp = []

# print wordList
# print ''

wordCount = len(wordList)
print wordCount
print 'words'
wordSet = sorted(set(wordList))

for iWord in wordSet:
	print iWord + " " + str(wordList.count(iWord))

print 'letters'
for iLetters in string.lowercase[:26]:
	count = 0
	for iWord in wordList:
		count += iWord.count(iLetters)
	print iLetters + " " + str(count)
	count = 0;