from DTAudit import DTAuditor
from DTAudit.auditor import auditor


def main():
    audit = DTAuditor(seeds='data/seeds.json',
                      endpoints='output/endpoints.json',
                      payloads='output/payloads.json',
                      exploits='output/exploits.json',
                      script='output/scripts.json')
    audit.launch()


def test_auditor():
    worker = auditor()

    worker.launch(['output/endpoints.json', 'output/payloads.json'], 'output/exploits.json')


test_auditor()
