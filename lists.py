a = [66.25, 333, 333, 1, 1234.5]

print a

print 'count(333)', a.count(333)
print 'count(66.25)', a.count(66.25)
print "count('x')", a.count('x')

a.insert(2, -1)
a.append(333)
print a

print a.index(333)

a.remove(333)
print a
print a.index(333)

a.reverse()
print a
print a.index(333)

a.sort()
print a
print a.index(333)

words = ['cat', 'window', 'defenestrate']
for w in words:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)

print words
