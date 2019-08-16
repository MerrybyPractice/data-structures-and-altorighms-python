import pytest
from data_structures.hashtable.hashtable import Hashtable

def test_hashtable(): 

  assert Hashtable() 


def test_add(): 

  Ĥ = Hashtable()

  Ĥ.add("hash", "table")

  assert Ĥ.get("hash") == "table"


def test_get(): 

  Ĥ = Hashtable()
  
  assert  Ĥ.get("hash") == None


def test_contains(): 

  Ĥ = Hashtable()

  Ĥ.add("hash", "table")

  assert Ĥ.contains("hash") == True


def test_hash(): 

  Ĥ = Hashtable()
  
  assert Ĥ.hash("hash") == Ĥ.hash("hash") 
