"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {"id": 1, "first_name": "John", "age": 33, "lucky_numbers": [7, 13, 22]},
            {"id": 2, "first_name": "Jane", "age": 35, "lucky_numbers": [10, 14, 3]},
            {"id": 3, "first_name": "Jimmy", "age": 5, "lucky_numbers": [1]},
        ]

    def _generate_id(self):
        if not self._members:
            return 1
        return max(member["id"] for member in self._members) + 1

    def get_all_members(self):
        return self._members

    def get_member(self, member_id):
        for member in self._members:
            if member["id"] == member_id:
                return member
        return None

    def add_member(self, member):
        self._members.append(member)
        return member

    def delete_member(self, member_id):
        for i, member in enumerate(self._members):
            if member["id"] == member_id:
                del self._members[i]
                return True
        return False