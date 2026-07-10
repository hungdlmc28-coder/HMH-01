from qrp.foundation import BaseComponent
from qrp.plugins import Plugin
from qrp.runtime import ComponentRegistry


def test_plugin_is_base_component() -> None:
    plugin = Plugin()

    assert isinstance(plugin, BaseComponent)


def test_plugin_lifecycle() -> None:
    plugin = Plugin()

    assert plugin.is_initialized is False

    plugin.initialize()

    assert plugin.is_initialized is True

    plugin.shutdown()

    assert plugin.is_initialized is False


def test_plugin_can_be_registered() -> None:
    registry = ComponentRegistry()
    plugin = Plugin("sample")

    registry.register(plugin)

    assert registry.get("sample") is plugin
