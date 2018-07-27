import imaplib, email, os,time, zipfile
user = 'cert@renu.ac.ug'
password = 'renu123'
imap_url = 'webmail.renu.ac.ug'

#Where you want your attachments to be saved (ensure this directory exists) 
#attachment_dir = '/home/daniel/Attachments'
#attachment_dir = os.path.dirname('/home/daniel/Attachments')
# define the name of the directory to be created
os.chdir("/home/daniel")
path = os.getcwd()
print("The current directory is %s "%path)
attachment_dir = os.path.join(path,'Attachments')
try:  
    os.mkdir(attachment_dir)
except OSError:  
    print ("Creation of the directory %s failed" % attachment_dir)
else:  
    print ("Successfully created the directory %s " % attachment_dir)
# sets up the authentication
def auth(user,password,imap_url):
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,password)
    return con
# extracts the body from the email
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)
# allows you to download attachments
def get_attachments(msg):
    for part in msg.walk():
        if part.get_content_maintype()=='multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()
        if bool(fileName):
            filePath = os.path.join(attachment_dir, fileName)
            with open(filePath,'wb') as f:
                f.write(part.get_payload(decode=True))
	
#extracts emails from byte array
def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs

con = auth(user,password,imap_url)
con.select('ShadowServer')

result, data = con.search(None, "(ON {0})".format( time.strftime("%d-%b-%Y")))
#result, data = con.search(None,'ALL')
ids = data[0]
id_list = ids.split()
print(id_list)

for email_id in id_list:
    result, data = con.fetch(email_id,'(RFC822)')

    raw = email.message_from_string(data[0][1])
    # print(get_body(raw))
    get_attachments(raw)

con.close()
con.logout()
