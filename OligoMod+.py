import tkinter as tk
from tkinter.filedialog import *
import csv
import os
import tkinter.ttk as ttk
import pandas as pd

def pathway():
    filepath = askopenfilename(title="Open a file",filetypes=[('mgf files', '.mgf'), ('txt files', '.txt')])
    e3.delete(0, "end")
    e3.insert(0, filepath)

def pathway2():
    filepath = askopenfilename(title="Open a file",filetypes=[('txt files', '.txt')])
    e4.delete(0, "end")
    e4.insert(0, filepath)

# program function

def Binomial(n,x,p):
    B = 0
    
    for i in range(x,n+1):
        way = factorial(n) / (factorial(i) * factorial(n-i))

        B += way * p**i * (1-p)**(n-i)
    
    return B

def ValueBinomial(n,k):
    line = content[k]
    value = line.split(';')[n]
    return float(value)
    
def Sort(elm):
    pos1 = elm.find('\t') +1
    pos2 = elm.rfind('\t')
    intensity = int(elm[pos1:pos2])
    return intensity
    
def Tri(elm):

    if len(elm) == 2:
        end = elm[1:]
        return end

    else:
        pos = elm.find(':')
        end = elm[1:pos]
        return end




def running():

    # settings
    
    try:
        ms_precision = float(e5.get())
    except:
        ms_precision = 0.1
        
    if ms_precision < 0:
        ms_precision = 0
    
    try:
        msms_precision = float(e6.get())
    except:
        msms_precision = 0.1
    
    if msms_precision < 0:
        msms_precision = 0
    
    enzyme = t9.get()
    
    enter_file_mgf_full = e3.get()
    
    name_mgf = os.path.basename(enter_file_mgf_full)
    pos_path = enter_file_mgf_full.find(name_mgf)
    
    path_mgf = enter_file_mgf_full[:pos_path]
    
    type_file = val.get()
    
    end_file_name = e1.get()
    
    if type_file == "text":
        full_end_file_name = path_mgf + end_file_name + ".txt"
        
    elif type_file == "csv":
        full_end_file_name = path_mgf + end_file_name + ".csv"
    
    else:
        full_end_file_name = path_mgf + end_file_name + ".xlsx"
        
    
    enter_file_fasta_full = e4.get()
    
    name_fasta = os.path.basename(enter_file_fasta_full)
    pos_path = enter_file_fasta_full.find(name_fasta)
    
    path_fasta = enter_file_fasta_full[:pos_path]
    
    name_seq = e2.get()
    
    name_file_seq = path_fasta + name_seq + ".rtf"
    
    result_precison_inter = 0.01

    if result_precison_inter == 1:
        result_precison = 0

    elif result_precison_inter == 0.1:
        result_precison = 1

    elif result_precison_inter == 0.01:
        result_precison = 2

    elif result_precison_inter == 0.001:
        result_precison = 3

    if enzyme == "RNase A":
        cut = ['C','U']

    else:
        cut = ['G']
    
    # opening sequence

    file_data = open(enter_file_fasta_full, 'r')
    content = file_data.readlines()

    file_data.close()

    header = content[0]
    print(header)

    sequence = ""

    for i in range(1,len(content)):
        sequence_inter = content[i]
        pos = sequence_inter.find('\n')
        sequence_piece = sequence_inter[:pos]

        sequence = sequence + sequence_piece
        
    # output: sequence string variable
    
    # Digestion

    if enzyme == "RNase T1":
        list_modif = ["(", "9","⊄","#","€","†","⊇","K","ε","O","ξ","]","∠","R","|","∨","æ","±","/","L","γ","7","∑","W","⊆","š","y","ς","φ","∉","Q","⇑","Ω","¥","D","Y"]

    else:
        list_modif = ["B", "'","v","?","Ç","%",">","µ","λ","τ","∅","M","°","β","¡","ℵ","¿","}","P","D","]","δ","κ","T","J","Z","2","4","∝","ρ","σ","F","∏","5","Ѷ","{","∫","&","◊","S","ω","~","1","l","r","℘","≥","V","∩","!","3",",","υ","π","¾","X","Þ",")","b","Ͽ","$","Ð","≅","¼","½","α","Ê","⊥","Γ","∃","Δ","h","f","\\"]

    list_inter = []
    list_fragment_inter = []
    index = 0
    last_pos = 0

    for i in range(0, len(sequence)):
        nucleo = sequence[i]

        if nucleo in cut:
            str_index = str(index)+ ".0"
            list_inter.append(str_index)
            list_inter.append(sequence[last_pos:i+1])

            last_pos = i+1

            index +=1
            list_fragment_inter.append(list_inter)
            list_inter = []
            print(last_pos)

    if last_pos != len(sequence):
        str_index = str(index) + ".0"
        list_inter.append(str_index)
        list_inter.append(sequence[last_pos:])
        list_fragment_inter.append(list_inter)
        list_inter = []

    #output: list of unmodified oligonucléotides

    # digestion of modified oligonucleotides
    
    list_origin = list_fragment_inter

    begin_pos = 0

    list_fragment = []
    list_inter = []

    for i in range(0, len(list_modif)):
        modif = list_modif[i]

        for j in range(0, len(list_fragment_inter)):
            seq = list_fragment_inter[j][1]

            for k in range(0, len(seq)-1):
                lettre = seq[k]

                if modif == lettre:

                    extract_indice = list_fragment_inter[j][0]
                    pos = extract_indice.find('.')
                    pos_indice = int(extract_indice[pos+1:])

                    frag_indice = int(extract_indice[:pos])

                    seq_origin = list_origin[frag_indice][1]

                    if pos_indice == 0:
                        indice = str(frag_indice) +"." +str(k+1)

                    else:
                        cal_indice = pos_indice - len(seq) +k +1
                        indice = str(frag_indice) +"." + str(cal_indice)

                    list_inter.append(indice)

                    list_inter.append(seq[0:k+1])

                    if list_inter not in list_fragment:
                        list_fragment.append(list_inter)

                    list_inter = []

                    seq_frag = seq[k+1:]

                    if pos_indice != 0:
                        indice = extract_indice

                    else:
                        indice = extract_indice[:pos+1]+ str(len(seq))

                    list_inter.append(indice)

                    list_inter.append(seq_frag)

                    if list_inter not in list_fragment:
                        list_fragment.append(list_inter)

                    list_inter = []

            indice = str(list_fragment_inter[j][0])

            list_inter.append(indice)

            list_inter.append(seq)

            list_fragment.append(list_inter)
            list_inter = []

        list_fragment_inter = list_fragment
        list_fragment = []
    
    #output: list of all oligonucleotides

    # Loading data to calculate mono masses

    file_mass = open("/Users/mevie/Desktop/stage_M2S4/prog2/data_full_mass.csv", 'r')
    reader = csv.reader(file_mass,delimiter=";")

    list_mono_mass_inter = []
    list_mono_mass = []

    for elm in reader:
        list_mono_mass_inter.append(elm)

    for i in range(1, len(list_mono_mass_inter)):
        list_mono_mass.append(list_mono_mass_inter[i])

    # output: list of masses of all nucleotides modified or not

    # Mass calculation

    list_fragment = list_fragment_inter

    calcul_mass = 0

    list_frag_mass = []

    for i in range(0, len(list_fragment)):
        fragment = list_fragment[i][1]

        for j in range(0, len(fragment)):
            frag_letter = fragment[j]

            for z in range(0, len(list_mono_mass)):
                name = list_mono_mass[z][0]

                if frag_letter == name:
                    mass_mono = float(list_mono_mass[z][1])

                    calcul_mass += mass_mono

        calcul_mass -= 61.9558
        list_frag_mass.append(calcul_mass)
        calcul_mass = 0

    # output: list of masses of oligonucleotides

    # MS m/z calculation

    list_mz_inter = []
    list_mz = []

    for i in range(0, len(list_fragment)):
        frag = list_fragment[i][1]
        mass_mono = list_frag_mass[i]

        if len(frag) <= 2:
            mass = mass_mono + 1.0078

            list_mz_inter.append(mass)

        else:
            number_z = len(frag)

            for j in range(1, number_z):
                mass = (mass_mono + (j*1.0078))/j
                list_mz_inter.append(mass)

        list_mz.append(list_mz_inter)
        list_mz_inter = []

    # output: list of m/z of all oligonucleotides
    
    # calculation of the m/z MS/MS of the fragments

    charge_list_c = []
    list_c = []
    charge_list_w = []
    list_w = []
    charge_list_y = []
    list_y = []
    list_calc = []
    charge_list_frag = []
    list_frag = []
    list_charge = []
    list_mB = []
    list_charge_mb = []
    first_list_charge_mb = []
    list_charge_mBH = []
    list_cwy = []
    first_list_charge_mbH = []
    list_mBH = []
    list_charge_aB = []
    list_aB = []


    for i in range(0, len(list_fragment)):
        frag = list_fragment[i][1]

        length = len(frag)

        mass_calcul_c = 0
        mass_calcul_w = 0
        mass_calcul_y = 0

        first_nucleo = frag[0]

        if length == 1:

            for z in range(0, len(list_mono_mass)):
                name = list_mono_mass[z][0]

                if name == frag:
                    list_frag.append(float(list_mono_mass[z][4]))

        else:
            for j in range(0, length-1):

                nucleo = frag[j+1]

                nucleo_c = frag[j]

                number = length - j -1
                nucleo_wy = frag[number]

                for z in range(0, len(list_mono_mass)):
                    name = list_mono_mass[z][0]

                    if name == nucleo_c:
                        if j == 0:
                            mass_calcul_c += float(list_mono_mass[z][2])

                        else:
                            mass_calcul_c += float(list_mono_mass[z][1])

                        charge_list_c.append(mass_calcul_c)

                        if j >= 1:

                            mass_calcul_aB = charge_list_c[0] + float(list_mono_mass[z][7])
                            list_charge_aB.append(mass_calcul_aB)

                            for l in range(2,j+1):

                                charged_mass_aB = (mass_calcul_aB + (l-1) * 1.0078)/l
                                list_charge_aB.append(charged_mass_aB)

                            list_aB.append(list_charge_aB)
                            list_charge_aB = []


                    if j == 0:
                        if name == first_nucleo:

                            mass_calcul_mB = list_mz[i][0] - float(list_mono_mass[z][5])
                            mass_calcul_mBH = list_mz[i][0] - float(list_mono_mass[z][6])
                            first_list_charge_mb.append(mass_calcul_mB)
                            first_list_charge_mbH.append(mass_calcul_mBH)


                            for k in range(2,len(frag)):
                                charged_mass_mB = (mass_calcul_mB + (k-1)*1.0078)/k
                                first_list_charge_mb.append(charged_mass_mB)

                                charged_mass_mBH = (mass_calcul_mBH + (k-1)*1.0078)/k
                                first_list_charge_mbH.append(charged_mass_mBH)

                            list_mB.append(first_list_charge_mb)
                            first_list_charge_mb = []

                            list_mBH.append(first_list_charge_mbH)
                            first_list_charge_mbH = []

                    if name == nucleo:

                        mass_calcul_mB = list_mz[i][0] - float(list_mono_mass[z][5])
                        list_charge_mb.append(mass_calcul_mB)

                        mass_calcul_mBH = list_mz[i][0] - float(list_mono_mass[z][6])
                        list_charge_mBH.append(mass_calcul_mBH)

                        for k in range(2, length):
                            charged_mass_calcul_mB = (mass_calcul_mB + (k-1)*1.0078)/k
                            list_charge_mb.append(charged_mass_calcul_mB)

                            charged_mass_calcul_mBH = (mass_calcul_mBH+ (k-1)*1.0078)/k
                            list_charge_mBH.append(charged_mass_calcul_mBH)

                        list_mB.append(list_charge_mb)
                        list_charge_mb = []

                        list_mBH.append(list_charge_mBH)
                        list_charge_mBH = []

                    if name == nucleo_wy:

                        if number == length-1:
                            mass_calcul_w += float(list_mono_mass[z][3])
                            mass_calcul_y += float(list_mono_mass[z][4])

                        else:
                            mass_calcul_w += float(list_mono_mass[z][1])
                            mass_calcul_y += float(list_mono_mass[z][1])

                        charge_list_w.append(mass_calcul_w)
                        charge_list_y.append(mass_calcul_y)

                if j > 0:
                    for h in range(1, j+1):
                        mass_calcul2_c = (mass_calcul_c + (h*1.0078))/(h+1)

                        mass_calcul2_w = (mass_calcul_w + (h*1.0078))/(h+1)

                        mass_calcul2_y = (mass_calcul_y+ (h*1.0078))/(h+1)

                        if mass_calcul2_c not in charge_list_c:
                            charge_list_c.append(mass_calcul2_c)

                        if mass_calcul2_w not in charge_list_w:
                            charge_list_w.append(mass_calcul2_w)

                        if mass_calcul2_y not in charge_list_y:
                            charge_list_y.append(mass_calcul2_y)

                list_charge.append(charge_list_c)
                list_charge.append(charge_list_w)
                list_charge.append(charge_list_y)

                charge_list_c = []
                charge_list_w = []
                charge_list_y = []

                list_cwy.append(list_charge)

                list_charge = []

            list_frag.append(list_cwy)
            list_frag.append(list_mB)
            list_frag.append(list_mBH)
            list_frag.append(list_aB)
            list_mB = []
            list_mBH = []
            list_cwy = []
            list_aB = []


        list_calc.append(list_frag)
        list_frag = []
    
    # output: list of all m/z of fragments for all ion series and all charge states

    # loading the mgf file

    file_data = open(enter_file_mgf_full, 'r')
    content_file = file_data.readlines()
    file_data.close()

    list_inter = []
    list_value = []
    list_mgf_inter = []
    max_intensity = 0

    for i in range(0, len(content_file)):
        line = content_file[i]
        extract_caract = line[0:6]


        if extract_caract == 'PEPMAS':
            list_inter.append(line)
        if extract_caract == 'RTINSE':
            list_inter.append(line)
        if extract_caract[0] == '1':
            list_value.append(line)
            pos = line.find('\t') +1
            extract_line = line[pos:]
            pos = extract_line.find('\t')
            intensity = int(extract_line[:pos])
            if max_intensity < intensity:
                max_intensity = intensity

        if extract_caract[0] == '2':
            list_value.append(line)
            pos = line.find('\t') +1
            extract_line = line[pos:]
            pos = extract_line.find('\t')
            intensity = int(extract_line[:pos])
            if max_intensity < intensity:
                max_intensity = intensity

        if extract_caract[0] == '3':
            list_value.append(line)
            pos = line.find('\t') +1
            extract_line = line[pos:]
            pos = extract_line.find('\t')
            intensity = int(extract_line[:pos])
            if max_intensity < intensity:
                max_intensity = intensity

        if extract_caract[0] == '4':
            list_value.append(line)
            pos = line.find('\t') +1
            extract_line = line[pos:]
            pos = extract_line.find('\t')
            intensity = int(extract_line[:pos])
            if max_intensity < intensity:
                max_intensity = intensity

        if extract_caract[0] == '5':
            list_value.append(line)
            pos = line.find('\t') +1
            extract_line = line[pos:]
            pos = extract_line.find('\t')
            intensity = int(extract_line[:pos])
            if max_intensity < intensity:
                max_intensity = intensity

        if extract_caract[0] == '6':
            list_value.append(line)
            pos = line.find('\t') +1
            extract_line = line[pos:]
            pos = extract_line.find('\t')
            intensity = int(extract_line[:pos])
            if max_intensity < intensity:
                max_intensity = intensity

        if extract_caract[0] == '7':
            list_value.append(line)
            pos = line.find('\t') +1
            extract_line = line[pos:]
            pos = extract_line.find('\t')
            intensity = int(extract_line[:pos])
            if max_intensity < intensity:
                max_intensity = intensity

        if extract_caract[0] == '8':
            list_value.append(line)
            pos = line.find('\t') +1
            extract_line = line[pos:]
            pos = extract_line.find('\t')
            intensity = int(extract_line[:pos])
            if max_intensity < intensity:
                max_intensity = intensity

        if extract_caract[0] == '9':
            list_value.append(line)
            pos = line.find('\t') +1
            extract_line = line[pos:]
            pos = extract_line.find('\t')
            intensity = int(extract_line[:pos])
            if max_intensity < intensity:
                max_intensity = intensity

        if extract_caract == 'END IO':
            list_inter.append(list_value)
            list_value = []

            list_inter.append(max_intensity)
            max_intensity = 0

            list_mgf_inter.append(list_inter)
            list_inter = []
    
    # output: list of m/z MS and MS/MS of mgf file

    # peak cleaning

    list_intensity = []
    list_mgf = []
    list_inter = []
    list_inter2 = []
    list_inter3 = []

    previous_value = 0

    for i in range(0, len(list_mgf_inter)):
        extract_value = list_mgf_inter[i]
        extract_msms = extract_value[2]

        if len(extract_msms) <= 10:
            list_mgf.append(extract_value)

        else:
            msms = extract_msms[0]
            pos = msms.find('.')
            hundred = int(int(msms[:pos])/100)

            list_inter2.append(msms)

            previous_value = hundred

            for j in range(1, len(extract_msms)):
                msms = extract_msms[j]
                pos = msms.find('.')
                hundred = int(int(msms[:pos])/100)

                if hundred == previous_value:
                    list_inter2.append(msms)

                else:
                    previous_value = hundred

                    if len(list_inter2) > 10:

                        sortedlist = sorted(list_inter2, key=Sort, reverse=True)

                        for z in range(0,10):
                            list_inter.append(sortedlist[z])

                            list_inter2 = []

                    else:
                        for z in range(0, len(list_inter2)):
                            list_inter.append(list_inter2[z])

                        list_inter2 = []

                        list_inter2.append(msms)

                if j == len(extract_msms)-1:

                    if len(list_inter2) <= 10:
                        for z in range(0,len(list_inter2)):
                            list_inter.append(list_inter2[z])

                        list_inter2 = []

                    else:

                        sortedlist = sorted(list_inter2, key=Sort, reverse=True)

                        for z in range(0, 10):
                            list_inter.append(sortedlist[z])

                        list_inter2 = []

            list_inter3.append(extract_value[0])
            list_inter3.append(extract_value[1])
            list_inter3.append(list_inter)
            list_inter3.append(extract_value[3])

            list_inter = []

            list_mgf.append(list_inter3)

            list_inter3 = []

    print("mgf")
    print(list_mgf)
    
    # output: list of m/z MS and MS/MS of the mgf file after peak cleaning

    # comparison of the reference with the mgf file

    list_inter = []
    list_mz_theore = []
    list_final = []
    list_mz_obs = []
    list_time = []
    list_ion = []

    list_elm_msms = []
    list_msms = []

    list_intensity = []
    list_inter2 = []
    list_final_intensity = []
    list_intensity_inter = []

    is_present =0

    list_inter3 = []

    for i in range(0, len(list_mz)):

        list_inter.append(list_fragment[i][0])

        list_inter.append(list_fragment[i][1])

        frag_mz = list_mz[i]

        max_intensity = 0
        mgf_max_intensity = 0

        for j in range(0, len(frag_mz)):
            extract_frag_mz = float(frag_mz[j])

            charge = str(j+1)

            mz_theore = str(round(extract_frag_mz, result_precison))+ '(+'+ str(charge) +')'

            list_mz_theore.append(mz_theore)

            for z in range(0, len(list_mgf)):
                mz_mgf_inter = list_mgf[z][1]
                pos = mz_mgf_inter.find('\t')
                mz_mgf = float(mz_mgf_inter[8:pos])

                sub = abs(mz_mgf - extract_frag_mz)

                if sub < ms_precision:

                    time = list_mgf[z][0]
                    pos = time.find('\n')
                    extract_time = float(time[12:pos])/60

                    mz_mgf_full = str(round(mz_mgf, result_precison)) + ' (+' + str(charge) + ')'

                    list_elm_msms.append(mz_mgf_full)
                    list_elm_msms.append(extract_time)

                    frag_msms = list_calc[i][0]
                    frag_msms_mB = list_calc[i][1]
                    frag_msms_mBH = list_calc[i][2]
                    frag_msms_aB = list_calc[i][3]

                    mgf_msms = list_mgf[z][2]

                    for l in range(0, len(mgf_msms)):
                        mgf_msms_inter = mgf_msms[l]

                        pos = mgf_msms_inter.find('\t')

                        extract_mgf_msms = float(mgf_msms_inter[:pos])

                        pos = mgf_msms_inter.find('\t')+1
                        intensity_mgf = mgf_msms_inter[pos:]
                        pos = intensity_mgf.find('\t')
                        intensity_frag_mgf = int(intensity_mgf[:pos])

                        list_inter2.append(extract_mgf_msms)
                        list_inter2.append(intensity_frag_mgf)

                        for k in range(0, len(frag_msms)):
                            indice_frag_msms = frag_msms[k]

                            for m in range(0, len(indice_frag_msms)):
                                cut_frag_msms = indice_frag_msms[m]

                                for n in range(0, len(cut_frag_msms)):
                                    charge_frag_msms = float(cut_frag_msms[n])

                                    sub_msms = abs(charge_frag_msms - extract_mgf_msms)

                                    if sub_msms < msms_precision:
                                        list_inter3.append(sub_msms)

                                        if m ==0:
                                            cut_type = 'c'
                                        elif m==1:
                                            cut_type = 'w'
                                        else:
                                            cut_type = 'y'

                                        observed_ion = cut_type +str(k+1)+ ' (+' + str(n+1) + ')'

                                        is_present += 1

                                        if observed_ion not in list_ion:
                                            list_ion.append(observed_ion)

                                        if max_intensity < intensity_frag_mgf:
                                            max_intensity = intensity_frag_mgf

                        for k in range(0, len(frag_msms_mB)):
                            for m in range(0, len(frag_msms_mB[k])):
                                extract_mB = frag_msms_mB[k][m]
                                extract_mBH = frag_msms_mBH[k][m]

                                sub_msms_mB = abs(extract_mB - extract_mgf_msms)
                                sub_msms_mBH = abs(extract_mBH - extract_mgf_msms)

                                if sub_msms_mB < msms_precision:
                                    list_inter3.append(sub_msms_mB)

                                    observed_mB = 'm-B'+str(k+1) + ' (+' + str(m+1) + ')'

                                    is_present += 1

                                    if observed_mB not in list_ion:
                                        list_ion.append(observed_mB)

                                    if max_intensity < intensity_frag_mgf:
                                        max_intensity = intensity_frag_mgf

                                if sub_msms_mBH < msms_precision:
                                    list_inter3.append(sub_msms_mBH)

                                    observed_mBH = 'm-BH' +str(k+1)+ ' (+'+ str(m+1) +')'

                                    is_present += 1

                                    if observed_mBH not in list_ion:
                                        list_ion.append(observed_mBH)

                                    if max_intensity < intensity_frag_mgf:
                                        max_intensity = intensity_frag_mgf

                        for k in range(0, len(frag_msms_aB)):
                            for m in range(0, len(frag_msms_aB[k])):
                                extract_aB = frag_msms_aB[k][m]

                                sub_msms_aB = abs(extract_aB - extract_mgf_msms)

                                if sub_msms_aB < msms_precision:
                                    list_inter3.append(sub_msms_aB)

                                    observed_aB = 'a-B'+str(k+2) + ' (+'+ str(m+1)+')'

                                    is_present += 1

                                    if observed_aB not in list_ion:
                                        list_ion.append(observed_aB)

                                    if max_intensity < intensity_frag_mgf:
                                        max_intensity = intensity_frag_mgf

                        if is_present != 0:
                            list_inter2.append('Match')

                        else:
                            list_inter2.append('None')

                        is_present = 0

                        list_intensity.append(list_inter2)
                        list_inter2 = []

                    list_elm_msms.append(list_ion)
                    list_ion = []

                    list_elm_msms.append(max_intensity)
                    max_intensity = 0

                    list_elm_msms.append(list_mgf[z][3])

                    list_elm_msms.append(list_inter3)
                    list_inter3 = []

                    list_msms.append(list_elm_msms)
                    list_elm_msms = []


                    list_intensity_inter.append(list_intensity)
                    list_intensity = []

        list_final_intensity.append(list_intensity_inter)
        list_intensity_inter = []


        list_inter.append(list_mz_theore)
        list_mz_theore = []

        list_inter.append(list_msms)
        list_msms = []

        list_final.append(list_inter)
        list_inter = []

    print("changement list final")
    print(list_final)
    print(len(list_final))

    print("intensité")
    print(list_final_intensity)
    print(len(list_final_intensity))
    
    # output 1: list of all oligonucleotides with mgf values if a match is found
    # output 2: list of intensities with presence or absence of the match

    # separation of values + sum of errors

    list_sum_error = []

    list_result = []
    list_inter = []

    for i in range(0,len(list_final)):
        extract_ion = list_final[i][3]

        if len(extract_ion) == 0:
            list_inter.append(list_final[i][0])
            list_inter.append(list_final[i][1])
            list_inter.append(list_final[i][2])
            list_result.append(list_inter)
            list_inter = []

            list_sum_error.append([])

        for j in range(0,len(extract_ion)):
            list_inter.append(list_final[i][0])
            list_inter.append(list_final[i][1])
            list_inter.append(list_final[i][2])
            list_inter.append(extract_ion[j][0])
            list_inter.append(extract_ion[j][1])
            list_inter.append(extract_ion[j][2])
            list_inter.append(extract_ion[j][3])
            list_inter.append(extract_ion[j][4])
            list_result.append(list_inter)
            list_inter = []

            list_sum_error.append(extract_ion[j][5])
    
    # output 1: same list as before but results are written differently
    # output 2: list of sum of errors for each result

    # 1st stage score calculation

    for i in range(0, len(list_result)):
        score_p = 0
        k = 0

        if len(list_result[i]) > 4:

            seq = list_result[i][1]
            frag = list_result[i][5]

            if len(frag) != 0:
                n = 3*(len(seq)-1) + len(seq)-2 + 2*len(seq)

                for j in range(0, len(frag)):
                    extract = frag[j][0]

                    if extract == 'c':
                        k+=1
                    elif extract == 'y':
                        k+=1

                # calculation of p

                extract_list = list_sum_error[i]

                sum = 0

                for j in range(0,len(extract_list)):
                    sum += extract_list[j]

                extract_ms = list_result[i][3]
                pos = extract_ms.find(" ")
                ms_value = float(extract_ms[:pos])

                print("score")
                print(sum)
                
                p = (n*0.1)/ms_value
                
                print(p)

                if k < n*p:
                    score_p = 1

                else:
                    for l in range(k,n+1):
                        way = factorial(n) / (factorial(l) * factorial(n-l))

                        score_p += way * p**l * (1-p)**(n-l)

            else:
                score_p = 1

        else:
            score_p = 1

        score_p = 0
        
        list_result[i].append(score_p)


    print("result 2")
    print(list_result)
    print(len(list_result))
    
    # output: list of oligonucleotides but with the score in addition

    # 2nd stage score calculation

    list_value = []

    for i in range(0,len(list_final_intensity)):
        extract_list = list_final_intensity[i]

        if len(extract_list) == 0:
            list_value.append(extract_list)

        else:
            for j in range(0, len(extract_list)):
                list_value.append(extract_list[j])

    print("list des intensités")
    print(list_value)
    print(len(list_value))
    
    # output: list of intensities

    # calculation
    # loading binomial values

    binomial_data = "/Users/mevie/Desktop/stage_M2S4/prog2/binomial_values.csv"

    binomial_file = open(binomial_data,'r')
    content = binomial_file.readlines()

    list_int1 = []
    list_int2 = []
    list_int3 = []
    list_int4 = []
    list_med = []
    list_score = []

    for i in range(0,len(list_value)):

        if len(list_result[i]) == 4:
            list_score.append(1)

        else:
            if len(list_result[i][5]) == 0:
                list_score.append(1)

            else:
                extract_list = list_value[i]
                length = len(extract_list)

                sm0 = 0
                sm1 = 0
                sm2 = 0
                sm3 = 0
                sm4 = 0

                if length ==1:
                    if extract_list[0][1] == 'None':
                        list_score.append(1)
                    else:
                        score = 0.5**4
                        list_score.append(score)

                elif length ==2:

                    for j in range(0, len(extract_list)):
                        extract_value = extract_list[j][0]

                        list_med.append(extract_value)

                        if extract_list[j][1] == 'Match':
                            sm0 += 1

                    med = int(stat.median(list_med))

                    list_med = []

                    for j in range(0, len(extract_list)):
                        if extract_list[j][0] >= med:
                            if extract_list[j][1] == 'Match':
                                sm1 +=1

                    score = ValueBinomial(sm0,sm1) * (ValueBinomial(sm1,sm1)**3)
                    list_score.append(score)

                    sm0 = 0
                    sm1 = 0

                elif length == 3 or length == 4:

                    for j in range(0, len(extract_list)):
                        extract_value = extract_list[j][0]

                        list_med.append(extract_value)

                        if extract_list[j][1] == 'Match':
                            sm0 +=1

                    med = int(stat.median(list_med))
                    list_med = []

                    for j in range(0, len(extract_list)):
                        if extract_list[j][0] >= med:
                            list_int1.append(extract_list[j])
                            list_med.append(extract_list[j][0])

                            if extract_list[j][1] == 'Match':
                                sm1 += 1

                    med = int(stat.median(list_med))
                    list_med = []

                    for j in range(0,len(list_int1)):
                        if list_int1[j][0] >= med:

                            if list_int1[j][1] == 'Match':
                                sm2 += 1

                    list_int1 = []

                    score = ValueBinomial(sm0,sm1) * ValueBinomial(sm1,sm2) * (ValueBinomial(sm2,sm2)**2)

                    list_score.append(score)

                    sm0 = 0
                    sm1 = 0
                    sm2 = 0

                elif length == 5 or length == 6 or length == 7 or length == 8:

                    for j in range(0, len(extract_list)):
                        list_med.append(extract_list[j][0])

                        if extract_list[j][1] == 'Match':
                            sm0 += 1

                    med = int(stat.median(list_med))
                    list_med = []

                    for j in range(0,len(extract_list)):
                        if extract_list[j][0] >= med:
                            list_int1.append(extract_list[j])
                            list_med.append(extract_list[j][0])

                            if extract_list[j][1] == 'Match':
                                sm1 += 1

                    med = int(stat.median(list_med))
                    list_med = []

                    for j in range(0, len(list_int1)):
                        if list_int1[j][0] >= med:
                            list_int2.append(list_int1[j])
                            list_med.append(list_int1[j][0])

                            if list_int1[j][1] == 'Match':
                                sm2 += 1

                    med = int(stat.median(list_med))
                    list_med = []

                    for j in range(0, len(list_int2)):
                        if list_int2[j][0] >= med:
                            list_int3.append(list_int2[j])

                            if list_int2[j][1] == 'Match':
                                sm3 += 1

                    score = ValueBinomial(sm0,sm1) * ValueBinomial(sm1,sm2) * ValueBinomial(sm2,sm3) * ValueBinomial(sm3,sm3)

                    list_score.append(score)

                    sm0 =0
                    sm1 = 0
                    sm2 = 0
                    sm3 = 0

                    list_int1 = []
                    list_int2 = []
                    list_int3 = []

                else:
                    for j in range(0, len(extract_list)):
                        list_med.append(extract_list[j][0])

                        if extract_list[j][1] == 'Match':
                            sm0 +=1

                    med = int(stat.median(list_med))
                    list_med = []

                    for j in range(0, len(extract_list)):
                        if extract_list[j][0] >= med:
                            list_int1.append(extract_list[j])
                            list_med.append(extract_list[j][0])

                            if extract_list[j][1] == 'Match':
                                sm1 += 1

                    med = int(stat.median(list_med))
                    list_med = []

                    for j in range(0, len(list_int1)):
                        if list_int1[j][0] >= med:
                            list_int2.append(list_int1[j])
                            list_med.append(list_int1[j][0])

                            if list_int1[j][1] == 'Match':
                                sm2 += 1

                    med = int(stat.median(list_med))
                    list_med = []

                    for j in range(0, len(list_int2)):
                        if list_int2[j][0] >= med:
                            list_int3.append(list_int2[j])
                            list_med.append(list_int2[j][0])

                            if list_int2[j][1] == 'Match':
                                sm3 += 1

                    med = int(stat.median(list_med))
                    list_med = []

                    for j in range(0, len(list_int3)):
                        if list_int3[j][0] >= med:
                            list_int4.append(list_int3[j])

                            if list_int3[j][1] == 'Match':
                                sm4 +=1

                    score = ValueBinomial(sm0,sm1) * ValueBinomial(sm1,sm2) * ValueBinomial(sm2,sm3) * ValueBinomial(sm3,sm4)

                    list_score.append(score)

                    sm0 = 0
                    sm1 = 0
                    sm2 = 0
                    sm3 = 0
                    sm4 = 0

                    list_int1 = []
                    list_int2 = []
                    list_int3 = []
                    list_int4 = []
    
    # output: list of scores for each result
    
    # output list creation

    writting_list = []
    list_inter = []
    previous_pos = 0
    previous_seq = ""
    previous_indice = ""
    previous_seq_pos = ""

    for i in range(0, len(list_result)):
        
        indice = list_result[i][0]

        pos = indice.find('.')
        first_indice = int(indice[:pos])

        second_indice = int(indice[pos+1:])

        seq = list_result[i][1]
        
        length = len(seq)
        
        if previous_indice == indice and previous_seq == seq:
            pos_seq = previous_seq_pos
        
        else:

            if second_indice == 0:
                
                if length == 1:
                    pos_seq = seq + str(previous_pos + 1)
                
                else:
                    pos_seq = seq[0]+ str(previous_pos+1)+ ":" + seq[len(seq)-1]+ str(previous_pos + length)
                    
                
                previous_pos += length
            
            else:
                
                if length == 1:
                    pos_seq = seq + str(previous_pos+second_indice)
                
                else:
                    
                    end_pos = previous_pos + second_indice
                    begin_pos = end_pos - length +1
                    
                    pos_seq = seq[0]+str(begin_pos) + ":"+ seq[length-1] + str(end_pos)
            
        
        list_inter.append(indice)
        list_inter.append(pos_seq)
        list_inter.append(seq)
        
        previous_seq = seq
        previous_seq_pos = pos_seq
        previous_indice = indice

        theore_ms = ', '.join(list_result[i][2])
        list_inter.append(theore_ms)

        if len(list_result[i])== 4:
            list_inter.append('None')
            list_inter.append(0)
            list_inter.append('None')
            list_inter.append(0)
            list_inter.append(0)
            list_inter.append(list_score[i])

        else:
            list_inter.append(list_result[i][3])
            time = round(list_result[i][4], result_precison)
            list_inter.append(time)

            if not list_result[i][5]:
                list_inter.append('None')
                list_inter.append(0)
                list_inter.append(0)
                list_inter.append(list_score[i])

            else:
                msms = ', '.join(list_result[i][5])

                intensity = list_result[i][6]
                max_intensity = list_result[i][7]
                score = round(intensity / max_intensity * 100, result_precison)
                list_inter.append(msms)
                list_inter.append(score)
                list_inter.append(list_result[i][8])
                list_inter.append(list_score[i])


        writting_list.append(list_inter)
        list_inter = []
        
    # output: output list

    # write the sequence in color

    # creating a list of redundant sequences

    list_double = []

    for i in range(0, len(writting_list)):
        extract_seq = writting_list[i][2]

        for j in range(i, len(writting_list)):
            extract_seq2 = writting_list[j][2]

            if extract_seq == extract_seq2:
                if writting_list[i][0] != writting_list[j][0]:

                    if extract_seq not in list_double:
                        list_double.append(extract_seq)

    # output: list of redundant sequences

    list_inter = []
    file_list = []
    list_inter2 = []

    previous_indice = 1
    previous_found = False

    length = 0

    for i in range(0, len(writting_list)):
        extract_indice = writting_list[i][0]
        pos = extract_indice.find('.')+1
        indice = int(extract_indice[pos:])

        if indice != 0:
            if writting_list[i][6] != 'None':
                list_inter.append(writting_list[i][1])

            previous_found = False

        else:

            if extract_indice != previous_indice:
                previous_indice = extract_indice
                seq = writting_list[i][2]

                if writting_list[i][6] != 'None':

                    if seq in list_double:
                        seq_full = "\cf5 " + seq

                    else:
                        seq_full = "\cf4 " +  seq

                    file_list.append(seq_full)
                    previous_found = True
                    length += len(seq)

                else :

                    if len(list_inter) == 0:
                        seq_full = "\cf3 " + seq
                        file_list.append(seq_full)
                        length += len(seq)

                    else:
                        sortedlist = sorted(list_inter, key=Tri)
                        extract_pos = writting_list[i][1]
                        pos = extract_pos.find(':')
                        b_pos = int(extract_pos[1:pos])
                        e_pos = int(extract_pos[pos+2:])

                        for j in range(0,len(sortedlist)):
                            extract = sortedlist[j]
                            pos = extract.find(':')
                            begin_pos = int(extract[1:pos])
                            end_pos = int(extract[pos+2:])

                            if length +1 == begin_pos:
                                frag = seq[begin_pos - length-1: end_pos-length]

                                length += len(frag)

                                if frag in list_double:
                                    seq_full = "\cf5 "+ frag

                                else:
                                    seq_full = "\cf4 " + frag

                                list_inter2.append(seq_full)

                            elif begin_pos < length +1:

                                if end_pos > length +1:
                                    frag = seq[length+1-b_pos:end_pos-e_pos+len(seq)]
                                    length += len(frag)

                                    frag2 = writting_list[i][2]

                                    if frag2 in list_double:
                                        seq_full = "\cf5 "+ frag

                                    else:
                                        seq_full = "\cf4 "+ frag

                                    list_inter2.append(seq_full)

                            else:

                                extract_pos = writting_list[i][1]
                                pos = extract_pos.find(':')
                                b_pos = int(extract_pos[1:pos])

                                p = begin_pos - (length+1)

                                frag = seq[length+1 - b_pos:p]

                                length += len(frag)

                                seq_full = "\cf3 " + frag

                                list_inter2.append(seq_full)

                                frag = seq[p:p + end_pos - begin_pos +1]

                                length += len(frag)

                                if frag in list_double:
                                    seq_full = "\cf5 " + frag

                                else:
                                    seq_full = "\cf4 " + frag

                                list_inter2.append(seq_full)

                        if length != e_pos:
                            frag = seq[length - len(seq)+1 :]

                            seq_full = "\cf3 " +frag

                            list_inter2.append(seq_full)

                            length += len(frag)

                        file_list.append(list_inter2)
                        list_inter2 = []

                        list_inter = []

            else:
                if previous_found == False:
                    if writting_list[i][6] != 'None':
                        seq = writting_list[i][2]

                        if seq in list_double:
                            file_list[len(file_list)-1] = "\cf5 " +  seq

                        else:
                            file_list[len(file_list)-1] = "\cf4 " +  seq

    # output: list of oligonucleotides reconstituting the sequence


    # overlay calculation

    counter = 0
    counter_all = 0
    counter_unique = 0

    for i in range(0, len(file_list)):
        extract = file_list[i]

        if type(extract) == list:
            for j in range(0,len(extract)):
                line = extract[j]
                pos = line.find(' ')
                seq = line[pos+1:]

                number = line[pos-1:pos]

                counter += len(seq)

                if number == '4':
                    counter_all += len(seq)
                    counter_unique += len(seq)

                elif number == '5':
                    counter_all += len(seq)

        else:
            pos = extract.find(' ')
            seq = extract[pos+1:]

            number = extract[pos-1:pos]

            counter += len(seq)

            if number == '4':
                counter_all += len(seq)
                counter_unique += len(seq)

            elif number == '5':
                counter_all += len(seq)

    coverage_all = counter / counter_all * 100
    coverage_unique = counter / counter_unique * 100
    
    # output: two overlay calculations

    # writing output files

    if type_file == "excel":
        list_position = []
        list_name = []
        list_theoretical_mz = []
        list_observed_ms = []
        list_time = []
        list_obs_ion = []
        list_score = []
        list_B = []
        list_B2 = []

        for i in range(0, len(writting_list)):

            list_position.append(writting_list[i][1])
            list_name.append(writting_list[i][2])
            list_theoretical_mz.append(writting_list[i][3])
            list_observed_ms.append(writting_list[i][4])
            list_time.append(writting_list[i][5])
            list_obs_ion.append(writting_list[i][6])
            list_score.append(writting_list[i][7])
            list_B.append(writting_list[i][8])
            list_B2.append(writting_list[i][9])

        df = pd.DataFrame({ 'Position in sequence':list_position, 'Oligonucleotide sequence':list_name, 'Theoretical m/z (Da)':list_theoretical_mz, 'Observed m/z (Da)':list_observed_ms,'Time (min)':list_time,'Observed De Novo product ions (charge states)':list_obs_ion,'Score MSMS (%)':list_score,'Score':list_B, 'Score2':list_B2})

        df3 = pd.DataFrame({'Chosen parameters':[''],'File analyzed (Fasta)':[enter_file_fasta],'File analyzed (mgf)':[enter_file_mgf],'M/z precision':[ms_precision], 'Msms precision':[msms_precision],'Result precision':[result_precison_inter]})


        with pd.ExcelWriter(full_end_file_name) as writer:
            df.to_excel(writer, index=False, sheet_name="Result")
            df3.to_excel(writer, index=False, sheet_name ="Parameters")
            print("done")

    elif type_file == "csv":

        fasta_file = "Fasta:  "+enter_file_fasta
        mgf_file = "Mgf:  "+enter_file_mgf
        Mz = "M/z precision:  " + str(ms_precision)
        msms = "Msms precision:  " + str(msms_precision)
        results = "Result precision:  "+str(result_precison_inter)


        list_title = ["Position in sequence", "Oligonucleotide sequence", "Theoretical m/z (Da)", "Observed m/z (Da)", "Time (min)", "Observed De Novo product ions (charge states)", "Score MSMS (%)"]

        list_parameters = ["Parameters:", fasta_file, mgf_file, Mz,msms,results]

        list_inter = []
        list_final = []

        for i in range(0,len(writting_list)):
            list_inter.append(writting_list[i][1])
            list_inter.append(writting_list[i][2])
            list_inter.append(writting_list[i][3])
            list_inter.append(writting_list[i][4])
            list_inter.append(writting_list[i][5])
            list_inter.append(writting_list[i][6])
            list_inter.append(writting_list[i][7])
            list_final.append(list_inter)
            list_inter = []

        out = open(full_end_file_name, "w")
        writer = csv.writer(out, delimiter=";")

        writer.writerow(list_title)

        for elm in list_final:
            writer.writerow(elm)

        writer.writerow(list_parameters)

        out.close()


    else:

        out = open(full_end_file_name, "w")

        out.write("Chosen parameters: \n")
        out.write("File analyzed (Fasta): "+enter_file_fasta + "\n")
        out.write("File analyzed (mgf): "+enter_file_mgf+"\n")
        out.write("M/z precision: "+ str(ms_precision) + " (Da) \n")
        out.write("Msms precision: "+str(msms_precision)+ " (Da) \n")
        out.write("Results precision: "+str(result_precison_inter) +" (Da) \n")
        out.write("\n")
        out.write("\n")
        out.write("\n")

        for i in range(0, len(writting_list)):
            position = str(writting_list[i][1])
            name = writting_list[i][2]
            theoretical_mz = writting_list[i][3]
            observed_ms = writting_list[i][4]
            time = str(writting_list[i][5])
            obs_ion = writting_list[i][6]
            score = str(writting_list[i][7])

            out.write("Position in sequence: "+position+"\n")
            out.write("Oligonucleotide sequence: "+name+"\n")
            out.write("Theoretical m/z (Da): "+theoretical_mz+"\n")
            out.write("Observed m/z (Da): "+observed_ms+"\n")
            out.write("Time (min): "+time+"\n")
            out.write("Observed De Novo product ions (charge states): "+obs_ion+"\n")
            out.write("Score MSMS (%): "+score+"\n")
            out.write("\n")

        out.close()

    # write rtf file

    seq = ''


    for i in range(0,len(file_list)):
        extract = file_list[i]

        if type(extract) == list:
            for j in range(0, len(extract)):
                seq += extract[j] + " "

        else:
            seq += extract + " "

    seq += " }"

    full_header = '\\cf2 ' + header + '\\\n'

    out = open(name_file_seq,'w')

    liste = ['{\\rtf1\\ansi\\ansicpg1252\\cocoartf2638\n', '\\cocoatextscaling0\\cocoaplatform0{\\fonttbl\\f0\\fswiss\\fcharset0 Helvetica;}\n', '{\\colortbl;\\red255\\green255\\blue255;\\red0\\green0\\blue0;\\red251\\green0\\blue7;\\red94\\green176\\blue32;\n', '\\red253\\green170\\blue9;}\n', '{\\*\\expandedcolortbl;;\\cssrgb\\c0\\c0\\c0;\\cssrgb\\c100000\\c12195\\c0;\\cssrgb\\c43067\\c72927\\c16222;\n', '\\cssrgb\\c100000\\c71834\\c0;}\n', '\\paperw11900\\paperh16840\\margl1440\\margr1440\\vieww11520\\viewh8400\\viewkind0\n', '\\pard\\tx566\\tx1133\\tx1700\\tx2267\\tx2834\\tx3401\\tx3968\\tx4535\\tx5102\\tx5669\\tx6236\\tx6803\\pardirnatural\\partightenfactor0\n']

    for i in range(0, len(liste)):
        out.write(liste[i])


    out.write(full_header)

    out.write(seq)

    out.close()

# Interface

root = tk.Tk()

root.title("OligoMod+")
root.geometry("590x670")
root.config(bg ='#D9D9D9')
root.minsize(590, 670)

f = tk.Frame(root, bg ='white', width= 20, height=1)
f.pack(fill='x')

texte_titre = tk.Label(f, text="OligoMod+", font=("Calibris 17 bold"), padx = 20, pady = 10)

texte_description = tk.Label(f, text="Sequences and locates RNA post-transcriptional modifications", padx = 20, pady = 10)

texte_titre.grid(row = 0, column = 0, sticky = 'w', pady = 2)
texte_description.grid(row = 1, column = 0, sticky = 'w', pady = 2)

l_inter = tk.Frame(root, bg = 'black', width = 1)
l_inter.pack(fill='x')

l = tk.LabelFrame(root, text=" Files ", bg = '#D9D9D9')
l.pack(fill="both", padx = 20, pady =20)

t = tk.Label(l, text="Output file name:", bg = '#D9D9D9', padx= 15, pady = 10)
t2 = tk.Label(l, text="Output file type:", bg = '#D9D9D9', padx= 15, pady = 10)
t3 = tk.Label(l, text="Output sequence name:", bg = '#D9D9D9', padx= 15, pady = 10)
t4 = tk.Label(l, text="Select MGF file:", bg = '#D9D9D9', padx= 15, pady = 10)
t5 = tk.Label(l, text="Select FASTA file:", bg = '#D9D9D9', padx= 15, pady = 10)
t12 = tk.Label(l, text=" .rtf ", bg = '#D9D9D9', padx= 15, pady = 10)

t.grid(row = 0, column = 0, sticky = 'w', pady = 2)
t2.grid(row = 1, column = 0, sticky = 'w', pady = 0)
t3.grid(row = 2, column = 0, sticky = 'w', pady = 0)
t4.grid(row = 3, column = 0, sticky = 'w', pady = 0)
t5.grid(row = 4, column = 0, sticky = 'w', pady = 0)

e1 = tk.Entry(l, width=15)
e1.insert(0, "output")
e1.grid(row = 0, column = 1, pady = 2)

val = tk.StringVar()
val.set("excel")

r3 = tk.Radiobutton(l, variable=val, text=".txt", bg = '#D9D9D9', value="text")
r4 = tk.Radiobutton(l, variable=val, text=".csv", bg = '#D9D9D9', value="csv")
r5 = tk.Radiobutton(l, variable=val, text=".xlsx", bg = '#D9D9D9', value="excel")

r3.grid(row = 1, column = 1, sticky='w', padx= 25, pady = 2)
r4.grid(row = 1, column = 2, sticky='w', padx= 0, pady = 0)
r5.grid(row = 1, column = 3, sticky='w', padx= 20, pady = 0)


e2 = tk.Entry(l, width=15)
e2.insert(0, "sequence")
e2.grid(row = 2, column = 1, sticky = 'w', pady = 2)

e3 = tk.Entry(l, width=15)
e3.grid(row = 3, column = 1, sticky = 'w', pady = 2)

e4 = tk.Entry(l, width=15)
e4.grid(row = 4, column = 1, sticky = 'w', pady = 2)

b = tk.Button(l, text= " Browse file ", command=pathway)
b.grid(row = 3, column = 2, sticky = 'w', padx= 10, pady = 2)

b2 = tk.Button(l, text= " Browse file ", command=pathway2)
b2.grid(row = 4, column = 2, sticky = 'w', padx= 10, pady = 2)

t12.grid(row = 2, column = 2, sticky = 'w', padx= 10, pady = 2)

###

l2 = tk.LabelFrame(root, text=" Settings ", bg = '#D9D9D9')
l2.pack(fill="both", padx = 20, pady =20)

t6 = tk.Label(l2, text="MS tolerance:", bg = '#D9D9D9', padx= 15, pady = 10)
t7 = tk.Label(l2, text="MS/MS tolerance:", bg = '#D9D9D9', padx= 15, pady = 10)
t8 = tk.Label(l2, text="Enzyme digestion:", bg = '#D9D9D9', padx= 15, pady = 10)

t6.grid(row = 0, column = 0, sticky = 'w', pady = 2)
t7.grid(row = 1, column = 0, sticky = 'w', pady = 2)
t8.grid(row = 2, column = 0, sticky = 'w', pady = 2)

e5 = tk.Entry(l2, width=15)
e5.insert(0, "0.01")
e5.grid(row = 0, column = 1, sticky = 'w', pady = 2)

e6 = tk.Entry(l2, width=15)
e6.insert(0, "0.01")
e6.grid(row = 1, column = 1, sticky = 'w', pady = 2)

DB_list = ["RNase T1", "RNase A"]

t9 = ttk.Combobox(l2, values=DB_list, state='readonly', width=15)
t9.current(0)
t9.grid(row =2, column=1, sticky='w', pady =0)

t10 = tk.Label(l2, text=" Da ", bg = '#D9D9D9', padx= 15, pady = 10)
t10.grid(row = 0, column = 2, sticky = 'w', pady = 2)

t11 = tk.Label(l2, text=" Da ", bg = '#D9D9D9', padx= 15, pady = 10)
t11.grid(row = 1, column = 2, sticky = 'w', pady = 2)

l3 = tk.Frame(root, bg = '#D9D9D9', width = 1)
l3.pack(fill="both", padx = 10, pady =10)

b3 = tk.Button(l3, text=" RUN ", bg = '#D9D9D9', command=running)
b3.configure(bg = '#D9D9D9')
b3.grid(row = 0, column = 1, sticky = 'w', padx = 225, pady = 0)

b4 = tk.Button(l3, text="help", bg = '#D9D9D9')
b4.configure(bg = '#D9D9D9')
b4.grid(row = 0, column = 0, sticky = 'w', padx = 10, pady = 0)

l_inter2 = tk.Frame(root, bg = 'black', width = 1)
l_inter2.pack(fill='x')

e7 = tk.Entry(root)
e7.pack(fill='x', ipady = 13)
e7.insert(0, 'Ready to start')

root.mainloop()

