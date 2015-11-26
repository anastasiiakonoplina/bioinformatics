import itertools

string = "CTTCTCACGTACAACAAAATC"


def patternToNumber(string):
	words = map(''.join, itertools.product('ACGT', repeat = len(string)))
	res = words.index(string)
	return res

print patternToNumber(string)