
class Sample(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

samples = [
    Sample(3),
    Sample(2),
    Sample(1),
]

sorted_samples = sorted(samples, key=lambda s: getattr(s, 'value'), reverse=False)


for sample in sorted_samples:
    print(sample)