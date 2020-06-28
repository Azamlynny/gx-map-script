import pyautogui
import time

img1 = "MapComputationDone.png"

startIndex = 0 # Which index in the array to start at

a = [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2]
b = [0.4, 0.4, 0.4, 0.4, 0.4, 0.8, 0.8, 0.8, 0.8, 0.8, 1.2, 1.2, 1.2, 1.2, 1.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.8, 0.8, 0.8, 0.8, 0.8, 1.2, 1.2, 1.2, 1.2, 1.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.8, 0.8, 0.8, 0.8, 0.8, 1.2, 1.2, 1.2, 1.2, 1.2]
q = [0.00024, 0.00028, 0.00032, 0.00036, 0.0004, 0.0004, 0.0006, 0.0008, 0.00089, 0.0011, 0.0013, 0.0015, 0.0017, 0.00192, 0.00215, 0.00020, 0.00023, 0.00028, 0.0003, 0.00036, 0.0005, 0.00055, 0.0006, 0.00075, 0.00080, 0.0011, 0.0012, 0.0014, 0.00158, 0.00165, 0.00016, 0.00018, 0.0002, 0.00025, 0.0003, 0.00038, 0.00045, 0.0005, 0.00055, 0.0006, 0.0007, 0.0008, 0.001, 0.0012, 0.0013]

print("Starting Up")
time.sleep(0.1) 
print("Successful load")

# while True:
#     input("Press enter when the mouse is in the desired location")
#     print(pyautogui.position())
 
pyautogui.FAILSAFE = True 

print("Starting in 5 seconds...")
time.sleep(5) 

for i in range(startIndex, len(q)):
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
    pyautogui.moveTo(1530, 578) # Reset Q for volume recomompute regardless of no change
    time.sleep(0.1)
    pyautogui.click(button='left')
    time.sleep(5) # Do not update volume
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

    time.sleep(5)
    pyautogui.moveTo(111, 114) # Compute rendering grid
    time.sleep(0.1)
    pyautogui.click(button='left')
    time.sleep(10)

    pyautogui.moveTo(23, 224) # Image view tab
    time.sleep(0.1)
    pyautogui.click(button='left')
    time.sleep(5)

    pyautogui.moveTo(348, 197) # [RCP+CCP] dropdown
    time.sleep(0.1)
    pyautogui.click(button='left')
    time.sleep(3)

    pyautogui.moveTo(327, 305) # T_I dropdown choice
    time.sleep(0.1)
    pyautogui.click(button='left')
    time.sleep(2)

    pyautogui.moveTo(1061, 56) # Synthetic Map Computation
    time.sleep(0.1)
    pyautogui.click(button='left')
    time.sleep(5)
    pyautogui.press('right')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(200) # Wait 200 seconds before checking for synthetic map computation

    while True: # Check whether map computation finished
        l = list(pyautogui.locateAllOnScreen(img1))
        if(len(l) > 0): # If on screen
            time.sleep(0.05)
            break

    # Save the .map file
    time.sleep(2)
    pyautogui.moveTo(201, 121) # Save Maps to File
    time.sleep(0.1)
    pyautogui.click(button='left')
    time.sleep(5)
    pyautogui.write("a" + str(a[i]) + "-b" + str(b[i]) + "-q" + str(q[i]))
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)

    print("Cycle " + str(i+1))
    print("--- %s seconds ---" % (time.time() - start_time))
