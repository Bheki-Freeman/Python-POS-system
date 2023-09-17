# printing lists without the square brackets
lst = ['People', 'man', 1, ['honda', 'toyota', 'venus']]

print(f'The list before any formating: \n{lst}')
print('The list after Unpacking square brackets: \n', *lst[0:3], *lst[3])
print(f'The inverse of the list: {lst[::-1]}')
print(f'Try unpacking the inverse of the list: ', *lst[::-1])

# Now, let's work with sets
print(f'\nNow, let\'s work with sets')
st = ('Nokwanda', 'Celiwe', 'Fakazile', 'Phelelile')
print(f'set before any formating: {st}')
print(f'reverse the set: {st[::-1]}')
print(f'Unpacke the set using the unpack construct:  ', *st)

# Now, let's take a look back into dictionaries
print(f'\nNow, let\'s take a look-back into dictionaries\n\
      We are gonna create a \'Real-World\' Dictionary')

oxford_dictionary = {
    'computer': 'An electronic device resposible for smartness',
    'Homo Sapien': 'A Scientific name of you',
    'People': 'Plural of a person, or we can just say many persons'
}

word = input('Enter a word to search for: ')
if word in oxford_dictionary:
    print(oxford_dictionary[word])
else:
    print(f'{word} Not found!')
