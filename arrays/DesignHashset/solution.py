class MyHashSet:
    def __init__(self):
        self.BASE = 769
        self.buckets = [[] for _ in range(self.BASE)]

    def _hash(self, key: int):
        return key % self.BASE

    def add(self, key: int) -> None:
        bucket_id = self._hash(key)
        curr_bucket = self.buckets[bucket_id]
        if key not in curr_bucket:
            curr_bucket.append(key)

    def remove(self, key: int) -> None:
        bucket_id = self._hash(key)
        curr_bucket = self.buckets[bucket_id]
        try:
            curr_bucket.remove(key)
        except ValueError:
            pass

    def contains(self, key: int) -> bool:
        bucket_id = self._hash(key)
        curr_bucket = self.buckets[bucket_id]
        return key in curr_bucket


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
