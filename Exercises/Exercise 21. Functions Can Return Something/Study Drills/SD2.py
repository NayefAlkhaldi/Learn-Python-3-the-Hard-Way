# Puzzle

# age = 35
# height = 74
# weight = 180
# iq = 50

  # what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
		# 	  ^ 35	 ^ subtract function: x-y
		# 	  				subtract(height,         multiply(weight, divide(iq, 2)))
		# 	  							^ height=74     ^ multiply function: y*x

		# 	  												multiply(weight,        divide(iq, 2))
		# 	  														  ^ weight=180	  ^ divide: x/y
		# 	  														  					so, divide is 25
		# 	  												  ^ multiply is 180 * 25: 4,500
		# 	  					^ subtract is 74 - 4,500: -4,426
		# 	  	^ add is 35 + -4,426: becomes 35 - 4,426 becuase it's negitive (an easier way to calculate numbers):-4,391
		# 	  																																																			^ assign a negitive sign.
# I think it's something called parse tree.
# The normal formula without functions is:
# what = age + ( height - ( weight * (iq / 2) ) )
# Read more about it: https://en.wikipedia.org/wiki/Parse_tree

# Done!