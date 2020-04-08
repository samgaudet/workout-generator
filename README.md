# workout-generator

Messing around with ben's idea for an automated workout randomizer.

## Example

Here is a simple example using the example JSON in this repo.

```python
from workout import Workout

myWorkout = Workout("excercises_example.json")
myWorkout.main()
```

Output:

```
Bicep Curls: 5 Sets
Calf Raises: 128 Reps
Leg Lifts: 111 Reps
Dips: 101 Reps
```
