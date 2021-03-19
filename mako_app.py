from mako.template import Template

mako_template = Template(filename='templates/mako_template')

mako_var = ('Ataşehir', 'Bağcılar', 'Bakırköy', 'Başakşehir', 'Bayrampaşa', 'Beylikdüzü', 'Beyoğlu',
            'Büyükçekmece', 'Çekmeköy', 'Esenler', 'Esenyurt', 'Eyüpsultan', 'Fatih', 'Gaziosmanpaşa',
            'Güngören', 'Kağıthane', 'Küçükçekmece', 'Sancaktepe', 'Şişli', 'Sultanbeyli', 'Sultangazi',
            'Ümraniye', 'Üsküdar', 'Zeytinburnu')

print(mako_template.render(ilceler=mako_var))

with open("static/site_main_mako.html", "w", encoding="utf-8") as file:
    file.write(mako_template.render(ilceler=mako_var))
