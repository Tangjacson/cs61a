# All cards available in a standard deck.
from classes import *

#TAs
aaron = TACard('Baron Aaron', 2100, 1300)
albert = TACard('Albert, Lethargy Incarnate', 1000, 2000)
alex = TACard('President Lieutenant Stennet for Senate', 1400, 2000)
aman = TACard('Aman', 1000, 2100)
anita = TACard("Anita, the Amazin' Avocado", 1500, 1900)
annie = TACard('Annie, the Annihilator of Water', 1700, 1500)
audrey = TACard('Audrey, Tree Whisperer', 2400, 1000)
brandon = TACard('The Wrong Fong ', 1000, 2300)
cesar = TACard('Cesar, Sponsor of Good Vibes™', 1600, 1700)
chae = TACard('Chae', 1500, 1900)
dalton = TACard('Dalton, Purveyor of Fate and Omens', 2300, 1000)
danelle = TACard('Danelle Nachos', 2200, 1100)
derek = TACard('Derek, The Wan and Only', 2000, 1000)
derrick = TACard('EZ4ENCE', 1100, 2000)
griffin = TACard('Griffin, Maximizer of Gains', 1100, 2300)
jack = TACard('Jack, The Coil King', 2100, 1200)
jade = TACard('Jade, Singher of Songs', 1700, 1500)
kartik = TACard('Karctic the Polar Bear Kapur', 2100, 1200)
kavi = TACard('Kavi Gupta', 2100, 1000)
lauren = TACard("Explorin' Lauren", 1200, 2200)
lillian = TACard('Lillian, Linda', 1100, 2100)
nancy = TACard('Nancy, The Sheep in the Jeep', 1100, 2100)
paul = TACard('Better Call Paul', 2100, 1200)
richard = TACard('Richard', 1500, 1900)
sean = TACard('Sean, Maker of Boba', 1700, 1500)
yannan = TACard('Yannan, Consumer of Anthocyanin', 1500, 1900)
yichen = TACard('Yichen, Drinker of Boba', 1800, 1500)

#Tutors
addison = TutorCard('Addison, Summer of Numbers', 1900, 1500)
ailyn = TutorCard('Ailyn, pronounced Eye-Lean', 1700, 1700)
aini = TutorCard('MacarAini and Cheese', 1800, 1500)
amy_m = TutorCard('Amy M', 1000, 2000)
christine = TutorCard('Christine', 1500, 1700)
grant = TutorCard('Grant', 1100, 2100)
jason = TutorCard('Jason, Counter of Chang-e', 1500, 1900)
jemmy = TutorCard('Jemmy', 1600, 1800)
nikhita = TutorCard('Nikhita the Fastest Cheetah', 1700, 1700)
olivia_b  = TutorCard('shocked pikachu', 1900, 1500)
olivia_s = TutorCard("Olivia, Guardian of Olives", 1800, 1600)
jennifer  = TutorCard('Jen, Head of Squirrels On Campus', 1600, 1700)
kaitlyn = TutorCard('Kaitlyn', 1300, 2000)
kevin = TutorCard('Kevin', 1500, 1900)
sam = TutorCard('Sam, The Exception-al Man', 1100, 2200)
shide = TutorCard('ShidzZz of YeetzZz', 1700, 1500)
uma = TutorCard('Uma, Empress of Eigenvalues', 2000, 1100)




# Professors
denero = ProfessorCard('John DeNero, Protector of Abstraction Barriers', 5000, 5000)

# A standard deck contains all standard cards.
standard_cards = [denero, aaron, albert, alex, aman, anita, annie, audrey, brandon, cesar, chae, dalton, danelle, derek, derrick, griffin, jack, jade, kartik, kavi, lauren, lillian, nancy, paul, richard, sean, yannan, yichen, addison, ailyn, aini, amy_m, christine, grant, jason, jemmy, nikhita, olivia_b , olivia_s, jennifer , kaitlyn, kevin, sam, shide, uma]
standard_deck = Deck(standard_cards)

# The player and opponent's decks are the standard deck by default.
player_deck = standard_deck.copy()
opponent_deck = standard_deck.copy()