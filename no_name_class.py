from copy import deepcopy

sample_class = type("SampleClass", (), {
    "name" : "test",
})

sample_class_2 = deepcopy(sample_class)
sample_class_2.name = "test2"

print(sample_class.name)
print(sample_class_2.name)