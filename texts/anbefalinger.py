import pandas as pd

# anbefalinger, som afhænger af kognitivt niveau
# Anbefalinger til lavt VFI:
VFI_anbefaling_lav = '''Verbal forståelse indebærer at kunne forklare betydningen af ord, ræsonnere om sproglige begreber, samt at kunne forklare tilegnet viden med ord.
Når man scorer lavt på VFI, kan man ofte have svært ved disse ting både skriftligt og mundtligt - samt at forstå og følge verbal instruktion.
Derfor kan det hjælpe at supplere instruktioner og beskeder med billeder, visualiseringer og gentagelser.
Man kan også med fordel visualisere strukturen i hverdagen og løsningen af opgaver (både ift. lektier og i undervisningen) fx form af billeder, piktogrammer og ugeskemaer. 
For at minimere elevens oplevelse af at være anderledes kan disse værktøjer fx anvendes i hele klassen, eller mere diskret på en computer.'''

# Anbefalinger til lavt AHI:
AHI_anbefaling_lav = '''Arbejdshukommelse er udtryk for hvor meget mental "plads" man har at arbejde på. 
Hvis arbejdshukommelsen har lav kapacitet kan det derfor være svært at løse komplekse opgaver, som består af mange dele, 
som samtidigt skal anvendes - da der ikke er plads til at fastholde dem alle i sindet på samme tid - nogle af delene kan blive "glemt", i takt med at andre bliver anvendt.
Så længe antallet af elementer ikke overstiger arbejdshukommelsens kapacitet behøver der ikke være udfordringer.
Mere komplekse opgaver stiller dog højere krav til arbejdshukommelsen.
Det vil derfor også være udfordrende at modtage komplekse instrukser verbalt, da de tit stiller store krav til, at man kan bearbejde mange ord på en gang.
Derfor kan det hjælpe at "eksternalisere" beskeder, instruktioner og opgaver - både i klasseværelset og fx ifbm. lektier.
Dette kan tage form af skriftlige instrukser, piktogrammer, tegninger eller andre visuelle hjælpemidler.
Disse visuelle hjælpemidler vil have til fælles, at de giver elever mulighed for, at vende tilbage til en information, hvis man "taber" et element under den mentale bearbejdning.
'''

# Anbefalinger til lavt FHI:
FHI_anbefaling_lav = '''Forarbejdningshastighed er udtryk for ens mentale arbejdshastighed.
En lav score på forarbejdningshastighed vil betyde at man vil være længere om at løse opgaver end en gennemsnitlig elev af samme køn.
Derfor anbefales det at man får længere tid til at løse opgaver - eller at der i stedet for at være fokus på hvor meget man kan nå af en opgave, at der s
'''

# Anbefalinger til lavt VSI:
VSI_anbefaling_lav = '''Det visuo-spatiale (visuelt-rummelige) indeks måler blandt andet evnen til at integrere forhold mellem helhed og del-elementer og evne til at rette sit fokus mod visuelle detaljer.
Hvis man er testet med en lav score på VSI, kan det være hjælpsomt at skabe en meget tydelig visuel struktur - samt at understøtte denne visuelle struktur med en verbal gennemgang.
Fx kan man ved at markere instruktioner med en farve (fx med overstregningstusch), for tydeligt at adskille svar fra spørgsmål.
Denne strategi kan eleven også selv gøre brug af.
Man kan også dække dele af ark med opgaver med papir, så eleven kun kan se den opgave de aktuelt arbejder med.
Det kan desuden være konstruktivt at man ikke inkluderer visuelle indtryk på uddelte papirer, som ikke har direkte relevant for løsningen af opgaven - da det kan være svært at ignorere irrelevant visuel information.'''

# Anbefalinger til lavt RSI:
RSI_anbefaling_lav = '''
Eksempel på anbefaling (RSI)
'''

#Anbefalinger til lav HIK
HIK_anbefaling_lav = ''''''

generelle_anbefalinger = '''- Ros værdier I synes er vigtige, som er indenfor elevernes kontrol (fx flid, omtanke, ærlighed eller mod) fremfor resultater (fx fejl, hastighed, karakter).
- Hvis det er vigtigt at pointere faglighed, så fokuserer på eleverne egen tidligere præstation, fremfor at sammenligninge med andre elever.
- Vær opmærksomme på også at understøtte et lignende fokus blandt eleverne og sæt passende og rimelige rammer for at undgå evt. uhensigtsmæssig sammenlignings-kultur blandt eleverne.
- Sørg for at gøre klassens rammer konkrete, tydelige (fx hvor længe de skal arbejde, og hvad der forventes i denne periode) og forudsigelige (fx gennem ugeskemaer, ved at dage/uger minder om hinanden, og at aftaler om opgaver/rammer/arbejdstid ikke ændres).
- Sørg for at opgaver har en passende sværhedsgrad (den enkelte elev bør kunne løse størstedelen af opgaverne, størstedelen af tiden)
- Hvis I oplever udfordringer med en elev, så undersøg om det kan forklares i konteksten (fx pga. forstyrrelser, hændelser inden eller efter undervisningen, for svære eller for lette opgaver). Overvej herefter om det kan forklares ved at elevens sociale, følelsesmæssige eller kognitive behov ikke bliver tilfredsstillet. 
- Opfordr elever til at spørge hvis der er noget de ikke forstår, eller ikke ved hvad de skal.
'''

rækker = ['VFI', 'VSI', 'LRI', 'AHI', 'FHI', 'HIK']
anbefalinger = [VFI_anbefaling_lav, AHI_anbefaling_lav, FHI_anbefaling_lav, VSI_anbefaling_lav, RSI_anbefaling_lav, HIK_anbefaling_lav]

# create DF for anbefalinger
lav_anbefaling_df = pd.DataFrame(anbefalinger, rækker)
#print(lav_anbefaling_df.loc[])
#Anbefalinger til lavt forarbejdningshastighed OG lavt AHI


# Generelle anbefalinger:
