import pytest

def fix_phone_num(phone_num_to_fix):
  # can only handle numbers that are exactly 10 digits long
  if (len(phone_num_to_fix) != 10):
    raise ValueError("Can only format numbers that are exactly 10 digits long")
