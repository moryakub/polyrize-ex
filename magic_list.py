class MagicList:
    def __init__(self, cls_type=None):
        self._list = []
        self._cls_type = cls_type

    def enforce_valid_index(self, index):
            if index >= (len(self._list) + 1):
                raise IndexError("list index out of range")

    def __getitem__(self, item):
        self.enforce_valid_index(item)

        if self._cls_type:
            self._list.insert(item, self._cls_type())
        return self._list[item]

    def __setitem__(self, key, value):
        self.enforce_valid_index(key)

        try:
            self._list[key] = value
        except IndexError:
            self._list.insert(key, value)

    def __str__(self):
        return self._list.__str__()
