import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_import_formaters_module_directly():
    import gendiff.formaters

def test_import_scripts_module_directly():
    import gendiff.scripts

