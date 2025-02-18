def solve(data: list, values: list, validations: list) -> list | None:
    for i, item in enumerate(data):
        if item == None:
            for value in values:
                data[i] = value
                if all(validation(data) for validation in validations):
                    if len(data) == len([i for i in data if i != None]):
                        return data
                    result = solve(list(data), values, validations)
                    if result is not None:
                        return result
        
    return None

def checkRows(data: list) -> bool:
    rows = [data[i:i+4] for i in range(0, len(data), 4)]
    for row in rows:
        notNone = [i for i in row if i != None]
        if len(notNone) != len(set(notNone)): #check if has duplicates
            return False
    return True

def checkColumns(data: list) -> bool:
    columns = [data[i::4] for i in range(4)]
    for column in columns:
        notNone = [i for i in column if i != None]
        if len(notNone) != len(set(notNone)): #check if has duplicates
            return False
    return True

def checkSquares(data: list) -> bool:
    squares = [
        [data[0], data[1], data[4], data[5]],
        [data[2], data[3], data[6], data[7]],
        [data[8], data[9], data[12], data[13]],
        [data[10], data[11], data[14], data[15]]
    ]
    for square in squares:
        notNone = [i for i in square if i != None]
        if len(notNone) != len(set(notNone)): #check if has duplicates
            return False
    return True

data = [
    1   ,None,None,None, 
    None,None,None,3   , 
    None,4   ,2   ,None, 
    None,None,None,None] #4x4 sudoku

# solution = [
#     1   ,3   ,2   ,4   , 
#     4   ,2   ,1   ,3   , 
#     2   ,4   ,3   ,1   , 
#     3   ,1   ,4   ,2   ]

def printData(data):
    if data is None:
        print("Solution not found")
    else:
        rows = [data[i:i+4] for i in range(0, len(data), 4)]
        for row in rows:
            print(row)

printData(data)

solution = solve(data, [1,2,3,4], [checkRows, checkColumns, checkSquares])
printData(solution)