import jinja2

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('/home/alimesut/DEV/ProjectDante'))
jinja_var = {'ilceler': ['Adalar', 'Ataşehir', 'Beykoz', 'Çekmeköy', 'Kadıköy', 'Kartal', 'Maltepe', 'Pendik',
                         'Sancaktepe', 'Sultanbeyli', 'Şile', 'Tuzla', 'Ümraniye', 'Üsküdar']}

template = jinja_env.get_template('templates/jinja_template')

print(template.render(jinja_var))

with open("static/site_main_jinja.html", "w", encoding="utf-8") as file:
    file.write(template.render(jinja_var))
