
class Sample(object):
    def __init__(self, value, value2):
        self.value = value
        self.value2 = value2

    def __str__(self):
        return self.value+", "+str(self.value2)

samples = [
    Sample('a',3),
    Sample('c', 2),
    Sample('b', 1),
]

print("###valueで並び替え###")
sorted_samples = sorted(samples, key=lambda s: getattr(s, 'value'), reverse=False)

for sample in sorted_samples:
    print(sample)


print("###value2で並び替え###")
sorted_samples2 = sorted(samples, key=lambda s: getattr(s, 'value2'), reverse=False)

for sample in sorted_samples2:
    print(sample)