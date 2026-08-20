class MyHashMap:
    def __init__(self):
        self.BASE = 769
        self.buckets = [[] for _ in range(self.BASE)]

    def _hash(self, key):
        return key % self.BASE

    def put(self, key: int, value: int) -> None:
        bucket_id = self._hash(key)
        curr_bucket = self.buckets[bucket_id]
        for pair in curr_bucket:
            if pair[0] == key:
                pair[1] = value
                return

        curr_bucket.append([key, value])

    def get(self, key: int) -> int:
        bucket_id = self._hash(key)
        curr_bucket = self.buckets[bucket_id]
        for pair in curr_bucket:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        bucket_id = self._hash(key)
        curr_bucket = self.buckets[bucket_id]
        for i, pair in enumerate(curr_bucket):
            if pair[0] == key:
                curr_bucket.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
