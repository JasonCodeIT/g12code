all: run

run:
	python audit.py

auditor-app1:
	python audit.py --action=auditor --endpoints=output/endpoints/app1.json --payloads=data/payloads.json

auditor-app3:
	python audit.py --action=auditor --endpoints=output/endpoints/app3.json --payloads=data/payloads.json

auditor-app5:
	python audit.py --action=auditor --endpoints=output/endpoints/app5.json --payloads=data/payloads.json

clean:
	rm -rf output/*
