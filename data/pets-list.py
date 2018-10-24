myPets = ['Zophie', 'Pooka', 'Fat-tail']
print ('Enter your pet\'s name: ')
name = input()
if name not in myPets:
    print ("You don't have such pet")
    print ("I am adding it")
    myPets.append(name)
    print(myPets)
               
else:
    print ("Your pet is " + name)
