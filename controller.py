from deepdiff import DeepDiff

def equals(shoe1, shoe2):
  diff = DeepDiff(shoe1, shoe2)
  # print(diff)
  if diff=={}:
    return True
  else: 
    return False