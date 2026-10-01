from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

print("===== RSA-2048 Encryption / Decryption =====")

# 1. 生成 RSA 私钥
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# 2. 从私钥得到公钥
public_key = private_key.public_key()

print("RSA 2048-bit key pair generated successfully.")

# 明文
message = b"Hello Cryptography RSA!"

print("Plaintext :", message.decode())

# 3. 公钥加密
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(
            algorithm=hashes.SHA256()
        ),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Ciphertext:", ciphertext.hex())

# 4. 私钥解密
decrypted = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(
            algorithm=hashes.SHA256()
        ),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Decrypted :", decrypted.decode())

if decrypted == message:
    print("RSA encryption/decryption SUCCESS")
else:
    print("RSA encryption/decryption FAILED")