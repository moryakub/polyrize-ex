from magic_list import MagicList
from person import Person

a = MagicList()
a[0] = 5
print(a)
a[1] = 3
print(a)
# a[3] = 4  # breaks index continuity, throws indexError

p = MagicList(cls_type=Person)
p[0].age = 1
p[1].age = 18
print(p)
# p[3].age = 20  # breaks index continuity, throws indexError
