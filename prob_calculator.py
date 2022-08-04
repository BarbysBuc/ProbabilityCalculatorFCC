import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **balls):
    self.contents = []
    for key in balls:
      for item in range(balls[key]):
        self.contents.append(key)

  def draw(self, qballs):
    if qballs >= len(self.contents):
      return self.contents
    else:
      new_balls = []
      for i in range(qballs):
        ball = random.choice(self.contents)
        new_balls.append(ball)
        self.contents.remove(ball)
      return new_balls  

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  N = num_experiments
  M = N
  for i in range(N):
    hat_copy = copy.deepcopy(hat)
    chance = hat_copy.draw(num_balls_drawn)
    for item in expected_balls:
      if expected_balls[item] > chance.count(item):
        M -= 1
        break
  return  M / N