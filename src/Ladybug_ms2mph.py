#C to F
# By Mostapha Sadeghipour Roudsari
# Sadeghipour@gmail.com
# Ladybug started by Mostapha Sadeghipour Roudsari is licensed
# under a Creative Commons Attribution-ShareAlike 3.0 Unported License.

"""
Convert from m/s to mile/h 
-
Provided by Ladybug 0.0.59
    
    Args:
        ms: Input wind speed in meters per second
    Returns:
        mph: Output wind speed in miles per hour
"""

ghenv.Component.Name = "Ladybug_ms2mph"
ghenv.Component.NickName = 'ms2mph'
ghenv.Component.Message = 'VER 0.0.59\nFEB_01_2015'
ghenv.Component.Category = "Ladybug"
ghenv.Component.SubCategory = "4 | Extra"
#compatibleLBVersion = VER 0.0.59\nFEB_01_2015
try: ghenv.Component.AdditionalHelpFromDocStrings = "0"
except: pass

def convertTomph(ms):
    return ms*2.23694
    
mph = []
for num in ms:
   if num == 'm/s': mph.append('mph')
   else:
       try: mph.append(convertTomph(num))
       except: mph.append(num)