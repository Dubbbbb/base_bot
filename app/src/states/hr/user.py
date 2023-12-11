from aiogram.fsm.state import State, StatesGroup

__all__ = [
    "UserManageStatesGroup",
]


class ApproveStatesGroup(StatesGroup):
    approve = State()


class UserDeleteStatesGroup(ApproveStatesGroup):
    ...


class UserCreateStatesGroup(ApproveStatesGroup):
    email = State()
    first_name = State()
    last_name = State()


class UserManageStatesGroup(StatesGroup):
    create = UserCreateStatesGroup
    delete = UserDeleteStatesGroup
