try:
    import __main__  # noqa pylint: disable=all
except ImportError:
    from src import __main__  # noqa
