from mako.template import Template

mako_template = Template(filename='templates/mako_template')

mako_var = ('Adalar', 'Ataşehir', 'Beykoz', 'Çekmeköy', 'Kadıköy', 'Kartal', 'Maltepe', 'Pendik',
            'Sancaktepe', 'Sultanbeyli', 'Şile', 'Tuzla', 'Ümraniye', 'Üsküdar')

print(mako_template.render(ilceler=mako_var))

with open("static/site_main_mako.html", "w", encoding="utf-8") as file:
    file.write(mako_template.render(ilceler=mako_var))
