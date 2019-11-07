def scratch_sqrt(num):
  a = 0  # Base of the exponent
  expo_guess = []  # This will hold exponential guesses
  limit_counter = 3  # Counter for loop stop
  while(True):
    # This will square the base and add answer to a list
    b = a**2
    expo_guess.append(b)

    # This will check if the answer is bigger than the original
    # number, and if so it will start a counter from 3 which breaks
    # the loop.
    if b > num:
      limit_counter -= 1
      if limit_counter <= 0:
        break

    a += 1  # Add one to the base

  amount_away = []  # This will store the amount the number is from the number its rooting
  # This makes a list of how close the exponents are to the actual number
  for element in expo_guess:
    if element >= num:
      amount_away.append(element - num)
    else:
      amount_away.append(num - element)

  # What all this does is it applies the Babylonian equation of
  # finding square roots an returns the completed square root
  closest_exponent = amount_away.index(min(amount_away))
  for i in range(4):
    answer = (closest_exponent + (num/closest_exponent)) / 2
    closest_exponent = answer

  return closest_exponent