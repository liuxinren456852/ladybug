# By Chris Mackey
# Chris@MackeyArchitecture.com
# Ladybug started by Mostapha Sadeghipour Roudsari is licensed
# under a Creative Commons Attribution-ShareAlike 3.0 Unported License.

#Wh to BTU
"""
Use this component to convert energy values in BTU to Wh or BTU/ft2 to Wh/m2.
-
Provided by Ladybug 0.0.57
    
    Args:
        _Wh: An energy value or list of energy values in BTU or BTU/ft2.  Note that, for the component to recognize flux or floor normalization, the input must have a Ladybug header.
    Returns:
        BTU: The input enervy values converted to Wh.
"""

ghenv.Component.Name = "Ladybug_BTU2Wh"
ghenv.Component.NickName = 'BTU2Wh'
ghenv.Component.Message = 'VER 0.0.57\nJUL_29_2014'
ghenv.Component.Category = "Ladybug"
ghenv.Component.SubCategory = "4 | Extra"
try: ghenv.Component.AdditionalHelpFromDocStrings = "4"
except: pass

floorNorm = False
Wh = []
for num in _BTU:
    if num == 'BTU/ft2':
        Wh.append('Wh/m2')
        floorNorm = True
    elif num == 'BTU':
        Wh.append('Wh')
        floorNorm = False
    elif num == 'kBTU':
        Wh.append('kWh')
        floorNorm = False
    elif num == 'kBTU/ft2':
        Wh.append('kWh/m2')
        floorNorm = True
    else:
        if floorNorm == True:
            try: Wh.append(float(num)*0.316998331)
            except: Wh.append(num)
        else:
            try: Wh.append(float(num)*3.41214163)
            except: Wh.append(num)