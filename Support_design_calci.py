print("--------*******--------********-------------**********------------*******---------")

rmr = []
ltr = struct_rating = rsr = b = b_g = sdr = gsr = 0
fos_g = fos_j = Rock_load_Gallery = Rock_load_Junction = 0

i = 0
while i < 2:

    while True:
        lt = float(input("Enter your LAYER THICKNESS(in CM)[0-100]:  "))
        try:
            if 0 <= lt < 0.4:
                ltr = 0
                print("Layer thickness Rating is ", ltr)
            elif 0.4 <= lt < 0.8:
                ltr = 1
                print("Layer thickness Rating is ", ltr)
            elif 0.8 <= lt < 1.2:
                ltr = 3
                print("Layer thickness Rating is ", ltr)
            elif 1.2 <= lt < 1.6:
                ltr = 4
                print("Layer thickness Rating is ", ltr)
            elif 1.6 <= lt < 2.0:
                ltr = 4
                print("Layer thickness Rating is ", ltr)
            elif 2 <= lt < 2.5:
                ltr = 5
                print("Layer thickness Rating is ", ltr)
            elif 2.5 <= lt < 3.3:
                ltr = 6
                print("Layer thickness Rating is ", ltr)
            elif 3.3 <= lt < 3.7:
                ltr = 7
                print("Layer thickness Rating is ", ltr)
            elif 3.7 <= lt < 4.3:
                ltr = 8
                print("Layer thickness Rating is ", ltr)
            elif 4.3 <= lt < 5.0:
                ltr = 9
                print("Layer thickness Rating is ", ltr)
            elif 5.0 <= lt < 5.6:
                ltr = 10
                print("Layer thickness Rating is ", ltr)
            elif 5.6 <= lt < 6.2:
                ltr = 11
                print("Layer thickness Rating is ", ltr)
            elif 6.2 <= lt < 6.5:
                ltr = 12
                print("Layer thickness Rating is ", ltr)
            elif 6.5 <= lt < 7.5:
                ltr = 13
                print("Layer thickness Rating is ", ltr)
            elif 7.5 <= lt < 9.0:
                ltr = 14
                print("Layer thickness Rating is ", ltr)
            elif 9 <= lt < 10.5:
                ltr = 15
                print("Layer thickness Rating is ", ltr)
            elif 10.5 <= lt < 12:
                ltr = 16
                print("Layer thickness Rating is ", ltr)
            elif 12 <= lt < 13.6:
                ltr = 17
                print("Layer thickness Rating is ", ltr)
            elif 13.6 <= lt < 15.3:
                ltr = 18
                print("Layer thickness Rating is ", ltr)
            elif 15.3 <= lt < 17:
                ltr = 19
                print("Layer thickness Rating is ", ltr)
            elif 17 <= lt < 19:
                ltr = 20
                print("Layer thickness Rating is ", ltr)
            elif 19 <= lt < 22:
                ltr = 21
                print("Layer thickness Rating is ", ltr)
            elif 22 <= lt < 25:
                ltr = 22
                print("Layer thickness Rating is ", ltr)
            elif 25 <= lt < 30:
                ltr = 23
                print("Layer thickness Rating is ", ltr)
            elif 30 <= lt < 35:
                ltr = 24
                print("Layer thickness Rating is ", ltr)
            elif 35 <= lt < 40:
                ltr = 25
                print("Layer thickness Rating is ", ltr)
            elif 40 <= lt < 45:
                ltr = 26
                print("Layer thickness Rating is ", ltr)
            elif 45 <= lt < 50:
                ltr = 27
                print("Layer thickness Rating is ", ltr)
            elif 50 <= lt < 60:
                ltr = 28
                print("Layer thickness Rating is ", ltr)
            elif 60 <= lt < 75:
                ltr = 29
                print("Layer thickness Rating is ", ltr)
            elif 75 <= lt <= 100:
                ltr = 30
                print("Layer thickness Rating is ", ltr)
            else:
                print(f"Invalid Input \nYour Input {lt}\nPlease Enter the Layer Thickness in [0-100]cm")
                continue
            break
        except ValueError:
            print("Invalid Input")

    print("--------*******--------********-------------**********------------*******---------")
    while True:
        sti = float(input("Enter your STRUCTURAL Indices[0-16]:  "))
        try:
            if sti == 16:
                struct_rating = 1
                print("Your Structural Rating is ", struct_rating)
            elif sti == 15:
                struct_rating = 3
                print("Your Structural Rating is ", struct_rating)
            elif sti == 14:
                struct_rating = 5
                print("Your Structural Rating is ", struct_rating)
            elif sti == 13:
                struct_rating = 7
                print("Your Structural Rating is ", struct_rating)
            elif sti == 12:
                struct_rating = 8
                print("Your Structural Rating is ", struct_rating)
            elif sti == 11:
                struct_rating = 9
                print("Your Structural Rating is ", struct_rating)
            elif sti == 10:
                struct_rating = 11
                print("Your Structural Rating is ", struct_rating)
            elif sti == 9:
                struct_rating = 12
                print("Your Structural Rating is ", struct_rating)
            elif sti == 8:
                struct_rating = 13
                print("Your Structural Rating is ", struct_rating)
            elif sti == 7:
                struct_rating = 14
                print("Your Structural Rating is ", struct_rating)
            elif sti == 6:
                struct_rating = 16
                print("Your Structural Rating is ", struct_rating)
            elif sti == 5:
                struct_rating = 17
                print("Your Structural Rating is ", struct_rating)
            elif sti == 4:
                struct_rating = 19
                print("Your Structural Rating is ", struct_rating)
            elif sti == 3:
                struct_rating = 21
                print("Your Structural Rating is ", struct_rating)
            elif sti == 2:
                struct_rating = 23
                print("Your Structural Rating is ", struct_rating)
            elif sti == 1:
                struct_rating = 24
                print("Your Structural Rating is ", struct_rating)
            elif sti == 0:
                struct_rating = 25
                print("Your Structural Rating is ", struct_rating)
            else:
                print(f"Invalid Input \nYour Input {sti}\nPlease Enter the Structural Rating again in [0-16]cm")
                continue
            break
        except ValueError:
            print("Invalid Input")
    print("--------*******--------********-------------**********------------*******---------")
    while True:
        sld = float(input("Enter your SLAKE DURABILITY(I) index % [0-100]:  "))
        try:
            if 0 <= sld < 30:
                sdr = 0
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif 30 <= sld < 40:
                sdr = 1
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif 40 <= sld < 50:
                sdr = 2
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif 50 <= sld < 60:
                sdr = 3
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif 60 <= sld < 65:
                sdr = 4
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif 65 <= sld < 70:
                sdr = 5
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif 70 <= sld < 75:
                sdr = 6
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif 75 <= sld < 80:
                sdr = 7
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif 80 <= sld < 85:
                sdr = 8
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif 85 <= sld < 87.4:
                sdr = 9
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif 87.4 <= sld < 89:
                sdr = 10
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif 89 <= sld < 92.2:
                sdr = 11
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif 92.2 <= sld < 94.6:
                sdr = 12
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif 94.6 <= sld < 97:
                sdr = 13
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif 97 <= sld < 97.5:
                sdr = 14
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif 97.5 <= sld < 98:
                sdr = 15
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif 98 <= sld < 98.5:
                sdr = 16
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif 98.5 <= sld < 99:
                sdr = 17
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif sld >= 99.3 > sld:
                sdr = 18
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif 99.3 <= sld < 99.6:
                sdr = 19
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))
            elif sld == 100:
                sdr = 20
                print("Your Slake Durability Rating for {} % is {} ".format(sld, sdr))

            else:
                print(f"Invalid Input \nYour Input {sld}\nPlease Enter the Slake Durability rating in [0-100]")
                continue
            break
        except ValueError:
            print("Invalid Input")
    print("--------*******--------********-------------**********------------*******---------")

    while True:

        rst = float(input("Enter your Rock STRENGTH (kg/cm²):  "))
        try:

            if 30 > rst >= 0:

                rsr = 0
                print("Rock Strength Rating at {} kg/cm² is {}".format(rst, rsr))
            elif 30 <= rst < 65:
                rsr = 1
                print("Rock Strength Rating at {} kg/cm² is {}".format(rst, rsr))
            elif 65 <= rst < 100:
                rsr = 2
                print("Rock Strength Rating at {} kg/cm² is {}".format(rst, rsr))
            elif 100 <= rst < 150:
                rsr = 3
                print("Rock Strength Rating at {} kg/cm² is {}".format(rst, rsr))
            elif 150 <= rst < 200:
                rsr = 4
                print("Rock Strength Rating at {} kg/cm² is {}".format(rst, rsr))
            elif 200 <= rst < 250:
                rsr = 5
                print("Rock Strength Rating at {} kg/cm² is {}".format(rst, rsr))
            elif 250 <= rst < 300:
                rsr = 6
                print("Rock Strength Rating at {} kg/cm² is {}".format(rst, rsr))
            elif 300 <= rst < 375:
                rsr = 7
                print("Rock Strength Rating at {} kg/cm² is {}".format(rst, rsr))
            elif 375 <= rst < 450:
                rsr = 8
                print("Rock Strength Rating at {} kg/cm² is {}".format(rst, rsr))
            elif 450 <= rst < 525:
                rsr = 9
                print("Rock Strength Rating at {} kg/cm² is {}".format(rst, rsr))
            elif 525 <= rst < 600:
                rsr = 10
                print("Rock Strength Rating at {} kg/cm² is {}".format(rst, rsr))
            elif 600 <= rst < 700:
                rsr = 11
                print("Rock Strength Rating at {} kg/cm² is {}".format(rst, rsr))
            elif 700 <= rst < 800:
                rsr = 12
                print("Rock Strength Rating at {} kg/cm² is {}".format(rst, rsr))
            elif 800 <= rst < 900:
                rsr = 13
                print("Rock Strength Rating at {} kg/cm² is {}".format(rst, rsr))
            elif 900 <= rst < 1500:
                rsr = 14
                print("Rock Strength Rating at {} kg/cm² is {}".format(rst, rsr))
            elif rst >= 1500:
                rsr = 15
                print("Rock Strength Rating at {} kg/cm² is {}".format(rst, rsr))
            else:
                print(f"Invalid input Rock Strength must be positive\nYou Entered {rst}")
                continue
            break
        except ValueError:
            print("Invalid Input")

    print("--------*******--------********-------------**********------------*******---------")
    while True:

        print("Press 0 for dry ground surface")
        grs = float(input("enter your GROUND SEEPAGE (ml/min):  "))
        try:
            if grs > 5000:
                gsr = 0
                print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
            elif 2000 < grs <= 5000:
                gsr = 1
                print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
            elif 800 < grs <= 2000:
                gsr = 2
                print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
            elif 300 < grs <= 800:
                gsr = 3
                print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
            elif 200 < grs <= 300:
                gsr = 4
                print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
            elif 140 < grs <= 200:
                gsr = 5
                print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
            elif 80 < grs <= 140:
                gsr = 6
                print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
            elif 20 < grs <= 80:
                gsr = 7
                print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
            elif 10 < grs <= 20:
                gsr = 8
                print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
            elif 0 < grs <= 10:
                gsr = 9
                print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
            elif grs == 0:
                gsr = 10
                print("Wow dry ground seepage\ngreat")
                print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
            else:
                print("GRS Input cant be Negative \nEnter the Value again!!")
                continue
            break
        except ValueError:
            print("Invalid Input")
    print("--------*******--------********-------------**********------------*******---------")

    rmr.append(ltr + struct_rating + sdr + rsr + gsr)

    i += 1

print("RMR of Coal/Metal is", rmr[0])
print("Rmr of Shale/Sandstone is", rmr[1])
print("--------*******--------********-------------**********------------*******---------")
print("We have to find the COMBINED RMR!! ")
t1 = float(input("Enter the overlying strata of Coal or Metal mine(m): "))
t2 = float(input("Enter the intermediate roof strata of shale/sandstone/else: "))
while True:
    t3 = float(input("Enter the Gallery Span Width (m): "))
    try:
        if 6 >= t3 >= 4.8:
            pass
        else:
            print("You Entered Abrupt data for Gallery\nIt must be in [4.8-6]m as per Indian Guidelines")
            continue
        break
    except ValueError:
        print("Invalid Input")

crmr = ((rmr[0] * t1) + (rmr[1] * (t3 - t1))) / t3
print("Combined RMR is {}".format(format(crmr, '0.2f')))

print("--------*******--------********-------------**********------------*******---------")
print("Now we have to Calculate Adjusted RMR")
depth = float(input("Enter the depth(in m):  "))
if depth < 250:
    armr = crmr * 1
elif 250 <= depth < 400:
    armr = crmr * 0.9
elif 400 <= depth < 600:
    armr = crmr * 0.8
else:
    armr = crmr * 0.7
print("ARMR AFTER DEPTH calculation is {} ".format(format(armr, '0.2f')))
print("--------*******--------********-------------**********------------*******---------")

print("CONDITIONS FOR LATERAL STRESS!!!!")
print("Press 1 for SMALL STRESS\nPress 2 for MEDIUM STRESS\nPress 3 for HIGH STRESS ")
while True:
    lateral_stress = float(input("Press 1 OR 2 OR 3 according to your data:  "))
    try:

        if lateral_stress == 1:
            armr = armr * 0.9
        elif lateral_stress == 2:
            armr = armr * 0.8
        elif lateral_stress == 3:
            armr = armr * 0.7
        else:
            print("Invalid Input\nPlease Enter 1 or 2 or 3")
            continue
        break
    except ValueError:
        print("Invalid Input")
print("ARMR after including lateral stress is {}".format(format(armr, '0.2f')))
print("--------*******--------********-------------**********------------*******---------")
print("CONDITION FOR INDUCED STRESS!!!")
print("Press 1 for NO ADJACENT WORKING IN THE SEAM\nPress 2 for EXTRACTION AREA WITHIN 20-40 m IN THE SAME SEAM\n"
      "Press 3 for EXTRACTION AREA WITHIN 10-20m in the same seam\nPress 4 for working with 10-20m parting\n"
      "Press 5 for working within 3 - 10m parting\nPress 6 if you dont have this data")
while True:
    induced_stress = float(input("Press THE INDUCED STRESS CONDITION CAREFULLY:  "))
    try:
        if induced_stress == 1:
            armr = armr * 1
        elif induced_stress == 2:
            armr = armr * 0.9
        elif induced_stress == 3:
            armr = armr * 0.75
        elif induced_stress == 4:
            armr = armr * 0.9
        elif induced_stress == 5:
            armr = armr * 0.75
        elif induced_stress == 6:
            print("For Unknown Induced Stress ARMR reduced by 25%")
            # print("Please Press the respective key:  ")
            armr = armr * 0.75
        else:
            print("Invalid Input")
            continue
        break
    except ValueError:
        print("Invalid data")
print("ARMR after including INDUCED STRESS is {}".format(format(armr, '0.2f')))
print("--------*******--------********-------------**********------------*******---------")
print("CONDITIONS FOR METHOD OF WORKING")
print("Press 1 for MECHANISED WORKING OR CONTINUOUS MINER\nPress 2 for UNDERCUT AND BLASTING\n"
      "Press 3 for BLASTING OFF THE SOLID\nPress 4 if you dont know  ")
while True:
    method_excavation = float(input("Press THE RESPECTIVE KEY CAREFULLY:  "))
    try:
        if method_excavation == 1:
            armr = armr * 1.1
        elif method_excavation == 2:
            armr = armr * 1
        elif method_excavation == 3:
            armr = armr * 0.9
        elif method_excavation == 4:
            print("PROGRAM GOT TO KNOW THAT YOU DONT HAVE THIS DATA\nSO ARMR  reduced by 15%")
            armr = armr * 0.85
        else:
            print("Invalid Input\nEnter the Respective Value again!!")
            continue
        break

    except ValueError:
        print("Invalid Input")

print("ARMR after including METHOD OF EXCAVATION is {}".format(format(armr, '0.2f')))

print("--------*******--------********-------------**********------------*******---------")
Gallery_span = t3 * 1
print('Gallery Span Already Entered is {} m'.format(t3))
if Gallery_span < 4.8:
    armr = armr * 1
elif 4.8 <= Gallery_span <= 6:
    armr = armr * 0.85
else:
    print("ok value will calculated without Gallery_span data")
print("ARMR after including Gallery calculation is {}".format(format(armr, '0.2f')))
print("--------*******--------********-------------**********------------*******---------")

if 90 < armr <= 100.0:
    print("your rmr is {}".format(format(armr, '0.2f')))
    print("EXCELLENT Rock")
elif 80 <= armr <= 90:
    print("Your rmr is {}".format(format(armr, '0.2f')))
    print("VERY GOOD STRATA")
elif 60 < armr < 80:
    print("Your rmr is {} ".format(format(armr, '0.2f')))
    print("GOOD STRATA")
elif 40 < armr <= 60:
    print("Your rmr is {} ".format(format(armr, '0.2f')))
    print("FAIR STRATA")
elif 20 < armr <= 40:
    print("Your rmr is {}".format(format(armr, '0.2f')))
    print("POOR STRATA")
elif 0 < armr <= 20:
    print("Your rmr is less than 20")
    print("VERY POOR STRATA")
else:
    print("Armr is {} ".format(format(armr, '0.2f')))
    print("VALUE ABSURD")
    print("RMR CAN'T BE GREATER THAN 100")
    print("MEASURE RMR INDICES AGAIN")
print("--------*******--------********-------------**********------------*******---------")
print("CALCULATING Rock LOAD....")
print("Press 1 for COAL MINE")
print("Press 2 for METAL MINE")

while True:

    Rock_l = int(input("Enter the respective key for the Rock load: "))
    mean_density = float(input("Enter the mean density (t/m^3): "))
    try:
        if Rock_l == 1:
            print("You selected the coal mine")
            # Gallery_span = float(input("Enter the Gallery span: "))
            print('Gallery Span Already Entered is {} m'.format(t3))
            r_load_height = t3 * (1.7 - 0.037 * armr + 0.0002 * armr ** 2)
            print("Rock LOAD HEIGHT is {} m".format(format(r_load_height, '.2f')))
            Rock_load_Gallery = mean_density * r_load_height
            print("Rock load based on Indian RMR")
            print("Rock load at Gallery {} t/m2:".format(format(Rock_load_Gallery, '.2f')))
            Rock_load_Junction = mean_density * r_load_height * 1.414
            print("Rock load at Junction {} t/m2:".format(format(Rock_load_Junction, '.2f')))
            print("Good luck!")
        elif Rock_l == 2:
            print("You selected the METAL MINE")
            # Gallery_span = float(input("Enter the Gallery span: "))
            print('Gallery Span Already entered is {} m'.format(t3))
            Rock_load_Gallery = ((100 - armr) / armr) * t3 * mean_density
            print("Rock load at Gallery is {} t/m2".format(format(Rock_load_Gallery, '.2f')))
            Rock_load_Junction = Rock_load_Gallery * 1.414
            print("Rock load at Junction is {} t/m2".format(format(Rock_load_Junction, '.2f')))
            print("All the best!")
        else:
            print("!!! WRONG KEY SELECTION\nInput Valid Key!!")
            continue
        break
    except ValueError:
        print("Invalid Input")
print("--------*******--------********------SUPPORT DESIGN--------**********------------*******---------")
print('Press 1 for Support Design For Gallery')
print("Press other than 1 for exit ")


support_design = float(input('Enter the value carefully:  '))
# fos =0.0

if support_design == 1:
    # fos = 0.0
    while True:
        try:
            print('Calculating support design...')
            print('Calculating Number of Bolts for Gallery')
            print("Press 1 for Cement Capsule = 6 tonne\nPress 2 for Resin Bolt = 10 tonne\nPress 3 for your Input")
            support = int(input('Enter Your Input Carefully: '))
            if support == 1:
                no_of_Bolts_Gallery = (t3 * Rock_load_Gallery) / 6
                no_of_Bolts_Gallery = round(no_of_Bolts_Gallery)
                print("Number of Bolts is {}".format(no_of_Bolts_Gallery))
                print("Calculating Spacings....")
                Bolts_spacing_Gallery = t3 / no_of_Bolts_Gallery
                print('Spacing Between Bolts in Gallery is {} m'.format(format(Bolts_spacing_Gallery, '0.2f')))
                support_load_provided = (no_of_Bolts_Gallery * 6) / (t3 * Bolts_spacing_Gallery)
                print("Support Load Provided is {}t/m2".format(format(support_load_provided, '0.2f')))
                print("Rock Load in Gallery is {}t/m2".format(format(Rock_load_Gallery, '0.2f')))
                fos_g = support_load_provided / Rock_load_Gallery
                while not (1.6 <= fos_g <= 2.0):
                    # b =  int(input("Enter Number of Bolts greater/less than {}:  ".format(no_of_Bolts_Gallery)))
                    if fos_g <= 1.6:
                        b_g: int = int(input("Enter Number of Bolts greater than {}:  ".format(no_of_Bolts_Gallery)))
                        print("Your Input: {}".format(b_g))
                    elif fos_g >= 2.0:
                        b_g: int = int(input("Enter Number of Bolts greater than {}:  ".format(no_of_Bolts_Gallery)))
                        print("Your Input: {}".format(b_g))
                    Bolts_spacing_Gallery = t3 / b_g
                    print('Spacing Between Bolts in Gallery is {} m'.format(format(Bolts_spacing_Gallery, '0.2f')))
                    support_load_provided = (b_g * 6) / (t3 * Bolts_spacing_Gallery)
                    print("Support Load Provided is {}t/m2".format(format(support_load_provided, '0.2f')))
                    print("Rock Load in Gallery is {}t/m2".format(format(Rock_load_Gallery, '0.2f')))
                    fos_g = support_load_provided / Rock_load_Gallery
                    if fos_g > 2:
                        print("Current FOS is {}".format(format(fos_g, '0.2f')))
                        print("Your Input: {}".format(b_g))
                        print("Decrease Number of Bolts than {}".format(b_g))
                    elif fos_g < 1.6:
                        print("Current FOS is {}".format(format(fos_g, '0.2f')))
                        print("Your Input: {}".format(b_g))
                        print("Increase Number of Bolts than {} ".format(b_g))

                print("Factor of Safety is {}".format(format(fos_g, '0.2f')))
                print("Number of Bolts Required At Gallery is {}".format(b_g))

            elif support == 2:
                no_of_Bolts_Gallery = (t3 * Rock_load_Gallery) / 10
                no_of_Bolts_Gallery = round(no_of_Bolts_Gallery)
                print("Number of Bolts is {}".format(no_of_Bolts_Gallery))
                print("Calculating Spacings....")
                Bolts_spacing_Gallery = t3 / no_of_Bolts_Gallery
                print('Spacing Between Bolts in Gallery is {} m'.format(format(Bolts_spacing_Gallery, '0.2f')))
                support_load_provided = (no_of_Bolts_Gallery * 10) / (t3 * Bolts_spacing_Gallery)
                print("Support Load Provided is {}t/m2".format(format(support_load_provided, '0.2f')))
                print("Rock Load in Gallery is {}t/m2".format(format(Rock_load_Gallery, '0.2f')))
                fos_g = support_load_provided / Rock_load_Gallery
                while not (1.6 <= fos_g <= 2.0):
                    # b =  int(input("Enter Number of Bolts greater/less than {}:  ".format(no_of_Bolts_Gallery)))
                    if fos_g <= 1.6:
                        b_g = int(input("Enter Number of Bolts greater than {}:  ".format(no_of_Bolts_Gallery)))
                        print("Your Input: {}".format(b_g))
                    elif fos_g >= 2.0:
                        b_g = int(input("Enter Number of Bolts less than {}:  ".format(no_of_Bolts_Gallery)))
                        print("Your Input: {}".format(b_g))
                    Bolts_spacing_Gallery = t3 / b_g
                    print('Spacing Between Bolts in Gallery is {} m'.format(format(Bolts_spacing_Gallery, '0.2f')))
                    support_load_provided = (b_g * 10) / (t3 * Bolts_spacing_Gallery)
                    print("Support Load Provided is {}t/m2".format(format(support_load_provided, '0.2f')))
                    print("Rock Load in Gallery is {}t/m2".format(format(Rock_load_Gallery, '0.2f')))
                    fos_g = support_load_provided / Rock_load_Gallery
                    if fos_g > 2:
                        print("Current FOS is {}".format(format(fos_g, '0.2f')))
                        print("Your Input: {}".format(b_g))
                        print("Decrease Number of Bolts than {}".format(b_g))
                    elif fos_g < 1.6:
                        print("Current FOS is {}".format(format(fos_g, '0.2f')))
                        print("Increase Number of Bolts than {}".format(b_g))
                print("Factor of Safety is {}".format(format(fos_g, '0.2f')))
                print("Number of Bolts Required At Gallery is {}".format(b_g))
            elif support == 3:
                a = float(input("Enter the loading capacity in tonne:  "))
                no_of_Bolts_Gallery = (t3 * Rock_load_Gallery) / a
                no_of_Bolts_Gallery = round(no_of_Bolts_Gallery)
                print("Number of Bolts is {}".format(no_of_Bolts_Gallery))
                print("Calculating Spacings....")
                Bolts_spacing_Gallery = t3 / no_of_Bolts_Gallery
                print('Spacing Between Bolts in Gallery is {} m'.format(format(Bolts_spacing_Gallery, '0.2f')))
                support_load_provided = (no_of_Bolts_Gallery * a) / (t3 * Bolts_spacing_Gallery)
                print("Support Load Provided is {}t/m2".format(format(support_load_provided, '0.2f')))
                print("Rock Load in Gallery is {}t/m2".format(format(Rock_load_Gallery, '0.2f')))
                fos_g = support_load_provided / Rock_load_Gallery
                while not (1.6 <= fos_g <= 2.0):
                    # b = int(input("Enter Number of Bolts greater/less than {}:  ".format(no_of_Bolts_Gallery)))
                    if fos_g <= 1.6:
                        b_g = int(input("Enter Number of Bolts greater than {}:  ".format(no_of_Bolts_Gallery)))
                        print("Your Input: {}".format(b_g))
                    elif fos_g >= 2.0:
                        b_g = int(input("Enter Number of Bolts less than {}:  ".format(no_of_Bolts_Gallery)))
                        print("Your Input: {}".format(b_g))
                    Bolts_spacing_Gallery = t3 / b_g
                    print('Spacing Between Bolts in Gallery is {} m'.format(format(Bolts_spacing_Gallery, '0.2f')))
                    support_load_provided = (b_g * a) / (t3 * Bolts_spacing_Gallery)
                    print("Support Load Provided is {}t/m2".format(format(support_load_provided, '0.2f')))
                    print("Rock Load in Gallery is {}t/m2".format(format(Rock_load_Gallery, '0.2f')))
                    fos_g = support_load_provided / Rock_load_Gallery
                    if fos_g > 2:
                        print("Current FOS is {}".format(format(fos_g, '0.2f')))
                        print("Decrease Number of Bolts than {}".format(b_g))
                    elif fos_g < 1.6:
                        print("Current FOS is {}".format(format(fos_g, '0.2f')))
                        print("Increase Number of Bolts than {}".format(b_g))
                print("Factor of Safety at Gallery is {}".format(format(fos_g, '0.2f')))
                print("Number of Bolts Required At Gallery is {}".format(b_g))
            else:
                print("Enter Valid Digit Again!! ")
                continue
            break
        except ValueError:
            print("Invalid Input")


else:
    exit(0)
print("--------*******--------********-------------**********------------*******---------")
print("Press 1 For Calculating Support Design For Junction")
print("Press Any other Key for Exit")
support_j = int(input("Enter the key carefully:  "))
if support_j == 1:
    while True:
        try:
            print("Calculating Support Design FOr Junction....")
            print("Press 1 for Cement Capsule = 6 tonne\nPress 2 for Resin Bolt = 10 tonne\nPress 3 for your Input")
            support_ = int(input('Enter Your Input Carefully: '))
            if support_ == 1:
                no_of_Bolts_Junction = (t3 * t3 * Rock_load_Junction) / 6
                no_of_Bolts_Junction = pow(no_of_Bolts_Junction, 0.5)
                no_of_Bolts_Junction = round(no_of_Bolts_Junction)
                no_of_Bolts_Junction = pow(no_of_Bolts_Junction, 2)
                no_of_Bolts_Junction_row = pow(no_of_Bolts_Junction, 0.5)
                print("Number of Bolts at Junction is {}".format(no_of_Bolts_Junction))
                print("Number of Bolts in a row at Junction is {}".format(no_of_Bolts_Junction_row))
                print("Calculating Spacings....")
                Bolts_spacing_Junction = t3 / no_of_Bolts_Junction_row
                print('Spacing Between Bolts in Junction is {} m'.format(format(Bolts_spacing_Junction, '0.2f')))
                support_load_provided = (no_of_Bolts_Junction * 6) / (t3 * t3)
                print("Support Load Provided is {}t/m2".format(format(support_load_provided, '0.2f')))
                print("Rock Load in Junction is {}t/m2".format(format(Rock_load_Junction, '0.2f')))
                fos_j = support_load_provided / Rock_load_Junction
                while not (1.6 <= fos_j <= 2.0):
                    # b = int(input("Enter Number of Bolts greater/less than {}:  ".format(no_of_Bolts_Junction_row)))
                    if fos_j <= 1.6:
                        b = int(input("Enter Number of Bolts greater than {}:  ".format(no_of_Bolts_Junction_row)))
                        print("Your Input: {}".format(b))
                    elif fos_j >= 2.0:
                        b = int(input("Enter Number of Bolts less than {}:  ".format(no_of_Bolts_Junction_row)))
                        print("Your Input: {}".format(b))
                    Bolts_spacing_Junction = t3 / b
                    print('Spacing Between Bolts in Gallery is {} m'.format(format(Bolts_spacing_Junction, '0.2f')))
                    support_load_provided = (b * 6) / (t3 * Bolts_spacing_Junction)
                    print("Support Load Provided is {}t/m2".format(format(support_load_provided, '0.2f')))
                    print("Rock Load in Gallery is {}t/m2".format(format(Rock_load_Junction, '0.2f')))
                    fos_j = support_load_provided / Rock_load_Junction
                    if fos_j > 2:
                        print("Current FOS is {}".format(format(fos_j, '0.2f')))
                        print("Decrease Number of Bolts than {}".format(b))
                    elif fos_j < 1.6:
                        print("Current FOS is {}".format(format(fos_j, '0.2f')))
                        print("Increase Number of Bolts than {} ".format(b))
                print("Factor of Safety is {}".format(format(fos_j, '0.2f')))
                print("Number of Bolts Required At Junction is {}X{} is {}".format(b, b, pow(b, 2)))

            elif support_ == 2:
                no_of_Bolts_Junction = (t3 * t3 * Rock_load_Junction) / 10
                no_of_Bolts_Junction = pow(no_of_Bolts_Junction, 0.5)
                no_of_Bolts_Junction = round(no_of_Bolts_Junction)
                no_of_Bolts_Junction = pow(no_of_Bolts_Junction, 2)
                no_of_Bolts_Junction_row = pow(no_of_Bolts_Junction, 0.5)
                print("Number of Bolts at Junction is {}".format(no_of_Bolts_Junction))
                print("Number of Bolts in a row at Junction is {}".format(no_of_Bolts_Junction_row))
                print("Calculating Spacings....")
                Bolts_spacing_Junction = t3 / no_of_Bolts_Junction_row
                print('Spacing Between Bolts in Junction is {} m'.format(format(Bolts_spacing_Junction, '0.2f')))
                support_load_provided = (no_of_Bolts_Junction * 10) / (t3 * t3)
                print("Support Load Provided is {}t/m2".format(format(support_load_provided, '0.2f')))
                print("Rock Load in Junction is {}t/m2".format(format(Rock_load_Junction, '0.2f')))
                fos_j = support_load_provided / Rock_load_Junction
                while not (1.6 <= fos_j <= 2.0):
                    # b = int(input("Enter Number of Bolts greater/less than {}:  ".format(no_of_Bolts_Junction_row)))
                    if fos_j <= 1.6:
                        b = int(input("Enter Number of Bolts greater than {}:  ".format(no_of_Bolts_Junction_row)))
                        print("Your Input: {}".format(b))
                    elif fos_j >= 2.0:
                        b = int(input("Enter Number of Bolts less than {}:  ".format(no_of_Bolts_Junction_row)))
                        print("Your Input: {}".format(b))
                    Bolts_spacing_Junction = t3 / b
                    print('Spacing Between Bolts in Gallery is {} m'.format(format(Bolts_spacing_Junction, '0.2f')))
                    support_load_provided = (b * 10) / (t3 * Bolts_spacing_Junction)
                    print("Support Load Provided is {}t/m2".format(format(support_load_provided, '0.2f')))
                    print("Rock Load in Gallery is {}t/m2".format(format(Rock_load_Junction, '0.2f')))
                    fos_j = support_load_provided / Rock_load_Junction
                    if fos_j > 2:
                        print("Current FOS is {}".format(format(fos_j, '0.2f')))
                        print("Decrease Number of Bolts than {} ".format(b))
                    elif fos_j < 1.6:
                        print("Current FOS is {}".format(format(fos_j, '0.2f')))
                        print("Increase Number of Bolts than {}".format(b))
                print("Factor of Safety is {}".format(format(fos_j, '0.2f')))
                print("Number of Bolts Required At Junction is {}X{} is {}".format(b, b, pow(b, 2)))

            elif support_ == 3:
                a = float(input("Enter the loading capacity in tonne:  "))
                no_of_Bolts_Junction = (t3 * t3 * Rock_load_Junction) / a
                no_of_Bolts_Junction = pow(no_of_Bolts_Junction, 0.5)
                no_of_Bolts_Junction = round(no_of_Bolts_Junction)
                no_of_Bolts_Junction = pow(no_of_Bolts_Junction, 2)
                no_of_Bolts_Junction_row = pow(no_of_Bolts_Junction, 0.5)
                print("Number of Bolts at Junction is {}".format(no_of_Bolts_Junction))
                print("Number of Bolts in a row at Junction is {}".format(no_of_Bolts_Junction_row))
                print("Calculating Spacings....")
                Bolts_spacing_Junction = t3 / no_of_Bolts_Junction_row
                print('Spacing Between Bolts in Junction is {} m'.format(format(Bolts_spacing_Junction, '0.2f')))
                support_load_provided = (no_of_Bolts_Junction * a) / (t3 * t3)
                print("Support Load Provided is {}t/m2".format(format(support_load_provided, '0.2f')))
                print("Rock Load in Junction is {}t/m2".format(format(Rock_load_Junction, '0.2f')))
                fos_j = support_load_provided / Rock_load_Junction
                while not (1.6 <= fos_j <= 2.0):
                    # b = int(input("Enter Number of Bolts greater/less than {}:  ".format(no_of_Bolts_Junction_row)))
                    if fos_j <= 1.6:
                        b = int(input("Enter Number of Bolts greater than {}:  ".format(no_of_Bolts_Junction_row)))
                        print("Your Input: {}".format(b))
                    elif fos_j >= 2.0:
                        b = int(input("Enter Number of Bolts less than {}:  ".format(no_of_Bolts_Junction_row)))
                        print("Your Input: {}".format(b))
                    Bolts_spacing_Junction = t3 / b
                    print('Spacing Between Bolts in Junction is {} m'.format(format(Bolts_spacing_Junction, '0.2f')))
                    support_load_provided = (b * a) / (t3 * Bolts_spacing_Junction)
                    print("Support Load Provided is {}t/m2".format(format(support_load_provided, '0.2f')))
                    print("Rock Load in Junction is {}t/m2".format(format(Rock_load_Junction, '0.2f')))
                    fos_j = support_load_provided / Rock_load_Junction
                    if fos_j > 2:
                        print("Current FOS is {}".format(format(fos_j, '0.2f')))
                        print("Decrease Number of Bolts than {} ".format(b))

                    elif fos_j < 1.6:
                        print("Current FOS is {}".format(format(fos_j, '0.2f')))
                        print("Increase Number of Bolts than {}".format(b))
                print("Factor of Safety at junction is {}".format(format(fos_j, '0.2f')))
                print("Number of Bolts Required At Junction is {}X{} is {}".format(b, b, pow(b, 2)))

            else:
                print("Enter the Valid Input Again!!")
                continue
            break
        except ValueError:
            print("Invalid Input")
    print("***************---HENCE---WE--GOT---****************")
    print("Factor of Safety at Gallery is {}".format(format(fos_g, '0.2f')))
    print("Number of Bolts Required At Gallery is {}".format(b_g))
    print("Factor of Safety at Junction is {}".format(format(fos_j, '0.2f')))
    print("Number of Bolts Required At Junction is {}X{} is {}".format(b, b, pow(b, 2)))
else:
    exit(0)
