import math, re, sys

table = []

class Play:
    def __init__(self, level, score, title, difficulty):
        self.title = title
        self.score = score
        self.level = level
        self.difficulty = difficulty

        # stolen from OngekiScoreLog https://github.com/project-primera/ongeki-score
        # also adapted part of chunithmratingbreakdown
        levelBase = level*100
        rating = 0
        if score >= 1_007_500:
            rating = (levelBase + 200)/100
        elif score >= 1_000_000:
            rating = math.floor((levelBase + 150) + (math.floor((score - 1000000) / 150))) / 100
        elif score >= 970_000:
            rating = math.floor(levelBase + (math.floor((score - 970000) / 200))) / 100
            #rating = round((levelBase + (score - 970_000) / 30_000 * 150)/100, 2)
        else:
            #according to the gamerch ongeki wiki, below 900k this formula is not verified
            rating = math.floor(levelBase - (math.floor((970000 - score) / 175 + 1))) / 100
            rating = 0 if rating < 0 else rating

        self.rating = rating

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

class Table:
    def __init__(self):
        self.scores = [] 
    
    def __str__(self):
        topavg = round(sum([x.rating for x in self.scores]) / len(self.scores) , 7)
        # average with rounding to prevent floating point errors

        return( f'Table of {str(len(self.scores))}:\n'+'\n'.join([str(x) for x in sorted(self.scores, reverse=True)]) +
                f'\nAverage: {topavg}' )
        # overall rating is always rounded down by two decimal places, but keeping raw decimal
        # so you can see exactly where you are


if __name__ == "__main__":
    f = open(sys.argv[1], encoding='utf-8').read()

    linepattern = r'(\t?Music	Level	Score )?\d+: (.*?)\t(Expert|Master|Advanced) Lv\. (\d\d\.\d)\t(\d+)'
    #print(re.match(linepattern, 'Music	Level	Score 1: Re：End of a Dream 	Expert Lv. 12.7	1000473').groups())
    lines = f.splitlines()
    status = 0

    bo30 = Table()
    new15 = Table()
    recent10 = Table() #10 best of 50

    for l in lines:
        if l.startswith('Total Best 30'):
            status = 1

        elif l.startswith('New Song Best 15'):
            status = 2
        
        elif l.startswith('Recent Best 10'):
            status = 3
        
        elif l.startswith('===='):
            status = 0

        m = re.match(linepattern, l)
        if not m == None:
            #print(m.groups())
            match status:
                case 1:
                    bo30.scores.append(Play(float(m.group(4)), int(m.group(5)), m.group(2), m.group(3)))
                case 2: 
                    new15.scores.append(Play(float(m.group(4)), int(m.group(5)), m.group(2), m.group(3)))
                case 3:
                    recent10.scores.append(Play(float(m.group(4)), int(m.group(5)), m.group(2), m.group(3)))
                case _:
                    continue


    print(str(bo30))
    print()
    print(str(new15))
    print()
    print(str(recent10))
