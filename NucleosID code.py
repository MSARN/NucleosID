#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2017 CNRS and University of Strasbourg
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License

import tkinter as tk
from tkinter.filedialog import *
import csv
import os
import tkinter.ttk as ttk
import pandas as pd

def pathway():
    filepath = askopenfilename(title="Open a file",filetypes=[('mgf files', '.mgf'), ('txt files', '.txt')])
    e2.delete(0, "end")
    e2.insert(0, filepath)

def running():
    
    try:
    
        # Settings
        
        try:
            precision = float(s.get())
        except:
            precision = 0.1
        
        if precision > 100:
            precision = 100
        elif precision < 0:
            precision = 0
        
        # choice of database
        ref_name = t11.get()
        
        # choice of output file format
        type_file = val.get()
        
        #choice of the output file name
        end_file_name = e1.get()
        
        # file path of the enter file
        path_data = e2.get()
        
        enter_file_name = os.path.basename(path_data)
        
        pos_path = path_data.find(enter_file_name)
        path_output = path_data[:pos_path]
        
            
        if type_file == "text":
            inter_end_file_name = end_file_name + ".txt"
        elif type_file == "csv":
            inter_end_file_name = end_file_name + ".csv"
        else:
            inter_end_file_name = end_file_name + ".xlsx"
        

        full_end_file_name = path_output + inter_end_file_name

        try:
            score_threshold = int(e3.get())
        except:
            threshold = e3.get()
            pos = threshold.find('.')
            
            try:
                score_threshold = int(threshold[:pos])
            except:
                score_threshold = 20
        
        # relative intensity threshold value
        if score_threshold < 0:
            score_threshold = 0
        elif score_threshold > 100:
            score_threshold = 100

        try:
            frequency = float(s2.get())
        except:
            frequency = 0.1
        
        if frequency < 0.00001:
            frequency = 0.00001
        elif frequency > 10:
            frequency = 10
        
        comparison_type = val2.get()
        

        precision_inter_time = str(frequency)
        pos = precision_inter_time.find('.') +1
        precision_inter_time2 = precision_inter_time[pos:]

        precision_time = len(precision_inter_time2)

        precision_inter_ms = str(precision)
        pos = precision_inter_ms.find('.')+1
        precision_inter_ms2 = precision_inter_ms[pos:]

        precision_ms = len(precision_inter_ms2)
        
        sys_info = str(os.uname())
    
        pos = sys_info.find('sysname') + 9
    
        sys_name = sys_info[pos:pos+1]
    
            
        try:
            reference_value = int(e4.get())
        except:
            reference = e4.get()
            pos = reference.find('.')
            
            try:
                reference_value = int(reference[:pos])
            except:
                reference_value = 0
        
        if reference_value < 0:
            reference_value = 0
        
        # opening the reference file

        try:
        
#            if sys_name == 'W':
#                file_modif = open("BD\\"+ref_name+".csv")
#            else:
#                file_modif = open("BD/"+ref_name+".csv")
            file_modif = open("BD/"+ref_name+".csv")
            reader = csv.reader(file_modif,delimiter=";")

            list_inter_modif_ARN = []
            list_modif_ARN = []

            for elm in reader:
                list_inter_modif_ARN.append(elm)

            for i in range(1,len(list_inter_modif_ARN)):
                list_modif_ARN.append(list_inter_modif_ARN[i])

            file_modif.close()

            # output: list containing the references


            # Importing the data file
            
            try:
                file_data = open(path_data, 'r')
                contents = file_data.readlines()

                file_data.close()

                list_interm = []
                list_final_inter = []
                list_value = []

                for i in range(0,len(contents)):
                    line = contents[i]
                    extract_character = line[0:6]
                    if extract_character == 'RTINSE':
                        list_interm.append(line)
                    elif extract_character == 'PEPMAS':
                        list_interm.append(line)
                    elif extract_character[0] == '1':
                        list_value.append(line)
                    elif extract_character[0] == '2':
                        list_value.append(line)
                    elif extract_character[0] == '3':
                        list_value.append(line)
                    elif extract_character[0] == '4':
                        list_value.append(line)
                    elif extract_character[0] == '5':
                        list_value.append(line)
                    elif extract_character[0] == '6':
                        list_value.append(line)
                    elif extract_character[0] == '7':
                        list_value.append(line)
                    elif extract_character[0] == '8':
                        list_value.append(line)
                    elif extract_character[0] == '9':
                        list_value.append(line)
                    elif extract_character == 'END IO':
                        list_interm.append(list_value)
                        list_final_inter.append(list_interm)
                        list_value = []
                        list_interm = []

                # output: mgf data list
            
                # Background noise suppression
            
                list_final = []
                list_inter = []
                list_msms = []

                for i in range(0,len(list_final_inter)):
                    extract_msms = list_final_inter[i][2]

                    for j in range(0,len(extract_msms)):
                        msms_inter = extract_msms[j]
                        pos = msms_inter.find('\t') +1
                        pos2 = msms_inter.rfind('\t')

                        msms = int(msms_inter[pos:pos2])

                        if msms >= reference_value:
                            list_msms.append(msms_inter)

                    if len(list_msms) != 0:
                        list_inter.append(list_final_inter[i][0])
                        list_inter.append(list_final_inter[i][1])
                        list_inter.append(list_msms)
                        list_final.append(list_inter)
                        list_inter = []
                    
                    list_msms = []
                
                # output: mgf data list

                # Comparison of the data file with the reference file

                try:
                    list_found = []
                    list_inter = []
                    list_modif = []
                    list_msms = []
                    list_theoretical = []
                    list_observed = []

                    list_test = []
                    list_test2 = []

                    maximum = 0
                    max_int = 0
                    value_found = False

                    for i in range(0,len(list_final)):
                        mass = list_final[i][1]
                        pos = mass.find('\t')
                        extract_mass = float(mass[8:pos])

                        for j in range(0,len(list_modif_ARN)):
                            ms_modif = float(list_modif_ARN[j][1])

                            if comparison_type == "Da":
                                substraction = abs(extract_mass - ms_modif)

                            else:
                                substraction = abs(ms_modif - extract_mass)/ms_modif * 1000000

                            if substraction < precision:
                                msms_mgf = list_final[i][2]

                                msms_theoretical = list_modif_ARN[j][2]
                                msms_theoretical = msms_theoretical.split(',')

                                for k in range(0,len(msms_mgf)):
                                    frag = msms_mgf[k]
                                    frag = frag.split("\t")
                                    frag_value = float(frag[0])

                                    intensity = int(frag[1])
                                    if intensity > maximum:
                                        maximum = intensity

                                    extract_msms = round(frag_value)

                                    for z in range(0,len(msms_theoretical)):

                                        extract_mgf = int(msms_theoretical[z])

                                        if extract_msms == extract_mgf:

                                            value_found = True

                                            if intensity > max_int:
                                                max_int = intensity

                                            list_observed.append(frag)

                                if value_found:

                                    list_msms.append(list_modif_ARN[j][0])
                                    list_msms.append(list_observed)
                                    list_theoretical.append(ms_modif)
                                    list_theoretical.append(msms_theoretical)

                                    list_msms.append(list_theoretical)
                                    list_msms.append(max_int)

                                    list_theoretical = []
                                    list_observed = []
                                    max_int = 0

                                    list_modif.append(list_msms)

                                    list_msms = []

                        if value_found:

                            list_inter.append(extract_mass)
                            list_inter.append(list_final[i][0])
                            list_inter.append(list_modif)
                            list_inter.append(maximum)

                            list_modif = []

                            list_found.append(list_inter)
                            list_inter = []

                        value_found = False
                        maximum = 0

                    # output: list of modifications found in the comparison
                
                    # relative intensity calculation + deletion of redundant results and lower than the threshold value
                    
                    try:
                    
                        list_inter = []
                        list_msms = []
                        list_terminal = []

                        for i in range(0, len(list_found)):
                            msms = list_found[i][2]

                            for j in range(0,len(msms)):
                                list_inter.append(msms[j][0])
                                list_inter.append(round(list_found[i][0],precision_ms))

                                theoretical = msms[j][2]
                                list_inter.append(round(theoretical[0],precision_ms))

                                observed = msms[j][1]
                                intensity_max = 0

                                for k in range(0,len(observed)):
                                    #extract_obs = round(float(observed[k][0]))

                                    extract_obs = str(round(float(observed[k][0])))

                                    if extract_obs not in list_msms:
                                        list_msms.append(extract_obs)
                                    #list_msms.append(extract_obs)

                                    intensity = int(observed[k][1])

                                    if intensity > intensity_max:
                                        intensity_max = intensity

                                msms_obs = ', '.join(list_msms)

                                list_inter.append(msms_obs)

                                msms_theo = theoretical[1]
                                msms_theoretical = ', '.join(msms_theo)

                                list_inter.append(msms_theoretical)

                                score = round(intensity_max / list_found[i][3] * 100, 1)

                                list_inter.append(score)

                                time = list_found[i][1]
                                pos = time.find('\n')
                                extract_time = round(float(time[12:pos])/60, precision_time)

                                list_inter.append(extract_time)

                                list_msms = []

                                list_terminal.append(list_inter)

                                list_inter = []

                        list_terminal2 = []
                        is_present = 0

                        list_terminal2.append(list_terminal[0])

                        for i in range(1,len(list_terminal)):
                            score = list_terminal[i][5]
                            if score > score_threshold:

                                time = list_terminal[i][6]

                                for j in range(0, len(list_terminal2)):
                                    extract_time = list_terminal2[j][6]

                                    substraction = abs(time-extract_time)

                                    if substraction < frequency:
                                        name = list_terminal[i][0]
                                        extract_name = list_terminal2[j][0]

                                        if name == extract_name:
                                            is_present += 1
                                            indice = j

                                if is_present == 0:
                                    list_terminal2.append(list_terminal[i])

                                else:
                                    score = list_terminal[i][5]
                                    extract_score = list_terminal2[indice][5]

                                    if score > extract_score:
                                        list_terminal2[j] = list_terminal[i]

                            is_present = 0
                        
                        # output: output list
                        
                        # file writing
                        
                        try:
                        
                            if type_file == "text":

                                result_file = open(full_end_file_name,'w')

                                result_file.write("Chosen parameters: \n")
                                result_file.write("File analyzed: "+path_data+"\n")
                                result_file.write("Database used: "+ref_name+"\n")
                                result_file.write("MS tolerance: "+str(precision)+comparison_type+"\n")
                                result_file.write("MS/MS absolute intensity threshold: "+str(reference_value)+"\n")
                                result_file.write("MS/MS score threshold: "+str(score_threshold)+"\n")
                                result_file.write("Active exclusion: "+str(frequency)+"\n")
                                
                                result_file.write("\n")

                                for i in range(0, len(list_terminal2)):
                                    result_file.write("Observed modification: "+list_terminal2[i][0]+"\n")
                                    result_file.write("Observed MS: "+str(list_terminal2[i][1])+" Da \n")
                                    result_file.write("Theoretical MS: "+str(list_terminal2[i][2])+" Da \n")
                                    result_file.write("Observed MS/MS: "+list_terminal2[i][3]+" Da \n")
                                    result_file.write("Theoretical MS/MS: "+list_terminal2[i][4]+" Da \n")
                                    result_file.write("Relative intensity: "+str(list_terminal2[i][5])+" % \n")
                                    result_file.write("Detection time: "+str(list_terminal2[i][6])+" min \n")
                                    result_file.write("\n")

                                result_file.close()

                            elif type_file == "csv":
                                db_full = "Database: "+ref_name
                                precision_full = "MS tolerance: "+ str(precision)+comparison_type
                                score_full = "MS/MS threshold: "+ str(score_threshold)
                                frequency_full = "Active exclusion: "+str(frequency)
                                threshold_full = "MS/MS abs I threshold: "+str(reference_value)

                                list_param = ["Chosen parameters: ", enter_file_name, db_full, precision_full, threshold_full, score_full, frequency_full]
                                list_title = ["Modification", "Observed MS", "Theoretical MS", "Observed MS/MS","Theoretical MS/MS", "Relative intensity (%)", "Detection time (min)"]

                                out = open(full_end_file_name, "w+")
                                writer = csv.writer(out, delimiter=";")

                                writer.writerow(list_param)

                                writer.writerow(list_title)

                                for i in range(0, len(list_terminal2)):
                                    writer.writerow(list_terminal2[i])

                                out.close()

                            else:
                                
#                                print("1")

                                list_name = []
                                list_MS = []
                                list_MS_theo = []
                                list_MSMS = []
                                list_MSMS_theo = []
                                list_score = []
                                list_time = []

                                for i in range(0, len(list_terminal2)):

                                    list_name.append(list_terminal2[i][0])
                                    list_MS.append(list_terminal2[i][1])
                                    list_MS_theo.append(list_terminal2[i][2])
                                    list_MSMS.append(list_terminal2[i][3])
                                    list_MSMS_theo.append(list_terminal2[i][4])
                                    list_score.append(list_terminal2[i][5])
                                    list_time.append(list_terminal2[i][6])
                                
#                                print("2")
                                
                                #print(type(comparison_type))
                                
                                precision_full = str(precision) + comparison_type
                                
#                                print("3")

                                df = pd.DataFrame({'Modification': list_name, 'Observed MS (Da)': list_MS, 'Theoretical MS (Da)':list_MS_theo, 'Observed MS/MS (Da)': list_MSMS, 'Theoretical MS/MS (Da)':list_MSMS_theo, 'Relative intensity (%)': list_score, 'Detection time (min)': list_time})
                                df2 = pd.DataFrame({'Chosen parameters':[''], 'File analyzed': [enter_file_name], 'Database':[ref_name], 'MS tolerance':[precision_full], 'MS/MS abs I threshold':[reference_value], 'MS/MS threshold': [score_threshold], 'Active exclusion (min)':[frequency]})

                                with pd.ExcelWriter(full_end_file_name) as writer:
                                    df.to_excel(writer, index=False, sheet_name="Result")
                                    df2.to_excel(writer, index=False, sheet_name="Parameter")
                            
                            e5.delete(0, "end")
                            e5.insert(0, 'Done')
                        
                        except:
                            print("error 5")
                            
                            e5.delete(0, "end")
                            e5.insert(0, 'Error 5')
                    
                    except:
                        print("error 4")
                        
                        e5.delete(0, "end")
                        e5.insert(0, 'Error 4')
                
                except:
                    print("error 3")
                    
                    e5.delete(0, "end")
                    e5.insert(0, 'Error 3')
            
            except:
                print("error 2")
                
                e5.delete(0, "end")
                e5.insert(0, 'Error 2')

        except:
        
            e5.delete(0, "end")
            e5.insert(0, 'Error 1')
            print("error 1")

        
    except:
        e5.delete(0, "end")
        e5.insert(0, 'Error 6')
        print("erreur 6")


# Interface

root = tk.Tk()

root.title("Nucleos'ID")
root.geometry("650x670")
root.config(bg ='#D9D9D9')
root.minsize(650, 670)

f = tk.Frame(root, bg ='white', width= 20, height=1)
f.pack(fill='x')

texte_titre = tk.Label(f, text="Nucleos'ID", font=("Calibris 17 bold"), padx = 20, pady = 10)

texte_description = tk.Label(f, text="Identifies RNA post-transcriptionnal modifications at nucleosides level", padx = 20, pady = 10)

texte_titre.grid(row = 0, column = 0, sticky = 'w', pady = 2)
texte_description.grid(row = 1, column = 0, sticky = 'w', pady = 2)

c = tk.Canvas(f, width=86, height=86)
c.grid(row = 0, column = 1, rowspan = 2, padx = 60, pady = 5)


img = tk.PhotoImage(file = 'logo3.png')
c.create_image(0,0, anchor='nw', image=img)

l_inter = tk.Frame(root, bg = 'black', width = 1)
l_inter.pack(fill='x')

l = tk.LabelFrame(root, text=" Input & output files ", bg = '#D9D9D9')
l.pack(fill="both", padx = 20, pady =20)

t = tk.Label(l, text="Output file name:", bg = '#D9D9D9', padx= 15, pady = 10)
t2 = tk.Label(l, text="Input MGF file:", bg = '#D9D9D9', padx= 15, pady = 10)

t.grid(row = 1, column = 0, sticky = 'w', pady = 2)
t2.grid(row = 0, column = 0, sticky = 'w', pady = 2)

t6 = tk.Label(l, text="Output file format:", bg = '#D9D9D9', padx= 15, pady = 10 )
t6.grid(row=2, column = 0, sticky = 'w', pady = 2)

e1 = tk.Entry(l, width=15)
e1.insert(0, "output")
e1.grid(row = 1, column = 1, pady = 2)

val = tk.StringVar()
val.set("excel")

r3 = tk.Radiobutton(l, variable=val, text=".txt", bg = '#D9D9D9', value="text")
r4 = tk.Radiobutton(l, variable=val, text=".csv", bg = '#D9D9D9', value="csv")
r5 = tk.Radiobutton(l, variable=val, text=".xlsx", bg = '#D9D9D9', value="excel")

r3.grid(row = 2, column = 1, sticky='w', padx= 30, pady = 2)
r4.grid(row = 2, column = 2, sticky='w', padx= 0, pady = 0)
r5.grid(row = 2, column = 3, sticky='w', padx= 0, pady = 0)

e2 = tk.Entry(l, width=15)
e2.grid(row = 0, column = 1, sticky = 'w', pady = 2)

b = tk.Button(l, text= " Browse file ", command=pathway)
b.grid(row = 0, column = 2, sticky = 'w', padx= 10, pady = 2)

l2 = tk.LabelFrame(root, text=" Settings ", bg = '#D9D9D9')
l2.pack(fill="both", padx = 20, pady =20)

t12 = tk.Label(l2, text="Database choice: ", bg = '#D9D9D9', padx = 20, pady = 10)
t4 = tk.Label(l2, text="MS tolerance: ", bg = '#D9D9D9', padx = 20, pady = 10)
t7 = tk.Label(l2, text="MS/MS score threshold:", bg = '#D9D9D9', padx = 20, pady = 10)
#t7 = tk.Label(l2, text="MS/MS absolute intensity threshold:", bg = '#D9D9D9', padx = 20, pady = 10)
t8 = tk.Label(l2, text="Active exclusion during:", bg = '#D9D9D9', padx = 20, pady = 10)
t9 = tk.Label(l2, text=" %", bg = '#D9D9D9', padx = 20, pady = 10)
t10 = tk.Label(l2, text=" min", bg = '#D9D9D9', padx = 20, pady = 10)
#t13 = tk.Label(l2, text="Threshold intensity value:", bg = '#D9D9D9', padx = 20, pady = 10)
t13 = tk.Label(l2, text="MS/MS absolute intensity threshold:", bg = '#D9D9D9', padx = 20, pady = 10)
t14 = tk.Label(l2, text="AU", bg = '#D9D9D9', padx = 20, pady = 10)

t12.grid(row = 0, column = 0, sticky = 'w')
t4.grid(row = 1, column = 0, sticky = 'w')
t13.grid(row = 2, column = 0, sticky = 'w')
t7.grid(row = 3, column = 0, sticky = 'w')
t8.grid(row = 4, column = 0, sticky = 'w')
t9.grid(row = 3, column = 2, sticky = 'w')
t10.grid(row = 4, column = 2, sticky = 'w')
t14.grid(row = 2, column = 2, sticky = 'w')


DB_list = ["Archaea", "Eukarya", "Eubacteria", "Archaea+Eubacteria", "Archaea+Eukarya", "Eubacteria+Eukarya", "Archaea+Eubacteria+Eukarya"]

t11 = ttk.Combobox(l2, values=DB_list, state='readonly')
t11.current(6)
t11.grid(row =0, column=1, sticky='w', pady =0)

l_value = [1, 0.1, 0.01, 0.001, 0.0001]

s = tk.Spinbox(l2, value=l_value, increment=0.0001)
s.delete(0, 5)
s.insert(0, 0.02)
s.grid(row=1, column=1, sticky='w', pady =0 )

e3 = tk.Entry(l2, width=15)
e3.insert(0, "20")
e3.grid(row = 3, column = 1, sticky = 'w', pady = 0)

l_value2 = ['0.1', '0.2', '0.5', '1', '2']

s2 = tk.Spinbox(l2, value=l_value2, increment=0.1)
s2.delete(0, 5)
s2.insert(0, 1)
s2.grid(row=4, column=1, sticky= 'w', pady=0)

val2 = tk.StringVar()
val2.set("Da")

r6 = tk.Radiobutton(l2, variable=val2, text="Da", bg = '#D9D9D9', value="Da")
r7 = tk.Radiobutton(l2, variable=val2, text="ppm", bg = '#D9D9D9', value="ppm")

r6.grid(row = 1, column = 2, sticky = 'w', pady = 2)
r7.grid(row = 1, column = 3, sticky = 'w', pady = 2)

e4 = tk.Entry(l2, width=15)
e4.insert(0, "0")
e4.grid(row=2, column=1, sticky= 'w')

l3 = tk.Frame(root, bg = '#D9D9D9', width = 1)
l3.pack(fill="both", padx = 10, pady =10)

b = tk.Button(l3, text=" RUN ", bg = '#D9D9D9', command=running)
b.configure(bg = '#D9D9D9')
b.grid(row = 0, column = 1, sticky = 'w', padx = 225, pady = 0)

b2 = tk.Button(l3, text="help", bg = '#D9D9D9')
b2.configure(bg = '#D9D9D9')
b2.grid(row = 0, column = 0, sticky = 'w', padx = 10, pady = 0)

l_inter2 = tk.Frame(root, bg = 'black', width = 1)
l_inter2.pack(fill='x')

e5 = tk.Entry(root)
e5.pack(fill='x', ipady = 13)
e5.insert(0, 'Ready to start')

root.mainloop()

