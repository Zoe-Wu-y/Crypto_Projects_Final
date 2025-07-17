import hashlib

def private_set_intersection(user_hashes, leaked_db_hashes):
    return set(user_hashes) & set(leaked_db_hashes)

if __name__ == "__main__":
    user = ["password1", "hello123"]
    db = [hashlib.sha256(b"hello123").hexdigest()]
    print(private_set_intersection([hashlib.sha256(p.encode()).hexdigest() for p in user], db))
