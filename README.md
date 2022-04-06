# APISpec-fromfile

[![Tests Status](https://github.com/ovh/python-apispec-fromfile/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/ovh/python-apispec-fromfile/actions/workflows/tests.yml)
[![PyPI version](https://img.shields.io/pypi/v/apispec-fromfile)](https://pypi.python.org/pypi/apispec-fromfile)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/apispec-fromfile.svg)](https://pypi.python.org/pypi/apispec-fromfile)


[APISpec](https://apispec.readthedocs.io/en/latest/) plugin to import [OpenAPI specifications](https://github.com/OAI/OpenAPI-Specification) from a file instead of putting YAML into docstrings.


## Installation

```console
    pip install apispec-fromfile
```

## Usage

Create a YAML file `my/spec/file.yml`:

```yaml
---
get:
  summary: Hello
  operationId: hello
  responses:
    200:
      content:
        application/json:
          schema:
            type: string
```


Then, use APISpec in your Python code:

```python
from apispec import APISpec
from apispec_fromfile import FromFilePlugin
from apispec_fromfile import from_file

# Create an APISpec
spec = APISpec(
    title="Swagger Petstore",
    version="1.0.0",
    openapi_version="3.0.3",
    plugins=[
        FromFilePlugin("resource"),
    ],
)

# Create an endpoint
@from_file("my/spec/file.yml")
def hello():
    return {"hello"}

# Register entities and paths
spec.path("/hello", resource=hello)
```

# Related links

* Contribute: https://github.com/ovh/python-apispec-fromfile/blob/master/CONTRIBUTING.md
* Report bugs: https://github.com/ovh/python-apispec-fromfile/issues
* Get latest version: https://pypi.org/project/apispec-fromfile

# License

Copyright 2020 OVH SAS

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
