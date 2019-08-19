from challanges.repeated_word.repeated_word import repeated_word
import pytest

def test_repeated_word(): 

  assert repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...") == "it"

def test_repeated_word_none(): 

  assert repeated_word("a quick brown fox jumps over the lazy dog") == None

def test_repeated_word_all_same(): 

  assert repeated_word("a a a a a a a a a a a a ") == "a"

def test_repeated_word_not_in_dict(): 

  assert repeated_word("@#$%^&*()!:;<>,.?/--_=+|~`") == None