import sys, json, unittest;
from test.support import captured_stdin, captured_stdout
from io import StringIO

def flatten_json_from_stdin():
  input_dict = json.load(sys.stdin)
  output_dict = recursive_flatten(input_dict)
  print(json.dumps(output_dict, sort_keys=True, indent=4))

# Performance: O(num_keys*depth_of_values)
def recursive_flatten(input_dict):
  # Initialize output
  output_dict  = {}
  for key, value in input_dict.items():
    # If value is dict, recursively flatten on value.
    if isinstance(value, dict):
      for key2, value2 in recursive_flatten(value).items():
        output_dict["{}.{}".format(key, key2)] = value2
    else:
      output_dict[key] = value
  return output_dict

if __name__ == '__main__':
    flatten_json_from_stdin()
