import os

def makeCommits(days):
    if days < 1:
        # Final push to remote after all commits
        os.system('git push')
        return
    else:
        # Set commit date for n days ago
        dates = f"{days} days ago"

        # Write something to data.txt
        with open('data.txt', 'a') as file:
            file.write(f'{dates} <- this was the commit for the day!!\n')

        # Add file to staging
        os.system('git add data.txt')

        # Commit with a backdated timestamp
        os.system(f'git commit --date="{dates}" -m "Commit for {dates}"')

        # Recursively call for previous day
        makeCommits(days - 1)

# Run the function with desired number of days
makeCommits(365)  # Change this number to however many days you want
