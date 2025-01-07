"""
file: sitcomalyzer_app.py

Description: Implementation of Sitcomalyzer that loads txts of scripts
from pilot episodes of various sitcoms and shows different graphs
"""

from sitcomalyzer import Sitcomalyzer
import pprint as pp

def main():
    # initialize class and load stop words and scripts
    sca = Sitcomalyzer()
    sca.load_stop_words("stopwords.txt")
    sca.load_text('scripts/bbt_script.txt', 'big bang theory')
    sca.load_text('scripts/brooklyn99.txt', 'brooklyn99')
    sca.load_text('scripts/friends.txt', 'friends')
    sca.load_text('scripts/himym_script.txt', 'himym')
    sca.load_text('scripts/modern_family_script.txt', 'modern family')
    sca.load_text('scripts/new_girl_script.txt', 'new girl')
    sca.load_text('scripts/office.txt', 'office')
    sca.load_text('scripts/parks_and_rec.text', 'parks and rec')
    sca.load_text('scripts/seinfeld_script.txt', 'seinfeld')
    sca.load_text('scripts/the_good_place_script.txt', 'the good place')

    #print data and show graphs
    pp.pprint(sca.data)
    sca.compare_sentiment_scores()
    sca.sub_plots()
    sca.wordcount_sankey()

if __name__ == '__main__':
    main()
