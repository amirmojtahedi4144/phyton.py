name1 = input("name1 plz enter your name:")
name2 = input ("name2 plz enter your name:")
name3 = input("name3 plz enter your name:")

country1 = input(f"{name1} where are you from:")
country2 = input(f"{name2} where are you from:")
country3  = input(f"{name3} where are you from:")

rank1 =int(input(f"{name1} from {country1} what is your rank ? "))
rank2 = int(input(f"{name2} from {country2} what is your rank ? "))
rank3 = int(input(f"{name3} from {country3} what is your rank ? "))

if  rank1 == 3 and rank2 == 1 and rank3 == 2: 
    print(f"{name3} in {country3} get gold medal")
    print(f"{name1} in {country1} get silver medal")
    print(f"{name2} in {country2} get boronz medal")
elif rank2 == 1:
    print(f"{name1} in  {country1} get silver medal")
elif rank3 == 2:
    print(f"{name2} in {country2} get boronz medal")