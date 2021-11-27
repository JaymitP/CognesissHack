import smtplib, ssl

class room:
    traits = {
        "pattern_recognition" : 0, # 3
        "emotional_intelligence" : 0, # 1
        "long_think" : 0, # 1
        "organisation" : 0, # 12
        "initiative" : 0, # 1
        "conscientious" : 0, # 4
        "patience" : 0, # 2
        "attentive" : 0, # 1
        "empathy" : 0, # 1
        "composure" : 0, # 1
        "memory" : 0 # 2
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
    
    def update_traits(self):
        room.traits["patience"] += 1

    text1 = "It may take a moment to send an email, if you want to skip press next."

    def send_email(self, user_email):
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "branchrooms@gmail.com"
        receiver_email = user_email # to be filled 
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
                            
    def selection(self, character):
        if (character == "A"):
            value = self.traits.get('initiative')
            self.traits.update({'initiative' : value + 1})
        if (character == "B"):
            value = self.traits.get('organisation')
            self.traits.update({'organisation' : value + 1})
        if (character == "C"):
            value = self.traits.get('long_think')
            self.traits.update({'long_think' : value + 1})

    

class room4(room):

    def __init__(self):
        room.__init__(self)
    
    def update_traits(self,points):
        room.traits["organisation"] += points
    text1 = """
        You should start getting dressed. Grab what you need and go. 
        """
    
class room5(room):
    def __init__(self):
        room.__init_(self)
    
    def update_traits(self): # update if fix_car button is pressed
        room.traits["conscientious"] += 1
        
    text1 = """You're driving your car to the interview.
            Suddenly, your car's engine starts to sputter
            and your car comes to a halt. You get out of your car
            and observe your surroundings.
            """
    

class room5_body(room): # body option
    def __init__(self):
        room.__init_(self)
        room.traits["empathy"] += 1

    def update_traits(self): # if cpr is successful, press buttton 50 times 
            room.traits["patience"] += 1
            room.traits["conscientious"] += 1

    text1 = """You approach what seems to be a bloody human body
            which is confirmed on closer inspection. The person
            is not breathing and responding to any of your 
            prompts. Do you perform CPR and try and resuscitate
            the person or fix your car?"""

        
class room6(room):
    
    def __init__(self):
        room.__init_(self)

    def update_traits(self): # if user takes more than 3 times to get it right
        room.traits["conscientious"] += 1
        
    text1 = """You open up the hood of your car. A cloud of trapped smoke 
            rises and reveals that the engine needs to be reassembled.
            """
            
    text2 = """You fix the car's engine and it sputters back to life!
            Then it immediately dies again."""
    
    

class room7(room):

    def __init__(self):
        room.__init_(self)

    title = "An unexpected encounter"

    def update_traits(self,points):
        room.traits["composure"] += points

    text1 = """
        You can't afford to waste anymore time trying to get the car working. If you're
        going to make it in time, you will have to walk from this point onwards; and so you
        did. As you walk down the road, a man pulling out a short blade approaches you and says "Wallet. Phone. NOW!"      
        """
        
class room8(room):

    def __init__(self):
        room.__init_(self)
        
    title = ""

    text1 = """
        You walk towards the building just in time for your interview; you've made it!
        Now it's time for you to enter the building. Oddly, it appears that the door is
        locked with some sort of mechanism to open it beside it.   
        """

class room9(room):

    def __init__(self):
        room.__init_(self)
        
    title = "The interview begins"

    text1 = """
        You walk up the stairs. That was quite odd, why would the door need to be opened
        in that way? Perhaps it was part of the interview? Either way, you need to focus up,
        as you approach the door to the interview room. Your interview will begin the moment
        you enter through that door. You hope that you're ready. 
        You walk through the door and see a man standing by the window, gazing out across the city.
        This must be the person interviewing you. A brief moment passes as you wait for him to
        turn around and greet you, but he shows no signs of doing so.
        """

class room10(room):

    def __init__(self):
        room.__init_(self)
        
    title = "Friends"

    text1 = """
        You get a phone call from your friend. He's going through a rough time, struggling and
        incredibly vulnerable and emotional right now and wants you to support him. However,
        you promised your other friend beforehand that you would drive him to a wedding.
        Which friend do you go to?
        """

class room11(room):

    def __init__(self):
        room.__init_(self)
        
    title = "Jackpot"

    text1 = """
        You decided to try your luck with the lottery and against all odds, you've won!
        You get a choice of either recieving £10000 instantly or £20000 over a period
        of 6 months. Which one do you go for?
        """

class room12(room):

    def __init__(self):
        room.__init__(self)
        
    title = "The Future"

    text1 = """
        Which one of these do you believe is the most important for the survival of humanity?
        Improving and maintain the health of humans? Improving quality of life through technology?
        Gaining knowledge and understanding our universe?
        """

class results(room):
    def __init__(self):
        room.__init__(self)

    def getResults(self):
        jobs = {
            "Biomedical_Scientist" : biomedical_scientist(),
            "Pharmacist" : pharmacist()
            "Crime_Scene_Investigator" : CSI()
            "Surgeon" : surgeon()
            "Application_Development" : application_development()
            "Cyber_Security" : cyber_security()
            "IT_Teaching" : it_teaching()
            "Website_Design" : website_design()
            "Contracting_Civil Engineer" : contracting_civil()
            "Mechanical_Engineer" : mechanical_engineer()
            "Nuclear_Engineer" : nuclear_engineer()
            "Actuarial_Analyst" : actuarial_analyst()
            "Accountant" : accountant()
            "Data_Analyst" : data_analyst()
            "Maths_Teacher" : maths_teacher()
        }

    def biomedical_scientist():
        return (room.traits["pattern_recognition"] + room.traits["emotional_intelligence"] + room.traits["conscientioius"] + room.traits["attentive"])/9.0*100


    def pharmacist():
        return (room.traits["long_think"] + room.traits["organisation"] + room.traits["attentive"] + room.traits["memory"])/16.0*100


    def CSI():
        return (room.traits["attentive"] + room.traits["composure"] + room.traits["pattern_recognition"] + room.traits["memory"])/7*100

    
    def surgeon():
        return (room.traits["initiative"] + room.traits["conscientious"] + room.traits["attentive"] + room.traits["composure"])/7*100

    def application_development():
        return (room.traits["pattern_recognition"] + room.traits["emotional_intelligence"] + room.traits["organisation"] + room.traits["conscientious"] + room.traits["patience"])/22*100

    def cyber_security():
        return (room.traits["pattern_recognition"] + room.traits["long_think"] + room.traits["initiative"] + room.traits["attentive"] )/6*100

    def it_teaching():
        return (room.traits["pattern_recognition"] + room.traits["emotional_intelligence"] + room.traits["organisation"] + room.traits["initiative"] + room.traits["patience"] + room.traits["attentive"] + room.traits["empathy"] + room.traits["composure"] + room.traits["memory"])/24*100

    def website_design():
        return (room.traits["long_think"] + room.traits["organisation"])/13*100
        
    def contracting_civil():
        return (room.traits["organisation"] + room.traits["long_think"] + room.traits["conscientious"] + room.traits["attentive"])/18*100

    def mechanical_engineer():
        return (room.traits["conscientious"] + room.traits["long_think"])/5*100
        
    def nuclear_engineer():
        return (room.traits["organisation"] + room.traits["long_think"] + room.traits["conscientious"] + room.traits["attentive"])/18*100
    
    def actuarial_analyst():
        return (room.traits["pattern_recognition"] + room.traits["attentive"])

    def accountant():
        return (room.traits["organisation"] + room.traits["attentive"] + room.traits["long_think"])
    
    def data_analyst():
        return (room.traits["pattern_recognition"] + room.traits["attentive"])
    
    def maths_teacher():
        return (room.traits["pattern_recognition"] + room.traits["emotional_intelligence"] + room.traits["organisation"] + room.traits["initiative"] + room.traits["patience"] + room.traits["attentive"] + room.traits["empathy"] + room.traits["composure"] + room.traits["memory"])/24*100






# traits


# processing speed
