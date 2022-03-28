import unittest
from traverse import Path


# Checkign if BFS works
test = {"a" : ["b","c"], "b" : [], "c" : ["d","e"], "d" : [], "e" : []}
expected = ["a","b","c","d","e"]
result = Path.BFS(test,"a")
if result != expected:
    print(f"BFS test failed; Path.BFS() \nExpected : {expected}\nGot : {result} ")


