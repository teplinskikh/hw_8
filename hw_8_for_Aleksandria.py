# part with find() and rfind()
st1 = 'This string is used to study string methods such as find() and rfind()'
print('First entrance from the left:', st1.find('string'))
print('First entrance from the right:', st1.rfind('string'))

# with start parameter
print('First entrance from the left:', st1.find('d', 4))
print('First entrance from the right:', st1.rfind('d', 4))

# with start and end parameters
print('First entrance from the left:', st1.find('find', 30, 70))
print('First entrance from the right:', st1.rfind('find', 30, 70))


# an example with no such symbol in string
st2 = 'hello, world'
print(st2.find('a'))
print(st2.rfind('a'))

