'''

Create a function called word_split() which takes in a string phrase and 
a list of words. The function will then determine if it is possible to
split tge string in a way that which words can be made from the list of 
words. You can assume the phrase will only contain words found in the 
dictionary if it is completely splittable. 

'''

def word_split(phrase,list_of_words,output=None):
	
	if output == None:
		output = []
	
	for word in list_of_words:
		
		if phrase.startswith(word):
			output.append(word)
			return word_split(phrase[len(word):],list_of_words,output)
	return output


ans = word_split('themanran',['clown','man','ran'])
if sum(list(map(len,ans))) == len('themanran'):
	print(ans)
else:
	print([])
ans = word_split('clownthemanran',['clown','man','ran'])
if sum(list(map(len,ans))) == len('themanran'):
	print(ans)
else:
	print([])
ans = word_split('themanran',['man','ran','the'])
if sum(list(map(len,ans))) == len('themanran'):
	print(ans)
else:
	print([])
ans = word_split('thegoodman',['bad','nice','good','average','the','a','an','man','woman'])
if sum(list(map(len,ans))) == len('thegoodman'):
	print(ans)
else:
	print([])