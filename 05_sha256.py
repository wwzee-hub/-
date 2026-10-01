from cryptography.hazmat.primitives import hashes

print("===== SHA-256 Hash =====")

message = b"Hello Cryptography Hash!"

digest = hashes.Hash(
    hashes.SHA256()
)

digest.update(message)

hash_value = digest.finalize()

print("Message:", message.decode())
print("SHA-256:", hash_value.hex())
print("Hash length:", len(hash_value) * 8, "bits")