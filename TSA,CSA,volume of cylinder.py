import Cylindermodule as CM
h=float(input("Enter the Heigt of Cylinder:"))
r=float(input("Enter the Radius of Cylinder:"))
print("The CSA:",CM.CSA(h,r))
print("The TSA:",CM.TSA(h,r))
print("The Volume:",CM.VV(h,r))
