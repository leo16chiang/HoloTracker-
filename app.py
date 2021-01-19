from flask import Flask, render_template, url_for
import urllib.request
import json
from urllib.request import urlopen

app = Flask(__name__)

# Google API Key
key = YOUR_API_KEY_HERE

# Vtuber object
class vtuber:
    def __init__(self, name, subcount, live, id):
        self.name = name
        self.subcount = subcount
        self.live = live
        self.id = id

# Returns the number of subscribers by entering Channel ID
def get_subs(vtuber):
    data = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + vtuber.id + "&key=" + key).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    return "{:,d}".format(int(subs))

# Checks if channel is live by entering Channel ID
def get_is_live(vtuber):
    data = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=" + vtuber.id + "&eventType=live&type=video&key=" + key).read()
    channel_name_locator = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/channels?part=snippet&id=" + vtuber.id + "&key=" + key).read()
    channel_name = json.loads(channel_name_locator)["items"][0]["snippet"]["title"]
    if json.loads(data)["pageInfo"]["totalResults"] == 0:
        return print(channel_name + " is not currently live.")
    is_live = json.loads(data)["items"][0]["snippet"]["liveBroadcastContent"]
    vidid = json.loads(data)["items"][0]["id"]["videoId"]
    if is_live == "live":
        return print(
            channel_name + " is live. Here is the link: https://www.youtube.com/watch?v=" + vidid + "\nHere is the thumbnail: https://img.youtube.com/vi/" + vidid + "/hq720.jpg")
    elif is_live == "upcoming":
        return print(
            channel_name + " has an upcoming live stream. Here is the link: https://www.youtube.com/watch?v=" + vidid + "\nHere is the thumbnail: https://img.youtube.com/vi/" + vidid + "/hq720.jpg")

# Returns whether vtuber is live, the video url, the thumbnail, and vtuber english name
def get_is_live_comp(vtuber):
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=" + vtuber.id + "&eventType=live&type=video&key=" + key).read()
    if json.loads(data)["pageInfo"]["totalResults"] == 0:
        return [False]
    is_live = json.loads(data)["items"][0]["snippet"]["liveBroadcastContent"]
    vidid = json.loads(data)["items"][0]["id"]["videoId"]
    vidurl = "https://www.youtube.com/watch?v=" + vidid
    thumbnail = "https://img.youtube.com/vi/" + vidid + "/hq720.jpg"
    if is_live == "live":
        temp = [True, vidurl, thumbnail, vtuber.name]
        return temp

# Returns the profile picture and channel link
def get_pfp_c(vtuber):
    data = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/channels?part=snippet&id=" + vtuber.id + "&key=" + key).read()
    pfp = json.loads(data)["items"][0]["snippet"]["thumbnails"]["high"]["url"]
    channel = "https://www.youtube.com/channel/" + vtuber.id
    return (pfp, channel)

# Returns the info of live vtubers from a list
def list_live(selection):
    group = []
    for i in selection:
        temp = get_is_live_comp(i)
        if temp[0]:
            temp2 = get_pfp_c(i)
            for i in temp2:
                temp.append(i)
            group.append(temp)
    return group

# Determines the length of a row where rows have a max of 3 slots
def rowlength(list, row):
    length = len(list) - (3 * (row-1))
    if length >= 3:
        return 3
    elif length < 0:
        return 0
    else:
        return length

# Returns a list of a specific index for each element in the list
def indexer(selection, index):
    lst = []
    for i in selection:
        lst.append(i[index])
    return lst

# Vtuber declarations
sora = vtuber("Tokino Sora", 0, False, "UCp6993wxpyDPHUpavwDFqgg" )
roboco = vtuber("Roboco", 0, False, "UCDqI2jOz0weumE8s7paEk6g")
miko = vtuber("Sakura Miko", 0, False, "UC-hM6YJuNYVAmUWxeIr9FeA")
suisei = vtuber("Hoshimachi Suisei", 0, False, "UC5CwaMl1eIgY8h02uZw7u8A")
mel = vtuber("Yozora Mel", 0, False, "UCD8HOxPs4Xvsm8H0ZxXGiBw")
fubuki = vtuber("Shirakami Fubuki", 0, False, "UCdn5BQ06XqgXoAxIhbqw5Rg")
matsuri = vtuber("Natsuiro Matsuri", 0, False, "UCQ0UDLQCjY0rmuxCDE38FGg")
akirose = vtuber("Aki Rosenthal", 0, False, "UCFTLzh12_nrtzqBPsTCqenA")
haachama = vtuber("Haachama", 0, False, "UC1CfXB_kRs3C-zaeTG3oGyg")
aqua = vtuber("Minato Aqua", 0, False, "UC1opHUrw8rvnsadT-iGp7Cg")
shion = vtuber("Murasaki Shion", 0, False, "UCXTpFs_3PqI41qX2d9tL2Rw")
ayame = vtuber("Nakiri Ayame", 0, False, "UC7fk0CB07ly8oSl0aqKkqFg")
choco = vtuber("Yuzuki Choco", 0, False, "UC1suqwovbL1kzsoaZgFZLKg")
subaru = vtuber("Oozora Subaru", 0, False, "UCvzGlP9oQwU--Y0r9id_jnA")
mio = vtuber("Ookami Mio", 0, False, "UCp-5t9SrOQwXMU7iIjQfARg")
okayu = vtuber("Nekomata Okayu", 0, False, "UCvaTdHTWBGv3MKj3KVqJVCw")
korone = vtuber("Inugami Korone", 0, False, "UChAnqc_AY5_I3Px5dig3X1Q")
pekora = vtuber("Usada Pekora", 0, False, "UC1DCedRgGHBdm81E1llLhOQ")
rushia = vtuber("Uruha Rushia", 0, False, "UCl_gCybOJRIgOXw6Qb4qJzQ")
flare = vtuber("Shiranui Flare", 0, False, "UCvInZx9h3jC2JzsIzoOebWg")
noel = vtuber("Shirogane Noel", 0, False, "UCdyqAaZDKHXg4Ahi7VENThQ")
marine = vtuber("Houshou Marine", 0, False, "UCCzUftO8KOVkV4wQG1vkUvg")
kanata = vtuber("Amane Kanata", 0, False, "UCZlDXzGoo7d44bwdNObFacg")
coco = vtuber("Kiryu Coco", 0, False, "UCS9uQI-jC3DE0L4IpXyvr6w")
watame = vtuber("Tsunomaki Watame", 0, False, "UCqm3BQLlJfvkTsX_hvm0UmA")
towa = vtuber("Tokoyami Towa", 0, False, "UC1uv2Oq6kNxgATlCiez59hw")
luna = vtuber("Himemori Luna", 0, False, "UCa9Y57gfeY0Zro_noHRVrnw")
lamy = vtuber("Yukihana Lamy", 0, False, "UCFKOVgVbGmX65RxO3EtH3iw")
nene = vtuber("Momosuzu Nene", 0, False, "UCAWSyEs_Io8MtpY3m-zqILA")
botan = vtuber("Shishiro Botan", 0, False, "UCUKD-uaobj9jiqB-VXt71mA")
polka = vtuber("Omaru Polka", 0, False, "UCK9V2B22uJYu3N7eR_BT9QA")
risu = vtuber("Ayunda Risu", 0, False, "UCOyYb1c43VlX9rc_lT6NKQw")
moona = vtuber("Moona Hoshinova", 0, False, "UCP0BspO_AMEe3aQqqpo89Dg")
iofi = vtuber("Airani Iofifteen", 0, False, "UCAoy6rzhSf4ydcYjJw3WoVg")
ollie = vtuber("Kureiji Ollie", 0, False, "UCYz_5n-uDuChHtLo7My1HnQ")
anya = vtuber("Anya Melfissa", 0, False, "UC727SQYUvx5pDDGQpTICNWg")
reine = vtuber("Pavolia Reine", 0, False, "UChgTyjG-pdNvxxhdsXfHQ5Q")
calli = vtuber("Mori Calliope", 0, False, "UCL_qhgtOy0dy1Agp8vkySQg")
kiara = vtuber("Takanashi Kiara", 0, False, "UCHsx4Hqa-1ORjQTh9TYDhww")
ina = vtuber("Ninomae Ina'nis", 0, False, "UCMwGHR0BTZuLsmjY_NT5Pwg")
gura = vtuber("Gawr Gura", 0, False, "UCoSrY_IQQVpmIRZ9Xf-y93g")
ame = vtuber("Watson Amelia", 0, False, "UCyl1z3jo3XHR1riLFKG5UAg")

# Vtuber groups
gjp0 = [sora, roboco, miko, suisei]
gjp1 = [mel, fubuki, matsuri, akirose, haachama]
gjp2 = [aqua, shion, ayame, choco, subaru]
ggamers = [fubuki, mio, okayu, korone]
gjp3 = [pekora, rushia, flare, noel, marine]
gjp4 = [kanata, coco, watame, towa, luna]
gjp5 = [lamy, nene, botan, polka]
gid1 = [risu, moona, iofi, ollie, anya, reine]
gen1 = [calli, kiara, ina, gura, ame]
gall = [sora, roboco, miko, suisei, mel, fubuki, matsuri, akirose, haachama, aqua, shion, ayame, choco, subaru,
mio, okayu, korone, pekora, rushia, flare, noel, marine, kanata, coco, watame, towa, luna, lamy, nene, botan, polka,
risu, moona, iofi, ollie, anya, reine, calli, kiara, ina, gura, ame]


@app.route('/')
def base():
  return render_template('home.html')

@app.route('/jp0')
def jp0():
  live = list_live(gjp0)
  row1length = rowlength(live, 1)
  row2length = rowlength(live, 2)
  row1v = indexer(live[0:3], 1)
  row2v = indexer(live[3:6], 1)
  row1tb = indexer(live[0:3], 2)
  row2tb = indexer(live[3:6], 2)
  row1name = indexer(live[0:3], 3)
  row2name = indexer(live[3:6], 3)
  row1pfp = indexer(live[0:3], 4)
  row2pfp = indexer(live[3:6], 4)
  row1ch = indexer(live[0:3], 5)
  row2ch = indexer(live[3:6], 5)

  return render_template('jp0.html', row1length = row1length, row2length = row2length, row1v = row1v, row2v = row2v,
  row1tb = row1tb, row2tb = row2tb, row1name = row1name, row2name = row2name, row1pfp=row1pfp, row2pfp = row2pfp, 
  row1ch = row1ch, row2ch = row2ch)

@app.route('/jp1')
def jp1():
  live = list_live(gjp1)
  row1length = rowlength(live, 1)
  row2length = rowlength(live, 2)
  row1v = indexer(live[0:3], 1)
  row2v = indexer(live[3:6], 1)
  row1tb = indexer(live[0:3], 2)
  row2tb = indexer(live[3:6], 2)
  row1name = indexer(live[0:3], 3)
  row2name = indexer(live[3:6], 3)
  row1pfp = indexer(live[0:3], 4)
  row2pfp = indexer(live[3:6], 4)
  row1ch = indexer(live[0:3], 5)
  row2ch = indexer(live[3:6], 5)

  return render_template('jp1.html', row1length = row1length, row2length = row2length, row1v = row1v, row2v = row2v,
  row1tb = row1tb, row2tb = row2tb, row1name = row1name, row2name = row2name, row1pfp=row1pfp, row2pfp = row2pfp, 
  row1ch = row1ch, row2ch = row2ch)

@app.route('/jp2')
def jp2():
  live = list_live(gjp2)
  row1length = rowlength(live, 1)
  row2length = rowlength(live, 2)
  row1v = indexer(live[0:3], 1)
  row2v = indexer(live[3:6], 1)
  row1tb = indexer(live[0:3], 2)
  row2tb = indexer(live[3:6], 2)
  row1name = indexer(live[0:3], 3)
  row2name = indexer(live[3:6], 3)
  row1pfp = indexer(live[0:3], 4)
  row2pfp = indexer(live[3:6], 4)
  row1ch = indexer(live[0:3], 5)
  row2ch = indexer(live[3:6], 5)

  return render_template('jp2.html', row1length = row1length, row2length = row2length, row1v = row1v, row2v = row2v,
  row1tb = row1tb, row2tb = row2tb, row1name = row1name, row2name = row2name, row1pfp=row1pfp, row2pfp = row2pfp, 
  row1ch = row1ch, row2ch = row2ch)

@app.route('/jpgamers')
def jpgamers():
  live = list_live(gjpgamers)
  row1length = rowlength(live, 1)
  row2length = rowlength(live, 2)
  row1v = indexer(live[0:3], 1)
  row2v = indexer(live[3:6], 1)
  row1tb = indexer(live[0:3], 2)
  row2tb = indexer(live[3:6], 2)
  row1name = indexer(live[0:3], 3)
  row2name = indexer(live[3:6], 3)
  row1pfp = indexer(live[0:3], 4)
  row2pfp = indexer(live[3:6], 4)
  row1ch = indexer(live[0:3], 5)
  row2ch = indexer(live[3:6], 5)

  return render_template('jpgamers.html', row1length = row1length, row2length = row2length, row1v = row1v, row2v = row2v,
  row1tb = row1tb, row2tb = row2tb, row1name = row1name, row2name = row2name, row1pfp=row1pfp, row2pfp = row2pfp, 
  row1ch = row1ch, row2ch = row2ch)

@app.route('/jp3')
def jp3():
  live = list_live(gjp3)
  row1length = rowlength(live, 1)
  row2length = rowlength(live, 2)
  row1v = indexer(live[0:3], 1)
  row2v = indexer(live[3:6], 1)
  row1tb = indexer(live[0:3], 2)
  row2tb = indexer(live[3:6], 2)
  row1name = indexer(live[0:3], 3)
  row2name = indexer(live[3:6], 3)
  row1pfp = indexer(live[0:3], 4)
  row2pfp = indexer(live[3:6], 4)
  row1ch = indexer(live[0:3], 5)
  row2ch = indexer(live[3:6], 5)

  return render_template('jp3.html', row1length = row1length, row2length = row2length, row1v = row1v, row2v = row2v,
  row1tb = row1tb, row2tb = row2tb, row1name = row1name, row2name = row2name, row1pfp=row1pfp, row2pfp = row2pfp, 
  row1ch = row1ch, row2ch = row2ch)

@app.route('/jp4')
def jp4():
  live = list_live(gjp4)
  row1length = rowlength(live, 1)
  row2length = rowlength(live, 2)
  row1v = indexer(live[0:3], 1)
  row2v = indexer(live[3:6], 1)
  row1tb = indexer(live[0:3], 2)
  row2tb = indexer(live[3:6], 2)
  row1name = indexer(live[0:3], 3)
  row2name = indexer(live[3:6], 3)
  row1pfp = indexer(live[0:3], 4)
  row2pfp = indexer(live[3:6], 4)
  row1ch = indexer(live[0:3], 5)
  row2ch = indexer(live[3:6], 5)

  return render_template('jp4.html', row1length = row1length, row2length = row2length, row1v = row1v, row2v = row2v,
  row1tb = row1tb, row2tb = row2tb, row1name = row1name, row2name = row2name, row1pfp=row1pfp, row2pfp = row2pfp, 
  row1ch = row1ch, row2ch = row2ch)

@app.route('/jp5')
def jp5():
  live = list_live(gjp5)
  row1length = rowlength(live, 1)
  row2length = rowlength(live, 2)
  row1v = indexer(live[0:3], 1)
  row2v = indexer(live[3:6], 1)
  row1tb = indexer(live[0:3], 2)
  row2tb = indexer(live[3:6], 2)
  row1name = indexer(live[0:3], 3)
  row2name = indexer(live[3:6], 3)
  row1pfp = indexer(live[0:3], 4)
  row2pfp = indexer(live[3:6], 4)
  row1ch = indexer(live[0:3], 5)
  row2ch = indexer(live[3:6], 5)

  return render_template('jp5.html', row1length = row1length, row2length = row2length, row1v = row1v, row2v = row2v,
  row1tb = row1tb, row2tb = row2tb, row1name = row1name, row2name = row2name, row1pfp=row1pfp, row2pfp = row2pfp, 
  row1ch = row1ch, row2ch = row2ch)

@app.route('/id1')
def id1():
  live = list_live(gid1)
  row1length = rowlength(live, 1)
  row2length = rowlength(live, 2)
  row1v = indexer(live[0:3], 1)
  row2v = indexer(live[3:6], 1)
  row1tb = indexer(live[0:3], 2)
  row2tb = indexer(live[3:6], 2)
  row1name = indexer(live[0:3], 3)
  row2name = indexer(live[3:6], 3)
  row1pfp = indexer(live[0:3], 4)
  row2pfp = indexer(live[3:6], 4)
  row1ch = indexer(live[0:3], 5)
  row2ch = indexer(live[3:6], 5)

  return render_template('id1.html', row1length = row1length, row2length = row2length, row1v = row1v, row2v = row2v,
  row1tb = row1tb, row2tb = row2tb, row1name = row1name, row2name = row2name, row1pfp=row1pfp, row2pfp = row2pfp, 
  row1ch = row1ch, row2ch = row2ch)

@app.route('/en1')
def en1():
  live = list_live(gen1)
  row1length = rowlength(live, 1)
  row2length = rowlength(live, 2)
  row1v = indexer(live[0:3], 1)
  row2v = indexer(live[3:6], 1)
  row1tb = indexer(live[0:3], 2)
  row2tb = indexer(live[3:6], 2)
  row1name = indexer(live[0:3], 3)
  row2name = indexer(live[3:6], 3)
  row1pfp = indexer(live[0:3], 4)
  row2pfp = indexer(live[3:6], 4)
  row1ch = indexer(live[0:3], 5)
  row2ch = indexer(live[3:6], 5)

  return render_template('en1.html', row1length = row1length, row2length = row2length, row1v = row1v, row2v = row2v,
  row1tb = row1tb, row2tb = row2tb, row1name = row1name, row2name = row2name, row1pfp=row1pfp, row2pfp = row2pfp, 
  row1ch = row1ch, row2ch = row2ch)

  live = list_live(holostars)
  row1length = rowlength(live, 1)
  row2length = rowlength(live, 2)
  row3length = rowlength(live, 3)
  row1v = indexer(live[0:3], 1)
  row2v = indexer(live[3:6], 1)
  row3v = indexer(live[6:9], 1)
  row1tb = indexer(live[0:3], 2)
  row2tb = indexer(live[3:6], 2)
  row3tb = indexer(live[6:9], 2)
  row1name = indexer(live[0:3], 3)
  row2name = indexer(live[3:6], 3)
  row3name = indexer(live[6:9], 3)
  row1pfp = indexer(live[0:3], 4)
  row2pfp = indexer(live[3:6], 4)
  row3pfp = indexer(live[6:9], 4)
  row1ch = indexer(live[0:3], 5)
  row2ch = indexer(live[3:6], 5)
  row3ch = indexer(live[6:9], 5)

  return render_template('holostars.html', row1length = row1length, row2length = row2length, row3length = row3length,
  row1v = row1v, row2v = row2v, row3v = row3v, row1tb = row1tb, row2tb = row2tb, row3tb = row3tb, row1name = row1name,
  row2name = row2name, row3name = row3name, row1pfp = row1pfp, row2pfp = row2pfp, row3pfp = row3pfp, row1ch = row1ch,
  row2ch = row2ch, row3ch = row3ch)

@app.route('/all')
def all():
  live = list_live(gall)
  row1length = rowlength(live, 1)
  row2length = rowlength(live, 2)
  row3length = rowlength(live, 3)
  row4length = rowlength(live, 4)
  row5length = rowlength(live, 5)
  row6length = rowlength(live, 6)
  row1v = indexer(live[0:3], 1)
  row2v = indexer(live[3:6], 1)
  row3v = indexer(live[6:9], 1)
  row4v = indexer(live[9:12], 1)
  row5v = indexer(live[12:15], 1)
  row6v = indexer(live[15:18], 1)
  row1tb = indexer(live[0:3], 2)
  row2tb = indexer(live[3:6], 2)
  row3tb = indexer(live[6:9], 2)
  row4tb = indexer(live[9:12], 2)
  row5tb = indexer(live[12:15], 2)
  row6tb = indexer(live[15:18], 2)
  row1name = indexer(live[0:3], 3)
  row2name = indexer(live[3:6], 3)
  row3name = indexer(live[6:9], 3)
  row4name = indexer(live[9:12], 3)
  row5name = indexer(live[12:15], 3)
  row6name = indexer(live[15:18], 3)
  row1pfp = indexer(live[0:3], 4)
  row2pfp = indexer(live[3:6], 4)
  row3pfp = indexer(live[6:9], 4)
  row4pfp = indexer(live[9:12], 4)
  row5pfp = indexer(live[12:15], 4)
  row6pfp = indexer(live[15:18], 4)
  row1ch = indexer(live[0:3], 5)
  row2ch = indexer(live[3:6], 5)
  row3ch = indexer(live[6:9], 5)
  row4ch = indexer(live[9:12], 5)
  row5ch = indexer(live[12:15], 5)
  row6ch = indexer(live[15:18], 5)

  return render_template('all.html', row1length = row1length, row2length = row2length, row3length = row3length,
  row4length = row4length, row5length = row5length, row6length = row6length, row1v = row1v, row2v = row2v, 
  row3v = row3v, row4v = row4v, row5v = row5v, row6v = row6v, row1tb = row1tb, row2tb = row2tb, row3tb = row3tb, 
  row4tb = row4tb, row5tb = row5tb, row6tb = row6tb, row1name = row1name, row2name = row2name, row3name = row3name,
  row4name = row4name, row5name = row5name, row6name = row6name, row1pfp = row1pfp, row2pfp = row2pfp, row3pfp = row3pfp, 
  row4pfp = row4pfp, row5pfp = row5pfp, row6pfp = row6pfp, row1ch = row1ch, row2ch = row2ch, row3ch = row3ch, 
  row4ch = row4ch, row5ch = row5ch, row6ch = row6ch)

if __name__ == "__main__":
    app.run(debug=True)
