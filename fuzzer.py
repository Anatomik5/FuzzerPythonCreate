import random
enum = ["int_arr"]
class MyFuzzer:
    def __init__(self,seed,str):
        if str in enum:
            self.mutator = MyMutator_arr_int(seed)
        else:
            raise Exception("Sorry, this type is not ")         
class MyMutator_arr_int:
    def __init__(self,seed):
        random.seed(seed)
    def mutate(self):
        arr_len=random.randint(1, 100)
        arr = [random.randint(0, 100) for _ in range(arr_len)]
        return arr