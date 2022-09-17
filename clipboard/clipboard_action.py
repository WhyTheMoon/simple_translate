import time
import win32api as api
import win32con as con
import win32clipboard as clp

# copy text from clipboard
def get_clipbd() :
    try : 
        clp.OpenClipboard()
        text = clp.GetClipboardData(con.CF_TEXT)
        clp.CloseClipboard()
        return text
    except :
        return None

# set clipboard text
def set_clipbd(text) :
    try :
        clp.OpenClipboard()
        clp.SetClipboardText(text)
        clp.CloseClipboard()
        return
    except :
        return 

# copy current highlighted text while keep original clipboard content
def active_copy() :
    try :
        text_now = get_clipbd()
        kb.press_and_release('ctrl+c')
        time.sleep(0.2)
        text_tmp = get_clipbd()
        set_clipbd(text_now)
        if ( text_tmp != text_now ) :
            return text_tmp
        return None
    except :
        return None

# return highlighted text if cursor hovering & highlight events occur simultaneously
def hover(last_text) :
    pos_now = api.GetCursorPos()
    time.sleep(0.5)
    pos_tmp = api.GetCursorPos()

    if ( pos_tmp == pos_now ):
        text = active_copy()
        if ( text!=None and text!=last_text) :
            return text

# playground
last_text = ''
while True :
    now_text = hover(last_text)
    if(now_text != None) :
        print(now_text)
        last_text = now_text
