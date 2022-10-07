def main():
    cough = in_boolean("This is a fever diagnosis system.\n\
To facilitate our diagnosis, please answer the following questions.(Yes or\
 No)\n-------------------------\nAre you coughing? ")
    # to make logical chain clear, we'll ask headache before short_breath
    headache = in_boolean("Do you have a headache? ")
    # to make codes readable, we add a variable check_aching to check whether
    # we should ask aching bones or joints which's unnecessary. But bc. main()
    # returns when matching any diagnosis, so if function is still execuating
    # after making all previous evaluation, we should check the aching question

    # because we find a common area consists of the same bunch of questions
    # so we'll deal with other symptoms first
    if (cough):
        short_breath = in_boolean("Are you short of breath\
 or wheezing or coughing up phlegm? ")
        if (short_breath):
            print("Possibilities include pneumonia or infection\
 of airways.")
            return
        elif (headache):
            # headache or aching would have the diagnosis
            # but still decide to seperate these two conditions
            print("Possibilities include viral infection.")
            return
    elif (headache):
        f_pain = in_boolean("Are you experiencing any of the following\
 pain when bending your head forward, nausea or vomiting, bright\
 light hurting your eyes, drowsiness or confusion? ")
        if (f_pain):
            print("Possibilities include menigitis.")
            return
        elif (in_boolean("Are you vomiting or had diarrhead? ")):
            print("Possibilities include digestive tract infection")
            return
    check_aching()


# All diagnoses based on the answer to aching or not are as follows.
def check_aching():
    aching_bj = in_boolean("Do you have aching bones or\
aching joints? ")
    if (aching_bj):
        print("Possibilities include viral infection.")
        return
    elif (in_boolean("Do you have a rash? ")):
        print("Insufficient information to list possibilities.")
        return
    elif (in_boolean("Do you have a sore throat? ")):
        print("Possibilities include a throat infection.")
        return
    elif (in_boolean("Do you have back pain just above the waist with\
chills and fever? ")):
        print("Possibilities include kidney infection.")
        return
    elif (in_boolean("Do you have pain urinating or are urinating\
more often? ")):
        print("Possibilities include a urinary tract infection.")
        return
    elif (in_boolean("Have you spent the day in the sun or in hot\
conditions? ")):
        print("Possibilities sunstroke or heat exhaustion.")
        return
    else:
        print("Insufficient information to list possibilities.")


# Assume we only have input of yes or no
# define a function to convert input answer to boolean value
# True for yes, False for no(actually for answer except yes)
def in_boolean(prompt):
    in_lower = input(prompt).lower()
    return in_lower == "yes"


main()
