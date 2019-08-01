from challanges.multi_bracket_validation.multi_bracket_validation import MultiBrackatValidation
import pytest

@pytest.mark.skip('work on later')
def test_multi_bracket_validation(): 

  test = MultiBrackatValidation()

  actual = test.multi_bracket_validation("{}") 

  assert actual == True
@pytest.mark.skip('work on later')
def test_multi_bracket_validation_false(): 

  test = MultiBrackatValidation()

  actual = test.multi_bracket_validation("[[[[[[[")  

  assert actual == False