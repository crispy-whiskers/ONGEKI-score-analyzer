import math, re

table = []

class Play:
    def __init__(self, level, score, title, difficulty):
        self.title = title
        self.score = score
        self.level = level
        self.difficulty = difficulty

        # stolen from ChunithmRatingBreakdown, adjusted for ongeki
        levelBase = level*100
        rating = 0
        if score >= 1_007_500:
            rating = levelBase + 200
        elif score >= 1_000_000:
            rating = levelBase + 150 + (score - 1_000_000) / 7_500 * 500
        elif score >= 990_000:
            rating = levelBase + 100 + (score - 990_000) / 10_000 * 500
        elif score >= 970_000:
            rating = levelBase + (score - 970_000) / 20_000 * 500
        elif score >= 940_000:
            rating = levelBase - 500 + (score - 940_000) / 30_000 * 500
        elif score >= 900_000:
            rating = (levelBase - 500) / 2 + ((score - 900_000)
                                              * ((levelBase - 500) / 2)) / 100_000

        self.rating = rating/100

    def __str__(self):
        return f'{math.floor(self.rating*100)/100:.2f}\tfrom '+'{:,}'.format(self.score)+f'\ton {self.level}\t{self.title} {self.difficulty}'
        #string representation of score
        #rating displayed rounded down
        #{:,} for comma denoted numbers

    def __lt__(self, other):
        return self.rating < other.rating

    def __eq__(self, other):
        return self.title.__eq__(other.title) and self.score == other.score
    
    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    #f = open(sys.argv[1], encoding='utf-8').read()

    linepattern = r'\d\:\s()'

    p = Play(12.7, 1000473, 'Re:End of a Dream', 'EXPERT')
    print(str(p))