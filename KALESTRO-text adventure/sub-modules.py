import main as m
def PC_health_status(current_HP):
    HP_stats = {"FINE":"You are feeling fine!","INJURED":"Some cuts and bruises but otherwise you are just fine","CAUTION":"You are deeply wounded","DANGER":"You are gravely wounded","NEAR-DEATH":"YOU ARE AT DEATH's DOOR!"}
    if current_HP<=100 and current_HP>75:
        HP_level = "FINE"
    print(HP_stats[HP_level])
PC_health_status(m.player_char.health)
    
    