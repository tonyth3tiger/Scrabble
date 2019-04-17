#Scrabble Game
#Game ends when all tiles are drawn and a player uses all their tiles or all but one.
#import pyDictionary to check if words exist
#create the 15 x 15 board using a 2D array or module?
#apply bonuses on specific tiles.
#first turn needs to place a tile on the middle space.





letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

count = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1] # number of tiles per letter

player_tiles = {} # the 7 tiles each player has | [player] = [ 7 letters ]

#points_and_count = zip(points, count)

letter_to_points = {letter: point for letter, point in zip(letters, points)}
letter_to_points[" "] = [0] #add count of 2 to blank space

player_to_words = {"player1": ['BLUE', 'TENNIS', 'EXIT'], "wordNerd": ['EARTH', 'EYES', 'MACHINE'],
                   "Lexi Con": ['ERASER', 'BELLY', 'HUSKY'], "Prof Reader": ['ZAP', 'COMA', 'PERIOD']}

player_to_points = {}


def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total


def play_word(player, word):
    player_to_words.setdefault(player, []).append(word.upper())


def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points

def check_bag_size():
    #make sure the size of the bag is not 0
    #if bag size is 0, check player tile count. If count is <= 1, declare winner and game is over.
    def check_player_count():
        pass

    def declare_winner():
        #max(update_point_values)
        #"The winner is [player]"
        pass


def check_valid():
    #check if word played is actual word by searching for it in pyDictionary
    #if real, pass, else, prompt player to enter another word
    pass


def exchange_tiles():
    #check_bag_size(), and print bag size. If 0, player cannot exchange tiles.
    #remove num of tiles and place them in a temp dict.
    #draw same amount of tiles from the bag
    #move temp tiles back into bag whilst updating the count of each tile.
    pass


def draw_tiles():
    #player draws the same number as len(word) and subtracts count for each letter.
    #create RNG of 1-26 and check if letter count is > 0. draw if true and re-roll if false.
    pass


def player_turn(player, word):
    #play_word
    #display_board
    #draw_tiles
    #update_point_totals
    #check bag_size

    #next_player
    pass


brownie_points = score_word("BROWNIE")
print(brownie_points)
update_point_totals()
print(player_to_points)
play_word("player1", "HELLO")
print (player_to_words)