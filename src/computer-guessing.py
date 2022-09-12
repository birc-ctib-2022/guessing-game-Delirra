# The following code is just to setup the exercise. You do not need to
# understand but can jump to the game below.


def input_selection(prompt: str, options: list[str]) -> str:
    """Get user input, restrict it to fixed options."""
    modified_prompt = "{} [{}]: ".format(
        prompt.strip(), ", ".join(options)
    )
    while True:
        inp = input(modified_prompt)
        if inp in options:
            return inp
        # nope, not a valid answer...
        print("Invalid choice! Must be in [{}]".format(
            ", ".join(options)
        ))


print("Please thing of a number from 1 to 20, both included.")
print("Let me know how good my guess is.\n")

# Here, we implement the computer's strategy for guessing
# the number you are thinking of. Don't lie to the
# computer. It won't punish you, but it will frown upon it.

# Guessing low to high
# for guess in range(1, 21):
#     result = input_selection(
#         "I'm guessing {}\nHow is my guess?".format(guess),
#         ["low", "hit", "high"]
#     )
#     if result == "hit":
#         print("Wuhuu!")
#         break

#     print("I must have been too low, right?", result)


# Guessing high to low
# for guess in range(20, 0, -1):
#     result = input_selection(
#         "I'm guessing {}\nHow is my guess?".format(guess),
#         ["low", "hit", "high"]
#     )
#     if result == "hit":
#         print("Wuhuu!")
#         break

#     print("I must have been too high, right?", result)

# Guessing midpoint of intervals

interval_low, interval_high = 0, 20
guess = (interval_low + interval_high) // 2

while True:
    result = input_selection(
        "I'm guessing {}\nHow is my guess?".format(guess),
        ["low", "hit", "high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break
    elif result == "low":
        print("I must have been too low, right?", result)
        interval_low = guess
        guess = (interval_low + interval_high) // 2
        continue
    elif result == "high":
        print("I must have been too high, right?", result)
        interval_high = guess
        guess = (interval_low + interval_high) // 2
        continue

