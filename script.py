import pyautogui
import time

img1 = "1.png"
img2 = "2.png"

cycles = 1

a = [0.80, 0.80, 0.80, 1.00, 1.00, 1.00, 1.20, 1.20, 1.20]
b = [0.40, 0.80, 1.20, 0.40, 0.80, 1.20, 0.40, 0.80, 1.20]
q = [0.000289293, 0.000676966, 0.00151511, 0.00024744, 0.000571665, 0.00125265, 0.000210111, 0.000472174, 0.00101649]

print("Starting Up")
time.sleep(0.1) 
print("Successful load")

# while True:
#     print(pyautogui.position())
 
pyautogui.FAILSAFE = True # 1070, 380



pyautogui.moveTo(img1x, img1y)




cycles = 0
cycles = int(input("Input how many cycles to buy: "))

input("Press enter when the mouse is on the item in the store")
# a = pyautogui.position()
# # print(pyautogui.position())
# img1x = a[0]
# img1y = a[1]
print(str(img1x) + " " + str(img2x))

print("Starting in 5 seconds...")
time.sleep(5) 

foundPos = False

for o in range(0,cycles):
    start_time = time.time()

    pyautogui.moveTo(img1x, img1y)

    time.sleep(0.05)

    pyautogui.click(button='right')

    pyautogui.moveTo(10,500)

    time.sleep(0.05)

    pyautogui.moveTo(1070, 380)
    time.sleep(0.07)
    pyautogui.click(button='left', clicks=1000, interval=0.13343567)

    time.sleep(0.02)

    pyautogui.press('esc')
    time.sleep(0.05)
    pyautogui.press('t')
    time.sleep(0.05)
    pyautogui.write('/sbmenu')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.5)


    pyautogui.moveTo(960, 440)
    time.sleep(0.1)
    pyautogui.click(button='left')
    time.sleep(0.01)
    pyautogui.moveTo(10,500)
    time.sleep(0.1)
    
    pyautogui.moveTo(1120, 330)
    time.sleep(0.1)
    pyautogui.click(button='left', clicks=30, interval=0.0403343567)

    time.sleep(0.05)
    pyautogui.press('e')        
    
    time.sleep(0.05)

    time.sleep(0.05)
    pyautogui.press('t')
    time.sleep(0.05)
    pyautogui.write('/sbmenu')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.moveTo(1125, 385)
    time.sleep(0.25)
    pyautogui.click(button='left')
    time.sleep(0.20)
    pyautogui.moveTo(745, 810)
    pyautogui.keyDown('shift')
    time.sleep(0.05)
    pyautogui.click(button='left')
    time.sleep(0.05)
    pyautogui.keyUp('shift')
    pyautogui.press('e') 

    time.sleep(0.15)
    pyautogui.click(button='right')
    time.sleep(0.25)

    print("Cycle " + str(o+1))
    print("--- %s seconds ---" % (time.time() - start_time))

