"""Bootstrap for the Quant Research Platform."""

from __future__ import annotations

from .component_registry import ComponentRegistry
from .configuration import Configuration
from .runtime import Runtime


class Bootstrap:
    """Compose the runtime and its dependencies."""

    def build(
        self,
        config: Configuration | None = None,
    ) -> Runtime:
        """Build a configured runtime."""

        configuration = config or Configuration()
        registry = ComponentRegistry()

        return Runtime(
            configuration=configuration,
            registry=registry,
        )
