
with open("states.csv", "r") as states_file:
    states = states_file.read().split('\n')

print '<select>'

for state in states:
    abbr_and_name = state.split(",")
    print "\t<option value='{0}'>{1}</option>".format(
        abbr_and_name[0], abbr_and_name[1])

print "</select>"

print states
