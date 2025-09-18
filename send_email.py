
import smtplib
def send_email(text):
    
    email = "luckyjoker2004@gmail.com"
    password = "xawb yidf lgkw aehu"
    recipient_email = "vmnithwin@gmail.com"

    subject = "A message from your Application"
    message = f"Subject: {subject}\n\n {text}"

    print("Connecting the server")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        print("Logging in...")
        server.login(email, password)
        server.sendmail(email, recipient_email, message)
    print("Email send successfully")