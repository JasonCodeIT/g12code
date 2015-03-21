from DTAudit import DTAuditor

def main():

    print 'audit script'

    auditor = DTAuditor(seeds = 'data/seeds.json',
            endpoints = 'data/endpoints.json',
            payloads = 'data/payloads.json',
            exploits = 'data/expoits.json',
            script = 'data/scripts.json')

    auditor.launch()

main()
