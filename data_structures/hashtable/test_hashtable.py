import pytest
from data_structures.hashtable.hashtable import Hashtable

def test_hashtable(): 

  assert Hashtable() 

def test_add_and_get(): 

  Ĥ = Hashtable()

  Ĥ.add("hash", "table")

  assert Ĥ.get("hash") == "table"

def test_add_and_get_two(): 

  Ĥ = Hashtable() 

  Ĥ.add("hash", "table") 
  Ĥ.add("table", "hash") 

  assert Ĥ.get("hash") == "table" 
  assert Ĥ.get("table") == "hash"

def test_get_none(): 

  Ĥ = Hashtable()
  
  assert  Ĥ.get("hash") == None

def test_contains(): 

  Ĥ = Hashtable()

  Ĥ.add("hash", "table")

  assert Ĥ.contains("hash") == True

def test_contains_many_on_end(): 

  Ĥ = Hashtable()

  Ĥ.add("hash", "table")
  Ĥ.add("table", "hash")
  Ĥ.add("linked", "list")

  assert Ĥ.contains("hash") == True

def test_contains_many_middle(): 

  Ĥ = Hashtable()

  Ĥ.add("hash", "table")
  Ĥ.add("table", "hash")
  Ĥ.add("linked", "list")

  assert Ĥ.contains("table") == True

def test_contains_many_first(): 

  Ĥ = Hashtable()

  Ĥ.add("hash", "table")
  Ĥ.add("table", "hash")
  Ĥ.add("linked", "list")

  assert Ĥ.contains("linked") == True

def test_hash(): 

  Ĥ = Hashtable()
  
  assert Ĥ.hash("hash") == Ĥ.hash("hash") 

def test_hash_different(): 

  Ĥ = Hashtable()

  assert not Ĥ.hash("hash") == Ĥ.hash("table")
