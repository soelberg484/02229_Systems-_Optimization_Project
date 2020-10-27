from ortools.sat.python import cp_model
import models

def main():
  p1 = models.Device("hey", "link")
  
  model = cp_model.CpModel()
  return p1.name

print(main())