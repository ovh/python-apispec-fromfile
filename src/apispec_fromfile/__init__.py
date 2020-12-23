import pkg_resources

from .plugin import FromFilePlugin
from .plugin import from_file


__version__ = str(
    pkg_resources.get_distribution("apispec-fromfile").parsed_version
)

__all__ = [
    "FromFilePlugin",
    "from_file",
]
