from calc_modules import calc, ref  
from pad4pi import rpi_gpio
import os
#peness
GPIO.setwarnings(False)

programlist= [calc,ref] 
inp=''
matrix= [
    ['%',7,'=',0,'RM',None],
    ['M-',8,'M+',1,4,None], 
    ['clr',9,'/',2,5,None],
    ['+','-','X',3,6,'on'],
    [None,None,None,'sqrt','.',None]   ]
row= [4,11,22,18,10]
col= [17,9,27,14,3,15]

factory= rpi_gpio.KeypadFactory()
keypad= factory.create_keypad(keypad=matrix,row_pins=row,col_pins=col)
   
def prog_validate(key):
    global inp, programlist
    if (len(inp)<8) and (type(key)== int):
        inp=inp+str(key)
        print(inp)
    if key== '=':
        try:
            inp10= int(inp,2)
			keypad.registerKeyPressHandler(programlist[inp10])
        except ValueError:
            print('Error')
		except IndexError:
			print('Error')
        else:
            print('Valid binary input.')
            print(inp10)
			keypad.unregisterKeyPressHandler(prog_validate)
    if key== 'clr'or key== '=':
        inp=''
        
def default(prog_name):
    keypad.unregisterKeyPressHandler(prog_name)
    keypad.registerKeyPressHandler(prog_validate)
	
keypad.registerKeyPressHandler(prog_validate)
