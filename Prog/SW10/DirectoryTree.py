import os

def getIndent(level):
    return "|      " * (level - 1) + "| - -  "

def print_tree(path, level=0):
    if level == 0:  
        print(os.path.basename(path)+"/")
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print(getIndent(level) + item + "/")
            print_tree(item_path, level + 1)
        else:
            print(getIndent(level) + item)

if __name__ == "__main__":
    print_tree(input("Enter the path to the directory: "))