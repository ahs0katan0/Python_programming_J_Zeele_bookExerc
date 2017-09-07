
import math

def calc_volume_surfacearea_from_radius (radius):
    volume = 4/3 * math.pi * radius**3
    surf_area = 4 * math.pi * radius**2
    print (volume, surf_area)
    return volume, surf_area
    
calc_volume_surfacearea_from_radius (4)
