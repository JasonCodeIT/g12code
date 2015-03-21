# g12code

Entrance script is `audit.py`.

`DTAudit` folder contains source code for sub modules.

## Call stack

1. `audit.py`
2. `DTAudit.DTAuditor.launch()` &raquo; in `DTAudit/__init__.py`
3. `DTAudit.robot.robot.launch()` &raquo; in `DTAudit/robot.py`
4. `DTAudit.factory.factory.launch()` &raquo; in `DTAudit/factory.py`
5. `DTAudit.auditor.auditor.launch()` &raquo; in `DTAudit/auditor.py`
6. `DTAudit.automator.automator.launch()` &raquo; in `DTAudit/automator.py`

## Code organization

The 4 parts of the scanner are divided into 4 Python modules:

1. `DTAudit.robot` for the crawler;
2. `DTAudit.factory` for the payload generator;
3. `DTAudit.auditor` for the injection of payloads and exploit generation;
4. `DTAudit.automator` for the automation script generation.

Class `robot.robot`, `factory.factory`, `auditor.auditor` and
`automator.automator` all inherit from `pipe.pipe`, which is
a simple modular component for processing JSON input and output
in a "pipelined" fasion.

## How to proceed

Implement the `process()` method for the following classes:

1. `robot.robot`
2. `factory.factory`
3. `auditor.auditor`
4. `automator.automator`

