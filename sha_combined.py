import hashlib

# Input string to be hashed
input_str = "This is the input string to be hashed"

# Generate a salted hash using SHA-1024
sha1024_salt = "randomly_generated_salt"
sha1024_input = input_str.encode('utf-8') + sha1024_salt.encode('utf-8')
sha1024_hash = hashlib.sha3_512(sha1024_input).hexdigest()

# Generate a SHA-3 hash of the SHA-1024 hash
sha3_hash = hashlib.sha3_512(sha1024_hash.encode('utf-8')).hexdigest()

# Output the results
print("Input string: ", input_str)
print("Salt used for SHA-1024 hash: ", sha1024_salt)
print("SHA-1024 hash with salt: ", sha1024_hash)
print("SHA-3 hash of SHA-1024 hash: ", sha3_hash)
