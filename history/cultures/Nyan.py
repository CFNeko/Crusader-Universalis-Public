from pathlib import Path
path = Path.cwd()

files = [e for e in path.iterdir() if e.is_file()]
print(files)


for file in files:
	with open(file, 'a') as f:
		f.write("""
1444.11.11 = {
	discover_innovation = innovation_currency_03
	discover_innovation = innovation_divine_right
	discover_innovation = innovation_guilds
	discover_innovation = innovation_heraldry
	discover_innovation = innovation_land_grants
	discover_innovation = innovation_scutage
	discover_innovation = innovation_development_03
	discover_innovation = innovation_windmills

	discover_innovation = innovation_advanced_bowmaking
	discover_innovation = innovation_castle_baileys
	discover_innovation = innovation_hoardings
	discover_innovation = innovation_knighthood
	discover_innovation = innovation_men-at-arms
	discover_innovation = innovation_trebuchet
}
			""")

