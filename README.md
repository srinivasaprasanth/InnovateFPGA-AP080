# InnovateFPGA-AP080
Project name: Autonomous rag picking bot for garbage management in smart cities

CODE OVERVIEW:
-------------
coming to our codes, we have attached 4 python files along with some packages and requirements, they are bot_control.py, main_file.py, send.py, servo_control.py. bot_control file contains the code for chassis control of the bot. main_file contains the code for processing and making decisions. send.py contains the code to send the data to the azure cloud and finally servo_control file contains the code for bottle picking.
                                                                  
                          Azure cloud
                               ↑                                                                   
                           file.txt
                               ↑                                                                   
                            send.py
                               ↑                                                                   
     servo_control.py  ⇆  main_file.py  →  bot_control.py
                                         
We have used file handling techiniques to implement our code. main_file.py is the main file from where we can access send.py and bot_control.py. All these 3 mentioned
files were written inside HPS part of DE10 nano. Servo_control file is written inside rasp-pi.

PROJECT LINK:
------------
https://www.innovatefpga.com/cgi-bin/innovate/teams.pl?Id=AP080&All=1

