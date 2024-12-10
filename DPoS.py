def dpos(voters, delegates):
    votes = {delegate: 0 for delegate in delegates}
    
    for voter, delegate in voters.items():
        if delegate in votes:
            votes[delegate] += 1

    sorted_delegates = sorted(votes.items(), key=lambda x: x[1], reverse=True)
    return sorted_delegates[:3]  # Top 3 délégués

# Test DPoS
voters = {"User1": "Delegate1", "User2": "Delegate2", "User3": "Delegate1", "User4": "Delegate3"}
delegates = ["Delegate1", "Delegate2", "Delegate3"]
top_delegates = dpos(voters, delegates)
print(f"Top délégués élus : {top_delegates}")
