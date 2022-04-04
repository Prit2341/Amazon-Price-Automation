import requests
from time import sleep

Sub = "BOT"
Body = "Your Cosmic byte keybrod price fell check out\nhttps://www.amazon.in/gp/product/B09MQZY875/ref=ox_sc_act_image_2?smid=A14CZOWI0VEHLG&psc=1"
Email =  "pritmayani359@gmail.com"
#Make Function For the sending mail to notify
def Email_alert(subject,body,to):
    '''Impoet Some Librery For The perfoming'''
    import smtplib
    from email.message import EmailMessage

    #Take Input for The Subjext Body And Emali For The Sender
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
            
    user = "novagaming990768@gmail.com"
    msg['from'] = user
    password = 'nhscvtwijvmogtvg'
        
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
            
    server.quit()
            

            
    #print('Source:')
    #print('https://www.youtube.com/watch?v=B1IsCbXp0uE')
    #print('for mobile Check Below link:')
    #print('https://www.digitaltrends.com/mobile/how-to-send-a-text-from-your-email-account/')

    

    

#This is Amazon Price Api Thats Give the Price Data
import requests

url = "https://amazon-product-price-data.p.rapidapi.com/product"

querystring = {"asins":"B09MQZY875,B07PQYFPV8","locale":"IN"}

headers = {
	"X-RapidAPI-Host": "amazon-product-price-data.p.rapidapi.com",
	"X-RapidAPI-Key": "867fcb8387msh034f2da34f91894p1015dbjsn0af672c8f15a"
}

response = requests.request("GET", url, headers=headers, params=querystring)


while True:
    Data = response.json()
    title_venth = Data[0]['product_name']
    Price_venth = Data[0]['current_price']

    title_neon = Data[1]['product_name']
    Price_neon = Data[1]['current_price']
    if (Price_neon < 2199) or (Price_venth < 1950):
        Email_alert(Sub,Body,Email)
    else:
        pass
    sleep(43200)
