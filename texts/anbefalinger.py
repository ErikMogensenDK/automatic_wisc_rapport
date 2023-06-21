import pandas as pd

# anbefalinger, som afhænger af kognitivt niveau
# Anbefalinger til lavt VFI:
VFI_anbefaling_lav = '''
Verbal forståelse indebærer at kunne forklare betydningen af ord, samt at kunne forklare abstrakte sammenhænge imellem ord.
Når man scorer lavt på VFI, vil man derfor ofte have svært ved sproglige fag - samt at forstå og følge verbal instruktion.
Derfor kan det hjælpe at supplere med visuel afbildning af strukturen i hverdagen og løsningen af opgaver (både ift. lektier og i undervisningen) fx form af piktogrammer, ugeskemaer. 
'''

# Anbefalinger til lavt AHI:
AHI_anbefaling_lav = '''Arbejdshukommelse er udtryk for for meget mental "plads" man har at arbejde på. 
Hvis arbejdshukommelsen har lav kapacitet kan det derfor være svært at løse komplekse opgaver som består af mange dele, 
som samtidigt skal anvendes - da der ikke er plads til at holde dem alle i sindet på samme tid.
Man kan sammenligne det med at have et mindre skrivebord at arbejde på. 
Så længe antallet af elementer ikke overstiger skrivebordets kapacitet behøver der ikke være udfordringer.
Mere komplekse opgaver kræver dog mere plads på skrivebordet!
Det vil ligeledes være udfordrende at modtage komplekse instrukser verbalt, da de tit stiller store krav til, at man kan bearbejde mange ord på en gang.
Derfor kan det hjælpe at "eksternalisere" beskeder, instruktioner og opgaver - både i klasseværelset og fx ifbm. lektier.
Dette kan tage form af skriftlige instrukser, piktogrammer, tegninger eller andre visuelle hjælpemidler.
Det kan også være konstruktivt at hjælpe eleven.
Disse visuelle hjælpemidler vil have til fælles, at de giver mulighed for, at man kan vende tilbage til en information, hvis man "taber" et element under den mentale bearbejdning.
'''

# Anbefalinger til lavt FHI:
FHI_anbefaling_lav = '''Forarbejdningshastighed er udtryk for ens mentale arbejdshastighed.
En lav score på forarbejdningshastighed vil betyde at man vil være længere om at løse opgaver end en gennemsnitlig elev af samme køn.
Derfor anbefales det, at 
Derfor anbefales det at man får længere tid til at løse opgaver - eller at der i stedet for at være fokus på hvor meget man kan nå af en opgave, at der s
'''

# Anbefalinger til lavt VSI:
VSI_anbefaling_lav = '''
Eksempel på anbefaling (VSI)
'''

# Anbefalinger til lavt RSI:
RSI_anbefaling_lav = '''
Eksempel på anbefaling (RSI)
'''

#Anbefalinger til lav HIK
HIK_anbefaling_lav = '''Lav HIK.'''


rækker = ['VFI', 'VSI', 'LRI', 'AHI', 'FHI', 'HIK']
anbefalinger = [VFI_anbefaling_lav, AHI_anbefaling_lav, FHI_anbefaling_lav, VSI_anbefaling_lav, RSI_anbefaling_lav, HIK_anbefaling_lav]

# create DF for anbefalinger
lav_anbefaling_df = pd.DataFrame(rækker, anbefalinger)
lav_anbefaling_df.head()

#Anbefalinger til lavt forarbejdningshastighed OG lavt AHI


# Generelle anbefalinger:
