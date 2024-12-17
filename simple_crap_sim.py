"""
Make the simple carp sim and trace the results 
"""

import random 

def roll_dice():
	"""
	The function to roll the dice 
	"""
	return random.randint(1, 6)


class Game:

	def __init__(self):
		
		self.point = None
		self.total = None
	

	def two_dice_roll(self):
		""" 
		Give the two dice roll
		"""
		
		first_dice = roll_dice()
		second_dice = roll_dice()

		return (first_dice,second_dice)



	def come_out_game_rules(self,two_dice_roll, active = True):
		"""
		The method to put the game rules 
		"""
		
		#make the sum of dice roll
		sum_dice_roll = sum(two_dice_roll)

		if active : 

			if sum_dice_roll in (7,11):
				return "Won"
			
			elif sum_dice_roll in (2,3,12):
				return "Lose"

			else:
				self.point = sum_dice_roll
			
		else:

			if sum_dice_roll in (2,3) :

				return "Won"

			elif sum_dice_roll in (7,11):

				return "Lose"

			elif sum_dice_roll == 12 :

				return "Push"
				
			else:

				self.point = sum_dice_roll



	def point_game(self,two_dice_roll):
		"""
		The function to make the point game rule
		"""

		dice_roll_sum = sum(two_dice_roll)

		print(dice_roll_sum)

		#make the point matching 

		if dice_roll_sum == self.point:
			return "You Win"
		
		elif dice_roll_sum == 7 :
			return "You Lose"




	def play_craps(self):
			"""
			Start the game and run the rules.
			"""
			# Start the game with the come-out roll

			#make the bet in don't pass line or pass line 
			active_bet = False

			come_out = self.two_dice_roll()
			print(f"Come-Out Roll: {come_out} (Total: {sum(come_out)})")

			# Apply come-out game rules
			result = self.come_out_game_rules(come_out, active_bet)

			if result:

				print("You ", result)

				#Win or loss case 
				if "Won" in result or "Lose" in result: 
					return "Game Over on the Come-Out Roll!"
				
				if "Pass" in result : 
					print("Game gets in the Pass")


			# If a point is established
			print(f"The Point is set to {self.point}")

			# Continue with the point game
			while True:
				roll = self.two_dice_roll()
				print(f"Rolling Dice: {roll} (Total: {sum(roll)})")
				
				result = self.point_game(roll)
				if result == "You Win":
					return "Game Over: You Hit the Point and Won!"
				elif result == "You Lose":
					return "Game Over: You Rolled a 7 and Lost!"



if __name__ == "__main__":

	game = Game()
	print(game.play_craps())




			

