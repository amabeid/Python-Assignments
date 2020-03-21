'''
#Take a word from user,
#Print both synonym and antonym of that word
'''

#create synonym dictionary
syn_dict = {
'altitude'  : ['distance', 'elevation'],
'latitude'  : ['breadth', 'extent'],
'continuum' : ['continuity', 'sequence'],
'ingenuity' : ['ability', 'brilliance'],
'intellect' : ['acumen', 'genius',]
}

#create antonym dictionary
ant_dict = {
'altitude'  : ['nadir', 'depth'],
'latitude'  : ['extreme', 'limitation'],
'continuum' : ['discontinuity', 'gap'],
'ingenuity' : ['clumsiness', 'inability'],
'intellect' : ['foolishness', 'stupidity',]
}

#Welcome
print("\nSynonyms and Antonyms Dictionary.")

#Show dictionary keys
print ('\nWords:', syn_dict.keys(), '\n')

#Take input from user
search_word = input('Type a word from the list above: ')

#Show synonym values and show 'not found' when the key is not in the dictinary
print('\nSynonyms:', syn_dict.get(search_word, 'Sorry, not found'))

#Show antonym values and show 'not found' when the key is not in the dictinary
print('\nAntonyms:', ant_dict.get(search_word, 'Sorry, not found'))
exit('\nGoodbye!\n')
