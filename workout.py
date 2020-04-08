#!/usr/bin/env python3

import json
import random


class Workout:

    def __init__(self, exercises_filepath, seed=None):

        self.exercises_filepath = exercises_filepath

        # if a seed is provided, set the seed for random library
        if seed is not None:
            random.seed(seed)

    def open_json_from_filepath(self):

        with open(self.exercises_filepath, "r") as json_file:
            self.exercises = json.load(json_file)

    def get_workout_groupings_from_json(self):

        self.workout_groupings = list(self.exercises.keys())

    def choose_exercises(self):

        self.workouts = {}

        for workout_group in self.workout_groupings:
            workouts = list(self.exercises[workout_group].keys())
            workout = workouts[random.randint(0, len(workouts))]
            self.workouts[workout_group] = workout

    # def
