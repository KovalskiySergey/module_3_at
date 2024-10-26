def calculete_sum(data):
    total_sum = 0
    def recursive_(item):
        nonlocal total_sum
        if isinstance(item, (int, float)):
            total_sum += item
        elif isinstance(item, str):
            total_sum += len(item)
        elif isinstance(item, list):
            for i in item:
                recursive_(i)
        elif isinstance(item, set):
            for j in item:
                recursive_(j)
        elif isinstance(item, tuple):
            for k in item:
                recursive_(k)
        elif isinstance(item, dict):
            for key, value in item.items():
                recursive_(key)
                recursive_(value)
    for l in data:
        recursive_(l)
    return total_sum
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
                  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculete_sum(data_structure)
print(result)

