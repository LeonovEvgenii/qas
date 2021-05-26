from random import choice
# import experta
from pyknow import *


class Light(Fact):

    a = 0

    @classmethod
    def m(self):
        print("hello world!")
        return 2


class RobotCrossStreet(KnowledgeEngine):
    #@DefFacts()
    #def light_def(self):
        # yield Light(color='green')
        # yield Light(color='red') 
        # yield Light(color='black')            
        # yield AS.light << Light(color=L('yellow') | L('blinking-yellow'))


    @Rule(Light(color='black'))
    def green_black(self):
        print("bl")

    @Rule(Light(color='green'))
    def green_light(self):
        print("Walk")

    @Rule(Light(color='red'))
    def red_light(self):
        print("Don't walk")

    @Rule(AS.light << Light(color=L('yellow') | L('blinking-yellow')))
    def cautious(self, light):
        print("Be cautious because light is", light["color"])


engine = RobotCrossStreet()
# engine.reset()
# engine.declare(Light(color=choice(['green', 'yellow', 'blinking-yellow', 'red'])))
# engine.run()



while 1:
    c = input("введи цвет: ")
    obj = Light(color=c)
    engine.reset()
    engine.declare(obj)
    print(engine.facts)
    print("----")
    engine.run()
    print(engine.facts)
    print("++++")
    
