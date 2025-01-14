from aiogram.dispatcher.filters.state import State, StatesGroup


class NewEventStates(StatesGroup):
    """Машина состояний нового события."""
    name = State()
    event_date = State()
    event_time = State()
    complexity = State()
    payment = State()
    comment = State()
    approve = State()
