"""Simple Nornir Example"""
try:
    from importlib.metadata import version, PackageNotFoundError  # type: ignore
except ImportError:
    from importlib_metadata import version, PackageNotFoundError  # type: ignore


try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "unknown"
