from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

# 生成 256 bit AES 密钥
key = AESGCM.generate_key(bit_length=256)

# 创建 AES-GCM 对象
aesgcm = AESGCM(key)

# GCM 推荐使用 12 字节 nonce
nonce = os.urandom(12)

# 明文
plaintext = b"Hello Cryptography AES!"

# 加密
ciphertext = aesgcm.encrypt(
    nonce,
    plaintext,
    None
)

print("===== AES-256-GCM =====")
print("Plaintext :", plaintext.decode())
print("Key       :", key.hex())
print("Nonce     :", nonce.hex())
print("Ciphertext:", ciphertext.hex())

# 解密
decrypted = aesgcm.decrypt(
    nonce,
    ciphertext,
    None
)

print("Decrypted :", decrypted.decode())

if decrypted == plaintext:
    print("AES encryption/decryption SUCCESS")
else:
    print("AES encryption/decryption FAILED")