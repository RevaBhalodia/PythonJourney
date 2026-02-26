#Develop a simple console-based voting system that allows users to vote for predefined candidates and
#displays detailed election results including winner, tie handling, total votes, and vote percentage.

# Voting System with Result Analysis
# Step 1: Store candidates
candidates = ["mike", "eleven", "will"]

# Step 2: Initialize vote dictionary
votes = {}

for candidate in candidates:
    votes[candidate] = 0

print("=================================")
print("        VOTING SYSTEM")
print("=================================")
print("Candidates:", ", ".join(candidates))
print("Type 'stop' to finish voting.")
print("=================================\n")

# Step 3: Voting Process
while True:
    user_vote = input("Enter candidate name: ").strip()

    if user_vote.lower() == "stop":
        break

    # Make voting case-insensitive
    found = False
    for candidate in candidates:
        if user_vote.lower() == candidate.lower():
            votes[candidate] += 1
            print("✅ Vote recorded!\n")
            found = True
            break

    if not found:
        print("❌ Invalid candidate! Please try again.\n")

# Step 4: Result Analysis
print("\n=================================")
print("        VOTING RESULTS")
print("=================================")

total_votes = sum(votes.values())
print("Total Votes Cast:", total_votes)
print("---------------------------------")

# If no votes
if total_votes == 0:
    print("No votes were cast.")
else:
    # Find highest vote count
    max_votes = max(votes.values())

    # Find winner(s)
    winners = []
    for candidate, count in votes.items():
        if count == max_votes:
            winners.append(candidate)

    # Display vote count and percentage
    for candidate, count in votes.items():
        percentage = (count / total_votes) * 100
        print(f"{candidate}: {count} votes ({percentage:.2f}%)")

    print("---------------------------------")

   # Winner or Tie
    if len(winners) == 1:
        print(f" Winner is: {winners[0]}")
    else:
        print(" It's a tie between:", ", ".join(winners))
print("=================================")