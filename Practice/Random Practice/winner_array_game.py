def getWinner(arr, k):
    winner = arr[0]
    wins = 0

    for challenger in arr[1:]:
        if winner > challenger:
            wins += 1
        else:
            winner = challenger
            wins = 1

        if wins == k:
            return winner

    return winner