from DTAudit import DTAuditor
from DTAudit.auditor import auditor
from DTAudit.factory import factory
from DTAudit.automator import automator
import sys, getopt
from classes.robot import Robot
from twisted.internet import reactor
from scrapy import log
from DTAudit.util import Hunter
import json


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

        seed_idx = 0
        count = 0
        entrances = json.load(open(seeds, 'r'))
        holes = []

        for seed in entrances:
            if seed['auth'] is not None and 'grabs' in seed['auth']:
                hunter = Hunter(seed, seed_idx)
                holes += hunter.hunt()
                count += 1
            seed_idx += 1

            if 'extra_endpoints' in seed:
                holes += seed['extra_endpoints']

        spider = Robot(seeds)
        outputs = []
        if count < len(entrances):
            outputs = spider.crawl()
            log.start(loglevel=log.DEBUG)
            reactor.run()


        spider.transform(outputs, endpoints, appends=holes)

    elif action == 'payload':
        plant = factory()
        plant.launch([], payloads)

    elif action == 'auditor':
        worker = auditor(seeds)
        worker.launch([endpoints, payloads], exploits)

    elif action == 'automate':
        auto = automator('data/script.py', 'data/post.py', script)
        auto.launch([exploits], script + "/listing.json")


if __name__ == '__main__':
    main(sys.argv)
