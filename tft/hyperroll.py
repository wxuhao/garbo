from python_imagesearch.imagesearch import imagesearch
from python_imagesearch.imagesearch import imagesearcharea
import pyautogui
import time

time.sleep(3)
screenWidth, screenHeight = pyautogui.size()
shopTop=screenHeight*0.95
shopLeft=540
shopRight=2200
print(screenHeight)

poppy = 0
tf = 0
zoe = 0
while(poppy<8 or tf<8 or zoe<8):
    pyautogui.press('d')
    poppy_pos = imagesearcharea(
        "./poppy.png", shopLeft, shopTop, shopRight, screenHeight)
    tf_pos = imagesearcharea("./tf.png", shopLeft,
                             shopTop, shopRight, screenHeight)
    zoe_pos = imagesearcharea("./zoe.png", shopLeft,
                              shopTop, shopRight, screenHeight)
    while(poppy_pos[0] != -1 and poppy<8):
        print("position : ", poppy_pos[0], poppy_pos[1])
        pyautogui.moveTo(shopLeft+poppy_pos[0]+25, shopTop+poppy_pos[1]+25)
        pyautogui.click(button="left")
        poppy += 1
        poppy_pos = imagesearcharea(
            "./poppy.png", shopLeft, shopTop, shopRight, screenHeight)
    while(tf_pos[0] != -1 and tf<8):
        print("position : ", tf_pos[0], tf_pos[1])
        pyautogui.moveTo(shopLeft+tf_pos[0]+25, shopTop+tf_pos[1]+25)
        pyautogui.click(button="left")
        tf += 1
        tf_pos = imagesearcharea(
            "./tf.png", shopLeft, shopTop, shopRight, screenHeight)
    while(zoe_pos[0] != -1 and zoe<8):
        print("position : ", zoe_pos[0], zoe_pos[1])
        pyautogui.moveTo(shopLeft+zoe_pos[0]+25, shopTop+zoe_pos[1]+25)
        pyautogui.click(button="left")
        zoe += 1
        zoe_pos = imagesearcharea(
            "./zoe.png", shopLeft, shopTop, shopRight, screenHeight)
