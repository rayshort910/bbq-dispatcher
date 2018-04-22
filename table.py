rounds = ['chicken', 'ribs', 'pork', 'brisket']

class Table:

    def __init__(self, id=1, limit=6):
        self.id = id
        self.limit = limit
        self.boxes = {
            'chicken': [],
            'ribs': [],
            'pork': [],
            'brisket': [],
        }

    def add_box(self, round, box):
        self.boxes[round].append(box)
    
    def has_box(self, box):
        return any(box in self.boxes[rnd] for rnd in rounds)

    def can_take(self, round, box):
        return not self.has_box(box) and self.limit > len(self.boxes[round])
