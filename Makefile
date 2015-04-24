all: own

payload:
	python audit.py --action=payload --payloads=output/payloads.json

app%:
	python audit.py --action=robot --seeds=data/seeds/public/$@.json --endpoints=output/endpoints/$@.json
	python audit.py --action=auditor --seeds=data/seeds/public/$@.json --endpoints=output/endpoints/$@.json --payloads=output/payloads.json --exploits=output/exploits/$@.json
	python audit.py --action=automate --exploits=output/exploits/$@.json --script=output/scripts/$@

crawl-app%:
	python audit.py --action=robot --seeds=data/seeds/public/app$*.json --endpoints=output/endpoints/app$*.json

audit-app%:
	python audit.py --action=auditor --seeds=data/seeds/public/app$*.json --endpoints=output/endpoints/app$*.json --payloads=output/payloads.json --exploits=output/exploits/app$*.json

automate-app%:
	python audit.py --action=automate --exploits=output/exploits/app$*.json --script=output/scripts/app$*

own:
	python audit.py --action=robot \
		--seeds=data/seeds/own.json \
		--endpoints=output/endpoints/own.json
	python audit.py --action=auditor \
		--seeds=data/seeds/own.json \
		--endpoints=output/endpoints/own.json \
		--payloads=output/payloads.json \
		--exploits=output/exploits/own.json
	python audit.py --action=automate \
		--exploits=output/exploits/own.json \
		--script=output/scripts/own
