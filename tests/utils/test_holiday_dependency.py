import builtins

import pytest

from mootdx.exceptions import MootdxModuleNotFoundError


def test_holidays_missing_racer_dependency_message(monkeypatch):
    original_import = builtins.__import__

    def _fake_import(name, globals=None, locals=None, fromlist=(), level=0):
        if name == 'py_mini_racer':
            raise ImportError('mocked missing mini-racer')
        return original_import(name, globals, locals, fromlist, level)

    monkeypatch.setattr(builtins, '__import__', _fake_import)

    from mootdx.utils.holiday import holidays

    with pytest.raises(MootdxModuleNotFoundError) as exc:
        holidays()

    message = str(exc.value)
    assert 'mini-racer' in message
    assert 'py_mini_racer' in message