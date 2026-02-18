def safe_float(s):
  try:
   return float(s)
   
  except (ValueError, TypeError):
      return None
  

def clean_string(s):
    if not isinstance(s, str):
        return None
    return s.strip().lower()
  
test_inputs = [" 77 ", "3.44", "sun", "", " 99 "]

float_results = [safe_float(x) for x in test_inputs]
clean_results = [clean_string(x) for x in test_inputs]
float_results, clean_results



