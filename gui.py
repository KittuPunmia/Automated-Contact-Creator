import pyautogui,time
import csv
inputfile = csv.reader(open("C:/Users/user/Desktop/Python/Automated Contact Creator/Book1.csv","r"))
time.sleep(5)
pyautogui.click(1189,630)
time.sleep(2)
ctr=0;
for row in inputfile:
    if ctr !=0:
        name = row[0]
        no=row[1]
        pyautogui.click(1165,128)
        time.sleep(2)
        pyautogui.click(153,254)
        pyautogui.typewrite(name, interval=0.25)
        pyautogui.click(157,425)
        pyautogui.typewrite(no, interval=0.25) 
        pyautogui.click(167,116)
        time.sleep(2) 
        pyautogui.press('esc')
        time.sleep(5)
    else:
        ctr=1