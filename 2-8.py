from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()

userName = input("請輸入姓名: ")
message = input("請輸入發言: ")
cherinehsu.postToChat(" <"+userName + "> " + message)