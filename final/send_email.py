import csv
from email import message
import smtplib, ssl
import get_news
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "dhru.a.patel@gmail.com"
password = input("Enter email for {sender_email}")

def build_message(name,sender_email, receiver_email, subject):

    news_data = get_news.get_data()

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email  
    message["Subject"] = subject
    header = f"""\
        <html>
            <body>
               <left><p style ="font-size:15px">
               Good Morning {name}, <br>
                <center>Here is your daily sports briefing. We hope you enjoy the content!</center>
               </p></left>
            </body>
        </html>
        """
    body = ""
    for i in range(len(news_data)):
        title = str(news_data[i]['title'])
        author = str(news_data[i]['author'])
        
        if author == "None":
            author = "No author"
        
        summary = str(news_data[i]['description'])
        link = str(news_data[i]['url'])
        body = body + f"""\
            <html>
                <body>
                  <center>
                    <h1 style="font-size:30px"> {title} </h1>
                    <p> {link}<br>
                        By:{author}<br>
                        {summary}<br>
                    </p> </center>
                </body>
            </html>
            """
        #print(body)
    signature = f"""\
       
        Thanks for reading with us!
        
        - Dhru A. Patel
        
        """
    
    format_header = MIMEText(header, "html")
    format_body = MIMEText(body, "html")
    format_sig = MIMEText(signature, "plain")
    message.attach(format_header)
    message.attach(format_body)
    message.attach(format_sig)
    built_message = message.as_string()
    return built_message
# Create a secure SSL context
context = ssl.create_default_context()
def send_out():
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        # TODO: Send email here
        with open ('names.csv') as file:
            reader = csv.reader(file)
            next(reader)
            for name, email, medium in reader:
                message = build_message(name, sender_email, email, "Daily Sports Update")
                server.sendmail(sender_email, email, message)
                print(f"sent to {name}")

    except Exception as e:
        # Print any error messages to stdout
        print("error: " ,e)
    finally:
        server.quit() 
send_out()