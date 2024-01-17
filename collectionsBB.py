import json
import pandas as pd



prodat = pd.read_json("output.json")

def collectionINF(name_of_collection):
    '''
    {name_of_collection} ~ MUST BE WRITTEN IN ALL CAPS
    '''
    with open("./skillsDAT/Foraginglvlreq.json") as file:
        collection_values = json.load(file)
        player_collection = prodat["profile"]["members"]["c3ca1ae1236c45d5922f2b1ec7eca271"]["collection"][f"{name_of_collection}"]
        found_level = "Level 0"
        percent_to_next = 0
        amount_to_next = 0
        overflow_items_v = False
        overflow_items = 0
        x = 0

        last_iterated_level = ""
        for level, value in exp_values.items():
            if value > player_exp:
                found_level = last_iterated_level
                break;
            last_iterated_level = level
            x = x + 1
        if x == 51:
            overflow_exp_v = True
            overflow_exp = exp_values["Level 50"] - player_exp
            return {
            'level': found_level,
            'xp_current': player_exp,
            'xp_for_next': "0",
            'progress': "100%",
            'overflow_exp': overflow_exp
            }
        else:
            next_level = exp_values[f"Level {x}"]
            next_level_amount = (exp_values[f"Level {x}"] - exp_values[f"Level {x-1}"])
            next_level_player = (player_exp - exp_values[f"Level {x-1}"])
            percent_to_next = (next_level_player/next_level_amount)*100
            amount_to_next = next_level-player_exp
            # print(exp_values[f"Level {x}"])
            # print(percent_to_next)
            # print(next_level_amount)
            # print(next_level_player)
            # print(amount_to_next)
            return {
                'level': found_level,
                'xp_current': next_level_player,
                'xp_for_next': next_level_amount,
                'progress': percent_to_next
            }