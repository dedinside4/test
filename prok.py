import random
def death_check():
  global game_over
  if health<=0:
    game_over=True
print('test')
health=100
mana=20
game_over=False
while not game_over:
  health-=random.random()
  print(health)
  death_check()
print('game_over')
