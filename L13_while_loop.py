count = 1
while count < 5:  # condition to check if the loop should continue
    print(count)  # body of the loop, will execute as long as the condition is true
    count += 1  # this is same as writing count = count + 1

count = 1
while count <= 5:  # condition to check if the loop should continue
    print(count)  # body of the loop, will execute as long as the condition is true
    count += 1  # this is same as writing count = count + 1

# be careful to avoid infinite loops where the while condition never comes true and
# the while loop will continue to run for ever. It is important to check and avoid infinite loop situations
