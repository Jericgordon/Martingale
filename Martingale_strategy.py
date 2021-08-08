import random
import matplotlib.pyplot as plt
import numpy as np

bankroll = 1000
bet_size = 10

total_bets_placed = 0
bets_lost = 0

bankroll_history = []
total_bets_history = []

gamblers = 0
gamble_success = 0
gamble_no_loss = 0
gamble_fail = 0
gambler_final_bankroll = []

def strip_unique_sort(list):
    dictionary = {}
    for item in list:
        if item not in dictionary.keys():
            dictionary[item] = 1
        else:
            dictionary[item] += 1
    return(dictionary)
            

#betting parameters
def place_bet(bet_size,bets_lost):
    wager = bet_size * (2 ** (bets_lost + 1))
    global bankroll
    bankroll -= wager
    global total_bets_placed
    total_bets_placed += 1
def record():
    bankroll_history.append(bankroll)
    total_bets_history.append(total_bets_placed)


    

def reset():
    global bankroll
    bankroll = 1000
    global bet_size
    bet_size = 10

    global total_bets_placed
    total_bets_placed = 0
    global bets_lost
    bets_lost = 0

    global bankroll_history 
    bankroll_history = []
    global total_bets_history
    total_bets_history = []


def gamble():
    global bankroll
    global bets_lost
    while bankroll < 10000 and bankroll > 0:
        print(bankroll)
        place_bet(bet_size,bets_lost)
        if bankroll < 0:
            bankroll = bankroll_history[-1]
            break
        else:
            record()
        ball_roll = random.choice(range(2))

        if ball_roll == 0:
            bankroll += 2 * bet_size * (2 ** (bets_lost + 1))
            bets_lost = 0
            
        elif ball_roll == 1:
            bets_lost += 1
            
fig, ax = plt.subplots()  # Create a figure containing a single axes.

for x in range(100):
    gamble()
    gamblers += 1
    gambler_final_bankroll.append(bankroll)
    if bankroll >= 10000:
        key = 'b'
        gamble_success += 1
    elif bankroll >= 1000 and bankroll < 10000:
        key = 'orange'
        gamble_no_loss += 1
    elif bankroll < 1000 :
        key = 'g'
        gamble_fail += 1
    ax.plot(total_bets_history,bankroll_history, color =key)
    reset()
    
dictionary_of_wins= strip_unique_sort(gambler_final_bankroll)
print(dictionary_of_wins)
labels_bar = sorted(dictionary_of_wins.keys())

winnings = []
for key in labels_bar:
    winnings.append(dictionary_of_wins[key])
    



#bar chart
x = np.arange(len(labels_bar))
width_bar = .5

fig2, ax2 = plt.subplots()
rects1 = ax2.bar(labels_bar,winnings, .3, label="Gambler's winnings")
ax.set_xticklabels(labels_bar)

ax2.bar_label(rects1, padding =1)
fig2.tight_layout()

#Pie chart
labels = "reached 10000", "Made Money", "Lost money"
sizes = [gamble_success,gamble_no_loss,gamble_fail]
fig1, ax1 = plt.subplots()
ax1.pie(sizes,labels =labels, explode = [0,0,0], autopct = '%1.1f%%', shadow = False, startangle=90,)
ax1.axis('equal')
plt.show()

