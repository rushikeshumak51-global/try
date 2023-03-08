import email.utils
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('rushikeshumak51.office@gmail.com','Rushikesh@123')
message='this is very good light'
s.sendmail("rushikeshumak51.office@gmail.com",'renukapunkar2004@gmail.com',message)
s.quit()







