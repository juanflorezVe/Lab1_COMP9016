
import sys
sys.path.append('../../')
from agents import *
from notebook import *



class Mario(Agent):
    def jump(self, thing):
        print("Mario rides Yoshi at {}.".format(self.location))
            
    def collect(self, thing):
        if not isinstance(thing, Coin):
            print("no coin here")
            print(Coin)
            return False
        
        print("Mario collected a coin at {}.".format(self.location))
    
    def rescue(self, thing):
        print("Mario restcued the princess at {}.".format(self.location))
        
    def move_right(self):
        print("Mario moved right from {}".format(self.location))
        self.location += 1
    
    def move_left(self):
        self.location -= 1


class Coin(Thing):
    pass

class Princess(Thing):
    pass

class Yoshi(Thing):
    pass

class Castle(Environment):
    
    def percept(self, agent):
        """ list of things at the agent location """
        return self.list_things_at(agent.location)[1:]
    
    def execute_action(self, agent, action):
        """ move right 
            move left
            jump
            collect
            rescue
        """
        
        if action == "move right":
            agent.move_right()
            return True
        elif action == "collect":
            coin = self.percept(agent)[0]
            print(coin)
            agent.collect(coin)
            self.delete_thing(coin)
            return True
        elif action == "jump":
            yoshi = self.percept(agent)[0]
            print(yoshi)
            agent.jump(yoshi)
            self.delete_thing(yoshi)
            return True
        elif action == "rescue":
            princess = self.percept(agent)[0]
            print(princess)
            agent.rescue(princess)
            self.delete_thing(princess)
            return True
        
        print("an action needs to be implemented for " + action)
        return False
    
        
        
    def is_done(self):
        """ It is done when there are no princesses in the castle """
        if not princess in self.things:
            return True
        return False

    
def program(percepts):
    """ things that the agent of this program can do """
    for t in percepts:
        if isinstance(t, Coin):
            return 'collect'
        elif isinstance(t, Yoshi):
            return 'jump'
        elif isinstance(t, Princess):
            return 'rescue'
    return "move right"




castle = Castle()
mario = Mario(program)
coin1 = Coin()
coin2 = Coin()
yoshi = Yoshi()
princess = Princess()


castle.add_thing(mario, 1)
castle.add_thing(coin1, 5)
castle.add_thing(coin2, 10)
castle.add_thing(yoshi, 15)
castle.add_thing(princess, 20)
castle.run(7)



