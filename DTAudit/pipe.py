import abc
import json


class JSONPipe:
    """A module that is used to form a pipeline.

    Extend this class to create a component that
    takes a JSON format file as input and produces
    a JSON format file as output.

    Multiple such modules can be connected together
    to form a `pipeline` to finish a certain task.
    In our case, the DTAudit scanner.
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    def launch(self, inFiles, outFile):
        '''Launch the pipe with input file `inFile` and save its output to file `outFile`

        inFile  : JSON format file
        outFile : JSON format file
        '''
        incomings = []
        outgoing = []

        for path in inFiles:
            incomings.append(self.parse(path))

        outgoing = self.process(incomings)

        self.save(outgoing, outFile)

    @abc.abstractmethod
    def process(self, incomings):
        """Process the inputs

        Child class needs to implement this method.
        """
        return incomings

    def parse(self, path):
        """Parse the JSON format file at `path` and
        return the parsed Python object.
        """
        return json.loads(open(path).read())

    def save(self, items, path):
        """Save the Python object `items` as a JSON
        format file at `path`.
        """
        with open(path, 'w') as f:
            f.write(json.dumps(items, indent=4, separators=(',', ': ')))
            f.close()
