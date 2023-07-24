import pandas as pd

# anbefalinger, som afhænger af kognitivt niveau
# Anbefalinger til lavt VFI:
VFI_anbefaling_lav = '''Det verbale forståelses-indeks (VFI) måler evnen til at forstå verbal information.
Det indebærer at ræsonnere i forhold til verbale begreber, og at kommunikere tanker og ideer.
Det måler også tilegnet viden.
Derfor kan de følgende tiltag være relevante for at støtte en elev som har scoret lavt på det verbale forståelses-indeks:
- Giv simple og korte instruktioner.
- Definer alle nye begreber før undervisningen går i gang og lad barnet have sin egen "ordbog" i kladdehæftet.
- Arbejd med at bygge videre på ordforråd.
- Svar ved at gentage det, som eleven spørger om.
- Lær barnet at bruge en ordbog/synonymordbog.
- Spørg om barnet har forstået instrukser.
- Støt barnet at spørge, hvis de er i tvivl.
- Brug visuelle støtte-materialer.
- Lad barnet optage dele af undervisningen/instruktioner på telefon.
- Visualiser strukturen i hverdagen og løsningen af opgaver (både ift. lektier og i undervisningen) fx ved brug af billeder, piktogrammer og ugeskemaer. 
For at minimere elevens oplevelse af at være anderledes kan nogle af disse værktøjer fx anvendes i hele klassen, eller mere diskret på en computer - fremfor, at eleven fx er den eneste med piktogrammer på deres bord.
'''

# Anbefalinger til lavt AHI:
AHI_anbefaling_lav = '''Arbejdshukommelses Indeks måler evnen til mentalt at "holde flere bolde i luften". 
Dette kræver brug af opmærksomhed, koncentration og mental kontrol.
Hvis arbejdshukommelsen har lav kapacitet kan det derfor være svært at løse komplekse opgaver, som består af mange dele, som samtidigt skal anvendes - da der ikke er plads til at fastholde dem alle i sindet på samme tid - nogle af delene kan blive "glemt", i takt med at andre bliver anvendt.
I forlængelse heraf kan følgende tiltag anvendes for at støtte en elev med nedsat arbejdshukommelse.
- Vær sikker på at barnet ved hvad de skal gøre for at løse opgaven
- Øv at følge instruktioner ifbm. opgaveløsning
- Bryd instruktioner ned i mindre bidder og gentag dem gerne
- Bryd opgaven ned i mindre dele
- Lær barnet at bruge egne strategier (fx at spørge en underviser, brug af hjælpemidler som it-computer, opdeling af opgaver i overskuelige dele)
- Reducer distraktioner i omgivelserne
- Giv visuelle påmindelser fx i form af skriftlige instrukser, piktogrammer, tegninger eller andre visuelle hjælpemidler.
Disse hjælpemidler vil have til fælles, at de støtter eleven i at kunne vende tilbage til information, hvis man "taber" et element under den mentale bearbejdning.
'''

# Anbefalinger til lavt FHI:
FHI_anbefaling_lav = '''Forarbejdningshastighed er udtryk for ens mentale arbejdshastighed.
En lav score på forarbejdningshastighed vil betyde at man vil være længere om at løse opgaver end en gennemsnitlig elev af samme køn.
Derfor kan de følgende tiltag være relevante for at støtte en elev som har scoret lavt på forarbejdningshastighed:
- Giv god tid til svar og beslutningstagen
- Lad ikke eleven arbejde under tidspres
- Læg vægt på kvalitet frem for kvantitet i skoleopgaver
- Giv ekstra tid til at færdiggøre opgaver
- Vær opmærksom på distraktorer i omgivelserne
'''

# Anbefalinger til lavt VSI:
VSI_anbefaling_lav = '''Visuo-Spatialt Indeks måler evnen til rumlig bearbejdning og at kunne opfatte forholdet mellem helhed og dele. 
Desuden måles evnen til at rette fokus på visuelle detaljer samt øje-hånd koordination.
Hvis man er testet med en lav score på VSI, kan det være hjælpsomt at skabe en meget tydelig visuel struktur - samt at understøtte denne visuelle struktur med en verbal gennemgang.
Derfor kan de følgende tiltag være relevante for at støtte en elev som har scoret lavt på det visuo-spatiale indeks:
- Fjern/undlad ikke-relevant visuel information
- Tilføj meget tydelig visuel information
- Brug verbal forklaring/instruktion
- Opmuntr eleven til at bruge indre tale/selvinstruktion
- Undlad at bede eleven bruge visuelle strategier, som virker forvirrende for ham/hende
- Når der anvendes farver, så brug farver som er tydeligt forskellige (kontraster)
- Brug klodser og andre hjælpemidler til geometri
- Reducer kravene til nøjagtighed, når barnet kopierer
- Støt eleven i selv at skabe tydelig visuel struktur 
	fx ved at:
	- Overstrege instruktioner med tusch, for tydeligt at adskille svar fra spørgsmål
	- Overstrege dele af en tekst som er relevant for løsning af opgaver
	- Dæk dele af ark med opgaver med papir, så eleven kun kan se den opgave de aktuelt arbejder med.
'''

# Anbefalinger til lavt RSI:
RSI_anbefaling_lav = '''Ræsonnerings-indekset måler evnen til at tænke logisk og abstrakt, udvikle nye tankemønstre, løse problemer på en kreativ måde, drage konklusioner og se mønstre og sammenhænge.
Indekset måler også overordnet visuel evne og evnen til at bearbejde informationer samtidigt.
Følgende støtte kan være relevant for en elev, som scorer lavt på RSI :
- Lær eleven at bruge selvtale og verbal hukommelse til problemløsning
- Lær barnet teknikke for problemløsning (fx at arbejde trin for trin, marker eller saml relevante dele til løsning af opgave)
- Brug lister/procedurer til problemløsning
- Overindlær gennem repetition
- Undgå lange instruktioner og metaforer
- Vær opmærksom på om der er vanskeligheder med at organisere og med sociale færdigheder
'''

#Anbefalinger til lav HIK
HIK_anbefaling_lav = ''''''

generelle_anbefalinger = '''Det er ofte konstruktivt, at man ikke bare ser på, hvordan man kan rumme den enkelte elevs udfordringer, men også tager hensyn ved at være opmærksom på klasse-niveau.
Derfor anbefales følgende:
- Ros værdier I synes er vigtige, som er indenfor elevernes kontrol (fx flid, omtanke, ærlighed eller mod) fremfor resultater (fx fejl, hastighed, karakter).
- Hvis det er vigtigt at pointere faglighed, så fokuserer på eleverne egen tidligere præstation, fremfor at sammenligne med andre elever.
- Vær opmærksomme på også at understøtte et lignende fokus blandt eleverne og sæt passende og rimelige rammer for at undgå evt. uhensigtsmæssig sammenlignings-kultur blandt eleverne.  - Sørg for at gøre klassens rammer konkrete, tydelige (fx hvor længe de skal arbejde, og hvad der forventes i denne periode) og forudsigelige (fx gennem ugeskemaer, ved at dage/uger minder om hinanden, og at aftaler om opgaver/rammer/arbejdstid ikke ændres).  - Sørg for at opgaver har en passende sværhedsgrad (den enkelte elev bør kunne løse størstedelen af opgaverne, størstedelen af tiden) - Hvis I oplever udfordringer med en elev, så undersøg om det kan forklares i konteksten (fx pga. forstyrrelser, hændelser inden eller efter undervisningen, for svære eller for lette opgaver). Overvej herefter om det kan forklares ved at elevens sociale, følelsesmæssige eller kognitive behov ikke bliver mødt. 
- Opfordr elever til at spørge hvis der er noget de ikke forstår, eller ikke ved hvad de skal.
Det er vigtigt starte med at implementere 2-3 tiltag for den enkelte elev, og efter minimum 2 uger tager stilling til, om de tiltag man vælger at tage i brug har den ønskede virkning, eller en uforudset negativ virkning.
Først herefter bør man tilføje eller erstatte tiltag.
'''

rækker = ['VFI', 'VSI', 'RSI', 'AHI', 'FHI', 'HIK']
anbefalinger = [VFI_anbefaling_lav, AHI_anbefaling_lav, FHI_anbefaling_lav, VSI_anbefaling_lav, RSI_anbefaling_lav, HIK_anbefaling_lav]

# create DF for anbefalinger
lav_anbefaling_df = pd.DataFrame(anbefalinger, rækker)
#print(lav_anbefaling_df.loc[])
#Anbefalinger til lavt forarbejdningshastighed OG lavt AHI


# Generelle anbefalinger:

# Currently the format us fucked up by the adding to DF, so i probably need to find a different way to index into the recommendations for the different indexes... 

# Noget med at tilføje kokke-metaforen i stedet for Kate From's metafor.