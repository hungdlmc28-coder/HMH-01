"""Event bus for the Quant Research Platform."""

from __future__ import annotations

from collections.abc import Callable


class EventBus:
    """Simple synchronous event bus."""

    def __init__(self) -> None:
        self._listeners: dict[type, list[Callable[[object], None]]] = {}

    def subscribe(
        self,
        event_type: type,
        listener: Callable[[object], None],
    ) -> None:
        """Subscribe a listener to an event type."""
        listeners = self._listeners.setdefault(event_type, [])

        if listener not in listeners:
            listeners.append(listener)

    def unsubscribe(
        self,
        event_type: type,
        listener: Callable[[object], None],
    ) -> None:
        """Unsubscribe a listener from an event type."""
        listeners = self._listeners.get(event_type)

        if listeners is None:
            return

        if listener in listeners:
            listeners.remove(listener)

    def publish(self, event: object) -> None:
        """Publish an event to all subscribed listeners."""
        for listener in self._listeners.get(type(event), []):
            listener(event)
