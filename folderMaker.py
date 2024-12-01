import os
# pinnacle of laziness
for day in range(1, 26):
    dayFolder = f"day{day}"
    os.makedirs(os.path.join(dayFolder, "puzzle1"), exist_ok=True)
    os.makedirs(os.path.join(dayFolder, "puzzle2"), exist_ok=True)
    open(os.path.join(dayFolder, "puzzle1", "puzzle1.py"), 'a').close()
    open(os.path.join(dayFolder, "puzzle2", "puzzle2.py"), 'a').close()