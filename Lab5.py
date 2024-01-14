def BMI(waga, wzrost):
    bmi= waga/(wzrost*wzrost)
    if bmi<=18.5:
        print("Niedowaga, BMI=", bmi)
    elif 18.5 <bmi < 24.9:
        print("Norma, BMI=", bmi)
    elif 25< bmi< 30:
        print("Nadwaga, BMI=", bmi)
    else:
        print("Otyłość, BMI=", bmi)
BMI(90, 1.6)
