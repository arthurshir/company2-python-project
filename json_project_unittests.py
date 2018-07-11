import sys, unittest;
from test.support import captured_stdout
from io import StringIO
from json_project import flatten_json_from_stdin
from inspect import cleandoc

class TestProcessJsonMain(unittest.TestCase):
  def test_single_value_json(self):
    input_string =\
      '{\
          "a": 1\
      }'
    expected_output = cleandoc(\
      """
      {
          "a": 1
      }
      """) + "\n"

    sys.stdin = StringIO(input_string)
    with captured_stdout() as stdout:
        flatten_json_from_stdin()
    self.assertEqual(stdout.getvalue(), expected_output)

  def test_provided_example(self):
    input_string =\
      '{\
          "a": 1,\
          "b": true,\
          "c": {\
              "d": 3\
          }\
      }'
    expected_output = cleandoc(\
      """
      {
          "a": 1,
          "b": true,
          "c.d": 3
      }
      """) + "\n"

    sys.stdin = StringIO(input_string)
    with captured_stdout() as stdout:
        flatten_json_from_stdin()
    self.assertEqual(stdout.getvalue(), expected_output)

  def test_complex_input(self):
    input_string =\
      '{\
        "problems": {\
          "Diabetes": {\
            "medications": {\
              "medicationsClasses": {\
                "className": {\
                  "associatedDrug": {\
                    "name": "asprin",\
                    "dose": "",\
                    "strength": "500 mg"\
                  },\
                  "associatedDrug#2": {\
                    "name": "somethingElse",\
                    "dose": "",\
                    "strength": "500 mg"\
                  }\
                },\
                "className2": {\
                  "associatedDrug": {\
                    "name": "asprin",\
                    "dose": "",\
                    "strength": "500 mg"\
                  },\
                  "associatedDrug#2": {\
                    "name": "somethingElse",\
                    "dose": "",\
                    "strength": "500 mg"\
                  }\
                }\
              }\
            },\
            "labs": {\
              "missing_field": "missing_value"\
            }\
          },\
          "Asthma": [\
            1,\
            2,\
            3,\
            4,\
            5\
          ]\
        }\
      }'
    expected_output =cleandoc(\
      """{
          "problems.Asthma": [
              1,
              2,
              3,
              4,
              5
          ],
          "problems.Diabetes.labs.missing_field": "missing_value",
          "problems.Diabetes.medications.medicationsClasses.className.associatedDrug#2.dose": "",
          "problems.Diabetes.medications.medicationsClasses.className.associatedDrug#2.name": "somethingElse",
          "problems.Diabetes.medications.medicationsClasses.className.associatedDrug#2.strength": "500 mg",
          "problems.Diabetes.medications.medicationsClasses.className.associatedDrug.dose": "",
          "problems.Diabetes.medications.medicationsClasses.className.associatedDrug.name": "asprin",
          "problems.Diabetes.medications.medicationsClasses.className.associatedDrug.strength": "500 mg",
          "problems.Diabetes.medications.medicationsClasses.className2.associatedDrug#2.dose": "",
          "problems.Diabetes.medications.medicationsClasses.className2.associatedDrug#2.name": "somethingElse",
          "problems.Diabetes.medications.medicationsClasses.className2.associatedDrug#2.strength": "500 mg",
          "problems.Diabetes.medications.medicationsClasses.className2.associatedDrug.dose": "",
          "problems.Diabetes.medications.medicationsClasses.className2.associatedDrug.name": "asprin",
          "problems.Diabetes.medications.medicationsClasses.className2.associatedDrug.strength": "500 mg"
      }
      """) + "\n"
    sys.stdin = StringIO(input_string)
    with captured_stdout() as stdout:
        flatten_json_from_stdin()
    self.assertEqual(stdout.getvalue(), expected_output)


if __name__ == '__main__':
  unittest.main()
