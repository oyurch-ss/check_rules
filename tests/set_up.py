class User:
    def __init__(self, rules):
        self.rules = rules

no_rights_only = [
    'no_rights',
]

all_rights = [
    'no_rights',
    'request_to_blacklist',
    'root',
    'change_driver_rate',
    'blacklist',
    'sec',
    'set_card',
    'cash_update',
]

all_rights_without_set_card = [
    'no_rights',
    'request_to_blacklist',
    'root',
    'change_driver_rate',
    'blacklist',
    'sec',
    'cash_update',
]

all_rights_without_cash_update = [
    'no_rights',
    'request_to_blacklist',
    'root',
    'change_driver_rate',
    'blacklist',
    'sec',
    'set_card',
]

root_rights_only = [
    'root',
]

not_valid_rights = [
    'some_not_valid_rights',
]

one_not_valid_rights = [
    'request_to_blacklist',
    'some_not_valid_rights',
    'change_driver_rate',
]
