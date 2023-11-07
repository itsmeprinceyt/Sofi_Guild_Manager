########################## - AUTO UPDATOR - ##############################
#
# REQUIREMENTS
#
# 0- File Exporerer should be fullscreen
# 0- No other notepad should be open
# 1- Discord Sofi Lane Server Open [ Discord full screen ] + [ 3rd position in taskbar ]
# 2- Google Chrome Open with 2 YouTube Tabs Open [ Google Chrome Full screen]
# 3- Vs Code Open [ at 4th position in taskbar]
# 4- Check If Dischook Website is working or not   [ size 33% ]
# 5- Check If Notepad Is full size or not [ Notepad full screen]
# 6- Check If Both Files in Output are present or not
#
##########################################################################

from cryptography.fernet import Fernet
import pyautogui
import time
import keyboard

class AU:
    WebHook="https://discord.com/api/webhooks/1124816839311118457/7QfL--WdYq8j1ShrxvGJVn7LBc4AIQaLXMRiOUegIjHc4uWhx0j1vjNKhpAsp39Gtqiy"
    MessageLink="https://discord.com/channels/310675536340844544/1124690966683582555/1124848745419374633"
    current_balance=""

    def move_click(x,y):
        time.sleep(0.5)
        pyautogui.moveTo(x,y,duration=0.5)
        time.sleep(0.5)
        pyautogui.click()

    def move_doubleclick(x,y):
        time.sleep(0.5)
        pyautogui.moveTo(x,y,duration=0.5)
        time.sleep(0.5)
        pyautogui.doubleClick()
    
    def control_a():
        time.sleep(0.5)
        keyboard.press_and_release('ctrl+a')
        
    def control_c():
        time.sleep(0.5)
        keyboard.press_and_release('ctrl+c')
    
    def control_v():
        time.sleep(0.5)
        keyboard.press_and_release('ctrl+v')
    
    def press_enter():
        time.sleep(0.5)
        keyboard.press('enter')
    
    def paste_string(str):
        time.sleep(0.5)
        keyboard.write(str)


    def auto_update_pls():
        
        #Getting Current Vault Balance from DATABASE_Bank_Balance.txt
        with open("key\key.txt",'rb') as f:
            k=f.read()
        MK= Fernet(k)
        with open("DataBase\DATABASE_Bank_Balance.txt",'rb') as f:
            Rbalance=f.read()
        balanceD=MK.decrypt(Rbalance)
        with open("DataBase\DATABASE_Bank_Balance.txt",'wb') as f:
            f.write(balanceD)
        with open("DataBase\DATABASE_Bank_Balance.txt",'r') as f:
            ok=f.read()
        AU.current_balance=ok
        balanceE=MK.encrypt(balanceD)
        with open("DataBase\DATABASE_Bank_Balance.txt",'wb') as f:
            f.write(balanceE)
        
        #Auto Update
        AU.move_click(596,743)
        AU.move_click(635,210)
        AU.move_click(621,333)
        AU.move_doubleclick(228,213)
        AU.move_doubleclick(228,213)
        AU.move_doubleclick(228,213)
        AU.move_doubleclick(239,254)
        AU.move_doubleclick(231,280)
        AU.move_doubleclick(233,186)
        AU.move_click(567,368)
        AU.control_a()
        AU.control_c()
        AU.move_click(618,743)
        AU.move_click(649,90)
        AU.move_click(677,201)
        time.sleep(3)
        AU.move_click(205,159)
        time.sleep(3)
        AU.paste_string(AU.WebHook)
        AU.move_click(61,357)
        AU.paste_string(AU.MessageLink)
        AU.move_click(662,362)
        AU.move_click(753,435)
        AU.move_click(15,297)
        AU.move_click(14,324)
        AU.move_click(67,368)
        AU.control_a()
        AU.control_v()
        AU.move_click(16,462)
        AU.move_click(40,503)
        AU.move_click(77,522)
        AU.move_click(283,670)
        AU.move_click(15,297)
        AU.move_click(658,747)
        AU.move_doubleclick(261,220)
        AU.move_click(567,368)
        AU.control_a()
        AU.control_c()
        AU.move_click(618,743)
        AU.move_click(15,318)
        AU.move_click(14,346)
        AU.move_click(90,398)
        AU.control_a()
        AU.control_v()
        AU.move_click(14,485)
        AU.move_click(40,523)
        AU.move_click(79,543)
        AU.move_click(661,162)
        pyautogui.leftClick()
        AU.move_click(232,16)
        AU.move_click(707,742)
        AU.move_click(142,247)
        AU.move_click(391,674)
        AU.paste_string(AU.current_balance)
        AU.press_enter()
        AU.move_click(145,444)
        AU.move_click(1312,8)
        AU.move_click(796,741)
        AU.move_click(502,16)
        AU.move_click(266,17)
        AU.move_click(769,742)

if __name__=="__main__":
    AU.auto_update_pls()