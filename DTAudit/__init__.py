from robot import robot
from factory import factory
from auditor import auditor
from automator import automator

class DTAuditor:

    def __init__(self, seeds, endpoints, payloads, exploits, script):
        self.seeds     = seeds
        self.endpoints = endpoints
        self.payloads  = payloads
        self.exploits  = exploits
        self.script    = script

    def launch(self):

        print '-- * DTAuditor launched * --'


        # Assemble the pipeline.
        bot   = robot()
        plant = factory()
        audit = auditor()
        auto  = automator()

        # seeds as input, output endpoints
        print '\t-- started crawling...'
        bot.launch([self.seeds], self.endpoints)
        print '\t-- done crawling.'

        # no inputs, output payloads
        print '\t-- started payload generation...'
        plant.launch([], self.payloads)
        print '\t-- done payload generation.'

        # endpoints and payloads as input, output exploits
        print '\t-- started exploiting...'
        audit.launch([self.endpoints, self.payloads], self.exploits)
        print '\t-- done exploiting.'

        # exploits as input, output scripts.
        # scripts' paths saved in the file self.script
        print '\t-- started automation script generation...'
        auto.launch([self.exploits], self.script)
        print '\t-- done automation script generation.'

        print '-- * DTAuditor finished auditing * --'
