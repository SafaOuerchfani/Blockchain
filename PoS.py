import random

def proof_of_stake(validators):
    total_stake = sum(validators.values())
    rnd = random.uniform(0, total_stake)
    cumulative = 0
    
    for validator, stake in validators.items():
        cumulative += stake
        if cumulative >= rnd:
            return validator

# Test PoS
validators = {"Alice": 50, "Bob": 50, "Charlie": 20}
selected_validator = proof_of_stake(validators)
print(f"Validateur choisi : {selected_validator}")
