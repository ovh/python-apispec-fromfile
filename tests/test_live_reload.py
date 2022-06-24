""" Test for apispec_fromfile """

from apispec import APISpec
from apispec.yaml_utils import load_operations_from_docstring

from apispec_fromfile import FromFilePlugin
from apispec_fromfile import from_file


def write_yaml_file(path, summary: str = 'Hello'):
    """
    Generate method spec with given summary and save in an external file
    """

    yaml_content = f"""
    ---
    get:
      summary: {summary}
      operationId: hello
      responses:
        '200':
          content:
            application/json:
              schema:
                type: string
    """
    yaml_file = path / "hello.yml"
    yaml_file.write_text(yaml_content)

    return yaml_file, yaml_content


def make_spec(func):
    """
    Create apispec object with default params for passed '/hello' method handler
    """

    spec = APISpec(
        title="Petstore",
        version="1.0.0",
        openapi_version="3.0.3",
        plugins=[FromFilePlugin("func")],
    )

    spec.path("/hello", func=func)

    return spec


def test_spec_is_not_updated_without_live_reload_flag(tmp_path):
    """
    Ensure that when external file changed,
    the method spec is not updated when not using live-reload flag
    """
    yaml_file, yaml_content = write_yaml_file(tmp_path)

    @from_file(str(yaml_file))
    def hello():
        return "hello"

    assert load_operations_from_docstring(yaml_content) == make_spec(hello).to_dict()['paths']['/hello']

    # update file contents
    yaml_file, yaml_content_updated = write_yaml_file(tmp_path, summary = 'Hello world')

    # check that yaml content has changed, but the method spec has not

    assert load_operations_from_docstring(yaml_content) != load_operations_from_docstring(yaml_content_updated)
    assert load_operations_from_docstring(yaml_content) == make_spec(hello).to_dict()['paths']['/hello']
    assert load_operations_from_docstring(yaml_content_updated) != make_spec(hello).to_dict()['paths']['/hello']


def test_spec_is_updated_with_live_reload_flag(tmp_path):
    """
    Ensure that when external file changed,
    the method spec is updated when using live-reload flag
    """

    yaml_file, yaml_content = write_yaml_file(tmp_path)

    @from_file(str(yaml_file), live_reload = True)
    def hello():
        return "hello"

    assert load_operations_from_docstring(yaml_content) == make_spec(hello).to_dict()['paths']['/hello']

    # update file contents
    yaml_file, yaml_content_updated = write_yaml_file(tmp_path, summary = 'Hello world')

    # check that yaml content has changed, and the method spec as well

    assert load_operations_from_docstring(yaml_content) != load_operations_from_docstring(yaml_content_updated)
    assert load_operations_from_docstring(yaml_content) != make_spec(hello).to_dict()['paths']['/hello']
    assert load_operations_from_docstring(yaml_content_updated) == make_spec(hello).to_dict()['paths']['/hello']
