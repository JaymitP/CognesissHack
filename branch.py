import smtplib, ssl

class room:
    traits = {
        "crisis_mangement" : 0,
        "design_thinking" : 0,
        "pattern_recognisition" : 0,
        "resilience" : 0,
        "emotional_intelligence" : 0,
        "determiness" : 0,
        "open_mind" : 0,
        "long_think" : 0,
        "organisation" : 0,
        "leadership" : 0,
        "conscientious" : 0,
        "patience" : 0,
        "attentive" : 0,
    }
    def __init__(self):
        pass

class room1(room):

    def __init__(self):
        room.__init__(self)
        self.text = "Enter your email"
        self.tick1 = "Tick to recive newsletter."
        self.tick2 = "Tick to recieve a notification to when we update the game."
        self.tick3 = "Tick to recieve your results at the end."
        self.checkboxes = []

    """
    javascript
    button: "Submit" --> goes to next room
        save to database
    """
    
    
    
class room2(room):
    def__init__(self):
        room.__init__(self)

    text1 = "It may take a moment to send an email, if you want to skip press next."

    def send_email(self):
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "branchrooms@gmail.com"
        receiver_email = "jeremy.ockenden@hotmail.co.uk" # to be filled 
        password = "hackathon123" 
        message = """
        Subject: Hi there

        This message is sent from Python.
        """

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

class Room3(room):

    title = "Waking Up  "
    text1 = '''27th November 2021 insert calender with interview at todays date at 11.
                You just woke up. You seem to be very nervous this morning; today's the big day.
                Maybe you should go brush your teeth, it's already 10am.
                The tap is broken.
                            Do you want to:
                            A. Try to fix it yourself
                            B. Call a plumber and get it fixed later
                            C. Don't brush your teeth and get dressed.'''
    val = input("")
    if (val == "A"):
        value = self.traits.get('attentive')
        print(value)
        self.traits.update({'attentive' : value + 1})
        print(self.traits.get('attentive'))
    if (val == "B"):
        value = self.traits.get('orginisation')
        print(value)
        self.traits.update({'orginisation' : value + 1})
        print(self.traits.get('orginisation'))
    if (val == "C"):
        value = self.traits.get('crisis_mangement')
        print(value)
        self.traits.update({'crisis_mangement' : value + 1})
        print(self.traits.get('crisis_mangement')) 
    
#

    
        
r = room1()
r.send_email()
