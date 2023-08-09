fruits = {'fruit': 'apple', 'color': 'green'}

sorted_footballers_by_goals = sorted(
    fruits.items(), key=lambda x: x[1])
print(sorted_footballers_by_goals)
#print(footballers_goals.items())


