import hashlib
import time

def proof_of_work(difficulty):
    prefix = '0' * difficulty
    nonce = 0
    start_time = time.time()
    
    while True:
        hash_result = hashlib.sha256(f"{nonce}".encode()).hexdigest()
        if hash_result.startswith(prefix):
            break
        nonce += 1
    
    end_time = time.time()
    return nonce, hash_result, end_time - start_time

# Test PoW
difficulty = 4
nonce, hash_result, duration = proof_of_work(difficulty)
print(f"Nonce trouvé : {nonce}, Hash : {hash_result}, Temps : {duration:.2f} secondes")
