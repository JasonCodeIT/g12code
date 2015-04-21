all: run

run:
	python audit.py --action=auditor --seeds=data/seeds.bk.json --endpoints=output/endpoints/all.json --payloads=data/payloads-tiny.json --exploits=output/exploits.json

robot:
	python audit.py --action=robot


robot-own:
	python audit.py --action=robot --seeds=data/ownseeds.json --endpoints=output/endpoints-own.json

auditor-own:
	python audit.py --action=payload --payloads=output/payloads.json
	python audit.py --action=auditor --seeds=data/ownseeds.json --endpoints=output/endpoints-own.json --payloads=data/payloads-tiny.json --exploits=output/exploits/own-exploits.json

robot-app1:
	python audit.py --action=robot --seeds=data/seeds/public/app1.json --endpoints=output/endpoints/app1.json

auditor-app1:
	python audit.py --action=auditor --endpoints=output/endpoints/app1.json --payloads=data/payloads-tiny.json --exploits=output/exploits/app1.json

automator-app1:
	python audit.py --action=automate --exploits=output/exploits/app1.json --script=s.json

auditor-app3:
	python audit.py --action=auditor --endpoints=output/endpoints/app3.json --payloads=data/payloads-tiny.json --exploits=output/exploits/app3.json

auditor-app5:
	python audit.py --action=auditor --endpoints=output/endpoints/app5.json --payloads=data/payloads-tiny.json --exploits=output/exploits/app5.json

auditor-app6:
	python audit.py --action=auditor --endpoints=output/endpoints/app6.json --payloads=data/payloads-tiny.json --exploits=output/exploits/app6.json

auditor-app7:
	python audit.py --action=auditor --endpoints=output/endpoints/app7.json --payloads=data/payloads-tiny.json --exploits=output/exploits/app7.json

auditor-app8:
	python audit.py --action=auditor --endpoints=output/endpoints/app8.json --payloads=data/payloads-tiny.json --exploits=output/exploits/app8.json

auditor-app9:
	python audit.py --action=auditor --endpoints=output/endpoints/app9.json --payloads=data/payloads-tiny.json --exploits=output/exploits/app9.json

auditor-app11:
	python audit.py --action=auditor --endpoints=output/endpoints/app11.json --payloads=data/payloads-tiny.json --exploits=output/exploits/app11.json


clean:
	rm -rf output/*
