# Simulated Brute Force Detector
attempts = {'user1': [401, 401, 200], 'user2': [401, 401, 401]}

for user, codes in attempts.items():
    if codes.count(401) >= 3:
        print(f"[!] Possible brute-force on {user}")
