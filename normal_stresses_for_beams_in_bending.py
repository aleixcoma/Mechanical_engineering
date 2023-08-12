# Equations are based on the following assumptions:
import math

# 1. The beam is subjected to pure bending: shear force is zero, and no torsion or axial loads.
# 2. The material is isotropic and homogeneous.
# 3. The material obeys Hooke's law: elastic behavior.
# 4. The beam is initially straight with a cross section that is constant throughout its length.
# 5. The beam has an axis of symmetry in the plane of bending.
# 6. Beam proportions are such that it would fail by bending rather than crushing, wrinkling, or sidewise buckling.
# 7. Plane cross sections of the beam remain plane during bending.

#M = float(input("Enter bending moment[N·m]: "))
#y = float(input("Enter distance from the neutral axis[m]: "))
#I = float(input("Enter second-area moment about the z axis[m^4]: ")) # x axis is the neutral/centroidal axis. x-z is the neutral plane
#sigma_x = -M*y/I # Stress in the direction of the neutral axis. Can be either positive (tension) or negative (compression)
#print(sigma_x)

# Two plane bending stresses. Assume:

# 1. Cross sections with one or two planes of symmetry only

# Previously, determine maximum bending stresses (M_z & M_y), distances from the neutral axis (z & y)
# and second-area moments (I_z & I_y).

#M_z = float(input("Enter bending moment in the xy plane[lbf·in]: "))
#M_y = float(input("Enter bending moment in the xz plane[lbf·in]: "))
#z = float(input("Enter distance from the neutral axis in the xz plane[in]: "))
#y = float(input("Enter distance from the neutral axis in the xy plane[in]: "))
#I_z = float(input("Enter second-area moment around the z axis[in^4]: "))
#I_y = float(input("Enter second-area moment around the y axis[in^4]: "))
#sigma_x = -M_z*y/I_z + M_y*z/I_y
#print(sigma_x)

# Circular cross section:

M_z = float(input("Enter bending moment in the xy plane[lbf·in]: "))
M_y = float(input("Enter bending moment in the xz plane[lbf·in]: "))
d = float(input("Enter diameter of the circular cross section [in]: "))
sigma_m = 32/(math.pi*d**3)*math.sqrt(M_y**2+M_z**2)
print(sigma_m)
print('Hello world!')