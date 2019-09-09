from django.db import models
from rubik_solver.Cubie import NaiveCube, Cube as FaceCube
from rubik_solver.Move import Move
from rubik_solver.utils import solve

import uuid

INITIAL_CUBE_STATE = "yyyyyyyyybbbbbbbbbrrrrrrrrrgggggggggooooooooowwwwwwwww"


class Rank(models.Model):
    username = models.CharField(max_length=255)
    time = models.DurationField()

    def __str__(self):
        return f'username: {self.username}, time: {self.time}'

    def __repr__(self):
        return self.__str__()

    def get_rank_position(self):
        return list(Rank.objects.all().order_by('time').values_list('id', flat=True)).index(self.id) + 1


class Cube(models.Model):
    key = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    positions = models.CharField(max_length=54, default=INITIAL_CUBE_STATE)

    def __str__(self):
        return self.positions

    def getNaiveCube(self):
        c = NaiveCube()
        c.set_cube(self.positions)
        return c

    def getFaceCube(self):
        c = self.getNaiveCube()
        fc = FaceCube()
        fc.from_naive_cube(c)
        return fc

    def execute_command(self, commands):
        c = self.getFaceCube()
        moves = [(Move(c) if c is not isinstance(c, Move) else c)
                 for c in commands]
        for m in moves:
            c.move(m)
        nc = c.to_naive_cube()
        self.positions = nc.get_cube()
        self.save()

    def get_solution(self):
        if self.getNaiveCube().is_solved():
            return []
        return solve(self.positions, "Kociemba")

    def get_solution_list(self):
        solution = self.get_solution()
        return [s.raw for s in solution]
