def volume(lenght:float, width:float, height:float):return (lenght * width * height / 3)
def printVolumePyramidScientific(volume:float, unit:str):
print(f"The volume of a pyramid in scientific notationis: {volume:.2e} {unit}.")
def printVolumeSimple(volume:float,unit:str):
print(f"The volume is{round(volume, 3)} {unit}.")
print("\nCalculating varius volumes:\n")
printVolumePyramidScientific(volume) 
printVolumePyramidScientific(volume)
printVolumePyramidScientific(volume)
printVolumePyramidScientific(volume)