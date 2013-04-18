class nihil(object):
    def __getattribute__(self, method):
        return self

    def __call__(self, *args, **kwargs):
        return self

    def __bool__(self):
        return False
    __nonzero__=__bool__

    def __iter__(self):
        raise StopIteration
        yield

    def __repr__(self):
        return u"nihil()"

    def __str__(self):
        return ""

    def __add__(self, other):
        return other
    def __radd__(self, other):
        return other
    def __sub__(self, other):
        return -other
    def __rsub(self, other):
        return -other
    def __or__(self, other):
        return other
    def __ror__(self, other):
        return other
    def __xor__(self, other):
        return other
    def __rxor__(self, other):
        return other

    def __mul__(self, other):
        return self
    def __rmul__(self, other):
        return self
    def __and__(self, other):
        return self
    def __rand__(self, other):
        return self

nihil = nihil()
