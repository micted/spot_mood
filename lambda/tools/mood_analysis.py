import pandas as pd
from tools.playlists import analyze_track_mood


# genre score

# lyrics score

# number of plays score

# whether liked music or not

def overall_mood(final):
    
    mood = {
        5: "Very Happy",
        4: "Happy",
        3: "Neutral",
        2: "Sad",
        1: "Very Sad"
    }

    countmood = {"5": 0, "4": 0, "3": 0, "2": 0, "1": 0, "0": 0}

    # 5: Very Happy
    # 4: Happy
    # 3: Neutral
    # 2: Sad
    # 1: Very Sad
    # Based on the overall mood score, you can assign the corresponding happiness level. For example:

    # If the overall mood score is between 0.35 and 0.4, assign 5 (Very Happy)
    # If the overall mood score is between 0.25 and 0.35, assign 4 (Happy)
    # If the overall mood score is between 0.15 and 0.25, assign 3 (Neutral)
    # If the overall mood score is between 0.05 and 0.15, assign 2 (Sad)
    # If the overall mood score is between 0 and 0.05, assign 1 (Very Sad)



    for f in final:

        if f>=0.4:
            if not countmood["5"]:
                countmood["5"] = 1
            countmood["5"] +=1

        elif 0.25 <= f <= 0.4:
            if not countmood["4"]:
                countmood["4"] = 1
            countmood["4"] +=1
            
        elif 0.15 <= f <= 0.25:
            if not countmood["3"]:
                countmood["3"] = 1
            countmood["3"] +=1

        elif 0.05 <= f <= 0.15:
            if not countmood["2"]:
                countmood["2"] = 1
            countmood["2"] +=1

        elif 0 <= f <= 0.05:
            if not countmood["1"]:
                countmood["1"] = 1
            countmood["1"] +=1
        else:
            if not countmood["0"]:
                countmood["0"] = 1
            countmood["0"] +=1

    
    max_value = max(countmood.values())

    for k,v in countmood.items():

        if v == max_value:

            majority_score = k

    
            
    if majority_score == "5":

        return "very happy"
    elif majority_score == "4":

        return "happy"

    elif majority_score == "3":

        return "Netural"
    elif majority_score == "2":

        return "sad"

    else:
        return "very sad"



        


    # if 0.35 <= overall_mood_score <= 0.4:
    #     happiness_level = 5
    #     print(mood.get(happiness_level,"none"))
    # elif 0.25 <= overall_mood_score <= 0.35:
    #     happiness_level = 4
        
    # elif 0.15 <= overall_mood_score <= 0.25:
    #     happiness_level = 3
    # elif 0.05 <= overall_mood_score <= 0.15:
    #     happiness_level = 2
    # elif 0 <= overall_mood_score <= 0.05:
    #     happiness_level = 1
    # else:
    #     happiness_level = 0

