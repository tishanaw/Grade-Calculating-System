from graphics import *


def get_credits(prompt):
    while True:
        try:
            credits = int(input(prompt))
            if validate_credits(credits):
                return credits
            else:
                print("Out of Range.")
        except ValueError:
            print("Integer Required")


def validate_credits(credits):
    return credits in [0, 20, 40, 60, 80, 100, 120]


def predict_outcome(pass_credits, defer_credits, fail_credits):
    total_credits = pass_credits + defer_credits + fail_credits

    if total_credits != 120:
        return "Total Incorrect!"
    elif pass_credits == 120:
        return "Progress."
    elif pass_credits == 100:
        return "Progress (module trailer)."
    elif pass_credits == 80 or pass_credits == 60:
        return "Do not Progress - module retriever."
    elif pass_credits == 40:
        if defer_credits == 80 and fail_credits == 0:
            return "Do not Progress - module retriever."
        elif defer_credits == 60 and fail_credits == 20:
            return "Do not Progress - module retriever."
        elif defer_credits == 40 and fail_credits == 40:
            return "Do not Progress - module retriever."
        elif defer_credits == 20 and fail_credits == 60:
            return "Do not Progress - module retriever."
        elif defer_credits == 60 and fail_credits == 20:
            return "Do not Progress - module retriever."
        elif defer_credits == 0 and fail_credits == 80:
            return "Exclude"
    elif pass_credits == 0:
        if defer_credits == 60 and fail_credits == 60:
            return "Do not Progress - module retriever."
    elif fail_credits in [120, 100, 80]:
        return "Exclude"
    elif pass_credits == 20:
        return "Do not Progress - module retriever."


def histogram(h, a, b, c, d):
    win = GraphWin("Histogram", 800, 600)
    win.setBackground("Mint Cream")
    my_heading = Text(Point(180, 40), 'Histogram Results')
    my_heading.draw(win)
    my_heading.setTextColor("Black")
    my_heading.setSize(26)
    my_heading.setStyle("bold")
    my_heading.setFace("helvetica")

    rect1 = Rectangle(Point(50, (480 - (a * h))), Point(200, 480))
    rect1.setFill("yellow")
    rect1.draw(win)

    rect2 = Rectangle(Point(220, (480 - (b * h))), Point(370, 480))
    rect2.setFill("blue")
    rect2.draw(win)

    rect3 = Rectangle(Point(390, (480 - (c * h))), Point(540, 480))
    rect3.setFill("red")
    rect3.draw(win)

    rect4 = Rectangle(Point(560, (480 - (d * h))), Point(710, 480))
    rect4.setFill("green")
    rect4.draw(win)

    line = Line(Point(10, 480), Point(750, 480))
    line.draw(win)

    text1 = Text(Point(120, 500), 'Progress')
    text1.draw(win)
    text1.setSize(18)
    text1.setStyle("bold")
    text1.setFace("helvetica")
    text1.setTextColor("Grey")

    text2 = Text(Point(290, 500), 'Trailer')
    text2.draw(win)
    text2.setSize(18)
    text2.setStyle("bold")
    text2.setFace("helvetica")
    text2.setTextColor("Grey")

    text3 = Text(Point(460, 500), 'Retriever')
    text3.draw(win)
    text3.setSize(18)
    text3.setStyle("bold")
    text3.setFace("helvetica")
    text3.setTextColor("Grey")

    text4 = Text(Point(640, 500), 'Excluded')
    text4.draw(win)
    text4.setSize(18)
    text4.setStyle("bold")
    text4.setFace("helvetica")
    text4.setTextColor("Grey")

    text5 = Text(Point(200, 550), f'{a + b + c + d} Outcomes in Total')
    text5.draw(win)
    text5.setSize(18)
    text5.setStyle("bold")
    text5.setFace("helvetica")
    text5.setTextColor("Grey")

    text_progress = Text(Point(120, ((480 - (a * h)) - 10)), a)
    text_progress.draw(win)
    text_progress.setSize(18)
    text_progress.setStyle("bold")
    text_progress.setFace("helvetica")
    text_progress.setTextColor("Grey")

    text_trailer = Text(Point(290, ((480 - (b * h)) - 10)), b)
    text_trailer.draw(win)
    text_trailer.setSize(18)
    text_trailer.setStyle("bold")
    text_trailer.setFace("helvetica")
    text_trailer.setTextColor("Grey")

    text_retriever = Text(Point(460, ((480 - (c * h)) - 10)), c)
    text_retriever.draw(win)
    text_retriever.setSize(18)
    text_retriever.setStyle("bold")
    text_retriever.setFace("helvetica")
    text_retriever.setTextColor("Grey")

    text_exclude = Text(Point(640, ((480 - (d * h)) - 10)), d)
    text_exclude.draw(win)
    text_exclude.setSize(18)
    text_exclude.setStyle("bold")
    text_exclude.setFace("helvetica")
    text_exclude.setTextColor("Grey")

    try:
        win.getMouse()
        win.close()
    except GraphicsError:
        pass


def main():
    outcomes = []
    outcome_values = {'Progress.': 0, 'Progress (module trailer).': 0, 'Do not Progress - module retriever.': 0,
                      'Exclude': 0}

    is_staff = input("Are you a staff member? (y/q): ").lower() == 'y'

    if is_staff:
        while True:
            pass_credits = get_credits("Please enter student's credits at pass: ")
            defer_credits = get_credits("Please enter student's credits at defer: ")
            fail_credits = get_credits("Please enter student's credits at fail: ")

            outcome = predict_outcome(pass_credits, defer_credits, fail_credits)
            print(outcome)

            outcomes.append(outcome)
            outcome_values[outcome] += 1

            another_entry = input("Would you like to enter another set of data? (y/q): ")
            if another_entry.lower() != 'y':
                break

    else:  # Student
        pass_credits = get_credits("Please enter your credits at pass: ")
        defer_credits = get_credits("Please enter your credits at defer: ")
        fail_credits = get_credits("Please enter your credits at fail: ")

        outcome = predict_outcome(pass_credits, defer_credits, fail_credits)
        print(outcome)

        outcomes.append(outcome)
        outcome_values[outcome] += 1

    print("Part 2 :")
    with open('text.txt', 'w') as file:
        file.write("Part 3 :\n")
        for outcome, count in outcome_values.items():
            print(outcome, "-", count)
            file.write(f"{outcome} - {count}\n")

    h = max(outcome_values.values())
    maxheight = 400
    height_for_one_point = maxheight / h
    histogram(height_for_one_point, outcome_values['Progress.'], outcome_values['Progress (module trailer).'],
              outcome_values['Do not Progress - module retriever.'], outcome_values['Exclude'])


if __name__ == "__main__":
    main()
