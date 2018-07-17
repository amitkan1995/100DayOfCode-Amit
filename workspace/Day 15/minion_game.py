# The Minion Game from Hackerrank
# Link to the problem  https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
    # Logic is that to check for all possible combinations
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print ("Kevin", kevsc)
    elif kevsc < stusc:
        print ("Stuart", stusc)
    else:
        print ("Draw")


    s = input()
    minion_game(s)