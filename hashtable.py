class HashTable:
    def __init__(self, size):
        self.__table = {x: None for x in range(size)}


if __name__ == "__main__":
    hash_table = HashTable(10)
    print('test')
