# mLab Coding Challenge
**Author**: Arthur Shir

**Development Duration**: 4:33PM - 6:39PM

## Problem Description

This is a simple JSON structure flattener. Performance of this flattener is O(num_keys*depth_of_values). Appropriate unit tests are also included.

## Requirements

Requires Python 3.0+. No other installation is needed.

## Run Commands

Run unit tests
```
  python json_project_unittests.py
```

Input JSON file by stdin
```
  cat example.json | python json_project.py
```

## Python Standard Libraries Used

- sys
- json
- unittest
- test.support.captured_stdout
- io.StringIO
- inspect.cleandoc

## Assumptions

* The input you receive will be a JSON object
* All keys name in the original object will be simple strings without ‘.’ characters
* The input JSON will not contain arrays
* You may use a library to parse JSON from a string to an object
* command line should correspond to linux conventions, eg using pipes `cat test.json | mycode` 