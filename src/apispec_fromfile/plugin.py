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

        if specs is None:
            get_specs = getattr(view, "__get_apispec__", None)

            if get_specs is not None:
                specs = get_specs()

        # update operations
        if specs is not None:
            operations.update(specs)


def read_spec(path: str):
    # get the file
    path = Path(path)
    if not path.exists():
        return None

    # get the content
    return path.read_text()


def load_spec(func, path):
    content = read_spec(path)
    spec = func.__dict__.get("__previous_apispec__", {})

    if content is None:
        return spec

    spec.update(load_operations_from_docstring(content))
    func.___previous_apispec__ = spec

    return spec


def from_file(spec_path, live_reload: bool = False):
    """ Decorate an endpoint with an OpenAPI spec file to import. """

    def wrapper(func):
        # save the content in a special attribute of the function
        content = read_spec(spec_path)

        if content is None:
            return func

        if live_reload:
            func.__get_apispec__ = lambda: load_spec(func, spec_path)
        else:
            func.__apispec__ = func.__dict__.get("__apispec__", {})
            func.__apispec__.update(load_operations_from_docstring(content))

        return func

    return wrapper
