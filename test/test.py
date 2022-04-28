from main import ValidIntegrid

entries = [
    ["Rio Branco", "Acre", "Brasil"],
    ["Boa Vista", "Acre", "Brasil"],
    # ["Campinas", "Acre", "Canada"],  # invalid
    ["Maceio", "Alagoas", "Brasil"],
    ["Maceio", "Alagoas", "Brasil"],
    ["Toronto", "Ontario", "Canada"],
    # ["Toronto", "Distrito Federal", "Brasil"],  # invalid
]

entries1 = [
    ["Rio Branco", "Acre", "Brasil"],
    ["Boa Vista", "Acre", "Brasil"],
    ["Campinas", "Acre", "Canada"],  # invalid
    ["Maceio", "Alagoas", "Brasil"],
    ["Maceio", "Alagoas", "Brasil"],
    ["Toronto", "Ontario", "Canada"],
    # ["Toronto", "Distrito Federal", "Brasil"],  # invalid
]

entries2 = [
    ["Rio Branco", "Acre", "Brasil"],
    ["Boa Vista", "Acre", "Brasil"],
    # ["Campinas", "Acre", "Canada"],  # invalid
    ["Maceio", "Alagoas", "Brasil"],
    ["Maceio", "Alagoas", "Brasil"],
    ["Toronto", "Ontario", "Canada"],
    ["Toronto", "Distrito Federal", "Brasil"],  # invalid
]

entries3 = [
    ["Rio Branco", "Acre", "Brasil"],
    ["Boa Vista", "Acre", "Brasil"],
    # ["Campinas", "Acre", "Canada"],  # invalid
    ["Maceio", "Alagoas", "Brasil"],
    ["Toronto", "Ontario", "Canada"],
    ["Maceio", "Ontario", "Brasil"], # invalid
    # ["Toronto", "Distrito Federal", "Brasil"],  # invalid
]


invalid_one = [
    ["Campinas", "Acre", "Canada"]
]

invalid_two = [
    ["Toronto", "Distrito Federal", "Brasil"],
]

invalid_thre = [
    ["Maceio", "Ontario", "Brasil"],
]

def test_ok():
    valid = ValidIntegrid(entries)
    valid.create_dict_data()
    invalides = valid.get_invalid()
    assert len(invalides) == 0

def test_invalid_one():
    valid = ValidIntegrid(entries1)
    valid.create_dict_data()
    invalides = valid.get_invalid()
    assert invalides == invalid_one

def test_invalid_two():
    valid = ValidIntegrid(entries2)
    valid.create_dict_data()
    invalides = valid.get_invalid()
    assert invalides == invalid_two

def test_invalid_three():
    valid = ValidIntegrid(entries3)
    valid.create_dict_data()
    invalides = valid.get_invalid()
    assert invalides == invalid_thre