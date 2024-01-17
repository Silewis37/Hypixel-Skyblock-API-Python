from fastapi import FastAPI
import skillsBB
import skillsFF
app = FastAPI()

@app.get("/my-first-api")
def hello():
  return {"Hello world!"}

# /KS43/
@app.get("/ks43/skill/foraging_skill")
def KS43_Foraging_skill():
        level_data = skillsBB.foragingLVL()
        skill = "Foraging"
        level = level_data["level"]
        xp_current = level_data["xp_current"]
        xp_for_next = level_data["xp_for_next"]
        progress = level_data["progress"]

        return {
            "skill": "Foraging",
            "level": f"{level}",
            "current_xp": f"{xp_current:.2f}",
            "xp_for_next": f"{xp_for_next}",
            "progress": f"{progress:.2f}%"
            }
@app.get("/ks43/skill/mining_skill")
def KS43_Mining_skill():
    level_data = skillsBB.miningLVL()
    skill = "Mining"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Mining",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }
@app.get("/ks43/skill/farming_skill")
def KS43_Farming_skill():
    level_data = skillsBB.farmingLVL()
    skill = "Farming"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Farming",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }
@app.get("/ks43/skill/combat_skill")
def KS43_Combat_skill():
    level_data = skillsBB.combatLVL()
    skill = "Combat"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Combat",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }
@app.get("/ks43/skill/fishing_skill")
def KS43_Fishing_skill():
    level_data = skillsBB.fishingLVL()
    skill = "Fishing"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Fishing",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }
@app.get("/ks43/skill/enchanting_skill")
def KS43_Enchanting_skill():
    level_data = skillsBB.enchantingLVL()
    skill = "Enchanting"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Enchanting",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }
@app.get("/ks43/skill/alchemy_skill")
def KS43_Alchemy_skill():
    level_data = skillsBB.alchemyLVL()
    skill = "Alchemy"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Alchemy",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }
@app.get("/ks43/skill/carpentry_skill")
def KS43_Carpentry_skill():
    level_data = skillsBB.carpentryLVL()
    skill = "Carpentry"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Carpentry",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }
@app.get("/ks43/skill/runecrafting_skill")
def KS43_Runecrafting_skill():
    level_data = skillsBB.runecraftingLVL()
    skill = "Runecrafting"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Runecrafting",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }
@app.get("/ks43/skill/social_skill")
def KS43_Social_skill():
    level_data = skillsBB.socialLVL()
    skill = "Social"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Social",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }
@app.get("/ks43/skill/taming_skill")
def KS43_Taming_skill():
    level_data = skillsBB.tamingLVL()
    skill = "Taming"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Taming",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }

# /ZAD5/
@app.get("/zad5/skill/foraging_skill")
def Zad5_Foraging_skill():
        level_data = skillsFF.foragingLVL()
        skill = "Foraging"
        level = level_data["level"]
        xp_current = level_data["xp_current"]
        xp_for_next = level_data["xp_for_next"]
        progress = level_data["progress"]

        return {
            "skill": "Foraging",
            "level": f"{level}",
            "current_xp": f"{xp_current:.2f}",
            "xp_for_next": f"{xp_for_next}",
            "progress": f"{progress:.2f}%"
            }
@app.get("/zad5/skill/mining_skill")
def Zad5_Mining_skill():
    level_data = skillsFF.miningLVL()
    skill = "Mining"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Mining",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }
@app.get("/zad5/skill/farming_skill")
def Zad5_Farming_skill():
    level_data = skillsFF.farmingLVL()
    skill = "Farming"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Farming",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }
@app.get("/zad5/skill/combat_skill")
def Zad5_Combat_skill():
    level_data = skillsFF.combatLVL()
    skill = "Combat"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Combat",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }
@app.get("/zad5/skill/fishing_skill")
def Zad5_Fishing_skill():
    level_data = skillsFF.fishingLVL()
    skill = "Fishing"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Fishing",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }
@app.get("/zad5/skill/enchanting_skill")
def Zad5_Enchanting_skill():
    level_data = skillsFF.enchantingLVL()
    skill = "Enchanting"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Enchanting",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }
@app.get("/zad5/skill/alchemy_skill")
def Zad5_Alchemy_skill():
    level_data = skillsFF.alchemyLVL()
    skill = "Alchemy"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Alchemy",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }
@app.get("/zad5/skill/carpentry_skill")
def Zad5_Carpentry_skill():
    level_data = skillsFF.carpentryLVL()
    skill = "Carpentry"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Carpentry",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }
@app.get("/zad5/skill/runecrafting_skill")
def Zad5_Runecrafting_skill():
    level_data = skillsFF.runecraftingLVL()
    skill = "Runecrafting"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Runecrafting",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }
@app.get("/zad5/skill/social_skill")
def Zad5_Social_skill():
    level_data = skillsFF.socialLVL()
    skill = "Social"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Social",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }
@app.get("/zad5/skill/taming_skill")
def Zad5_Taming_skill():
    level_data = skillsFF.tamingLVL()
    skill = "Taming"
    level = level_data["level"]
    xp_current = level_data["xp_current"]
    xp_for_next = level_data["xp_for_next"]
    progress = level_data["progress"]

    return {
        "skill": "Taming",
        "level": f"{level}",
        "current_xp": f"{xp_current:.2f}",
        "xp_for_next": f"{xp_for_next}",
        "progress": f"{progress:.2f}%"
        }