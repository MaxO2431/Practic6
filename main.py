def sizer(cls):
    class SizedClass(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.size = self._calc_size()

        def _calc_size(self):
            if hasattr(self, '__len__'):
                return len(self)
            elif hasattr(self, '__abs__'):
                return abs(self)
            else:
                return 0

    return SizedClass


@sizer
class MyClass:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __abs__(self):
        return sum(self.data)

obj = MyClass([1, 2, 3])
print(obj.size)  # 3

obj = MyClass([])
print(obj.size)  # 0

obj = MyClass([-1, 2, -3])
print(obj.size)  # 6


