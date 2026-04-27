def schetchik_bukv(text, char_dict=None):
    if char_dict is None:
      char_dict = {}
    if not text:
        return char_dict
    char = text[0]
    if char not in char_dict:
        char_dict[char] = text.count(char)
    return schetchik_bukv(text[1:], char_dict)

string_ = input("Enter your text: ")

result = schetchik_bukv(string_)

print("Here`s how much ur chars occur in ur text:")
for char, count in result.items():
    print("'{}': {}".format(char, count))