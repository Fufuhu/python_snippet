
class SampleClass(object):
    """
    ソート対象となるサンプルクラス
    """
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __str__(self):
        return str(self.value1) + "," + str(self.value2)


def sort(objs, sort_rule=("value1", "asc")):
    """
    ソート用の関数
    """
    key, order = sort_rule

    is_reverse = (order.lower() != "asc")
    if hasattr(objs[0], key):
        return sorted(objs, key=lambda obj: getattr(obj, key), reverse=is_reverse)

    print("hogehoge")
    return objs


targets = [
    SampleClass(value1="test003", value2="sample003"),
    SampleClass(value1="test002", value2="sample001"),
    SampleClass(value1="test001", value2="sample002")
]

# value1をキーにして並び替え
sorted_targets = sort(objs=targets)

for obj in sorted_targets:
    print(obj)

print("========")

# value2をキーにして、降順で並び替え
# dscを指定しているけれども、実際にはasc以外ならなんでも良い
sorted_targets = sort(objs=targets, sort_rule=("value2", "dsc"))

for obj in sorted_targets:
    print(obj)