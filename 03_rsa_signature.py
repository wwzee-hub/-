from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

print("===== RSA-PSS Digital Signature =====")

# 1. 生成 RSA 密钥对
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

message = b"This is an important message."

print("Message:", message.decode())

# 2. 使用私钥进行数字签名
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(
            hashes.SHA256()
        ),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("Signature:", signature.hex())

# 3. 使用公钥验证签名
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(
                hashes.SHA256()
            ),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("Signature verification SUCCESS")

except InvalidSignature:
    print("Signature verification FAILED")