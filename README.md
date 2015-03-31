# g12code

Entrance script is `audit.py`.

`classes` folder contains the models for the audit scanner.
`helpers` folder contains utility classess that works independently
`data` folder contains json files for communicating within our auditor application
`scrape` folder contains files for scrapy (spiders, items)

Modify `audit.py` with the start URL (e.g. `Robot("http://www.roboform.com/")`) and run the script:

    python audit.py

## Internal Running Sequence

1. `audit.py` instantiates `Robot`
2. `Robot` crawls using `scrapy` python module and output the endpoints to inject to `data/items.json`