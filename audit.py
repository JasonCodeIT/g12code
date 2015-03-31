__author__ = 'Jason Poh'
import scrapy
import os
import json
from classes.robot import Robot
from classes.phase1 import InjectionPoint
from helpers import jsonhelper, filehelper


def main():
    spider = Robot("http://www.roboform.com/")
    spider.crawl()
    # inject_point1 = InjectionPoint('/page.html', 'GET', "MEOW")
    # inject_point2 = InjectionPoint('/page.html', 'GET', "MEOW2")
    # inject_points = [inject_point1, inject_point2]
    # json.dump(jsonhelper.list_to_json(inject_points), filehelper.get_injection_points_file(), indent=2)

if __name__ == "__main__":
    main()
