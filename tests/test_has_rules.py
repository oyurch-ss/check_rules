from rules import has_rules, rules_array
from .set_up import (
    User, not_valid_rights, no_rights_only, one_not_valid_rights,
    all_rights, all_rights_without_cash_update, all_rights_without_set_card,
    root_rights_only,
)

# has_rules
def test_no_rights_only():
    user = User(no_rights_only)
    assert has_rules(rules_array, user) == False

def test_not_valid_rights():
    user = User(not_valid_rights)
    assert has_rules(rules_array, user) == False

def test_one_not_valid_rights():
    user = User(one_not_valid_rights)
    assert has_rules(rules_array, user) == False

def test_all_rights():
    user = User(all_rights)
    assert has_rules(rules_array, user) == True

def test_root_rights_only():
    user = User(root_rights_only)
    assert has_rules(rules_array, user) == False

def test_root_rights_only_strictly_false():
    user = User(root_rights_only)
    assert has_rules(rules_array, user, strictly=False) == True

def test_all_rights_strictly_false():
    user = User(all_rights)
    assert has_rules(rules_array, user, strictly=False) == True

def test_all_rights_without_cash_update_strictly_false():
    user = User(all_rights_without_cash_update)
    assert has_rules(rules_array, user, strictly=False) == True

def test_all_rights_without_set_card_strictly_false():
    user = User(all_rights_without_set_card)
    assert has_rules(rules_array, user, strictly=False) == True
