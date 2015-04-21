from DTAudit import DTAuditor
from DTAudit.auditor import auditor
import sys, getopt
from classes.robot import Robot
import os
import json
from twisted.internet import reactor
from scrapy import signals, log


def main(argv):
    try:
        opts, args = getopt.getopt(argv[1:], 'a:s:e:p:x:c:', ['action=', "seeds=", "endpoints=", 'payloads=', 'exploits=', 'scripts='])
    except getopt.GetoptError:
        print argv[0], ' [--seeds=seeds.json] [--endpoints=endpoints.json]\
        [--payloads=payloads.json] [--exploits=exploits.json] [--scripts=scripts.json]'
        sys.exit(2)

    print opts, args

    seeds = 'data/seeds.json'
    endpoints = 'data/items.json'
    payloads = 'output/payloads.json'
    exploits = 'output/exploits.json'
    script = 'output/scripts.json'
    action = 'DTAuditor'

    for opt, arg in opts:
        if opt == '--seeds':
            seeds = arg
        elif opt == '--endpoints':
            endpoints = arg
        elif opt == '--payloads':
            payloads = arg
        elif opt == '--exploits':
            exploits = arg
        elif opt == '--scripts':
            script = arg
        elif opt == '--action':
            action = arg

    if action == 'DTAuditor':
        audit = DTAuditor(seeds=seeds,
                          endpoints=endpoints,
                          payloads=payloads,
                          exploits=exploits,
                          script=script)
        audit.launch()
    elif action == 'robot':
        spider = Robot(seeds)
        spider.crawl()
        log.start(loglevel=log.DEBUG)
        reactor.run()
    elif action == 'auditor':
        worker = auditor(seeds)
        worker.launch([endpoints, payloads], exploits)


if __name__ == '__main__':
    main(sys.argv)
