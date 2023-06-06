import win32com.client
import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for file in files:
    if file.endswith(".msg"):
        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        msg = outlook.OpenSharedItem(file)        
        att=msg.Attachments
        for i in att:
            i.SaveAsFile(os.path.join(Pathname, i.FileName))#Saves the file with the attachment name