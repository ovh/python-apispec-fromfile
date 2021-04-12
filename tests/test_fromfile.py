""" Test for apispec_fromfile """

from apispec import APISpec
from apispec.exceptions import APISpecError
from apispec.yaml_utils import load_operations_from_docstring
import pytest

from apispec_fromfile import FromFilePlugin
from apispec_fromfile import from_file


def test_from_file_decorator(tmp_path):
    """ Test the from_file decorator. """
    # create a temp yaml file
    yaml_content = """
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
    """
    yaml_file = tmp_path / "hello.yml"
    yaml_file.write_text(yaml_content)

    # decorate a function with the from_file decorator
    @from_file(str(yaml_file))
    def hello():
        return {"hello"}

    assert load_operations_from_docstring(yaml_content) == hello.__apispec__


def test_plugin():
    """ Test the FromFilePlugin class. """
    # init the spec
    spec = APISpec(
        title="Petstore",
        version="1.0.0",
        openapi_version="3.0.3",
        plugins=[FromFilePlugin("func")],
    )

    # define a path
    def hello():
        return "hello"

    hello.__apispec__ = {"get": {}}

    # add a path
    spec.path("/hello", func=hello)

    # get paths
    paths = spec.to_dict()["paths"]
    hello_path = paths["/hello"]

    assert hello.__apispec__ == hello_path


def test_readme()
    """ Test the code in the readme file """
    # Create an APISpec
    spec = APISpec(
        title="Swagger Petstore",
        version="1.0.0",
        openapi_version="3.0.3",
        plugins=[FromFilePlugin("resource")],
    )

    # Create an endpoint
    @from_file("my-spec-file.yml")
    def hello():
        return {"hello"}

    # Register entities and paths
    with pytest.raises(APISpecError):
        spec.path(resource=hello)
    # use the right syntax, available for all framework
    spec.path("/hello", resource=hello)
