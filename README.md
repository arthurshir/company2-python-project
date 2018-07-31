# Company2 Coding Challenge
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
