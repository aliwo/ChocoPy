import winsound
import time

winsound.Beep(293, 200) # D
winsound.Beep(293, 200) # D
winsound.Beep(293, 200) # D
winsound.Beep(293, 600) # D
winsound.Beep(246, 600) # B

time.sleep(0.1)

winsound.Beep(369, 200)# F#
winsound.Beep(369, 200)# F#
winsound.Beep(369, 200)# F#
winsound.Beep(369, 600)# F#
winsound.Beep(329, 600) # E

time.sleep(0.1)

winsound.Beep(329, 200) # E
winsound.Beep(329, 200) # E
winsound.Beep(329, 200) # E
winsound.Beep(369, 500) # F#

time.sleep(0.9)

winsound.Beep(369, 200) # F#
winsound.Beep(369, 200) # F#
winsound.Beep(369, 200) # F#
winsound.Beep(369, 600) # F#

time.sleep(0.9)
winsound.Beep(369, 200) # F#
winsound.Beep(369, 200) # F#
winsound.Beep(369, 200) # F#

for i in range(4):
    winsound.Beep(369, 200) # F#
    time.sleep(0.1)

for i in range(4):
    winsound.Beep(369, 100) # F#
    time.sleep(0.1)

winsound.Beep(369, 600) # F#
