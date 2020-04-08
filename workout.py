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
            workout = workouts[random.randint(0, len(workouts)-1)]
            self.workouts[workout_group] = workout

    def create_workout(self):

        self.routine = ""

        for workout_group in list(self.workouts.keys()):

            exercise = self.workouts[workout_group]
            exercise_name = self.exercises[workout_group][exercise]["name"]

            # if the exercise is not a rest day, get the number and units of the exercise
            if exercise != "rest_day":
                number_of_units = random.randint(
                    self.exercises[workout_group][exercise]["min"], self.exercises[workout_group][exercise]["max"])
                units = self.exercises[workout_group][exercise]["unit"]

            # otherwise the exercise is
            else:
                number_of_units = ""
                units = ""

            routine_string = f"{exercise_name}: {number_of_units} {units}\n"
            self.routine += routine_string

    def main(self):

        self.open_json_from_filepath()
        self.get_workout_groupings_from_json()
        self.choose_exercises()
        self.create_workout()
        print(self.routine)
