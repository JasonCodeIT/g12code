all: run

run:
	python audit.py

auditor-app1:
	python audit.py --action=auditor --endpoints=output/endpoints/app1.json --payloads=data/payloads.json

auditor-app3:
	python audit.py --action=auditor --endpoints=output/endpoints/app3.json --payloads=data/payloads.json

auditor-app5:
	python audit.py --action=auditor --endpoints=output/endpoints/app5.json --payloads=data/payloads.json

auditor-app6:
	python audit.py --action=auditor --endpoints=output/endpoints/app6.json --payloads=data/payloads.json

auditor-app7:
	python audit.py --action=auditor --endpoints=output/endpoints/app7.json --payloads=data/payloads.json

auditor-app8:
	python audit.py --action=auditor --endpoints=output/endpoints/app8.json --payloads=data/payloads.json

auditor-app9:
	python audit.py --action=auditor --endpoints=output/endpoints/app9.json --payloads=data/payloads.json

auditor-app11:
	python audit.py --action=auditor --endpoints=output/endpoints/app11.json --payloads=data/payloads.json

clean:
	rm -rf output/*
