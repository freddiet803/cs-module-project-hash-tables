my_arr = ['some', 'words', 'in an', 'array']

#O(n) -- linear


def find_element(arr, el):
    for ele in arr:
        if ele == el:
            return True

    return False


# Binary search O(log n)

'''def magic_func_index(arr, el):
    return el_index'''


# hash tables == arrays + hashing function

# write a function that will take a string and return a number


# add up ascii  or unicode or .encode()

def ascii_hash(str):
    for letter in str:
        ##val = get_number_letter(letter)
        total += val

    return total


def utf8_hash(aString):
    utf8_bytes = aString.encode()
    print(utf8_bytes)
    total = 0
    for byte in utf8_bytes:
        total += byte

    return total


# basically a put
my_arr2 = [None] * 2000

our_hash = utf8_hash('supercalifragilisticexpialidocious')
print(our_hash)
idx = our_hash % len(my_arr2)

my_arr2[idx] = 'Mary Poppins'

# print(my_arr2)

# a get
# given the string supercali...
# essentially print my_arr2[3]

our_hash = utf8_hash('supercalifragilisticexpialidocious')
idx = our_hash % len(my_arr2)

val = my_arr2[idx]
print(val)

# supercalifragi... is the key and 'mary poppins' is the value

# a collision

key1 = 'dad'
key2 = 'add'

hash1 = utf8_hash(key1)
idx1 = hash1 % len(my_arr2)
my_arr2[idx1] = 'howdy'

print(my_arr2[idx1])
