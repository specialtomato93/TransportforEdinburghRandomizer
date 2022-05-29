import random

#List with all the routes that go through the city centre
routes=[1,2,3,4,5,7,8,10,11,12,14,15,16,19,22,23,24,25,26,27,29,30,31,33,34,36,37,41,42,44,45,47,49,"X18","X27","X28",43,104,"X7",113,124, "Tram"]
RS=random.choice(routes)

#All of the destinations
#Some lines only have one destination because they terminate in the city centre.

One=["Clermistion","Seafield"]
Two=["The Jewel", "Gyle Centre"]
Three=["Clovenstone","Mayfield","Dalkeith"]
Four=["Hillend","The Jewel"]
Five=["Hunter's Tryst","The Jewel"]
Seven=["Newhaven","Royal Infirmary"]
Eight=["Muirhouse","Royal Infirmary"]
Ten=["Western Harbour","Torphin","Bonaly"]
Eleven=["Ocean Terminal", "Hyvots Bank"]
Twelve=["Gyle Centre"]
Fourteen=["Muirhouse","Greendykes"]
Fifteen=["Easter Bush"]
Sixteen=["Silverknowes","Colinton"]
Nineteen=["Granton","King's Road"]
TwentyTwo=["Gyle Centre","Ocean Terminal"]
TwentyThree=["Trinity","Greenbank"]
TwentyFour=["Muirhouse","Royal Infirmary"]
TwentyFive=["Heriot Watt University","Restalrig"]
TwentySix=["Clerwood","Seton Sands","Tranent"]
TwentySeven=["Sliverknowes","Hunter's Tryst"]
TwentyNine=["Silverknowes","Gorebridge"]
Thirty=["Clovenstone","Musselburgh"]
ThirtyOne=["East Craigs","Bonnyrig","Polton Mill"]
ThirtyThree=["Wester Hailes","Millerhill"]
ThirtyFour=["Heriot Watt University","Ocean Terminal"]
ThirtySix=["Gyle Centre","Ocean Terminal"]
ThirtySeven=["Silverknowes","Penicuik","Easter Bush"]
FourtyOne=["Cramond","King's Buildings"]
FourtyTwo=["Craigleith","King's Road"]
FourtyFour=["Balerno","Wallyford"]
FourtyFive=["Heroit Watt University","Queen Margaret University"]
FourtySeven=["Granton","Penicuik"]
FourtyNine=["Fort Kinnaird","Rosewell"]
XEighteen=["Whitburn"]
XTwentySeven=["Whitburn"]
XTwentyEight=["Bathgate"]
FourtyThree=["Queensferry"]
HundredAndFour=["Haddington"]
XSeven=["Dunbar"]
HundredAndThirteen=["Pentcaitland","West Granton"]
HundredAndTwentyFour=["North Berwick"]
Tram=["Edinburgh Airport"]

#Picking a random direction
if RS==1:
    dest=(random.choice(One))

if RS==2:
    dest=(random.choice(Two))

if RS==3:
    dest=(random.choice(Three))

if RS==4:
    dest=(random.choice(Four))

if RS==5:
    dest=(random.choice(Five))

if RS==6:
    dest=(random.choice(Six))

if RS==7:
    dest=(random.choice(Seven))

if RS==8:
    dest=(random.choice(Eight))

if RS==10:
    dest=(random.choice(Ten))

if RS==11:
    dest=(random.choice(Eleven))

if RS==12:
    dest=(random.choice(Twelve))

if RS==14:
    dest=(random.choice(Fourteen))

if RS==15:
    dest=(random.choice(Fifteen))

if RS==16:
    dest=(random.choice(Sixteen))

if RS==19:
    dest=(random.choice(Nineteen))

if RS==22:
    dest=(random.choice(TwentyTwo))

if RS==23:
    dest=(random.choice(TwentyThree))

if RS==24:
    dest=(random.choice(TwentyFour))

if RS==25:
    dest=(random.choice(TwentyFive))

if RS==26:
    dest=(random.choice(TwentySix))

if RS==27:
    dest=(random.choice(TwentySeven))

if RS==29:
    dest=(random.choice(TwentyNine))

if RS==30:
    dest=(random.choice(Thirty))

if RS==31:
    dest=(random.choice(ThirtyOne))

if RS==33:
    dest=(random.choice(ThirtyThree))

if RS==34:
    dest=(random.choice(ThirtyFour))

if RS==36:
    dest=(random.choice(ThirtySix))

if RS==37:
    dest=(random.choice(ThirtySeven))

if RS==41:
    dest=(random.choice(FourtyOne))

if RS==42:
    dest=(random.choice(FourtyTwo))

if RS==43:
    dest=(random.choice(FourtyThree))

if RS==44:
    dest=(random.choice(FourtyFour))

if RS==45:
    dest=(random.choice(FourtyFive))

if RS==47:
    dest=(random.choice(FourtySeven))

if RS==49:
    dest=(random.choice(FourtyNine))

if RS=="X18":
    dest=(random.choice(XEighteen))

if RS=="X27":
    dest=(random.choice(XTwentySeven))

if RS=="X28":
    dest=(random.choice(XTwentyEight))

if RS==104:
    dest=(random.choice(HundredAndFour))

if RS=="X7":
    dest=(random.choice(XSeven))

if RS==113:
    dest=(random.choice(HundredAndThirteen))

if RS==124:
    dest=(random.choice(HundredAndTwentyFour))

if RS=="Tram":
    dest=(random.choice(Tram))


# Printing the final Line, Route and Destination.
if RS=="X18" or RS=="X27" or RS=="X28" or RS==43:
    print("The Random Route is Lothiancountry",RS)
    print("You're off to",dest)

elif RS=="Tram":
    print("You're going on a Tram")
    print("You're going to Edinburgh Airport")

elif RS==104 or RS=="X7" or RS==113 or RS==124:
    print("The Random Route is EastCoastbuses",RS)
    print("You're off to",dest)

else:
    print("The Random Route is Lothian Buses",RS)
    print("You're going to",dest)