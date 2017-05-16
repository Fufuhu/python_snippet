
def sort_with_multiple_keys(list_to_sort, sort_rules=[("name", "asc"),]):

    sorted_list = list_to_sort
    sort_rules.reverse()
    for key, value in sort_rules:
        print("key:" + key)
        print("value:" + value)
        if value.lower() != "asc":
            print("逆順でソートします")
            sorted_list = sorted(sorted_list, key=lambda node: node[key], reverse=True)
        else:
            print("正順でソートします")
            sorted_list = sorted(sorted_list, key=lambda node: node[key])

    return sorted_list

list_to_sort = [
    {
        "name" : "fujiwara",
        "age" : 24,
    },
    {
        "name" : "fujiwara",
        "age" : 18,
    },
    {
        "name" : "nagashima",
        "age" : 24,
    },
    {
        "name" : "fujiwara",
        "age" : 32,
    },
    {
        "name": "nagashima",
        "age": 16,
    }
]



sorted_list = sort_with_multiple_keys(list_to_sort)

print(str(sorted_list))

sort_rules = [
    ("name", "asc"),
    ("age", "asc"),
]
sorted_list = sort_with_multiple_keys(list_to_sort, sort_rules=sort_rules)

print(str(sorted_list))


sort_rules = [
    ("hogehoge", "asc"),
    ("age", "asc"),
]
sorted_list = sort_with_multiple_keys(list_to_sort, sort_rules=sort_rules)

print(str(sorted_list))


