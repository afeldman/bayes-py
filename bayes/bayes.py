import json
import math
import re

class Bayes(object):
    def __init__(self):
        self.classes = {}
        self.priors  = {}



class BayesText(Bayes):
    def __init__(self):
        super().__init__() 
        self.vocabulary = {}

        
    def train(self, classes):
        for klass in classes:
            self.classes.setdefault(klass,{})
            self.priors.setdefault(klass, 0)

            for document in classes[klass]:
                self.priors[klass] += 1
                for item in document:
                    self.vocabulary.setdefault(item, 0)
                    self.vocabulary[item] += 1
                    self.classes[klass].setdefault(item, 0)
                    self.classes[klass][item] += 1

                    
            
