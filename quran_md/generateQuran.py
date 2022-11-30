import json
from urllib.request import urlopen

ENTER = '\r\n'
NEWLINE = ENTER + '<br>'

transliteration= "en.transliteration"
asad = "en.asad"
pickthall = "en.pickthall"
arberry = "en.arberry"

url_base = 'http://api.alquran.cloud/v1/quran/'
#url_arabic = 'http://api.alquran.cloud/v1/quran/'
url_meta = 'https://api.alquran.cloud/v1/meta'

#surahurl_arb = urlopen(url_arabic)

metaURL = urlopen(url_meta)



# start by creating the files

#for surah in metajson['data']['surahs']['references']:
#    surahFile = open("Quran/"+str(surah['number'])+"-" +surah['englishName'] + ".md", "w", encoding='utf-8')
#    surahFile.write("---"+ENTER+ "alias:" + surah['englishName']+ ENTER +  "Name:" +surah['name']+ ENTER + "Ayahs:"+str(surah['numberOfAyahs']) +ENTER +"Revelation:"+surah['revelationType'] + ENTER+ "---" + ENTER + NEWLINE + ENTER + NEWLINE)

#####
#get english data asad

#surahurl_eng = urlopen(url_base + asad)

#surahJson = json.loads(surahurl_eng.read())

#for surah in surahJson['data']['surahs']:
#    surahFile = open("Quran/"+str(surah['number'])+"-" +surah['englishName'] + ".md", "w", encoding='utf-8')
#    surahFile.write("---"+ENTER+ "alias:" + ENTER + "- " + surah['englishName'] +ENTER + "- " + str(surah['number']) + ENTER +  "Name:" +surah['name']+ ENTER + ENTER +"Revelation:"+surah['revelationType'] + ENTER+ "---" + ENTER  + ENTER )
#    for ayah in surah['ayahs']:
#        surahFile.write("# "+ str(surah['number'])+":" + str(ayah['numberInSurah']) + ENTER +ENTER + ayah['text'] +"^qAsad"+str(ayah['number'])+ENTER +ENTER)

#pull data


asadData= json.loads(urlopen(url_base + asad).read())['data']['surahs']
transliterationData= json.loads(urlopen(url_base + transliteration).read())['data']['surahs']
pickthallData= json.loads(urlopen(url_base + pickthall).read())['data']['surahs']
arberryData= json.loads(urlopen(url_base + arberry).read())['data']['surahs']


metadata = json.loads(metaURL.read())['data']['surahs']['references']


for i in range(0 , 114):
    surahFile = open("Quran/"+str(metadata[i]['number'])+"-" +metadata[i]['englishName'] + ".md", "w", encoding='utf-8')
    surahFile.write("---"+ENTER+
                    "aliases:" + ENTER +
                    "- " + metadata[i]['englishName'] +ENTER +
                    "- " + "Q"+str(metadata[i]['number']) + ENTER +
                    "Name: " +metadata[i]['englishNameTranslation']+ ENTER +
                    "Revelation: "+metadata[i]['revelationType'] + ENTER+
                    "Ayahs: "+str(metadata[i]['numberOfAyahs'])+ENTER+
                    "---" + ENTER  + ENTER )
    #nextSurah = str(metadata[i + 1]['number'])+"-"+metadata[i+1]['englishName']
    #prevSurah = str(metadata[i - 1]['number'])+"-"+metadata[i-1]['englishName']
    #surahFile.write("▶ [[" + prevSurah + "]] | [[" + nextSurah + "]] ◀" + ENTER + ENTER  )

    transAyahs = transliterationData[i]['ayahs']
    asadAyahs = asadData[i]['ayahs']
    pickthallAyahs = pickthallData[i]['ayahs']
    arberryAyahs = arberryData[i]['ayahs']
    for j in range(0,metadata[i]['numberOfAyahs']):
        ayahNo = transAyahs[j]['number']
        surahFile.write("# "+ str(j+1) +ENTER)
        surahFile.write(ENTER + transAyahs[j]['text'] +" ^qTrans"+str(i)+str(j)+ENTER +ENTER)
        surahFile.write(ENTER + asadAyahs[j]['text'] +" ^qAsad"+str(i)+str(j)+ENTER +ENTER)
        surahFile.write(ENTER + pickthallAyahs[j]['text'] +" ^qPickthall"+str(i)+str(j)+ENTER +ENTER)
        surahFile.write(ENTER + arberryAyahs[j]['text'] +" ^qArberry"+str(i)+str(j)+ENTER +ENTER)


## Generate MOC

indexFile = open("Quran/__Quran" + ".md", "w", encoding='utf-8')
for i in range(0 , 114):
    indexFile.write("[["  +  str(metadata[i]['number'])+"-" +metadata[i]['englishName']  +  "]]"+ENTER+ENTER)
