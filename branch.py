import smtplib, ssl

class room:
    traits = {
        "pattern_recognition" : 0,
        "emotional_intelligence" : 0,
        "open_mind" : 0, 
        "long_think" : 0,
        "organisation" : 0, #
        "initative" : 0, #
        "conscientious" : 0, #
        "patience" : 0, #
        "attentive" : 0, #
        "emphathy" : 0 #
        "composure" : 0 #
    }

    def __init__(self):
        pass

class room1(room):
    def __init__(self):
        room.__init__(self)
        self.text = "Enter your email"
        self.tick1 = "Tick to receive newsletter."
        self.tick2 = "Tick to receive a notification to when we update the game."
        self.tick3 = "Tick to receive your results at the end."
        self.checkboxes = []
    
    def update_traits(self):
        if self.checkboxes[2] == True:
            room.traits["attentive"] += 1
    """
    javascript
    button: "Submit" --> goes to next room
        save to database
    """
    
class room2(room):
    def __init__(self):
        room.__init__(self)
    
    def update_traits():
        room.traits["patience"] += 1

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
 
class room3(room):
    def __init__(self):
        room.__init__(self)
    title = "Waking Up  "
    text1 = """27th November 2021 insert calender with interview at todays date at 11.
                You just woke up. You seem to be very nervous this morning; today's the big day.
                Maybe you should go brush your teeth, it's already 10am.
                The tap is broken.
                            Do you want to:
                            A. Try to fix it yourself
                            B. Call a plumber and get it fixed later
                            C. Don't brush your teeth and get dressed."""
    val = input("")
    if (val == "A"):
        value = self.traits.get('attentive')
        print(value)
        self.traits.update({'attentive' : value + 1})
        print(self.traits.get('attentive'))
    if (val == "B"):
        value = self.traits.get('organisation')
        print(value)
        self.traits.update({'organisation' : value + 1})
        print(self.traits.get('organisation'))
    if (val == "C"):
        value = self.traits.get('crisis_management')
        print(value)
        self.traits.update({'crisis_management' : value + 1})
        print(self.traits.get('crisis_management')) 
    

class Room4(room):

    def __init__(self):
        room.__init__(self)
    
    text1 = """You're driving your car to the interview.
            Suddenly, your car's engine starts to sputter
            and your car comes to a halt. You get out of your car
            and observe your surroundings."""


class Room5(room):

    def __init__(self):
        room.__init_(self)

    text1 = """You open up the hood of your car. A cloud of trapped smoke 
            rises and reveals that the engine needs to be reassembled.
            """

class Room6(room):

    def __init__(self):
        room.__init_(self)

    
class Room7(room):

    def __init__(self):
        room.__init_(self)

    text1 = """
            """            


    
