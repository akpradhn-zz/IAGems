#!/usr/bin/python

import gtk.gdk
import datetime
from datetime import datetime
import errno
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os import path


# Constants
#------------------------------------------------------------------------------------------------------------
scr_file = "/home/amit/Documents/CronTask/"                       # Dateed Directory Location for Screen Shots

dir_path = scr_file+ str(datetime.now().strftime('%Y-%m-%d'))     # Location for Screen shots

dateSTR = datetime.now().strftime("%H:%M" )                       # Send Mail at Specific Time



def filecreation():
    mydir = os.path.join(
        os.getcwd(), 
        datetime.now().strftime('%Y-%m-%d'))
    print ("Hurray Directory Created at %s",mydir)
    try:
        os.makedirs(mydir)
        
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise  # This was not a "directory exist" error..

# Create a directory based on date

filecreation()

#-----------------------------------------------------------------------------------
# Taking Scrren Shots

w = gtk.gdk.get_default_root_window()
sz = w.get_size()

print "The size of the window is %d x %d" % sz

pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])

pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])

if (pb != None):
    pb.save(scr_file+ str(datetime.now().strftime('%Y-%m-%d'))+"/"+str(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))+".png","png")
    print "Screenshot saved to screenshot.png."
else:
    print "Unable to get the screenshot."

#---------------------------------------------------------------------------------------
# Send Files at attachment and mail

def send_selenium_report(dir_path):
    
    files = [x for x in os.listdir(dir_path) if path.isfile(dir_path+os.sep+x)]
    
    msg = MIMEMultipart()
    msg['To'] = "******@gmail.com"
    msg['From'] = "******@gmail.com"
    msg['Subject'] = "Screenshots for the Day"

    body = MIMEText('Test results attached.', 'html', 'utf-8')  
    msg.attach(body)  # add message body (text or html)

    for f in files:  # add files to the message
        file_path = os.path.join(dir_path, f)
        attachment = MIMEApplication(open(file_path, "r").read(), _subtype="txt")
        attachment.add_header('Content-Disposition','attachment', filename=f)
        msg.attach(attachment)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("username", "password")
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    
    print 'done!'
    s.close()

#--------------------------------------------------------------------------------------------
#if dateSTR == ("11:07"):
   #Send Mail
    
send_selenium_report(dir_path)

'''
else:
    # do something useful till this time
    time.sleep(1)
    pass
'''