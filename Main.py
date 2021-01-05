import pyautogui
import time
import pandas as pd
from datetime import datetime
import os

print("started bot")

def close_zoom():
     try:
         os.system("taskkill /f /im Zoom.exe")
        
     except:
         print("Zoom not open")

def sign_in(meetingid, password):
     close_zoom()
     
     time.sleep(2)
     
     os.startfile('C:/Users/arpan/AppData/Roaming/Zoom/bin/Zoom.exe')
     
     time.sleep(5)
     
     pyautogui.moveTo(pyautogui.locateCenterOnScreen('join_meeting.PNG'))
     pyautogui.click()
     
     time.sleep(2)
     
     pyautogui.moveTo(pyautogui.locateCenterOnScreen('Metting.PNG'))
     pyautogui.click()
     pyautogui.write(meetingid)
     
     media_btn = pyautogui.locateAllOnScreen('media_btn.PNG')
     for btn in media_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()
     
     join = pyautogui.locateCenterOnScreen('join.PNG')
     pyautogui.moveTo(join)
     pyautogui.click()
     
     time.sleep(3)
     
     pass_btn = pyautogui.locateCenterOnScreen('pass.PNG')
     pyautogui.moveTo(pass_btn)
     pyautogui.click()
     pyautogui.write(password)
     pyautogui.press('enter')
     
     time.sleep(50)
     
     chat_btn = pyautogui.locateCenterOnScreen('chat_button.PNG')
     
     pyautogui.moveTo(chat_btn)
     pyautogui.click()
     
     chat_box = pyautogui.locateCenterOnScreen('chat_box.PNG')
     pyautogui.moveTo(chat_box)
     pyautogui.click()
     pyautogui.write("Arpan Bajpai 9E")
     
     pyautogui.press('enter')
     pyautogui.press('esc')
     
  

# Reading the file
df = pd.read_csv('timmings.csv')

while True:
     # checking of the current time exists in our csv file
     now = datetime.now().strftime("%H:%M")
 
     if now in str(df['timmings']):

         row = df.loc[df['timmings'] == now]
         m_id = str(row.iloc[0,1])
         m_pswd = str(row.iloc[0,2])

         sign_in(m_id, m_pswd)
         
         print('signed in')
         time.sleep(60)