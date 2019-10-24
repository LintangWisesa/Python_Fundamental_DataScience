
# Python provides another built-in type called a frozenset, 
# which is in all respects exactly like a set, except that a frozenset is immutable. 
# You can perform non-modifying operations on a frozenset:

x = frozenset([1, 2, 3])

print(x)
print(type(x))
print(len(x))

x.add(4)
x.pop()
x.clear()