"""CertViewer: Inspects TLS certificate details and expiration dates from a host."""

__version__ = "1.0.0"

from .core import run
from .cli import main

__all__ = ["main", "run", "__version__"]