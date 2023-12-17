# ONGEKI-score-analyzer
Find the worth of multiple ONGEKI scores.

# Use

This script requires any `Python 3` installation.

### Aqua Webui
This is primarily written with the Aqua webui in mind. Do not use the Aqua JSON export function, it does not contain enough information for a rating breakdown. First, open the Rating page in the webui. Hit `CTRL+A` and copy, then paste the contents into a text file. The text file will look like this: 

```
Aqua Viewer
Rating
Current Rating: 13.63
Highest Rating: 13.63
Total Best 30
Music	Level	Score 1: Re：End of a Dream 	Expert Lv. 12.7	1000473
2: CO5M1C R4ILR0AD 	Master Lv. 13.8	982064
3: 光線チューニング 	Master Lv. 12.8	996718
4: STARLIGHT TWILIGHT -GC edit- 	Master Lv. 13.8	975839
5: Halcyon 	Master Lv. 13.4	983198
...
```

Don't worry about the first score being in line with the table header. This is accounted for.

Run the script like this: 
```
python3 analyzer.py your_score_file.txt
```

### CSV input
Not really sure how other servers like Artemis export. For everything else, there is `csv`. Make sure the csv has the following format: