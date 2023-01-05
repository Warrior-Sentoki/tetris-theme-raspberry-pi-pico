# Tetris theme

from machine import Pin, PWM
import time

buzzer = PWM(Pin(13))

volume = 5000

b = 247
c = 262
d = 294
e = 329
f = 349
g = 391
gs = 415
A = 440
As = 466
B = 494
C = 523
D = 587
Ds = 622
E = 659
F = 698
Fs = 740
G = 784
Gs = 830
A2 = 880

# Function and arguments
def playtone(note,vol,delay1,delay2):
    buzzer.duty_u16(vol)
    buzzer.freq(note)
    time.sleep(delay1)
    buzzer.duty_u16(0)
    time.sleep(delay2)

# Verse 1
playtone(E,volume,0.2,0.2)
playtone(B,volume,0.1,0.1)
playtone(C,volume,0.1,0.1)
playtone(D,volume,0.2,0.2)
playtone(C,volume,0.1,0.1)
playtone(B,volume,0.1,0.1)

playtone(A,volume,0.2,0.2)
playtone(A,volume,0.1,0.1)
playtone(C,volume,0.1,0.1)
playtone(E,volume,0.2,0.2)
playtone(D,volume,0.1,0.1)
playtone(C,volume,0.1,0.1)

playtone(B,volume,0.2,0.2)
playtone(B,volume,0.1,0.1)
playtone(C,volume,0.1,0.1)
playtone(D,volume,0.2,0.2)
playtone(E,volume,0.2,0.2)

playtone(C,volume,0.2,0.2)
playtone(A,volume,0.2,0.2)
playtone(A,volume,0.2,0.2)

time.sleep(0.5) # Quarter rest

# Verse 2
playtone(D,volume,0.2,0.2)
playtone(F,volume,0.1,0.1)
playtone(A2,volume,0.2,0.2)
playtone(G,volume,0.1,0.1)
playtone(F,volume,0.1,0.1)

playtone(E,volume,0.2,0.3)
playtone(C,volume,0.1,0.1)
playtone(E,volume,0.2,0.2)
playtone(D,volume,0.1,0.1)
playtone(C,volume,0.1,0.1)

playtone(B,volume,0.2,0.2)
playtone(B,volume,0.1,0.1)
playtone(C,volume,0.1,0.1)
playtone(D,volume,0.2,0.2)
playtone(E,volume,0.2,0.2)

playtone(C,volume,0.2,0.2)
playtone(A,volume,0.2,0.2)
playtone(A,volume,0.2,0.2)

time.sleep(0.5) # Quarter rest 

# Verse 1 repeat
playtone(E,volume,0.2,0.2)
playtone(B,volume,0.1,0.1)
playtone(C,volume,0.1,0.1)
playtone(D,volume,0.2,0.2)
playtone(C,volume,0.1,0.1)
playtone(B,volume,0.1,0.1)

playtone(A,volume,0.2,0.2)
playtone(A,volume,0.1,0.1)
playtone(C,volume,0.1,0.1)
playtone(E,volume,0.2,0.2)
playtone(D,volume,0.1,0.1)
playtone(C,volume,0.1,0.1)

playtone(B,volume,0.2,0.2)
playtone(B,volume,0.1,0.1)
playtone(C,volume,0.1,0.1)
playtone(D,volume,0.2,0.2)
playtone(E,volume,0.2,0.2)

playtone(C,volume,0.2,0.2)
playtone(A,volume,0.2,0.2)
playtone(A,volume,0.2,0.2)

time.sleep(0.5) # Quarter rest

# Verse 2 repeat
playtone(D,volume,0.2,0.2)
playtone(F,volume,0.1,0.1)
playtone(A2,volume,0.2,0.2)
playtone(G,volume,0.1,0.1)
playtone(F,volume,0.1,0.1)

playtone(E,volume,0.2,0.3)
playtone(C,volume,0.1,0.1)
playtone(E,volume,0.2,0.2)
playtone(D,volume,0.1,0.1)
playtone(C,volume,0.1,0.1)

playtone(B,volume,0.2,0.2)
playtone(B,volume,0.1,0.1)
playtone(C,volume,0.1,0.1)
playtone(D,volume,0.2,0.2)
playtone(E,volume,0.2,0.2)

playtone(C,volume,0.2,0.2)
playtone(A,volume,0.2,0.2)
playtone(A,volume,0.2,0.2)

time.sleep(0.5) # Quarter rest

# Verse 3
playtone(E,volume,0.6,0.2)
playtone(C,volume,0.6,0.2)
playtone(D,volume,0.6,0.2)
playtone(B,volume,0.6,0.2)
playtone(C,volume,0.6,0.2)
playtone(A,volume,0.6,0.2)
playtone(gs,volume,0.6,0.2)
playtone(B,volume,0.6,0.2)
playtone(E,volume,0.6,0.2)
playtone(C,volume,0.6,0.2)
playtone(D,volume,0.6,0.2)
playtone(B,volume,0.6,0.2)

playtone(C,volume,0.2,0.2)
playtone(E,volume,0.2,0.2)
playtone(A2,volume,0.2,0.2)
playtone(A2,volume,0.2,0.2)
playtone(Gs,volume,0.6,0.6)

# Verse 1 repeat 2
playtone(E,volume,0.2,0.2)
playtone(B,volume,0.1,0.1)
playtone(C,volume,0.1,0.1)
playtone(D,volume,0.2,0.2)
playtone(C,volume,0.1,0.1)
playtone(B,volume,0.1,0.1)

playtone(A,volume,0.2,0.2)
playtone(A,volume,0.1,0.1)
playtone(C,volume,0.1,0.1)
playtone(E,volume,0.2,0.2)
playtone(D,volume,0.1,0.1)
playtone(C,volume,0.1,0.1)

playtone(B,volume,0.2,0.2)
playtone(B,volume,0.1,0.1)
playtone(C,volume,0.1,0.1)
playtone(D,volume,0.2,0.2)
playtone(E,volume,0.2,0.2)

playtone(C,volume,0.2,0.2)
playtone(A,volume,0.2,0.2)
playtone(A,volume,0.2,0.2)

time.sleep(0.5) # Quarter rest

# Verse 2 repeat
playtone(D,volume,0.2,0.2)
playtone(F,volume,0.1,0.1)
playtone(A2,volume,0.2,0.2)
playtone(G,volume,0.1,0.1)
playtone(F,volume,0.1,0.1)

playtone(E,volume,0.2,0.3)
playtone(C,volume,0.1,0.1)
playtone(E,volume,0.2,0.2)
playtone(D,volume,0.1,0.1)
playtone(C,volume,0.1,0.1)

playtone(B,volume,0.2,0.2)
playtone(B,volume,0.1,0.1)
playtone(C,volume,0.1,0.1)
playtone(D,volume,0.2,0.2)
playtone(E,volume,0.2,0.2)

playtone(C,volume,0.2,0.2)
playtone(A,volume,0.2,0.2)
playtone(A,volume,0.2,0.2)

time.sleep(0.5) # Quarter rest

# Turn off
buzzer.duty_u16(0)



