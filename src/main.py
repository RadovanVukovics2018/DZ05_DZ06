from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def unique():

	
	f = open("RAFraspored.csv","r", encoding='utf-8')
	citajIzFajla = f.read()
	redovi_fajla = citajIzFajla.split('\n')
	for red in redovi_fajla:
		splitovan_red = red.split(',')
	unique_list=[]
	f = open("RAFraspored.csv","r", encoding='utf-8')
	podaciFajl = f.read()
	redFajl = podaciFajl.split('\n')
	for red in redFajl:
		redsplit = red.split(',') 
	spisak = open('RAFraspored.csv', encoding='utf-8').read().splitlines()
	unique_list=[]
	sve_ucionice = [red.split(',')[6] for red in redFajl]
	jedinstveneUcionice = []
	for ucionica in sve_ucionice:
		if ucionica not in jedinstveneUcionice:
			jedinstveneUcionice.append(ucionica)

	sve_ucionice = jedinstveneUcionice.sort()

	svi_profesori = [red.split(',')[2] for red in redFajl]
	jedinstveniProfesori = []
	for profesor in svi_profesori:
		if profesor not in jedinstveniProfesori:
			jedinstveniProfesori.append(profesor)

	svi_profesori = jedinstveniProfesori.sort()


	for redFajl in spisak:
		if redFajl not in unique_list:
			unique_list.append(redFajl)

	for redFajl in unique_list:
		redsplit = redFajl.split(',')

	return render_template("index.html", unique_list=unique_list, redFajl = redFajl, redsplit = redsplit, red=red, sve_ucionice=jedinstveneUcionice, svi_profesori=jedinstveniProfesori, redovi=redovi_fajla)



if __name__ == '__main__':
	app.run()