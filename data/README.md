# File format samples

## endpoints.json

This is the output/input format of robot/auditor.

The file contains a list of endpoints. Each endpoint has the following format:

```
{
    "url": "http://www.google.com",
    "target": "http://bm1.com",
    "method": "GET",
    "params": {
      "path": "abc",
      "file": ""
    },
    "files": ["file"]
}
```

* `url` is the URL on which a form is present.
* `target` is the `action` of the form
* `method` is the `method` of the form
* `params` contains the input names and default values. If no default value is available, empty string should be used.
* `files` is a list of input names that are file inputs