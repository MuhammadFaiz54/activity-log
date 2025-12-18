import os
import random
from datetime import datetime, timedelta

start_date = datetime(2020, 1, 1)
end_date = datetime(2025, 12, 17) 

def make_commits(current_date):
    num_commits = random.randint(1, 6)
    
    for i in range(num_commits):
        with open("data.txt", "a") as file:
            file.write(f"Commit date: {current_date}\n")
        
        # Git Add
        os.system("git add data.txt")
        
        # Git Commit with PAST DATE
        # Format: YYYY-MM-DD HH:MM:SS
        date_str = current_date.strftime('%Y-%m-%d %H:%M:%S')
        commit_msg = f"Update work log for {date_str}"
        
        os.system(f'git commit --date="{date_str}" -m "{commit_msg}"')

# Main Loop
curr = start_date
while curr <= end_date:
    make_commits(curr)
    print(f"Committing for: {curr.strftime('%Y-%m-%d')}")
    curr += timedelta(days=1) # Next day

print("All commits generated! Now push to GitHub.")