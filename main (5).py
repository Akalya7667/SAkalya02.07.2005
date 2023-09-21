'''Implement a class called player that represents a cricket player.The player class should have a
method called play() which print "The player is playing cricket. Derive two classes, Batsman and
Bowler from the player class.override the play() method in each derived class to print "The batsman
is batting "and "The bowler is bowling ",respertively.Write a program to creat objects of both the
Batsman and Bowler classes and call tha play() method for each object.'''


# Define the base class player 
class player: 
  def play (self):
    print ("The player is playing cricket.")

# Define the derived class Botsman
class Batsman (player):
  def play (self):
    print ("The batsman is batting.")

# Define the derived class Bowler
class Bowler (player):
  def play (self):
    print("The bowler is bowling.")

# creat objects of Batsman and Bowler classs
batsman = Batsman()
bowler = Bowler()

# call the play() method for each object
batsman.play()
bowler.play()

