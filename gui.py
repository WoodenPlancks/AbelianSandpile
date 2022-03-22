import PySimpleGUI as sg
import main

layout = [
	[sg.Text("Welcome to the Abelian Sandpile Avatar Generator!")],
	[sg.Text("What size would you like your image to be?"), sg.InputText(key="n")],
	[sg.Text("How many grains of sand should your simulation have?"), sg.Input(key="ngrains")],
	[sg.Text("What colour scheme would you like for your avatar?")],
	[sg.Radio(text="Inferno", group_id="COLOUR_SCHEME", default=True, key="Inferno")],
	[sg.Radio(text="Pastel", group_id="COLOUR_SCHEME", default=False, key="Pastel")],
	[sg.Radio(text="Autumn", group_id="COLOUR_SCHEME", default=False, key="Autumn")],
	[sg.Radio(text="Greyscale", group_id="COLOUR_SCHEME", default=False, key="Greyscale")],
	[sg.Button("OK")]]

# Create the window
window = sg.Window("Abelian Sandpile Avatar Generator", layout)

# Create an event loop
while True:
	event, values = window.read()
	colour_map_dict = {
		"Inferno": "inferno",
		"Pastel": "pastel",
		"Autumn": "autumn",
		"Greyscale": "gray"
	}
	colour_map = ""
	for (key, val) in values.items():
		if key in ["Inferno", "Pastel", "Autumn", "Greyscale"] and val:
			colour_map = key
			break

	main.simulate_sandpile(int(values["n"]), int(values["ngrains"]), colour_map_dict[colour_map])
	# End program if user closes window or
	# presses the OK button
	if event == "OK" or event == sg.WIN_CLOSED:
		break

window.close()
