from DTAudit import DTAuditor

def main():

    auditor = DTAuditor(seeds = 'data/seeds.json',
            endpoints = 'output/endpoints.json',
            payloads = 'output/payloads.json',
            exploits = 'output/expoits.json',
            script = 'output/scripts.json')

    auditor.launch()

main()
