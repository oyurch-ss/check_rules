def has_rules(rules, user, strictly=True):
    user_rules_set = set(user.rules)
    rules_set = set(rules)

    # user has some not valid rights
    if user_rules_set - rules_set:
        return False

    if strictly:
        # user has all rules
        return len(rules_set - user_rules_set) == 0

    # user has at least one rule
    return len(user_rules_set.intersection(rules_set)) > 0


def check_rules(rules, user, strictly=True):
    for item in user.rules:
        test = False
        test = test or item in rules_array
        if not test:
            return test

    if strictly:
        can = True
        for role in rules:
            can = can and role in user.rules
    else:
        can = False
        for role in rules:
            can = can or role in user.rules

    return can

rules_array = [
    'no_rights',
    'request_to_blacklist',
    'root',
    'change_driver_rate',
    'blacklist',
    'sec',
    'set_card',
    'cash_update',
]
