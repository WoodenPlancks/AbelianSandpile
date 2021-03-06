import PySimpleGUI as sg
import main

layout = [
	[sg.Text("Welcome to the Abelian Sandpile Avatar Generator!")],
	[sg.Text("What size would you like your image to be?"), sg.InputText(default_text="90", key="n")],
	[sg.Text("How many grains of sand should your simulation have?"), sg.Input(default_text="583", key="ngrains")],
	[sg.Text("What colour scheme would you like for your avatar?")],
	[sg.Radio(text="Inferno", group_id="COLOUR_SCHEME", default=True, key="inferno"), sg.Image()],
	[sg.Radio(text="Blues", group_id="COLOUR_SCHEME", default=False, key="Blues")],
	[sg.Radio(text="Autumn", group_id="COLOUR_SCHEME", default=False, key="autumn")],
	[sg.Radio(text="Greyscale", group_id="COLOUR_SCHEME", default=False, key="gray")],
	[sg.ProgressBar(max_value=100, orientation="h", key="progress_bar")],
	[sg.Button("See Your Avatar!"), sg.Button("Close")],
	[sg.Image("", key="preview")]
]

# Create the window
window = sg.Window("Abelian Sandpile Avatar Generator", layout)
preValues = {}
# Create an event loop
while True:

	event, values = window.read()
	colour_map = ""

	for (key, val) in values.items():
		if key in ["inferno", "Blues", "autumn", "gray"] and val:
			colour_map = key
			break

	bar_val = main.loading_bar.percent_done


	# End program if user closes window or
	# presses the OK button
	if event == "See Your Avatar!":

		print(values["ngrains"], preValues)
		if "ngrains" not in preValues or values["ngrains"] != preValues["ngrains"]:
			grid = main.simulate_sandpile(window, int(values["n"]), int(values["ngrains"]))
		main.draw_grid(grid, colour_map)
		preValues = values
		window["preview"].update("C:\\Users\\micha\\OneDrive\\Documents\\Projects\\sandpile\\frames\\sandpile.png")

	if event == "Close" or event == sg.WIN_CLOSED:
		window.close()
		break
