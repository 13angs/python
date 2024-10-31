from collections import defaultdict

def group_by_field(array, field):
    # Initialize an empty dictionary to store the grouped objects.
    result = defaultdict(list)
    # Iterate over each object in the array.
    for obj in array:
        # Get the value of the specified field from the object.
        key = obj.get(field)
        # If the key is not already in the result dictionary, add it with an empty list.
        if key not in result:
            result[key] = []
        # Append the object to the list of its corresponding key.
        result[key].append(obj)
    # Return the dictionary of grouped objects.
    return result


array = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 30},
]

grouped_array = group_by_field(array, "age")
print(grouped_array)