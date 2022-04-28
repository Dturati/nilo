""" Online Python - IDE, Editor, Compiler, Interpreter
 Consider a denormalized database structure that stores location in the form 'city | state | country'.
 Create a function that validates the integrity, assuring a city belongs to a single state, and a state belongs to a single country
"""

class ValidIntegrid:

    def __init__(self, entries: list):
        self._entries = entries
        self._data_norm = {}
        self._invalid = []

    def _norm_coutry(self, value):
        if value[2] not in self._data_norm:
            self._data_norm[value[2]] = {}

    def _norm_state(self, value):
        if value[1] not in self._data_norm[value[2]]:
            self._data_norm[value[2]][value[1]] = []

    def _norm_city(self, value):
        if value[0] not in self._data_norm[value[2]][value[1]]:
            self._data_norm[value[2]][value[1]].append(value[0])

    def _verify_state(self, value) -> bool:
        for ver in self._data_norm:
            if value[2] not in ver:
                if value[1] in self._data_norm[ver]:
                    return False
        return True

    def _verify_city(self, value):
        for coutry in self._data_norm:
            if value[2] not in coutry:
                if value[1] not in self._data_norm[coutry]:
                    for res in self._data_norm[coutry]:
                        if value[0] in self._data_norm[coutry][res]:
                            return False
        return True

    def create_dict_data(self) -> None:
        for value in self._entries:
            if not self._verify_state(value):
                self._invalid.append(value)
            if not self._verify_city(value):
                self._invalid.append(value)
            self._norm_coutry(value)
            self._norm_state(value)
            self._norm_city(value)

    def get_entries(self) -> list:
        return self._entries

    def get_valid(self) -> dict:
        return self._data_norm

    def get_invalid(self) -> list:
        return self._invalid