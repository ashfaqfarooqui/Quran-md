import json
from urllib.request import urlopen

ENTER = '\r\n'
NEWLINE = ENTER + '<br>'

transliteration= "en.transliteration"
asad = "en.asad"
pickthall = "en.pickthall"
arberry = "en.arberry"

url_base = 'http://api.alquran.cloud/v1/quran/'
url_meta = 'https://api.alquran.cloud/v1/meta'
metaURL = urlopen(url_meta)

def fetchdata(author):
    return json.loads(urlopen(url_base + author).read())['data']['surahs']

asadData= fetchdata(asad)
transliterationData= fetchdata(transliteration)
pickthallData= fetchdata(pickthall)
arberryData= fetchdata(arberry)


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
                    "tag: "+ " Quran/"+str(metadata[i]['englishName'])+ENTER+
                    "---" + ENTER  + ENTER )
    if(i == 113):
      next=0
    else:
      next=i+1
    if(i==0):
        prev=113
    else:
        prev=i-1

    nextSurah = str(metadata[next]['number'])+"-"+metadata[next]['englishName']
    prevSurah = str(metadata[prev]['number'])+"-"+metadata[prev]['englishName']
    surahFile.write("▶ [[" + prevSurah + "]] | [[" + nextSurah + "]] ◀" + ENTER + ENTER  )

    transAyahs = transliterationData[i]['ayahs']
    asadAyahs = asadData[i]['ayahs']
    pickthallAyahs = pickthallData[i]['ayahs']
    arberryAyahs = arberryData[i]['ayahs']
    for j in range(0,metadata[i]['numberOfAyahs']):
        ayahNo = transAyahs[j]['number']
        str_i = str(i+1)
        str_j = str(j+1)
        surahFile.write("# "+ str_j +ENTER)
        surahFile.write(ENTER + transAyahs[j]['text'] +" ^qTrans"+str_i+str_j+ENTER +ENTER)
        surahFile.write(ENTER + asadAyahs[j]['text'] +" ^qAsad"+str_i+str_j+ENTER +ENTER)
        surahFile.write(ENTER + pickthallAyahs[j]['text'] +" ^qPickthall"+str_i+str_j+ENTER +ENTER)
        surahFile.write(ENTER + arberryAyahs[j]['text'] +" ^qArberry"+str_i+str_j+ENTER +ENTER)


## Generate index

indexFile = open("Quran/__Quran" + ".md", "w", encoding='utf-8')
for i in range(0 , 114):
    indexFile.write("[["  +  str(metadata[i]['number'])+"-" +metadata[i]['englishName']  +  "]]"+ " which means " + metadata[i]['englishNameTranslation']+ENTER+ENTER)
