import pytest

def test_fix_phone_num():
  assert fix_phone_num("5125558823") == '(512) 555 8823'
  
  # Now check that a too short string gives a ValueError
  with pytest.raises(ValueError):
    fix_phone_num("51")
