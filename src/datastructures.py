class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "Tommy",
                "age": 34,
                "lucky_numbers": [7, 13, 21],
                "last_name": self.last_name
            },
            {
                "id": self._generate_id(),
                "first_name": "Jessica",
                "age": 30,
                "lucky_numbers": [3, 9, 12],
                "last_name": self.last_name
            },
            {
                "id": self._generate_id(),
                "first_name": "Jake",
                "age": 28,
                "lucky_numbers": [5, 8, 18],
                "last_name": self.last_name
            }
        ]

    def _generate_id(self):
        current_id = self._next_id
        self._next_id += 1
        return current_id

    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generate_id()
        if "last_name" not in member:
            member["last_name"] = self.last_name
        self._members.append(member)

    def delete_member(self, id):
        self._members = [m for m in self._members if m["id"] != id]

    def update_member(self, id, updated_data):
        for member in self._members:
            if member["id"] == id:
                member.update(updated_data)
                return member
        return None

    def get_member(self, id):
        return next((m for m in self._members if m["id"] == id), None)

    def get_all_members(self):
        return self._members
