2021 / Python 3
# Window Controller

Change position and size of other program windows

# How to use it:

install Python 3 and modules keyboard and wx:
1) download and install python 3 (https://www.python.org/)
2) click start and type CMD and hit enter (run cmd)
3) copy and past this in the cmd window: python -m pip install keyboard
4) and this: python -m pip install wx

run the script:
5) double click Windows_Contraller.pyw (if everything is correct, then you should see a window now)
6) click the "Set Window" button, now a 5 seconds countdown begins
7) click on the program window you like to control (you need to have the target window selected when the countdown hit hit zero)
8) confirm that text under "Set Window" button is the same as the titelbar text of the target window
9) now you can change the edges of the target window with all the buttons with 1, 10, 100, -1, -10, -100 in the respective direction/edge or you can enter the desired position/size in the text boxes above the respective direction and press enter.

the *keyboard* and *wx* modules must be installed.
button group up and to the left is the position of the window and
button group down and to the right is the size of the window
