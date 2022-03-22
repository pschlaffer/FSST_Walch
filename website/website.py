# --------- Philip Schlaffer & Benedikt Mangott
# --------- 22.02.2022
# --------- FSST - Walch

# ------------------------------------------------------ Libarys
import webbrowser
from tkinter  import *
from datetime import date

def website_build(select, value1, value2, calculated):
    # ------------------------------------------------------ Resistor
    calc_string_value2_R1    = str("\nR1: " + str(value1) + "\n")
    calc_string_value2_R2    = str("R2: " + str(value2) + "\n")
    calc_string_calculated_R = str("Calculated: " + str(calculated) + "\n")
    name_today_parallel      = str("\n--------- Parallel Schaltung Berechnen --------- " + str(date.today()))
    name_today_seriell       = str("\n--------- Serielle Schaltung Berechnen --------- " + str(date.today()))
    # ------------------------------------------------------ Capacitor
    calc_string_value_H1     = str("H1: " + str(value2) + "\n")
    calc_string_value_F1     = str("F1: " + str(value2) + "\n")
    name_today_LC_glied      = str("\n--------- LC Glied Berechnen --------- " + str(date.today()))
    name_today_RC_glied      = str("\n--------- RC Glied Berechnen --------- " + str(date.today()))
    # ------------------------------------------------------ Spool
    name_today_RL_glied      = str("\n--------- RL Glied Berechnen --------- " + str(date.today()))
    
    # ------------------------------------------------------ Dateien
    date_file = str("website/calc_files/calc_" + str(date.today()) + ".txt")
    website_file_latest = open("website/calc_files/latest.txt", "a+")
    website_file_date   = open(date_file, "a+")

    # ------------------------------------------------------ Resistor
    # ------------------------------------------------------ Parallel Schaltung
    if select == "P":
        website_file_latest.write(name_today_parallel + calc_string_value2_R1 + calc_string_value2_R2 + calc_string_calculated_R)
        website_file_latest.close()
        website_file_date.write(name_today_parallel + calc_string_value2_R1 + calc_string_value2_R2 + calc_string_calculated_R)
        website_file_date.close()
    # ------------------------------------------------------ Serielle Schaltung
    if select == "S":
        website_file_latest.write(name_today_seriell + calc_string_value2_R1 + calc_string_value2_R2 + calc_string_calculated_R)
        website_file_latest.close()
        website_file_date.write(name_today_seriell + calc_string_value2_R1 + calc_string_value2_R2 + calc_string_calculated_R)
        website_file_date.close()
    
    # ------------------------------------------------------ Capacitor
    # ------------------------------------------------------ LC Glied
    if select == "LC":
        website_file_latest.write(name_today_LC_glied + "\n" + calc_string_value_F1 + calc_string_value_H1 + calc_string_calculated_R)
        website_file_latest.close()
        website_file_date.write(name_today_LC_glied + "\n" + calc_string_value_F1 + calc_string_value_H1 + calc_string_calculated_R)
        website_file_date.close()
    # ------------------------------------------------------ RC Glied
    if select == "RC":
        website_file_latest.write(name_today_RC_glied + calc_string_value2_R1 + calc_string_value_F1 + calc_string_calculated_R)
        website_file_latest.close()
        website_file_date.write(name_today_RC_glied + calc_string_value2_R1 + calc_string_value_F1 + calc_string_calculated_R)
        website_file_date.close()
    
    # ------------------------------------------------------ Spool
    # ------------------------------------------------------ RL Glied
    if select == "RL":
        website_file_latest.write(name_today_RL_glied + calc_string_value2_R1 + calc_string_value_H1 + calc_string_calculated_R)
        website_file_latest.close()
        website_file_date.write(name_today_RL_glied + calc_string_value2_R1 + calc_string_value_H1 + calc_string_calculated_R)
        website_file_date.close()