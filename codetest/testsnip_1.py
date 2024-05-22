piano_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_keys[2:5])
# ['c', 'd', 'e']
print(piano_keys[2:5:])
# ['c', 'd', 'e']
print(piano_keys[2])
# c
print(piano_keys[2:])
# ['c', 'd', 'e', 'f', 'g', 'h', 'i']
print(piano_keys[:])
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(piano_keys[:1])
# ['a']
print(piano_keys[:2])
# ['a', 'b']
print(piano_keys[2:])
# ['c', 'd', 'e', 'f', 'g', 'h', 'i']
print(piano_keys[2:7])
# ['c', 'd', 'e', 'f', 'g']
print(piano_keys[2:9])
# ['c', 'd', 'e', 'f', 'g', 'h', 'i']
print(piano_keys[2:10])
# ['c', 'd', 'e', 'f', 'g', 'h', 'i']
print(piano_keys[0])
# a
print(piano_keys[:0])
# []
print(piano_keys[:-0])
# []
print(piano_keys[:1])
# ['a']
print(piano_keys[:-1])
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(piano_keys[::-1])
# ['i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
print(piano_keys[::1])
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(piano_keys[::])
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(piano_keys[:])
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
