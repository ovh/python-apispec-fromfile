""" Plugin class """

from pathlib import Path

from apispec import BasePlugin
from apispec.yaml_utils import load_operations_from_docstring


class FromFilePlugin(BasePlugin):
    """APISpec plugin for importing OpenAPI specifications from a file.

    :param string func_key: the key used in `APISpec.path()` to register the
        function name
    """

    def __init__(self, func_key="view"):
        super().__init__()
        self.func_key = func_key

    def operation_helper(self, path=None, operations=None, **kwargs):
        """ apispec operation helper """
        # get the endpoint name
        view = kwargs.pop(self.func_key)

        # get specs
        specs = getattr(view, "__apispec__", None)

        # update operations
        if specs is not None:
            operations.update(specs)


def from_file(spec_path):
    """ Decorate an endpoint with an OpenAPI spec file to import. """

    def wrapper(func):
        # get the file
        path = Path(spec_path)
        if not path.exists():
            return func

        # get the content
        content = path.read_text()

        # save the content in a special attribute of the function
        func.__apispec__ = func.__dict__.get("__apispec__", {})
        func.__apispec__.update(load_operations_from_docstring(content))

        return func

    return wrapper
