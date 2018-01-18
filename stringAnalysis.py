#Sam Krimmel
#1/18/18
#stringAnalysis.py - reports data about a given sentence

sent = input('Enter a sentence: ')
spac = sent.count(' ')
char = len(sent)
print('Your sentence has', spac+1, 'words and', len(sent), 'characters and', char-spac, 'letters.')

schar = input('Enter a character to search for: ')
csent = sent.upper()
print('Your sentence has', csent.count(schar.upper()),'of the letter', schar)

sword = input('Enter a word to search for: ')
print('Your sentence has', sent.count(sword), 'of the word', sword)


