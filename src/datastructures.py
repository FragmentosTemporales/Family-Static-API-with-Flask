from random import randint
import random

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []

    def _generateId(self):
        return random.randint(0, 99999999)

    def add_member(self, member):
        member["last_name"] = self.last_name
        member["id"] = self._generateId()
        self._members.append(member)

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)

    def update_member(self, id, member):
        for i in range(len(self._members)):
            if self._members[i]["id"] == id:
                member["id"] = id
                member["last_name"] = self.last_name
                self._members[i] = member

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        return self._members
