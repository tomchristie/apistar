import os
import tempfile

import pytest

from apistar import App, exceptions
from apistar.main import default_app, load_app


def test_load_app():
    with tempfile.TemporaryDirectory() as tempdir:
        os.chdir(tempdir)
        app = App()
        app.main(['new', '.', '--layout', 'minimal'], standalone_mode=False)
        loaded = load_app()
        assert isinstance(loaded, App)


def test_default_app():
    default = default_app()
    assert isinstance(default, App)


def test_load_misconfigured_app():
    with tempfile.TemporaryDirectory() as tempdir:
        os.chdir(tempdir)
        with open('app.py', 'w') as app_file:
            app_file.write('')
        with pytest.raises(exceptions.ConfigurationError):
            load_app()
