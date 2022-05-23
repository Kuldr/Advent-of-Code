# ToDo
import pstats
from mainHelper import profilerPrintStats

profilerStats = pstats.Stats("profilerStats/profile.prof")

profilerPrintStats(profilerStats)