def find_common_elements(list1, list2):
    common_elements = [element for element in list1 if element in list2]
    for element in common_elements:
        print(element)
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
find_common_elements(list1, list2)