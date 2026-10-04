def count(x):
    print("Counting to", x)
    for i in range(x):
        print(i + 1)

def count_back(x):
    print("Counting back from", x)
    for i in range(x, 0, -1):
        print(i)

count(10)
count_back(10)