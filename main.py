import json
import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.geometry("600x300")
root.title("CONFIGURATION SET-TOP BOX")

frame_button=ttk.Frame(root)
frame_button.pack(fill="both",side="bottom",expand="true")
frame_list = ttk.Frame(root)
frame_list.pack(fill="both",side="left",expand="true")
frame_input = ttk.Frame(root)
frame_input.pack(fill="both",side="top",expand="true")
titre_input=tk.Label(frame_input,text="SAISIE DES PARAMETRES",bg="#E5E7E9",font=('Helvetica', 18, 'bold')).pack(fill="both",ipady=5)
frame_input1 = ttk.Frame(frame_input)
frame_input1.pack(fill="both",side="top",expand="true")
frame_input2 = ttk.Frame(frame_input)
frame_input2.pack(fill="both",side="top",expand="true")
frame_input3 = ttk.Frame(frame_input)
frame_input3.pack(fill="both",side="top",expand="true")
frame_output = ttk.Frame(root)
titre_output=tk.Label(frame_input,text="CONFIGURATION ACTUELLE",bg="#E5E7E9",font=('Helvetica', 18, 'bold')).pack(fill="both",ipady=5)
frame_output.pack(fill="both",side="top",expand="true")
frame_output1 = ttk.Frame(frame_output)
frame_output1.pack(fill="both",side="top",expand="true")
frame_output2 = ttk.Frame(frame_output)
frame_output2.pack(fill="both",side="top",expand="true")
frame_output3 = ttk.Frame(frame_output)
frame_output3.pack(fill="both",side="top",expand="true")

titre_liste=tk.Label(frame_list,text="CHAÎNES UTILISEES",bg="#E5E7E9",font=('Helvetica', 18, 'bold')).pack(fill="both")


Nom_chaine=tk.Label(frame_input1,text="Nom de la chaîne :",anchor="w",bg="#E5E7E9").pack(side="left",fill="both",expand=True)
var_chaine = tk.StringVar()
entry_chaine = tk.Entry(frame_input1,textvariable=var_chaine, width=20).pack(side="left",fill="both", expand=True)

ip_multicast=tk.Label(frame_input2,text="IP Multicast :",anchor="w",bg="#E5E7E9").pack(side="left",fill="both", expand=True)
var_multicast = tk.StringVar()
entry_multicast = tk.Entry(frame_input2,textvariable=var_multicast, width=20).pack(side="left",fill="both", expand=True)

port=tk.Label(frame_input3,text="PORT :",anchor="w",bg="#E5E7E9").pack(side="left",fill="both", expand=True)
var_port = tk.IntVar()
entry_port = tk.Entry(frame_input3,textvariable=var_port, width=20).pack(side="left",fill="both", expand=True)

liste_chaines = ("chaine 1", "chaine 2", "chaine 3", "chaine 4", "chaine 5", "chaine 6","chaine 7", "chaine 8", "chaine 9",
                 "chaine 10", "chaine 11", "chaine 12")

pl = tk.StringVar(value=liste_chaines)
pl_select = tk.Listbox(frame_list, listvariable=pl, height=6,bg="grey")
pl_select.pack(padx=10, pady=10)

varpt = tk.StringVar()
varch = tk.StringVar()
varipm= tk.StringVar()
label_chaine_lu=ttk.Label(frame_output1,text="Nom de la chaîne :",anchor="w").pack(side="left",fill="both",expand=True)
Nom_chaine_lu=ttk.Label(frame_output1,textvariable=varch,anchor="w").pack(side="left",fill="both",expand=True)
label_multicast_lu=tk.Label(frame_output2,text="IP Multicast :",anchor="w",bg="#E5E7E9").pack(side="left",fill="both", expand=True)
ip_multicast_lu=tk.Label(frame_output2,textvariable=varipm,anchor="w",bg="#E5E7E9").pack(side="left",fill="both", expand=True)
port_label=tk.Label(frame_output3,text="PORT :",anchor="w",bg="#E5E7E9").pack(side="left",fill="both", expand=True)
port_lu=tk.Label(frame_output3,textvariable=varpt,anchor="w",bg="#E5E7E9").pack(side="left",fill="both", expand=True)


def deteclist(event):
    selected_indices = pl_select.curselection()
    for i in selected_indices:
        chselected=pl_select.get(i)
        fichier = "settings.json"
        with open(fichier, "r") as f:
            settings = json.load(f)
            pt=settings[chselected]["port"]
            ch=settings[chselected]["chaine"]
            ip=settings[chselected]["multicast"]
            varpt.set(f"{pt}")
            varch.set(f"{ch}")
            varipm.set(f"{ip}")

pl_select.bind("<<ListboxSelect>>",deteclist)


def jsonread():
    selected_indices = pl_select.curselection()
    for i in selected_indices:
        chselected = pl_select.get(i)
        print(chselected)
        fichier = "settings.json"
        with open(fichier, "r") as f:
            settings = json.load(f)

        chaine=var_chaine.get()
        multicast = var_multicast.get()
        port = var_port.get()
        settings[chselected]["chaine"]=chaine
        settings[chselected]["multicast"]=multicast
        settings[chselected]["port"]=port

        with open(fichier,"w") as f:
            settings = json.dump(settings,f,indent=4)


bouton_envoyer = ttk.Button(frame_button,text="ENVOYER", command=jsonread)
bouton_envoyer.pack(side="left",expand="true")
bouton_quitter = ttk.Button(frame_button,text="QUITTER", command=root.destroy)
bouton_quitter.pack(side="left",expand="true")




root.mainloop()