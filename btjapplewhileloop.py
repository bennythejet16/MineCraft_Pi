# CWC,Benjamin Kilgore,1/28/20
# Base project format.
# put this on the desktop : git clone https://github.com/tritechsc/mcpi
from mcpi.minecraft import Minecraft
#from time import sleep
import random
def init():
    mc = Minecraft.create("192.168.7.226", 4711)
    mc.setting("world_immutable",False)
    #x, y, z = mc.player.getPos()        
    return mc

def flowers(mc,x,y,z,total):
    done = 0
    while(done < total):
        h = random.randint(0,10)
        l = random.randint(0,10)
        mc.setBlock(x+h,y,z+l,37)
        mc.postToChat("FLOWERS EVERYWARE BTJ")
        done = done + 1



def matrixFront(mc,x,y,z):
    m = [[1,1,1,1,1,1,1,1,1,1],
       [0,1,1,1,1,1,1,1,1,1],
     [0,0,0,0,0,0,0,0,1,1],
     [1,1,1,1,1,1,1,0,0,1],
     [1,1,1,0,1,1,1,0,1,1],
     [1,1,1,0,1,1,1,0,0,1],
     [1,1,1,0,0,0,0,0,1,1],
     [1,1,1,1,1,1,1,0,0,1],
     [1,1,1,1,1,1,1,1,0,1],
     [1,1,1,1,1,1,1,1,1,1]]
    print(m)
    for k in range (0,12):
        for l  in range (0,12):
            print(m[k][l],end="")
            mc.setBlocks(x-1,y+k,z+l,x+1,y+k,z+l,m[k][l])
    print()


def btjapple(mc,x,y,z):
    m = [[15,15,15,15,15,5,5,15,15,15],
         [15,15,15,15,5,5,15,15,15,15],
         [15,15,15,15,5,5,15,15,15,15],
         [15,4,4,4,4,4,4,4,4,4],
         [4,4,4,4,4,4,4,4,4,4],
         [1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,15],
         [14,14,14,14,14,14,14,14,14,15],
         [14,14,14,14,14,14,14,14,14,14],
         [15,2,2,2,2,2,2,2,2,2],
         [15,15,2,2,2,2,2,2,2,15,],
         [15,15,15,3,3,15,3,3,15,15]]
    print(m)
    for h in range (0,12):
        for l  in range (0,10):
            print(m[h][l],end="")
            mc.setBlocks(x+h,y-1, z+l, x+h,y+1,z+l,35,m[h][l])
        print()

def main():
    mc = init()
    x,y,z = mc.player.getPos()
    #matrixTop(mc, x,y,z)
    flowers(mc,x,y,z,100)
    btjapple(mc,x,y,z)
    mc.player.setPos(x,y+20,z-10)

if __name__ == "__main__":
    main()

# multiple line comment
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
