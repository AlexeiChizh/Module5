


class StringVar:

    def __init__(self):
         self.s = ''

    def set (self, val):

        self.s = val
    def get (self):

        return self.s

s = StringVar()
s1 = StringVar()

print(s.set('qqq'))
print(s1.set('aaa'))
print(s.get())
print(s1.get())
