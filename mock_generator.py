from unittest.mock import Mock


def get_mock():
    obj = Mock()
    obj.name = "test"
    return obj



obj1 = get_mock()
obj2 = get_mock()
obj2.name = "test02"

print(obj1.name)
print(obj2.name)