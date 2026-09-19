import hashlib;

print(hashlib.new("md4", "purPLE9795!@".encode("utf-16le")).hexdigest())
