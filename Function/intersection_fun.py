def find_intersection(list1, list2):
    """
    Find the intersection of two lists.
    The result contains unique elements present in both lists.

    Args:
        list1 (list): The first list of elements.
        list2 (list): The second list of elements.

    Returns:
        list: A list of unique elements common to both input lists.
    """
    return list(set(list1) & set(list2))


# Define the input lists
list1 = [4, 5, 6, 3, 3]
list2 = [2, 5, 6, 2, 6]

# Find and print the intersection
intersection_result = find_intersection(list1, list2)
print("Intersection:", intersection_result)
