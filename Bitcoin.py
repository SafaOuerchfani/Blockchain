import hashlib
import base58
from ecdsa import SigningKey, SECP256k1

# Étape 1: Générer une clé privée (un nombre aléatoire de 256 bits)
private_key = SigningKey.generate(curve=SECP256k1)
private_key_bytes = private_key.to_string()

# Étape 2: Générer la clé publique à partir de la clé privée (courbe elliptique)
public_key = private_key.get_verifying_key()
public_key_bytes = public_key.to_string()

# Étape 3: Effectuer SHA-256 sur la clé publique
sha256_bpk = hashlib.sha256(public_key_bytes).digest()

# Étape 4: Effectuer RIPEMD-160 sur le résultat du SHA-256
ripemd160 = hashlib.new('ripemd160')
ripemd160.update(sha256_bpk)
public_key_hash = ripemd160.digest()

# Étape 5: Ajouter le préfixe de version (0x00 pour une adresse Bitcoin standard)
versioned_public_key = b'\x00' + public_key_hash

# Étape 6: Effectuer un double hachage SHA-256 sur le résultat
checksum = hashlib.sha256(hashlib.sha256(versioned_public_key).digest()).digest()[:4]

# Étape 7: Ajouter le checksum à la fin de la versioned_public_key
binary_address = versioned_public_key + checksum

# Étape 8: Encoder l'adresse en Base58
bitcoin_address = base58.b58encode(binary_address)

# Afficher la clé privée et l'adresse Bitcoin
print(f"Clé privée (hex): {private_key_bytes.hex()}")
print(f"Adresse Bitcoin: {bitcoin_address.decode('utf-8')}")
