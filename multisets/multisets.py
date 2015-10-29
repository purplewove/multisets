'''
Created on Oct 23, 2015

@author: templetonc
'''
class MultisetPermuter():
    def __init__(self):
        pass
    
    def permute(self, multiset):
        self.multiset = multiset
        self.dict = self.make_dictionary(self.multiset)
        self.keys = self.dict.keys()
        self.solution = []
        self.backtrack()
        
    def backtrack(self):
        if self.is_solution():
            self.process_solution()
        else:
            candidates = self.construct_candidates()
            for candidate in candidates:
                self.make_move(candidate)
                self.backtrack()
                self.unmake_move(candidate)
    
    def is_solution(self):
        if len(self.multiset) == len(self.solution):
            return True
        else:
            return False
        
    def process_solution(self):
        print (self.solution)
        
    def make_move(self, candidate):
        self.solution.append(candidate)
        self.dict[candidate] -= 1
        
    def unmake_move(self, candidate):
        self.solution.pop()
        self.dict[candidate] += 1
        
    def construct_candidates(self):
        candidates = [key for key in self.keys if self.dict[key] > 0]
        return candidates
    
    def make_dictionary(self, l):
        d = {}
        for item in l:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1 
        return d
    
    
if __name__ == '__main__':
    multiset_permuter = MultisetPermuter()
    multiset_permuter.permute([1, 1, 2, 2])
        