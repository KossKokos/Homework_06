c_r = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
t_late = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

BAD_SYMBOLS = ('%', '*', ' ', '-')
TRANS = {}
for i, l in zip(c_r, t_late):
    TRANS[ord(i)] = l
    TRANS[ord(i.upper())] = l.upper()
    
for i in BAD_SYMBOLS:
    TRANS[ord(i)] = '_'

def normalize(name):
    trans_name = name.translate(TRANS)
    return trans_name

if __name__ == '__main__':
    print(normalize('****Привіт-Світ%****'))