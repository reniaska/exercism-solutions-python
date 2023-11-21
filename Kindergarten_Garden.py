# https://exercism.org/tracks/python/exercises/kindergarten-garden

CHILDREN = ('Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
                    'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry')

PLANTS = {'C': 'Clover',
          'G': 'Grass',
          'R': 'Radishes',
          'V': 'Violets'}


class Garden:
    def __init__(self, diagram, students=CHILDREN):
        self.diagram = diagram.split('\n')
        self.students = sorted(students)

    def plants(self, name):
        idx = self.students.index(name) * 2
        return [PLANTS[self.diagram[row][cup]] for row in [0, 1] for cup in (idx, idx + 1)]
