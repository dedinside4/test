import random
def death_check():
  if health<=0:
    game_over=True
print('test')
health=100
mana=20
game_over=True
while game_over:
  health-=random.random()
  death_check()
print('game_over')
