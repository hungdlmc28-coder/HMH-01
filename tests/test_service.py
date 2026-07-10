from qrp.foundation import BaseComponent
from qrp.runtime import ComponentRegistry
from qrp.services import Service


def test_service_is_base_component() -> None:
    service = Service()

    assert isinstance(service, BaseComponent)


def test_service_lifecycle() -> None:
    service = Service()

    assert service.is_initialized is False

    service.initialize()

    assert service.is_initialized is True

    service.shutdown()

    assert service.is_initialized is False


def test_service_can_be_registered() -> None:
    registry = ComponentRegistry()
    service = Service("sample")

    registry.register(service)

    assert registry.get("sample") is service
