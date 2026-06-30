print ("You wake up in a dark room with torches on the walls, there is a door across from you and a chest next to you. What do you do? A: Open the door and leave; B: Open the chest")
action0 = input("Choose your action: ")

if action0 == 'A': 
 print (" A swarm of bats attacked you and you died")
if action0 == 'B':
 print ("Inside you find an old rusty sword, its not much, but it will do")
 action1 = input("Press A to advance")

if action1 == "A" :
 print ("You enter a wide corridor, lined with empty ancient suits of armor. Torches are few and far between, so most arreas are plunged in darkness. Suddenly, you notice a huge swarm of bats fly your way, what do you do? A: Hold your sword high and charge at the blood thirsty brutes! B: hide in the corner and hope that they don't notice you. C: Jump into an old suit of armor and hide in there.")
 action2 = input("Choose your action: ")

if action2 == "A" :
 print ("Good news, you killed half of the flock. Bad news, now the other half is out for revenge and your sword is damaged. How do you save yourself? A: Attack them with the remains of your sword. B: Grab a flaming torch from the wall and attack them with that")
 action2a = input("Choose your action: ") 
 if action2a == "A" :
  print ("Your sword broke and the bats killed you, sucks to be you, I guess.")
 if action2a == "B" :
  print ("Congradulations, you made fried bat! It smells unapetising but you are hungry and your enemies are now about as dangerous as well.. a piece of fried bat. Unfortunately, your sword broke while you tried to use it to fillet the pieces. What do you do now? A: Leave the fried bats and the sword behind B: Take them with you")
  action2b = input("Choose your action: ")

if action2 == "B" :
 print ("The bats DID notice you and killed you.")

if action2 == "C" :
  print("Woops, the bats notice you and before you put the helmet back on, they fly inside the suit of armor and eat the flesh from the bones")
  

if action2b == "A":
  print("The smell of roast bat lured dungeon rats to you and they ate you")

if action2b == "A":
      print("You continue on down the corridor, it starts to get gradually wider untill you reach what looks like an old fortress. The gate is open and the walls are crumbling. The ground before it is littered with rubble. A horrid stench of burning flesh radiates from the inside. You want to see what's going on but you are interested in looking for anything else in the rubble. What do you do? A: You try to sneak in to the fortress. B:You look around on the ground.")
      action3 = input("Choose your action: ")
      if action3 == "A":
        print("Haven't you learned already! Don't rush into battle without preparation. Anyway, you're dead")
      if action3 == "B":
        print ("You search around and you find a few weapons on the ground. Unfortunately , you can only carry one. Choose the weapon for you final fight! A: The Golden Sword of Grandeur: It is a stunning claymore that shines brghtly. It's a weapon destined for a trully great hero. It's made of solid gold. B:The Silver Sword of Frost: At firsrt glance it looks fully silver. However, after you look at it deeper you see that it's not actually silver, just polished well. It feels very cold when you touch it. C: The Obsidian Blade of Darkness: It's as black as a piece of the night sky on a moonless night. It buzzes with with an od denergy that you can't quite describe. ")
        action4 = input("Choose your action: ")

if action4 == "A":
  print("You creep past the smoudering ruins into what once had been the throne room. You are so captivated by the remnants of a tapestry on the wall, that you don't notice the dragon that is now blocking the entry with it's massive body until too late. What do you do? A: Charge at him with your sword B: Hide behind the tapestry") 
  action5a = input("Choose your action:")
  if action5a == "A":
     print("Your sword melted and you died, didn't you know not to charge at a fire breathing beast with a golden sword")
  if action5a == "B":
     print("The dragon burns you alive")
  if action5a == "C":
     print("The dragon burns you alive")

if action4 == "B":
  print("You creep past the smoudering ruins inntovwhat once had been the throne room. You are so captivated by the remnants of a tapestry on the wall, that you don't notice the dragon that is now blocking the entry with it's massive body until too late. What do you do? A: Charge at him with your sword B: Hide behind the tapestry") 
  action5b = input("Choose your action:")
  if action5b == "A":
   print("The moment your sword enters the dragon's body, it turns black and start smoking. The moment the draggon takes it's last breath, you stare in wonder, as your sword starts transforming into silver")
   action6 = input("press A to advance:")

if action4 == "C":
  print("You creep past the smoudering ruins inntovwhat once had been the throne room. You are so captivated by the remnants of a tapestry on the wall, that you don't notice the dragon that is now blocking the entry with it's massive body until too late. What do you do? A: Charge at him with your sword B: Hide behind the tapestry") 
  action5b = input("Choose your action:")
  if action5b == "A":
    print("The moment the sword senses the enemy is near, it starts growing hotter and hotter. Your vision grows dark and you struggle to stay standing. By the time the dragon's fire reaches you, you are greatful, for your prayer for death has been answered")
  if action5b == "B":
    print("The dragon burns you alive")

if action6 == "A":
  print("You wander around the room, until you stumble upon a chest. Do you open it? A: Yes B: No")
  action7 = input("Choose your action")

if action7 == "A":
  print("Inside the chest, you find a dwarf that introduces himself as Hypnos, the king of the West Corridors. He leads you to a distant underground township, where his friends and subjects through a banket in your favour. You are offered a cup of a strange poppy-red drink, do you drink it. A: Yes B: No")
  action8 = input("Choose your action:")
  if action8 =="A":
    print("Your head goes woozy and your vision blurs. You slowly sink deeper and deeper into soft slumber, until finally you wake up in a room with torches on the walls...")
  if action8 =="B":
    print("You will spend the rest of your life, wondering what might have happened...")

if action7 =="B":
    print("You will spend the rest of your life, wondering what might have happened...")



  
