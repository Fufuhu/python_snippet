
def sort_with_name(list_to_sort):
    sorted_list = sorted(list_to_sort, key=lambda elem: elem.name , reverse=True)
    return sorted_list

class SampleClass:

    def do_something(self, list_to_sort, sort_method=sort_with_name):
        return sort_method(list_to_sort)


class SampleElement:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "Name:" + self.name


list_to_be_sorted = []
for i in range(0, 3):
    element = SampleElement("test_"+str(i))
    list_to_be_sorted.append(element)


for j in list_to_be_sorted:
    print(str(j))

sample = SampleClass()
sorted_list = sample.do_something(list_to_sort=list_to_be_sorted)

for k in sorted_list:
    print(str(k))