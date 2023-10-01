from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import datetime
print("--------*******--------********-------------**********------------*******---------")
ltr = struct_rating = rsr = b = b_g = sdr = gsr = Bolts_spacing_Junction = Bolts_spacing_Gallery = 0
rmr = []
ltr_r = []
struct_rating_r = []
rsr_r = []
sdr_r = []
gsr_r = []
armr_d = []
fos_g = fos_j = Rock_load_Gallery = Rock_load_Junction = 0
mine_name = input("Enter Mine Name: ").title()
location = input("Location of Mine: ").title()
owner = input("Owner of Mine: ").upper()
def select_mine_type():
    options = ['COAL', 'METAL']
    while True:
        print("Select the Mine Type:")
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        try:
            selected_index = int(input("Enter the number corresponding to your choice: "))
            if 1 <= selected_index <= len(options):
                selected_mine_type = options[selected_index - 1]
                print(f"You selected: {selected_mine_type} Mine")
                return selected_mine_type  # Return the selected mine type
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

mine_type = select_mine_type()
print(f"Mine Type: {mine_type}")
ore = input("Enter Ore Types: ").title()
def get_valid_input(prompt, lower_bound, upper_bound):
    while True:
        try:
            value = float(input(prompt))
            if lower_bound <= value <= upper_bound:
                return value
            else:
                print("Invalid Input. Enter again!")
        except ValueError:
            print("Invalid Input. Enter a numerical value.")
def calculate_layer_thickness_rating(lt):
    global ltr
    if 0 <= float(lt) < 0.4:
        ltr = 0
        print("Layer thickness Rating is ", ltr)
    elif 0.4 <= float(lt) < 0.8:
        ltr = 1
        print("Layer thickness Rating is ", ltr)
    elif 0.8 <= float(lt) < 1.2:
        ltr = 3
        print("Layer thickness Rating is ", ltr)
    elif 1.2 <= float(lt) < 1.6:
        ltr = 4
        print("Layer thickness Rating is ", ltr)
    elif 1.6 <= float(lt) < 2.0:
        ltr = 4
        print("Layer thickness Rating is ", ltr)
    elif 2 <= float(lt) < 2.5:
        ltr = 5
        print("Layer thickness Rating is ", ltr)
    elif 2.5 <= float(lt) < 3.3:
        ltr = 6
        print("Layer thickness Rating is ", ltr)
    elif 3.3 <= float(lt) < 3.7:
        ltr = 7
        print("Layer thickness Rating is ", ltr)
    elif 3.7 <= float(lt) < 4.3:
        ltr = 8
        print("Layer thickness Rating is ", ltr)
    elif 4.3 <= float(lt) < 5.0:
        ltr = 9
        print("Layer thickness Rating is ", ltr)
    elif 5.0 <= float(lt) < 5.6:
        ltr = 10
        print("Layer thickness Rating is ", ltr)
    elif 5.6 <= float(lt) < 6.2:
        ltr = 11
        print("Layer thickness Rating is ", ltr)
    elif 6.2 <= float(lt) < 6.5:
        ltr = 12
        print("Layer thickness Rating is ", ltr)
    elif 6.5 <= float(lt) < 7.5:
        ltr = 13
        print("Layer thickness Rating is ", ltr)
    elif 7.5 <= float(lt) < 9.0:
        ltr = 14
        print("Layer thickness Rating is ", ltr)
    elif 9 <= float(lt) < 10.5:
        ltr = 15
        print("Layer thickness Rating is ", ltr)
    elif 10.5 <= float(lt) < 12:
        ltr = 16
        print("Layer thickness Rating is ", ltr)
    elif 12 <= float(lt) < 13.6:
        ltr = 17
        print("Layer thickness Rating is ", ltr)
    elif 13.6 <= float(lt) < 15.3:
        ltr = 18
        print("Layer thickness Rating is ", ltr)
    elif 15.3 <= float(lt) < 17:
        ltr = 19
        print("Layer thickness Rating is ", ltr)
    elif 17 <= float(lt) < 19:
        ltr = 20
        print("Layer thickness Rating is ", ltr)
    elif 19 <= float(lt) < 22:
        ltr = 21
        print("Layer thickness Rating is ", ltr)
    elif 22 <= float(lt) < 25:
        ltr = 22
        print("Layer thickness Rating is ", ltr)
    elif 25 <= float(lt) < 30:
        ltr = 23
        print("Layer thickness Rating is ", ltr)
    elif 30 <= float(lt) < 35:
        ltr = 24
        print("Layer thickness Rating is ", ltr)
    elif 35 <= float(lt) < 40:
        ltr = 25
        print("Layer thickness Rating is ", ltr)
    elif 40 <= float(lt) < 45:
        ltr = 26
        print("Layer thickness Rating is ", ltr)
    elif 45 <= float(lt) < 50:
        ltr = 27
        print("Layer thickness Rating is ", ltr)
    elif 50 <= float(lt) < 60:
        ltr = 28
        print("Layer thickness Rating is ", ltr)
    elif 60 <= float(lt) < 75:
        ltr = 29
        print("Layer thickness Rating is ", ltr)
    else:
        ltr = 30
        print("Layer thickness Rating is ", ltr)
    ltr_r.append(ltr)
    return ltr
def calculate_structural_rating(sti):
    global struct_rating
    if int(sti) == 16:
        struct_rating = 1
        print("Your Structural Rating is ", struct_rating)
    elif int(sti) == 15:
        struct_rating = 3
        print("Your Structural Rating is ", struct_rating)
    elif int(sti) == 14:
        struct_rating = 5
        print("Your Structural Rating is ", struct_rating)
    elif int(sti) == 13:
        struct_rating = 7
        print("Your Structural Rating is ", struct_rating)
    elif int(sti) == 12:
        struct_rating = 8
        print("Your Structural Rating is ", struct_rating)
    elif int(sti) == 11:
        struct_rating = 9
        print("Your Structural Rating is ", struct_rating)
    elif int(sti) == 10:
        struct_rating = 11
        print("Your Structural Rating is ", struct_rating)
    elif int(sti) == 9:
        struct_rating = 12
        print("Your Structural Rating is ", struct_rating)
    elif int(sti) == 8:
        struct_rating = 13
        print("Your Structural Rating is ", struct_rating)
    elif int(sti) == 7:
        struct_rating = 14
        print("Your Structural Rating is ", struct_rating)
    elif int(sti) == 6:
        struct_rating = 16
        print("Your Structural Rating is ", struct_rating)
    elif int(sti) == 5:
        struct_rating = 17
        print("Your Structural Rating is ", struct_rating)
    elif int(sti) == 4:
        struct_rating = 19
        print("Your Structural Rating is ", struct_rating)
    elif int(sti) == 3:
        struct_rating = 21
        print("Your Structural Rating is ", struct_rating)
    elif int(sti) == 2:
        struct_rating = 23
        print("Your Structural Rating is ", struct_rating)
    elif int(sti) == 1:
        struct_rating = 24
        print("Your Structural Rating is ", struct_rating)
    else:
        struct_rating = 25
        print("Your Structural Rating is ", struct_rating)
    struct_rating_r.append(struct_rating)
    return struct_rating
def calculate_slake_durability_rating(sld):
    global sdr
    if 0 <= float(sld) < 30:
        sdr = 0
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    elif 30 <= float(sld) < 40:
        sdr = 1
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    elif 40 <= float(sld) < 50:
        sdr = 2
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    elif 50 <= float(sld) < 60:
        sdr = 3
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    elif 60 <= float(sld) < 65:
        sdr = 4
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    elif 65 <= float(sld) < 70:
        sdr = 5
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    elif 70 <= float(sld) < 75:
        sdr = 6
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    elif 75 <= float(sld) < 80:
        sdr = 7
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    elif 80 <= float(sld) < 85:
        sdr = 8
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    elif 85 <= float(sld) < 87.4:
        sdr = 9
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    elif 87.4 <= float(sld) < 89:
        sdr = 10
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    elif 89 <= float(sld) < 92.2:
        sdr = 11
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    elif 92.2 <= float(sld) < 94.6:
        sdr = 12
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    elif 94.6 <= float(sld) < 97:
        sdr = 13
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    elif 97 <= float(sld) < 97.5:
        sdr = 14
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    elif 97.5 <= float(sld) < 98:
        sdr = 15
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    elif 98 <= float(sld) < 98.5:
        sdr = 16
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    elif 98.5 <= float(sld) < 99:
        sdr = 17
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    elif float(sld) >= 99.3 > float(sld):
        sdr = 18
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    elif 99.3 <= float(sld) < 99.6:
        sdr = 19
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    else:
        sdr = 20
        print("Your Slake Durability Rating for {} % is {} ".format(float(sld), sdr))
    sdr_r.append(sdr)
    return sdr
def calculate_rock_strength_rating(rst):
    global rsr
    if 30 > float(rst) >= 0:
        rsr = 0
        print("Rock Strength Rating at {} kg/cm² is {}".format(float(rst), rsr))
    elif 30 <= float(rst) < 65:
        rsr = 1
        print("Rock Strength Rating at {} kg/cm² is {}".format(float(rst), rsr))
    elif 65 <= float(rst) < 100:
        rsr = 2
        print("Rock Strength Rating at {} kg/cm² is {}".format(float(rst), rsr))
    elif 100 <= float(rst) < 150:
        rsr = 3
        print("Rock Strength Rating at {} kg/cm² is {}".format(float(rst), rsr))
    elif 150 <= float(rst) < 200:
        rsr = 4
        print("Rock Strength Rating at {} kg/cm² is {}".format(float(rst), rsr))
    elif 200 <= float(rst) < 250:
        rsr = 5
        print("Rock Strength Rating at {} kg/cm² is {}".format(float(rst), rsr))
    elif 250 <= float(rst) < 300:
        rsr = 6
        print("Rock Strength Rating at {} kg/cm² is {}".format(float(rst), rsr))
    elif 300 <= float(rst) < 375:
        rsr = 7
        print("Rock Strength Rating at {} kg/cm² is {}".format(float(rst), rsr))
    elif 375 <= float(rst) < 450:
        rsr = 8
        print("Rock Strength Rating at {} kg/cm² is {}".format(float(rst), rsr))
    elif 450 <= float(rst) < 525:
        rsr = 9
        print("Rock Strength Rating at {} kg/cm² is {}".format(float(rst), rsr))
    elif 525 <= float(rst) < 600:
        rsr = 10
        print("Rock Strength Rating at {} kg/cm² is {}".format(float(rst), rsr))
    elif 600 <= float(rst) < 700:
        rsr = 11
        print("Rock Strength Rating at {} kg/cm² is {}".format(float(rst), rsr))
    elif 700 <= float(rst) < 800:
        rsr = 12
        print("Rock Strength Rating at {} kg/cm² is {}".format(float(rst), rsr))
    elif 800 <= float(rst) < 900:
        rsr = 13
        print("Rock Strength Rating at {} kg/cm² is {}".format(float(rst), rsr))
    elif 900 <= float(rst) < 1500:
        rsr = 14
        print("Rock Strength Rating at {} kg/cm² is {}".format(float(rst), rsr))
    else:
        rsr = 15
        print("Rock Strength Rating at {} kg/cm² is {}".format(float(rst), rsr))
    rsr_r.append(rsr)
    return rsr
def calculate_ground_seepage_rating(grs):
    global gsr
    if float(grs) > 5000:
        gsr = 0
        print("Ground Seepage Rating for {}ml/min is {}".format(float(grs), gsr))
    elif 2000 < float(grs) <= 5000:
        gsr = 1
        print("Ground Seepage Rating for {}ml/min is {}".format(float(grs), gsr))
    elif 800 < float(grs) <= 2000:
        gsr = 2
        print("Ground Seepage Rating for {}ml/min is {}".format(float(grs), gsr))
    elif 300 < float(grs) <= 800:
        gsr = 3
        print("Ground Seepage Rating for {}ml/min is {}".format(float(grs), gsr))
    elif 200 < float(grs) <= 300:
        gsr = 4
        print("Ground Seepage Rating for {}ml/min is {}".format(float(grs), gsr))
    elif 140 < float(grs) <= 200:
        gsr = 5
        print("Ground Seepage Rating for {}ml/min is {}".format(float(grs), gsr))
    elif 80 < float(grs) <= 140:
        gsr = 6
        print("Ground Seepage Rating for {}ml/min is {}".format(float(grs), gsr))
    elif 20 < float(grs) <= 80:
        gsr = 7
        print("Ground Seepage Rating for {}ml/min is {}".format(float(grs), gsr))
    elif 10 < float(grs) <= 20:
        gsr = 8
        print("Ground Seepage Rating for {}ml/min is {}".format(float(grs), gsr))
    elif 0 < float(grs) <= 10:
        gsr = 9
        print("Ground Seepage Rating for {}ml/min is {}".format(float(grs), gsr))
    else:
        gsr = 10
        print("Wow dry ground seepage\ngreat")
        print("Ground Seepage Rating for {}ml/min is {}".format(float(grs), gsr))
    gsr_r.append(gsr)
    return gsr
def calculate_rmr():
    ltr = calculate_layer_thickness_rating(get_valid_input("Enter your LAYER THICKNESS (in CM) [0-100]:  ", 0, 100))
    struct_rating = calculate_structural_rating(get_valid_input("Enter your STRUCTURAL Indices [0-16]:  ", 0, 16))
    sdr = calculate_slake_durability_rating(get_valid_input("Enter your SLAKE DURABILITY (I) index % [0-100]:  ", 0, 100))
    rst = calculate_rock_strength_rating(get_valid_input("Enter your ROCK STRENGTH (kg/cm²):  ", 0, float('inf')))
    grs = calculate_ground_seepage_rating(get_valid_input("Enter your GROUND SEEPAGE (ml/min):  ", 0, float('inf')))
    return ltr + struct_rating + sdr + rst + grs
for i in range(2):
    if i == 0:
        print("----------------*---ENTER DATA OF ORE---*------------")
    elif i == 1:
        print("----------*---ENTER DATA OF OVERBURDEN---*-----------")
    rmr_value = calculate_rmr()
    rmr.append(rmr_value)
print("RMR of Coal/Metal is", rmr[0])
print("RMR of Shale/Sandstone is", rmr[1])
print("We have to find the COMBINED RMR!! ")
t1 = float(input("Enter the overlying strata of Coal or Metal mine(m): "))
t2 = float(input("Enter the intermediate roof strata of shale/sandstone/else: "))
while True:
    t3 = float(input("Enter the Gallery Span Width (m): "))
    try:
        if 4.8 <= t3 <= 6:
            pass
        else:
            print("Gallery Width must be in [4.8-6]m as per Indian Guidelines")
            continue
        break
    except ValueError:
        print("Invalid Input")
if t1 <= t3:
    crmr = ((rmr[0] * t1) + (rmr[1] * (t3 - t1))) / t3
else:
    crmr = (rmr[0])
print("Combined RMR is {}".format(format(crmr, '0.2f')))
print("--------*******--------********-------------**********------------*******---------")
print("Now we have to Calculate Adjusted RMR")
depth = float(input("Enter the depth(in m):  "))
armr_d.append(depth)
if depth < 250:
    armr = crmr * 1
elif 250 <= depth < 400:
    armr = crmr * 0.9
elif 400 <= depth < 600:
    armr = crmr * 0.8
else:
    armr = crmr * 0.7
print("ARMR AFTER DEPTH calculation is {} ".format(format(armr, '0.2f')))
armr_d.append(armr)
print("--------*******--------********-------------**********------------*******---------")

print("CONDITIONS FOR LATERAL STRESS!!!!")
options = ['SMALL STRESS', 'MEDIUM STRESS', 'HIGH STRESS', 'If You dont Know Data']
for index, option in enumerate(options, start=1):
    print(f"Press {index} for {option}")
while True:
    lateral_stress = int(input("Press Lateral Stress Conditions Carefully:  "))
    try:
        if 1<= lateral_stress <= len(options):
            armr = armr*[0.9, 0.8, 0.7, 0.9][lateral_stress-1]
            armr_d.append(options[lateral_stress-1])
            break
        else:
            print("Invalid Input\nPlease Enter Conditions Again")
            continue
    except ValueError:
        print("Invalid Input")
print("ARMR after including lateral stress is {}".format(format(armr, '0.2f')))
armr_d.append(armr)
print("--------*******--------********-------------**********------------*******---------")
print("CONDITION FOR INDUCED STRESS!!!")
options = [
    "NO ADJACENT WORKING IN THE SEAM",
    "EXTRACTION AREA WITHIN 20-40 m IN THE SAME SEAM",
    "EXTRACTION AREA WITHIN 10-20m in the same seam",
    "working with 10-20m parting",
    "working within 3 - 10m parting",
    "If you dont have this data"
]

for index, option in enumerate(options, start=1):
    print(f"Press {index} for {option}")

while True:
    try:
        induced_stress = int(input("Press THE INDUCED STRESS CONDITION CAREFULLY: "))
        if 1 <= induced_stress <= len(options):
            armr = armr * [1, 0.9, 0.75, 0.9, 0.75, 0.75, 0.85][induced_stress-1]
            armr_d.append(options[induced_stress-1])

            break
        else:
            print("Invalid Input")
            continue
    except ValueError:
        print("Invalid data")

print("ARMR after including INDUCED STRESS is {}".format(format(armr, '0.2f')))
armr_d.append(armr)
print("--------*******--------********-------------**********------------*******---------")
print("CONDITIONS FOR METHOD OF WORKING")
options =[
    'MECHANISED WORKING OR CONTINUOUS MINER',
    'UNDERCUT AND BLASTING',
    'BLASTING OFF THE SOLID',
    'if you dont know data'
]
for index, option in enumerate(options, start=1):
    print(f"Press {index} for {option}")
while True:
    method_excavation = int(input("Press THE RESPECTIVE KEY CAREFULLY:  "))

    try:
        if 1<=method_excavation <= len(options):
            armr = armr * [1.1, 1, 0.9, 0.9][method_excavation-1]
            armr_d.append(options[method_excavation-1])
            break
        else:
            print("Invalid Input\nEnter the Respective Value again!!")
            continue

    except ValueError:
        print("Invalid Input")

print("ARMR after including METHOD OF EXCAVATION is {}".format(format(armr, '0.2f')))
armr_d.append(armr)
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
armr_d.append(armr)
# print(f"Final RMR : {armr:.2f}")
print("--------*******--------********-------------**********------------*******---------")
rmr_classification = ""
if 90 < armr <= 100.0:
    print("Final RMR : {}".format(format(armr, '0.2f')))
    rmr_classification = "EXCELLENT Rock"
elif 80 <= armr <= 90:
    print("Final RMR : {}".format(format(armr, '0.2f')))
    rmr_classification = "VERY GOOD STRATA"
elif 60 < armr < 80:
    print("Final RMR : {} ".format(format(armr, '0.2f')))
    rmr_classification = "GOOD STRATA"
elif 40 < armr <= 60:
    print("Final RMR : {} ".format(format(armr, '0.2f')))
    rmr_classification = "FAIR STRATA"
elif 20 < armr <= 40:
    print("Final RMR : {}".format(format(armr, '0.2f')))
    rmr_classification = "POOR STRATA"
elif 0 < armr <= 20:
    print("Final RMR Less than 20")
    rmr_classification = "VERY POOR STRATA"
else:
    print("Armr is {} ".format(format(armr, '0.2f')))
    print("VALUE ABSURD")
    print("RMR CAN'T BE GREATER THAN 100")
    print("MEASURE RMR INDICES AGAIN")
print("--------*******--------********-------------**********------------*******---------")
print("CALCULATING Rock LOAD....")

while True:

    Rock_l = mine_type
    mean_density = float(input("Enter the mean density (t/m^3): "))
    try:
        if Rock_l == "COAL":
            print("You Already selected the \"COAL MINE\"")
            armr_d.append('Coal Mine')
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
        elif Rock_l == "METAL":
            print("You Already selected the \"METAL MINE\"")
            armr_d.append('Metal Mine')
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
if support_design == 1:
    while True:
        try:
            print('Calculating Support Design...')
            print('Calculating Number of Bolts for Gallery')
            print("Press 1 for Cement Capsule = 6 tonne\nPress 2 for Resin Bolt = 10 tonne\nPress 3 for your Input")
            support = int(input('Enter Your Input Carefully: '))
            if support == 1:
                armr_d.append("Cement Capsule 6 tonne")
                no_of_Bolts_Gallery = (t3 * Rock_load_Gallery) / 6
                no_of_Bolts_Gallery = round(no_of_Bolts_Gallery)
                b_g = no_of_Bolts_Gallery
                print("Number of Bolts is {}".format(no_of_Bolts_Gallery))
                print("Calculating Spacings....")
                Bolts_spacing_Gallery = t3 / no_of_Bolts_Gallery
                print('Spacing Between Bolts in Gallery is {} m'.format(format(Bolts_spacing_Gallery, '0.2f')))
                support_load_provided = (no_of_Bolts_Gallery * 6) / (t3 * Bolts_spacing_Gallery)
                print("Support Load Provided is {}t/m2".format(format(support_load_provided, '0.2f')))
                print("Rock Load in Gallery is {}t/m2".format(format(Rock_load_Gallery, '0.2f')))
                fos_g = support_load_provided / Rock_load_Gallery
                while not (1.45 <= fos_g <= 2.0):
                    # b =  int(input("Enter Number of Bolts greater/less than {}:  ".format(no_of_Bolts_Gallery)))
                    if fos_g <= 1.45:
                        b_g: int = int(input("Enter Number of Bolts Greater than {}:  ".format(b_g)))
                        print("Your Input: {}".format(b_g))
                    elif fos_g >= 2.0:
                        b_g: int = int(input("Enter Number of Bolts Less than {}:  ".format(b_g)))
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
                    elif fos_g < 1.45:
                        print("Current FOS is {}".format(format(fos_g, '0.2f')))
                        print("Your Input: {}".format(b_g))
                        print("Increase Number of Bolts than {} ".format(b_g))

                print("Factor of Safety is {}".format(format(fos_g, '0.2f')))
                print("Number of Bolts Required At Gallery is {}".format(b_g))
                Bolts_spacing_Gallery = t3 / b_g
                print('New Spacing Between Bolts in Gallery is {} m'.format(format(Bolts_spacing_Gallery, '0.2f')))

            elif support == 2:
                armr_d.append('Resin Bolt 10 tonne')
                no_of_Bolts_Gallery = (t3 * Rock_load_Gallery) / 10
                no_of_Bolts_Gallery = round(no_of_Bolts_Gallery)
                b_g = no_of_Bolts_Gallery
                print("Number of Bolts is {}".format(no_of_Bolts_Gallery))
                print("Calculating Spacings....")
                Bolts_spacing_Gallery = t3 / no_of_Bolts_Gallery
                print('Spacing Between Bolts in Gallery is {} m'.format(format(Bolts_spacing_Gallery, '0.2f')))
                support_load_provided = (no_of_Bolts_Gallery * 10) / (t3 * Bolts_spacing_Gallery)
                print("Support Load Provided is {}t/m2".format(format(support_load_provided, '0.2f')))
                print("Rock Load in Gallery is {}t/m2".format(format(Rock_load_Gallery, '0.2f')))
                fos_g = support_load_provided / Rock_load_Gallery
                while not (1.45 <= fos_g <= 2.0):
                    if fos_g <= 1.45:
                        b_g = int(input("Enter Number of Bolts greater than {}:  ".format(b_g)))
                        print("Your Input: {}".format(b_g))
                    elif fos_g >= 2.0:
                        b_g = int(input("Enter Number of Bolts less than {}:  ".format(b_g)))
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
                    elif fos_g < 1.45:
                        print("Current FOS is {}".format(format(fos_g, '0.2f')))
                        print("Increase Number of Bolts than {}".format(b_g))
                print("Factor of Safety is {}".format(format(fos_g, '0.2f')))
                print("Number of Bolts Required At Gallery is {}".format(b_g))
                Bolts_spacing_Gallery = t3 / b_g
                print('New Spacing Between Bolts in Gallery is {} m'.format(format(Bolts_spacing_Gallery, '0.2f')))
            elif support == 3:
                a = float(input("Enter the loading capacity in tonne:  "))
                armr_d.append(f"Others Support {a} tonne")
                no_of_Bolts_Gallery = (t3 * Rock_load_Gallery) / a
                no_of_Bolts_Gallery = round(no_of_Bolts_Gallery)
                b_g = no_of_Bolts_Gallery
                print("Number of Bolts is {}".format(no_of_Bolts_Gallery))
                print("Calculating Spacings....")
                Bolts_spacing_Gallery = t3 / no_of_Bolts_Gallery
                print('Spacing Between Bolts in Gallery is {} m'.format(format(Bolts_spacing_Gallery, '0.2f')))
                support_load_provided = (no_of_Bolts_Gallery * a) / (t3 * Bolts_spacing_Gallery)
                print("Support Load Provided is {}t/m2".format(format(support_load_provided, '0.2f')))
                print("Rock Load in Gallery is {}t/m2".format(format(Rock_load_Gallery, '0.2f')))
                fos_g = support_load_provided / Rock_load_Gallery
                while not (1.45 <= fos_g <= 2.0):
                    # b = int(input("Enter Number of Bolts greater/less than {}:  ".format(no_of_Bolts_Gallery)))
                    if fos_g <= 1.45:
                        b_g = int(input("Enter Number of Bolts greater than {}:  ".format(b_g)))
                        print("Your Input: {}".format(b_g))
                    elif fos_g >= 2.0:
                        b_g = int(input("Enter Number of Bolts less than {}:  ".format(b_g)))
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
                    elif fos_g < 1.45:
                        print("Current FOS is {}".format(format(fos_g, '0.2f')))
                        print("Increase Number of Bolts than {}".format(b_g))
                print("Factor of Safety at Gallery is {}".format(format(fos_g, '0.2f')))
                print("Number of Bolts Required At Gallery is {}".format(b_g))
                Bolts_spacing_Gallery = t3 / b_g
                print('New Spacing Between Bolts in Gallery is {} m'.format(format(Bolts_spacing_Gallery, '0.2f')))

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
            print("Calculating Support Design For Junction....")
            print("Press 1 for Cement Capsule = 6 tonne\nPress 2 for Resin Bolt = 10 tonne\nPress 3 for your Input")

            support_ = int(input('Enter Your Input Carefully: '))
            if support_ == 1:
                armr_d.append('Cement Capsule 6 tonne')
                no_of_Bolts_Junction = (t3 * t3 * Rock_load_Junction) / 6
                no_of_Bolts_Junction = pow(no_of_Bolts_Junction, 0.5)
                no_of_Bolts_Junction = round(no_of_Bolts_Junction)
                no_of_Bolts_Junction = pow(no_of_Bolts_Junction, 2)
                no_of_Bolts_Junction_row = pow(no_of_Bolts_Junction, 0.5)
                b = no_of_Bolts_Junction_row
                print("Number of Bolts at Junction is {}".format(no_of_Bolts_Junction))
                print("Number of Bolts in a row at Junction is {}".format(no_of_Bolts_Junction_row))
                print("Calculating Spacings....")
                Bolts_spacing_Junction = t3 / no_of_Bolts_Junction
                print('Spacing Between Bolts in Junction is {} m'.format(format(Bolts_spacing_Junction, '0.2f')))
                support_load_provided = (no_of_Bolts_Junction * 6) / (t3 * t3)
                print("Support Load Provided is {}t/m2".format(format(support_load_provided, '0.2f')))
                print("Rock Load in Junction is {}t/m2".format(format(Rock_load_Junction, '0.2f')))
                fos_j = support_load_provided / Rock_load_Junction
                while not (1.45 <= fos_j <= 2.0):
                    # b = int(input("Enter Number of Bolts greater/less than {}:  ".format(no_of_Bolts_Junction_row)))
                    if fos_j <= 1.45:
                        b = int(input("Enter Number of Bolts greater than {}:  ".format(b)))
                        print("Your Input: {}".format(b))
                    elif fos_j >= 2.0:
                        b = int(input("Enter Number of Bolts less than {}:  ".format(b)))
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
                    elif fos_j < 1.45:
                        print("Current FOS is {}".format(format(fos_j, '0.2f')))
                        print("Increase Number of Bolts than {} ".format(b))
                print("Factor of Safety is {}".format(format(fos_j, '0.2f')))
                print("Number of Bolts Required At Junction is {}X{} is {}".format(b, b, pow(b, 2)))

                Bolts_spacing_Junction = t3 / b
                print('New Spacing Between Bolts in Junction is {} m'.format(format(Bolts_spacing_Junction, '0.2f')))

            elif support_ == 2:
                armr_d.append("Resin Bolt 10 tonne")
                no_of_Bolts_Junction = (t3 * t3 * Rock_load_Junction) / 10
                no_of_Bolts_Junction = pow(no_of_Bolts_Junction, 0.5)
                no_of_Bolts_Junction = round(no_of_Bolts_Junction)
                no_of_Bolts_Junction = pow(no_of_Bolts_Junction, 2)
                no_of_Bolts_Junction_row = pow(no_of_Bolts_Junction, 0.5)
                b = no_of_Bolts_Junction_row
                print("Number of Bolts at Junction is {}".format(no_of_Bolts_Junction))
                print("Number of Bolts in a row at Junction is {}".format(no_of_Bolts_Junction_row))
                print("Calculating Spacings....")
                Bolts_spacing_Junction = t3 / no_of_Bolts_Junction
                print('Spacing Between Bolts in Junction is {} m'.format(format(Bolts_spacing_Junction, '0.2f')))
                support_load_provided = (no_of_Bolts_Junction * 10) / (t3 * t3)
                print("Support Load Provided is {}t/m2".format(format(support_load_provided, '0.2f')))
                print("Rock Load in Junction is {}t/m2".format(format(Rock_load_Junction, '0.2f')))
                fos_j = support_load_provided / Rock_load_Junction
                while not (1.45 <= fos_j <= 2.0):
                    if fos_j <= 1.45:
                        b = int(input("Enter Number of Bolts greater than {}:  ".format(b)))
                        print("Your Input: {}".format(b))
                    elif fos_j >= 2.0:
                        b = int(input("Enter Number of Bolts less than {}:  ".format(b)))
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
                    elif fos_j < 1.45:
                        print("Current FOS is {}".format(format(fos_j, '0.2f')))
                        print("Increase Number of Bolts than {}".format(b))
                print("Factor of Safety is {}".format(format(fos_j, '0.2f')))
                print("Number of Bolts Required At Junction is {}X{} is {}".format(b, b, pow(b, 2)))

                Bolts_spacing_Junction = t3 / b
                print('New Spacing Between Bolts in Junction is {} m'.format(format(Bolts_spacing_Junction, '0.2f')))

            elif support_ == 3:
                a = float(input("Enter the loading capacity in tonne:  "))
                armr_d.append(f'Others Support {a} tonne')
                no_of_Bolts_Junction = (t3 * t3 * Rock_load_Junction) / a
                no_of_Bolts_Junction = pow(no_of_Bolts_Junction, 0.5)
                no_of_Bolts_Junction = round(no_of_Bolts_Junction)
                no_of_Bolts_Junction = pow(no_of_Bolts_Junction, 2)
                no_of_Bolts_Junction_row = pow(no_of_Bolts_Junction, 0.5)
                b = no_of_Bolts_Junction_row
                print("Number of Bolts at Junction is {}".format(no_of_Bolts_Junction))
                print("Number of Bolts in a row at Junction is {}".format(no_of_Bolts_Junction_row))
                print("Calculating Spacings....")
                Bolts_spacing_Junction = t3 / no_of_Bolts_Junction
                print('Spacing Between Bolts in Junction is {} m'.format(format(Bolts_spacing_Junction, '0.2f')))
                support_load_provided = (no_of_Bolts_Junction * a) / (t3 * t3)
                print("Support Load Provided is {}t/m2".format(format(support_load_provided, '0.2f')))
                print("Rock Load in Junction is {}t/m2".format(format(Rock_load_Junction, '0.2f')))
                fos_j = support_load_provided / Rock_load_Junction
                while not (1.45 <= fos_j <= 2.0):
                    # b = int(input("Enter Number of Bolts greater/less than {}:  ".format(no_of_Bolts_Junction_row)))
                    if fos_j <= 1.45:
                        b = int(input("Enter Number of Bolts greater than {}:  ".format(b)))
                        print("Your Input: {}".format(b))
                    elif fos_j >= 2.0:
                        b = int(input("Enter Number of Bolts less than {}:  ".format(b)))
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

                    elif fos_j < 1.45:
                        print("Current FOS is {}".format(format(fos_j, '0.2f')))
                        print("Increase Number of Bolts than {}".format(b))
                print("Factor of Safety at junction is {}".format(format(fos_j, '0.2f')))
                print("Number of Bolts Required At Junction is {}X{} is {}".format(b, b, pow(b, 2)))

                Bolts_spacing_Junction = t3 / b
                print('New Spacing Between Bolts in Junction is {} m'.format(format(Bolts_spacing_Junction, '0.2f')))

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

pdf_filename = f"m_{mine_name}_report" + '.pdf'
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

# Define styles
styles = getSampleStyleSheet()
title_style = styles["Title"]
normal_style = styles["Normal"]


# Define content
content = [
    Paragraph("Mine Stability Report", title_style),
    Paragraph(f"Recommendations for {mine_name}, {owner}, {location}", title_style),
    Spacer(1, 12),
    Paragraph("<b>ORE Information</b>", normal_style),
    Paragraph(f"Mines Type : <b>{armr_d[9]}:{ore}</b>"),
    Paragraph("-----------------------------------------------------------------------------------"),
    Paragraph(f"Layer Thickness Rating : <b>{ltr_r[0]}</b>"),
    Paragraph(f"Structural Rating : <b>{struct_rating_r[0]}</b>"),
    Paragraph(f"Slake Durability Rating : <b>{sdr_r[0]}</b>"),
    Paragraph(f"Rock Strength Rating : <b>{rsr_r[0]}</b>"),
    Paragraph(f"Ground Water Rating : <b>{gsr_r[0]}</b>"),
    Spacer(1, 6),
    Paragraph("<b>Roof Information</b>", normal_style),
    Paragraph("-----------------------------------------------------------------------------------"),
    Paragraph(f"Layer Thickness Rating : <b>{ltr_r[1]}</b>"),
    Paragraph(f"Structural Rating : <b>{struct_rating_r[1]}</b>"),
    Paragraph(f"Slake Durability Rating : <b>{sdr_r[1]}</b>"),
    Paragraph(f"Rock Strength Rating : <b>{rsr_r[1]}</b>"),
    Paragraph(f"Ground Water Rating : <b>{gsr_r[1]}</b>"),
    Paragraph("<b>Important</b>"),
    Paragraph("-----------------------------------------------------------------------------------"),
    Paragraph(f"OverLying Strata of ORE : <b> {t1} m</b> | Intermediate Roof Strata : <b> {t2} m</b>"),
    Paragraph(f"Mean Density : <b>{mean_density} t/m3</b>"),
    Paragraph(f"COMBINED RMR : <b>{crmr:.2f}</b>"),
    Paragraph("Adjusted RMR After Calculating"),
    Paragraph("-----------------------------------------------------------------------------------"),
    Paragraph("1. Depth [<b>{} m</b>] : <b>{:.2f}</b>".format(armr_d[0], armr_d[1])),
    Paragraph("2. Lateral Stress [<b>{}</b>] : <b>{:.2f}</b>".format(armr_d[2], armr_d[3])),
    Paragraph("3. Induced Stress [<b>{}</b>] : <b>{:.2f}</b>".format(armr_d[4], armr_d[5])),
    Paragraph("4. Mining Method [<b>{}</b>] : <b>{:.2f}</b>".format(armr_d[6], armr_d[7])),
    Paragraph("5. Gallery Width [<b>{} m</b>] : <b>{:.2f}</b>".format(t3, armr_d[8])),
    Paragraph(f'Final RMR of Mine:<b> {armr:.2f}</b>'),
    Paragraph(f'Remarks : <b>{rmr_classification} </b>', normal_style),
    Paragraph("Suggestion Based Upon Observation of Mine", normal_style),
    Paragraph("-----------------------------------------------------------------------------------"),
    Paragraph(f"Roof Support Provided in Gallery : <b>{armr_d[10]}</b>"),
    Paragraph("Factor of Safety at Gallery is <b>{:.2f}</b>".format(fos_g), normal_style),
    Paragraph("Number of Bolts Required At Gallery is <b>{}</b>".format(b_g), normal_style),
    Paragraph('Bolts Spacing in Gallery is <b>{} m</b>'.format(format(Bolts_spacing_Gallery, '0.2f')), normal_style),
    Paragraph(f"Roof Support Provided at Junction : <b>{armr_d[11]}</b>"),
    Paragraph("Factor of Safety at Junction is <b>{:.2f}</b>".format(fos_j), normal_style),
    Paragraph("Number of Bolts Required At Junction is <b>{}X{} is {}</b>".format(b, b, pow(b, 2)), normal_style),
    Paragraph('Bolts Spacing at Junction : <b>{} m</b>'.format(format(Bolts_spacing_Junction, '0.2f')), normal_style),
    Paragraph("-----------------------------------------------------------------------------------"),
    Spacer(1, 14),
    Paragraph(f"<b>Report Generated @: {datetime.datetime.now()}</b>", normal_style),

]
doc.build(content)
print(f"PDF report saved as {pdf_filename}")
