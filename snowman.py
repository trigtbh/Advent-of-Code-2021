# Run as:
# snowman(n, arr)
def snowman(n: int, arr: list) -> tuple:
    """
    A function that passes the Christmas challenge

    Parameters
    ---
    n        (int): Step for elimination
    arr     (list): Grid of elements to comb through
                    Should be a multidimensional array such as
                        Each line of the grid split into its individual characters (as integers)
                        [[int, int, int], [int, int, int], ...]
                    or
                        Each line of the grid split into its individual characters (as strings)
                        [[str, str, str], [str, str, str], ...]
                    or
                        Each line of the grid in its own list
                        [[str], [str], [str], ...]
    
    Returns
    ---
    return (tuple): Tuple containing the points of the snowman and Santa
                    (will give None as a point if the entity not found)
    
    Example Usage
    ---
    snowman(3, [["0006060066"], ["6900696600"], ["0000990006"], ["6060906606"]]) -> ((0, 6), (2, 9))
    """
    global flattened
    if isinstance(arr[0][0], int):
        flattened = [str(x) for line in arr for x in line]
        length = len(arr[0])
        height = len(arr)
    elif len(arr[0]) == 1:
        flattened = [x for line in arr for x in str(line[0])]
        height = len(arr)
        length = len(arr[0][0])
    else:
        flattened = [x for line in arr for x in line]
        length = len(arr[0])
        height = len(arr)

    arr = []

    def explode(point):
        global flattened
        y, x = point
        
        valid2 = list(filter(lambda newpoint: (0 <= newpoint[0] < height) and (0 <= newpoint[1] < length), [(y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)]))
        flattened[(point[0] * length) + point[1]] = "X"
        for p in valid2:
            val = flattened[(p[0] * length) + p[1]]
            if val == "9":
                explode(p)
                continue
            if flattened.count(val) > 1:
                flattened[(p[0] * length) + p[1]] = "X"
        valid2 = []

    i = 0
    
    size = length * height
    while True:
        p = 0
        while p < n:
            
            
            if i >= size:
                i -= size + 1
                continue
            if flattened[i] != "X":
                p += 1
            if p < n:
                i += 1
            
        px = i % length
        py = i // length
        val = flattened[(length * py) + px]
        if val == "9":
            explode((py, px))
            continue
        if flattened.count(val) > 1:
            flattened[(length * py) + px] = "X"
        else:
            break
    

    for item in ["0", "6"]:
        while flattened.count(item) > 1:
            flattened["".join(flattened).rindex(item)] = "X"

    inside = tuple((flattened.index(item) // length, flattened.index(item) % length) if item in flattened else None for item in ["0", "6"])
    # tuple comprehension for the win lmao
    
    flattened = []
    
    return inside