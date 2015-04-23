all: run

run:
	python audit.py --action=auditor --seeds=data/seeds.json --endpoints=output/endpoints/all.json --payloads=output/payloads.json --exploits=output/exploits.json

robot:
	python audit.py --action=robot

own:
	python audit.py --action=robot \
		--seeds=data/ownseeds.json \
		--endpoints=output/endpoints-own.json
	python audit.py --action=payload \
		--payloads=output/payloads.json
	python audit.py --action=auditor \
		--seeds=data/ownseeds.json \
		--endpoints=output/endpoints-own.json \
		--payloads=output/payloads.json \
		--exploits=output/exploits/own-exploits.json
	python audit.py --action=automate \
		--exploits=output/exploits/own-exploits.json \
		--script=output/script.json

payload:
	python audit.py --action=payload --payloads=output/payloads.json

app%:
	python audit.py --action=robot --seeds=data/seeds/public/$@.json --endpoints=output/endpoints/$@.json
	python audit.py --action=auditor --seeds=data/seeds/public/$@.json --endpoints=output/endpoints/$@.json --payloads=output/payloads.json --exploits=output/exploits/$@.json
	python audit.py --action=automate --exploits=output/exploits/$@.json --script=output/script.json

clean:
	rm -rf output/*
