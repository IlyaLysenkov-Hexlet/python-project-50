import os.path
__all__ = ["build_fixture_path"]
current_dir = os.path.dirname(os.path.abspath(__file__))
FIXTURES_PATH = os.path.join(current_dir, "fixtures")


def build_fixture_path(file, path=FIXTURES_PATH):
    return os.path.join(path, file)
