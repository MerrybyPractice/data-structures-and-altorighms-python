from challanges.multi_bracket_validation.multi_bracket_validation import MultiBrackatValidation

def test_multi_bracket_validation(): 

  test = MultiBrackatValidation()

  actual = test.multi_bracket_validation("{}") 

  assert actual == True

def test_multi_bracket_validation_false(): 

  test = MultiBrackatValidation()

  actual = test.multi_bracket_validation("[[[[[[[")  

  assert actual == False