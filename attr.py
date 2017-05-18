

class SampleClass(object):
    def __init__(self):
        self.foo = "FOO"
        self.bar = "BAR"


sample = SampleClass()

if hasattr(sample, "foo"):
    value = getattr(sample, "foo")
    print(value)

if hasattr(sample, "bar"):
    value = getattr(sample, "bar")
    print(value)