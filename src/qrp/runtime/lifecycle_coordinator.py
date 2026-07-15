from .lifecycle import LifecycleError, LifecycleState


class LifecycleCoordinator:
    """Coordinate lifecycle state transitions for registered components."""

    def __init__(self) -> None:
        self._states: dict[object, LifecycleState] = {}

    def register(self, component: object) -> None:
        """Register a component for lifecycle management."""

        if component in self._states:
            raise LifecycleError("Component is already registered.")

        self._states[component] = LifecycleState.CREATED

    def unregister(self, component: object) -> None:
        """Unregister a component from lifecycle management."""

        if component not in self._states:
            raise LifecycleError("Component is not registered.")

        if self._states[component] is LifecycleState.RUNNING:
            raise LifecycleError("Cannot unregister a running component.")

        del self._states[component]

    def initialize(self) -> None:
        """Initialize all registered components."""

        self._transition(
            LifecycleState.CREATED,
            LifecycleState.INITIALIZED,
        )

    def start(self) -> None:
        """Start all initialized components."""

        self._validate_transition(
            {
                LifecycleState.INITIALIZED,
                LifecycleState.RUNNING,
            }
        )

        self._transition(
            LifecycleState.INITIALIZED,
            LifecycleState.RUNNING,
        )

    def stop(self) -> None:
        """Stop all running components."""

        self._transition(
            LifecycleState.RUNNING,
            LifecycleState.STOPPED,
        )

    def state(self, component: object) -> LifecycleState:
        """Return the lifecycle state of a registered component."""

        if component not in self._states:
            raise LifecycleError("Component is not registered.")

        return self._states[component]

    def components(self) -> tuple[object, ...]:
        """Return all registered components."""

        return tuple(self._states.keys())

    def _validate_transition(
        self,
        allowed_states: set[LifecycleState],
    ) -> None:
        """Validate that all registered components may perform a transition."""

        invalid = [
            component
            for component, state in self._states.items()
            if state not in allowed_states
        ]
        if invalid:
            raise LifecycleError("Invalid lifecycle transition.")

    def _transition(
        self,
        source: LifecycleState,
        target: LifecycleState,
    ) -> None:
        """Transition eligible components to a new lifecycle state."""

        for component, state in self._states.items():
            if state is source:
                self._states[component] = target
