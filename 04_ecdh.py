from cryptography.hazmat.primitives.asymmetric import ec

print("===== ECDH Key Exchange =====")

# 1. Alice 生成自己的椭圆曲线密钥对
alice_private_key = ec.generate_private_key(
    ec.SECP256R1()
)

alice_public_key = alice_private_key.public_key()

# 2. Bob 生成自己的椭圆曲线密钥对
bob_private_key = ec.generate_private_key(
    ec.SECP256R1()
)

bob_public_key = bob_private_key.public_key()

# 3. Alice：
# Alice 私钥 + Bob 公钥
alice_shared_key = alice_private_key.exchange(
    ec.ECDH(),
    bob_public_key
)

# 4. Bob：
# Bob 私钥 + Alice 公钥
bob_shared_key = bob_private_key.exchange(
    ec.ECDH(),
    alice_public_key
)

print("Alice Shared Key:", alice_shared_key.hex())
print("Bob Shared Key  :", bob_shared_key.hex())

# 5. 比较双方共享密钥
if alice_shared_key == bob_shared_key:
    print("ECDH key exchange SUCCESS")
    print("Alice and Bob generated the same shared secret.")
else:
    print("ECDH key exchange FAILED")