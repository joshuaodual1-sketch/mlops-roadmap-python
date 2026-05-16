def main():
    time = input("What time is it? ").strip()
   #GETS INPUT FROM USER
    converted_time = convert(time)
    if 7.0 <= converted_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= converted_time <= 13.0:
        print("lunch time")
    elif 18.0 <= converted_time <= 19.0:
        print("dinner time")
        

def convert(time_str):
    hours, minutes = time_str.split(":")
    return float(hours) + float(minutes) / 60
#CONVERTS TIME TO FLOAT


if __name__ == "__main__":
    main()
