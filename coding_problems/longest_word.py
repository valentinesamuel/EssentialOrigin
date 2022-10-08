import re
"""
Longest Word
Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
Examples
Input: "fun&!! time"
Output: time
Input: "I love dogs"
Output: love
"""


def longestWord(sentence):
	if (not isinstance(sentence, str)):
		raise ValueError("Input is not a list")
	sentence = sentence.split(" ")
	longest_word = ''
	for word in sentence:
		word = re.sub(r'[^a-zA-Z0-9]', '', word)
		# print(word)
		if (len(word) > len(longest_word)):
			longest_word = word
	return longest_word


print(longestWord("This is$2346# just the rightestest time"))