import pyautogui
import time

img1 = "1.png"
img2 = "2.png"

startIndex = 0
cycles = 1

a = [0.80, 0.80, 0.80, 1.00, 1.00, 1.00, 1.20, 1.20, 1.20]
b = [0.40, 0.80, 1.20, 0.40, 0.80, 1.20, 0.40, 0.80, 1.20]
q = [0.000289293, 0.000676966, 0.00151511, 0.00024744, 0.000571665, 0.00125265, 0.000210111, 0.000472174, 0.00101649]

print("Starting Up")
time.sleep(0.1) 
print("Successful load")

# while True:
#     input("Press enter when the mouse is in the desired location")
#     print(pyautogui.position())
 
pyautogui.FAILSAFE = True 

print("Starting in 5 seconds...")
time.sleep(5) 

for i in range(startIndex, cycles):
    start_time = time.time() # Save the start time for tracking time elapsed

    # Inputing the a, b, q values
    time.sleep(0.1)
    pyautogui.moveTo(989, 508) # move to q[0]
    time.sleep(0.1)
    pyautogui.click(button='left')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a') # ctrl + a
    time.sleep(0.2)
    pyautogui.write(str(q[i])) # q[0]
    time.sleep(3) # Do not update volume
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('right')
    time.sleep(0.1)
    pyautogui.press('enter')

    time.sleep(0.3)
    pyautogui.moveTo(1127, 578) # move to Q
    time.sleep(0.1)
    pyautogui.click(button='left')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a') # ctrl + a
    time.sleep(0.2)
    pyautogui.write("q0*(B/q[1])^" + str(a[i]) + "/(L/q[2])^" + str(b[i]) + "") # b and a
    time.sleep(3) # Update Volume
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(40) 

    time.sleep(0.3)
    pyautogui.moveTo(23, 135) # Volume view tab
    time.sleep(0.1)
    pyautogui.click(button='left')

    print("Cycle " + str(o+1))
    print("--- %s seconds ---" % (time.time() - start_time))
