from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()

x,y,z = cherinehsu.player.getTilePos()

answer = input('請問你右邊要放什麼方塊:')
cherinehsu.setBlocs(x+1,y,z,answer)