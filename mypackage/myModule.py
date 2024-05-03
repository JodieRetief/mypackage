def top_n(items, n):
    """
    Return top n items in an array, in descending order.

    Args:
        items (array): list or array-like object
        n (int): number of items to return

    Return:
        array: top n items, in descending order

    Examples:
        >>> top_n([8,3,2,7,4], 3)
            [8,7,4]
    """
    for i in range(n):
        for j in range(len(items)-1-i):
            if items[j] < items[j+1]:  # Change '>' to '<' for descending order
                items[j], items[j+1] = items[j+1], items[j]

    top_n = items[-n:]

    return top_n[::-1]  # Reverse the list to get descending order


