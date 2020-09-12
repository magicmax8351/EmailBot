import ezgmail
from pdf2image import  convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError,

)

import random
from fpdf import FPDF
 
ezgmail.init()
 
Threads = ezgmail.unread()
 
lookAt = len(Threads)
 
count = 0


leonard_responses = ["Spent more money again huh :/" , "Leonard the bot says meow. You spend too much. Meow." , "MEOW MEOW MEOW MEOW MEOW MEOW MEOW "
                     , "If Leonard could talk he'd say he's disappointed in you >:(" , "silence", "money doesn't grow on trees!!","do you have a job? then why you spend money!!! >:(" ,
                     ]


 

leonardSays = random.choice(leonard_responses)

def PDFCreation():
    pdf = FPDF(format='letter', unit = 'in')
    pdf.add_page()
    
      
    pdf.add_font('leonard', '', r"C:\Users\Max\eclipse-workspace\pyBot\child-writing\child-writing.ttf", uni=True)
        
       
    pdf.set_font('leonard','',50)
     
     
    max_page_width = pdf.w - 2*pdf.l_margin
     
     
      
    pdf.multi_cell(max_page_width, 1,leonardSays)
     
    pdf.ln(2.0)
     
    pdf.output('angryLeonard.pdf', 'F')
    
    pages = convert_from_path(r'C:\Users\Max\eclipse-workspace\pyBot\angryLeonard.pdf')
    
    pages[0].save('angryLeonard.jpg','JPEG')
  
 
print("lookat is " + str(lookAt))
 
try: 
    while (count < lookAt):
        if(Threads[count].messages[0].sender.find("transaction@notice.aliexpress.com") != -1):
            Threads[count].markAsRead()
            leonardSays = random.choice(leonard_responses)
            PDFCreation()
            ezgmail.send('buffomax@gmail.com','Bot Email :)',leonardSays,['angryLeonard.jpg'])
            print('lookout leonard sent an email')
        count = count +1 
     
     
 
except Exception:
    print("something broke grr")










