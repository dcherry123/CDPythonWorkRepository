# 6-6. Polling: Use the code in favorite_languages.py (page 104).
# Make a list of people who should take the favorite languages poll. Include some names that are already in the
# dictionary and some that are not.
# Loop through the list of people who should take the poll. If they have already taken the poll, print a message
# thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take the poll.

participant = {
                      'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                     }
poll_taken = ['phil', 'sarah']
for name in participant.keys():
    print(name.title())
if name in poll_taken:
    print("")
    print("Hi " + name.title() + ", I see your favorite language is " + participant[name].title() + "!")

