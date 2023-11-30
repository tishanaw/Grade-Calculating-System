from graphics import *


# Function to get an integer input with validation
def get_credits(prompt):
    credits = int ( input ( prompt ) )
    return credits


# Functions to validate credits in the specified range.
def validate_credits(credits):
    if credits not in [0, 20, 40, 60, 80, 100, 120]:
        print ( "Out of Range" )
        return False
    return True


# Function based on credits to predict the outcome of the progression
def predict_outcome(pass_credits, defer_credits, fail_credits):
    total_credits = pass_credits + defer_credits + fail_credits

    if total_credits != 120:
        return "Total Incorrect!"
    elif pass_credits == 120:
        return "Progress."
    elif pass_credits == 100:
        return "Progress (module trailer)."
    elif pass_credits == 80:
        return "Do not Progress - module retriever."
    elif pass_credits == 60:
        return "Do not Progress - module retriever."
    elif pass_credits == 40:
        if defer_credits == 80 and fail_credits == 0:
            return "Do not Progress - module retriever."
    elif pass_credits == 40:
        if defer_credits == 40 and fail_credits == 40:
            return "Do not Progress - module retriever."
    elif pass_credits == 40:
        if defer_credits == 20 and fail_credits == 60:
            return "Do not Progress - module retriever."
    elif pass_credits == 40:
        if defer_credits == 60 and fail_credits == 20:
            return "Do not Progress - module retriever."
    elif fail_credits == 120 or fail_credits == 100 or fail_credits == 80:
        return "Exclude"
    elif pass_credits == 20:
        return "Do not Progress - module retriever."


# Function for graph
def histogram(h, a, b, c, d):
    win = GraphWin ( "Histogram", 800, 600 )
    win.setBackground ( "Mint Cream" )
    my_heading = Text ( Point ( 180, 40 ), 'Histogram Results' )
    my_heading.draw ( win )
    my_heading.setTextColor ( "Black" )
    my_heading.setSize ( 26 )
    my_heading.setStyle ( "bold" )
    my_heading.setFace ( "helvetica" )

    # Bargraph Bar : Progress
    rect1 = Rectangle ( Point ( 50, (480 - (a * h)) ), Point ( 200, 480 ) )
    rect1.setFill ( "yellow" )
    rect1.draw ( win )

    # Bargraph Bar : Module Trailer
    rect2 = Rectangle ( Point ( 220, (480 - (b * h)) ), Point ( 370, 480 ) )
    rect2.setFill ( "blue" )
    rect2.draw ( win )

    # Bargraph Bar : Module Retriever
    rect3 = Rectangle ( Point ( 390, (480 - (c * h)) ), Point ( 540, 480 ) )
    rect3.setFill ( "red" )
    rect3.draw ( win )

    # Bargraph Bar : Excluded
    rect4 = Rectangle ( Point ( 560, (480 - (d * h)) ), Point ( 710, 480 ) )
    rect4.setFill ( "green" )
    rect4.draw ( win )

    # Bargraph Bottom Line
    line = Line ( Point ( 10, 480 ), Point ( 750, 480 ) )
    line.draw ( win )

    # Bargraph Bottom Title 1
    text1 = Text ( Point ( 120, 500 ), 'Progress' )
    text1.draw ( win )
    text1.setSize ( 18 )
    text1.setStyle ( "bold" )
    text1.setFace ( "helvetica" )
    text1.setTextColor ( "Grey" )

    # Bargraph Bottom Title 2
    text2 = Text ( Point ( 290, 500 ), 'Trailer' )
    text2.draw ( win )
    text2.setSize ( 18 )
    text2.setStyle ( "bold" )
    text2.setFace ( "helvetica" )
    text2.setTextColor ( "Grey" )

    # Bargraph Bottom Title 3
    text3 = Text ( Point ( 460, 500 ), 'Retriever' )
    text3.draw ( win )
    text3.setSize ( 18 )
    text3.setStyle ( "bold" )
    text3.setFace ( "helvetica" )
    text3.setTextColor ( "Grey" )

    # Bargraph Bottom Title 4
    text4 = Text ( Point ( 640, 500 ), 'Excluded' )
    text4.draw ( win )
    text4.setSize ( 18 )
    text4.setStyle ( "bold" )
    text4.setFace ( "helvetica" )
    text4.setTextColor ( "Grey" )

    # Bargraph Bottom Text : Outcomes of Total
    text5 = Text ( Point ( 200, 550 ), f'{a + b + c + d} Outcomes in Total' )
    text5.draw ( win )
    text5.setSize ( 18 )
    text5.setStyle ( "bold" )
    text5.setFace ( "helvetica" )
    text5.setTextColor ( "Grey" )

    # Bargraph progress count
    text_progress = Text ( Point ( 120, (((480 - (a * h)) - 10)) ), a )
    text_progress.draw ( win )
    text_progress.setSize ( 18 )
    text_progress.setStyle ( "bold" )
    text_progress.setFace ( "helvetica" )
    text_progress.setTextColor ( "Grey" )

    # Bargraph trailer count
    text_trailer = Text ( Point ( 290, (((480 - (b * h)) - 10)) ), b )
    text_trailer.draw ( win )
    text_trailer.setSize ( 18 )
    text_trailer.setStyle ( "bold" )
    text_trailer.setFace ( "helvetica" )
    text_trailer.setTextColor ( "Grey" )

    # Bargraph retriever count
    text_retriever = Text ( Point ( 460, (((480 - (c * h)) - 10)) ), c )
    text_retriever.draw ( win )
    text_retriever.setSize ( 18 )
    text_retriever.setStyle ( "bold" )
    text_retriever.setFace ( "helvetica" )
    text_retriever.setTextColor ( "Grey" )

    # Bargraph exclude count
    text_exclude = Text ( Point ( 640, (((480 - (d * h)) - 10)) ), d )
    text_exclude.draw ( win )
    text_exclude.setSize ( 18 )
    text_exclude.setStyle ( "bold" )
    text_exclude.setFace ( "helvetica" )
    text_exclude.setTextColor ( "Grey" )

    # GraphicsError Exception Handling
    try:
        win.getMouse ()
        win.close ()
    except GraphicsError:
        pass


outcomes = []
outcome_values = []
progress = 0
trailer = 0
retriever = 0
exclude = 0

x = True
while x:
    while True:
        try:
            pass_credits = get_credits ( "Please enter your credits at pass: " )
            flag = validate_credits ( pass_credits )
            if flag == True:
                break
        except ValueError:
            print ( "Integer Required" )

    while True:
        try:
            defer_credits = get_credits ( "Please enter your credits at defer: " )
            flag = validate_credits ( defer_credits )
            if flag == True:
                break
        except ValueError:
            print ( "Integer Required" )

    while True:
        try:
            fail_credits = get_credits ( "Please enter your credits at fail: " )
            flag = validate_credits ( fail_credits )
            if flag == True:
                break
        except ValueError:
            print ( "Integer Required" )

    outcome = predict_outcome ( pass_credits, defer_credits, fail_credits )
    print ( outcome )
    if outcome == "Progress.":
        progress += 1
        outcomes.extend ( (outcome,) )
        outcome_values.extend ( (pass_credits, defer_credits, fail_credits), )
    elif outcome == "Progress (module trailer).":
        trailer += 1
        outcomes.extend ( (outcome,) )
        outcome_values.extend ( (pass_credits, defer_credits, fail_credits), )
    elif outcome == "Do not Progress - module retriever.":
        retriever += 1
        outcomes.extend ( (outcome,) )
        outcome_values.extend ( (pass_credits, defer_credits, fail_credits), )
    elif outcome == "Exclude":
        exclude += 1
        outcomes.extend ( (outcome,) )
        outcome_values.extend ( (pass_credits, defer_credits, fail_credits), )

    while True:
        again = input (
            "Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: " )
        if again.lower () == 'q':

            print ( "Part 2 :" )
            file = open ( 'text.txt', 'w' )
            file.write ( "Part 3 :\n" )

            for item in range ( len ( outcomes ) ):
                print ( outcomes[item], "-", outcome_values[item] )
                file.write ( f"{outcomes[item]} - {outcome_values[item]}\n" )
                file.close
            file = open ( 'text.txt', 'r' )

            h = max ( progress, trailer, retriever, exclude )
            maxheight = 400
            height_for_one_point = maxheight / h
            histogram ( progress, trailer, retriever, exclude, height_for_one_point )

            x = False
            break
        elif again.lower () == 'y':
            break
        else:
            print ( "Invalid input. Exiting." )