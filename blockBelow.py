from mcpi.minecraft import Minecraft
mc = Minecraft.creat()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
blockType = 10
mc.setBlock(x, y, z, blockType) 
