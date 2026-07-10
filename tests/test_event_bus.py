from qrp.runtime import EventBus


class TestEvent:
    pass


def test_subscribe_and_publish() -> None:
    bus = EventBus()
    received: list[object] = []

    def listener(event: object) -> None:
        received.append(event)

    event = TestEvent()

    bus.subscribe(TestEvent, listener)
    bus.publish(event)

    assert received == [event]


def test_publish_without_listener() -> None:
    bus = EventBus()

    bus.publish(TestEvent())


def test_unsubscribe() -> None:
    bus = EventBus()
    received: list[object] = []

    def listener(event: object) -> None:
        received.append(event)

    bus.subscribe(TestEvent, listener)
    bus.unsubscribe(TestEvent, listener)

    bus.publish(TestEvent())

    assert received == []


def test_duplicate_subscribe_is_ignored() -> None:
    bus = EventBus()
    calls = 0

    def listener(event: object) -> None:
        nonlocal calls
        calls += 1

    bus.subscribe(TestEvent, listener)
    bus.subscribe(TestEvent, listener)

    bus.publish(TestEvent())

    assert calls == 1


def test_listener_order() -> None:
    bus = EventBus()
    order: list[str] = []

    def listener_a(event: object) -> None:
        order.append("A")

    def listener_b(event: object) -> None:
        order.append("B")

    def listener_c(event: object) -> None:
        order.append("C")

    bus.subscribe(TestEvent, listener_a)
    bus.subscribe(TestEvent, listener_b)
    bus.subscribe(TestEvent, listener_c)

    bus.publish(TestEvent())

    assert order == ["A", "B", "C"]
