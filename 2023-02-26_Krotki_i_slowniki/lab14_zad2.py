'''
Napisz funkcje zamieniającą 3 listy na 1 krotkę bez powtarzających się elementów.
Przykład: [1, 2], [1, 1], [4, 4, 4] -> (1, 2, 4)
'''
def merge_list_without_duplicates(source, target):
    for e in source:
        if e not in target:
            target.append(e)

def transform_data(list_1, list_2, list_3):
    result=[]
    merge_list_without_duplicates(list_1,result)
    merge_list_without_duplicates(list_2, result)
    merge_list_without_duplicates(list_3, result)
    return tuple(result)

print(transform_data([1,2], [1,1], [4,4,4]))
print(transform_data([1,2,3], [1,2,3], [4,5,6]))
print(transform_data(["Ala", "ma"], ["Ala", "ma", "kota"], ["mysz"]))


