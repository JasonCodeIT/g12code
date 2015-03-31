__author__ = 'Jason Poh'

from classes.robot import Robot
from scrape.settings import DEPTH_LIMIT, START_URL

def main():
    spider = Robot(START_URL, DEPTH_LIMIT)
    spider.crawl()

if __name__ == "__main__":
    main()
