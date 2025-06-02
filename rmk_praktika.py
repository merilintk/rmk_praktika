
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Panen paika tekstist saadavad andmed:
koosolek = datetime.strptime("09:05:00", "%H:%M:%S").time()
peatusesse = 300  # 5 min
kontorisse = 240  # 4 min

# Arvutan minimaalse ja maksimaalse aja kodust kontorisse jõudmiseks:
# Min: buss tuleb kohe, kui Rita peatusesse jõuab ja sõidab kiiresti (13 min)
# Max: buss läheb just ära, järgmine tuleb 14 min hiljem ja sõidab aeglaselt 
ooteaeg_min = 0
ooteaeg_max = 840  # 12 min + 2 min = 14 min
soiduaeg_min = 780  # 13 min
soiduaeg_max = 960  # 14 min + 2 min = 16 min (lubatud bussi hilinemine)

# Simuleerime ühe töölesaabumise
def simuleeri_toolesaabumist(kodust_valjumine):
    ooteaeg = np.random.uniform(ooteaeg_min, ooteaeg_max)
    soiduaeg = np.random.uniform(soiduaeg_min, soiduaeg_max)

    # Funktsioon genereerib juhusliku oote- ja sõiduaja, argumendiks kodust_valjumine
    koguaeg = peatusesse + ooteaeg + soiduaeg + kontorisse
    saabumine = kodust_valjumine + timedelta(seconds=koguaeg)

    return saabumine.time() > koosolek

# Teeme 10 000 simulatsiooni etteantud vahemikes (Monte Carlo meetod)
def kaivita_simulatsioon():
    kodust_valjumised = [datetime.strptime(f"08:{m:02d}:00", "%H:%M:%S") for m in range(0, 60)] + [
        datetime.strptime("09:00:00", "%H:%M:%S")      #teisendamised
    ]

    simulatsioonide_arv = 10000
    hilinemise_tõenäosused = []
    
#loendab, mitu korda hilineb

    for valjumisaeg in kodust_valjumised:
        hilinemiste_arv = sum(simuleeri_toolesaabumist(valjumisaeg) for _ in range(simulatsioonide_arv))
        
#tõenäosuse jaoks jagan hilinemiste arvu simulatsioonide arvuga        
        hilinemise_tõenäosused.append(hilinemiste_arv / simulatsioonide_arv)

    return kodust_valjumised, hilinemise_tõenäosused

# Graafiku joonistamine
def kuva_tulemused(ajad, toenaosused):
    aja_sildid = [t.strftime("%H:%M") for t in ajad]
    märgitud_ajad = ["08:00", "08:15", "08:30", "08:45", "09:00"]
    märgitud_positsioonid = [aja_sildid.index(t) for t in märgitud_ajad if t in aja_sildid]

    plt.figure(figsize=(10, 6))
    plt.plot(aja_sildid, toenaosused, color="darkgreen", marker="o")
    plt.xticks(märgitud_positsioonid, märgitud_ajad)
    plt.ylim(0, 1)
    plt.xlabel("Kodust lahkumise aeg")
    plt.ylabel("Hilinemise tõenäosus")
    plt.title("Rita hilinemise tõenäosus sõltuvalt kodust lahkumise ajast")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# koodi käivitamine
if __name__ == "__main__":
    ajad, toenaosused = kaivita_simulatsioon()
    kuva_tulemused(ajad, toenaosused)


