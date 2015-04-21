__author__ = 'Jason Poh'

from classes.robot import Robot
import os
import json
from twisted.internet import reactor
from scrapy import signals, log

def main():
    spider = Robot()
    spider.crawl()
    log.start(loglevel=log.DEBUG)
    reactor.run()

    # Remove duplicates from data/items.json
    # Results stored in data/items_unique.json
    lines_seen = set() # holds lines already seen
    outfile = open(os.path.join(os.path.dirname(__file__), 'data/items_unique.json'), "w")
    for line in open(os.path.join(os.path.dirname(__file__), 'data/items.json'), "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    # End of remove duplicates

if __name__ == "__main__":
    main()
