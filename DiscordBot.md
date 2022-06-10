

# Discord Bot

----

### What is ChatBot ?

* 在通訊平台上，能夠與使用者聊天的機器人
* e.g. Messenger, Line, Discord, Twitch (relaxing234)

----

### What is API ?

* Application Programming Interface (應用程式介面)
* 讓你的App與其他App溝通的橋樑

![](https://i.imgur.com/IycWFnp.png =550x400)

----

### 前情提要

* 由於課程時間有限，我會盡量cover重要的東西
* 課程中會盡量搭配 [API reference](https://discordpy.readthedocs.io/en/stable/api.html)，教你如何找資料
* 投影片多數內容參考 [Proladon 的 Youtube 頻道](https://www.youtube.com/c/Proladon)

---

### Discord Bot Setup

----

### 在進入正題之前..

* 建議下載[桌面版 discord app](https://discord.com/download)
* 創一個自己的 server
![](https://i.imgur.com/WHYbjSW.png =300x450)


----

##### 1. https://discord.com/developers/applications
##### Click 'New Application'
![](https://i.imgur.com/7FQlG3c.png)

##### 2. 取名 -> Create
![](https://i.imgur.com/DqdHTFU.png =350x300)

----

##### 3. Bot -> Add Bot

![](https://i.imgur.com/LZu7zA3.png)

#### 4. 把 Priviledge Gateway Intents 全部打開

![](https://i.imgur.com/NPWeFqQ.png)

----

##### 5. OAuth2 -> URL Generator -> Scope 

![](https://i.imgur.com/FNYatEd.png =800x250)

----

##### 6. Bot Permissions

![](https://i.imgur.com/scdRIu7.png =700x500)

----

##### 7. Copy link to browser

![](https://i.imgur.com/u1WQnYR.png)

##### 8. Done !

![](https://i.imgur.com/8C2EvZn.png =300x400)

---

### Hello, world

----

##### 取得 token

![](https://i.imgur.com/teoVQVN.png)

##### 下載 discord 模組

```
pip install discord
```

##### 下載 dotenv 模組 (把重要的資料存在環境變數)

```
pip install python-dotenv
```

----

#### 下載[課程專案](https://github.com/EnzoHuang0807/DcBot_Tutorial/tree/main)

#### 把 token 複製到 .env
![](https://i.imgur.com/GnGBAqU.png)

----

#### For Music Bot

```
pip install yt-dlp
```

##### 把 [FFmpeg 執行檔](https://drive.google.com/drive/folders/1saBzH-jajJuDgn2_d_Ts_Yf-RtNj6aZa?usp=sharing)們下載下來放進 DcBot_Tutorial

![](https://i.imgur.com/cbdu3Kw.png)


----

##### 執行 `bot.py`
##### 會看到 "Bot is online"
![](https://i.imgur.com/5BGCJfK.png)
##### 在你的 Server 輸入 $Hello 
![](https://i.imgur.com/m62ZBnp.png)
##### 成功了!

---

### 專案解說時間

----

### 專案管理

* cmds : 儲存指令的地方

  * `main.py` : 主要指令
  * `event.py` : 間隔 / 定時指令
  * `music.py` : 音樂機器人
  * `event.py` : Event 相關指令
  
* `core.py` : 讀資料庫、使用Cog管理指令 
* `bot.py` : 執行 bot (Ctrl + C 中止)
* `.env` : 資料庫 (區隔開發環境與生產環境) 

----

### Cog 是甚麼 ?

##### [Reference](https://www.youtube.com/watch?v=KnO2-0l3BaM)

* 將每個擁有 discord 指令的檔案視為模組塊
* 可以自由載入與卸載 (使用bot command)
* 改完code之後直接reload該檔案，不用
重新執行bot
* 好管理，大作業合作方便
* [詳細實作](https://www.youtube.com/watch?v=4JptXXkqiKU)

----

![](https://i.imgur.com/9yEmDEt.png)

---

### Decorator

----

等等會用到的 code [在這裡](https://github.com/EnzoHuang0807/Sprout/blob/main/DiscordBot.ipynb)

----

##### 在 python 裡面，所有的東西都是物件，函式也不例外
##### 嘗試把一個function當作另一個function的參數

```python=
def logged(func): 
    def with_logging(*args): 
        L = list(args)
        return func(sum(L))
    return with_logging
 
def f(x):
    print(x**2)

result = logged(f)(1,2,3,4)

# > 100
```

##### 此時，logged(func) "裝飾" 了 f(x)，logged(func) 就是一個 Decorator

----

#### Syntax Candy "@" : 讓語法簡化的語法

```python=
def logged(func): 
    def with_logging(*args): 
        L = list(args)
        return func(sum(L))
    return with_logging
 
@logged
def f(x):
    print(x**2)

result = f(1,2,3,4)
```

----

#### Decorator 的意義是甚麼?

##### 如果是有很多個很類似的函式，或者是函式內容很複雜時，就可以使用 Decorator 將 code 簡化

#### [參考資料](https://medium.com/citycoddee/python%E9%80%B2%E9%9A%8E%E6%8A%80%E5%B7%A7-3-%E7%A5%9E%E5%A5%87%E5%8F%88%E7%BE%8E%E5%A5%BD%E7%9A%84-decorator-%E5%97%B7%E5%97%9A-6559edc87bc0)

---

### Asyncio

----

#### 同步 (Sync) 與異步 (Async)

##### 當你的函式大部分時間都在 "等待"，就可以使用異步函式讓你的等待時間拿來做其他事情

----

#### Sync : 一般的函式 -> 從頭做到尾

```python=
import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def task():
    for _ in range(3):
        count()

task()
# executed in  3.03 seconds.
```

----

#### Async : 在標記 await 的地方做其他的事情
```python=
import asyncio
import time

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def task():
    await asyncio.gather(count(), count(), count())

asyncio.run(task())

# executed in 1.01 seconds.
```

----

#### 關鍵字們

* async：用來宣告 function 能夠有異步的功能
* await：用來標記這個 function 切換暫停和繼續的點
* coroutine : 這種 function 的名稱 (中文 : 協程)

---

### 第一個 command 解說

----

#### Decorator

```python=
@commands.command()
async def Hello(self, ctx):
    await ctx.send("Hello, world")
```

###### 提醒 : 如果要在 `bot.py` 直接寫指令的話，Decorator 要改成 @bot.command 哦

----

![](https://i.imgur.com/6nnrqAo.png)

----

#### ctx 是甚麼 ? 它為甚麼有 'send' 這個 method ?

```python=
 @commands.command()
    async def Hello(self, ctx):
        await ctx.send("Hello, world")
```

----

#### ctx : 前後文參數

##### discord 內建的class，會記錄呼叫 bot command 的使用者的名稱、所在的channel等等

 ![](https://i.imgur.com/veCFbKh.png =650x500)

----

##### 除了普通的 string 以外，也可以傳 embed (?) 跟 file

![](https://i.imgur.com/8B2NEy6.png =750x600)

----

#### 練習 : 
  
  寫一個指令，呼叫該指令bot會傳一張梗圖
  
  (提示 : discord 會自動把看起來像 url 的 string 視為網址)

---

### Embed

----

#### Embed 是甚麼 ?
##### 把文字，網址，圖片等等收集起來一起輸出
![](https://i.imgur.com/MTxAU7B.png )

----

#### 練習 : 
 
做一個會輸出Embed的指令吧

[好用的網站](https://cog-creators.github.io/discord-embed-sandbox/)

可以把會用到的url寫在.env方便管理

---

### Event

----

#### 原本就有的 function, 自己定義細項
![](https://i.imgur.com/ckkJQvv.png)
#### 以 on_member_join 為例

----

#### 複製 channel id 到 `.env` 的 "general channel"

![](https://i.imgur.com/i3Nb2ls.png =400x500)


----

```python=
@commands.Cog.listener()
async def on_member_join(self, member):
        
    g_channel = \
    self.bot.get_channel(int(jdata["general_channel"]))
  
    await g_channel.send(f"歡迎{member}加入 !")
```      

##### 因為沒有context參數，所以要指定訊息發送的channel

----

#### 手把手查詢 API Reference 

![](https://i.imgur.com/BQD6HBd.png =500x150)

![](https://i.imgur.com/fHGpTvQ.png =750x400)


----

#### 其他 Event

##### on_message 可以偵測訊息內容 (專案中有範例)
##### on_command_error 可以處理例外 (指令輸入錯誤之類)

---

### 爬蟲 + Discord Bot

----

#### 先玩玩看

[唬爛產生器](https://howtobullshit.me/)

##### 去翻 github，竟然有提供 API !

![](https://i.imgur.com/Wld68Ps.png)

----

#### 根據提示寫一份 python 檔吧
```python=
import requests
import json
from bs4 import BeautifulSoup

url = "https://api.howtobullshit.me/bullshit"
topic = "資芽"
length = 100

post_params = {'Topic': topic, 'MinLen': length}
post = json.dumps(post_params)
response = requests.post(url, data = post)

soup = BeautifulSoup(response.text, "html.parser")
print(str(soup))
```

----

#### 練習
  寫成 discord 指令 !

---

### 間隔 / 定時指令

----

#### Import 新模組
``` python=
from discord.ext import tasks
```
#### 重新定義__init__
``` python=
def __init__(self):
        super().__init__()
        self.peanuts.start()
```

----

#### 每20秒輸出一次 "Peanuts !"

```python=
@tasks.loop(seconds=20.0)
async def peanuts(self):

    await self.bot.wait_until_ready()
    self.channel = \
self.bot.get_channel(int(jdata["general_channel"]))
    await self.channel.send("Peanuts !")
```
![](https://i.imgur.com/zxWI2FJ.png =600x350)

----

* 有了間隔時間執行指令的功能，就可以做出定時執行指令的功能
* i.e., 每隔一段時間就檢查時間到了沒
* 善用datetime模組
* [datetime documentation](https://docs.python.org/3/library/datetime.html)

----

#### 練習

用datetime模組印出24小時制的現在時間
(e.g. 1300, 1400)

##### 關鍵字

* timezone, timedelta
* datetime.datetime.now().strftime()

---

### Music Bot ?!

----

### 偷懶又輕鬆的方法 : 直接用別人的

###### 但是...

----

#### Rythm Bot 被邪惡的Youtube強制下架了
https://rythm.fm/
#### 但很快會有第二版!
#### 目前也有一些替代方案，但效果不如Rythm穩定
##### e.g. FredBoat , Hydra

----

#### 那就自己寫一個Music Bot 來制衡 Youtube 吧

----

#### Music Bot 運作流程

1. 用 yt-dlp 指令搭配 FFmpeg 去 youtube下載音檔 (mp3)
2. 把你的 Bot 連到 Voice Channel
3. 呼叫 discord.FFmpegPCMAudio 播歌

----

#### 今天會教的 Music Bot 指令

1. 下載音檔
2. 將 Bot 連到 Voice Channel 播歌 
   (沒有播放清單)
3. 暫停 / 繼續
4. 卡歌 / 讓 Bot 離開 Voice Channel

----

* ##### 可以用這些基本指令，延伸出 queue, skip 等酷東西
* ##### 使用完 Music Bot 記得呼叫 $leave 離開 Voice Channel，不然會因為閒置太久出錯 (重新啟動Bot)
* ##### [參考影片](https://www.youtube.com/watch?v=ml-5tXRmmFk)
* ##### 提醒 : 影片裡的 youtube_dl 套件爛掉了，改用 yt-dlp
* ##### [yt-dlp](https://www.mankier.com/1/yt-dlp) 不是 python 套件，所以我們會用神秘的方法讓 Music Bot 動起來

----

#### 關於 yt-dlp

* ##### yt-dlp 不是 python 套件，所以不能像之前用過的東西一樣直接 import
* ##### yt-dlp 是 terminal 的指令
* ##### 可以嘗試在小黑窗 (terminal) 輸入 
```bash=
yt-dlp <youtube url>
```
* ##### 為了讓我們可以在 python 裡面使用 terminal 的指令，我們呼叫 os.system()
```python=
os.system(f"yt-dlp {url}")
```

----

#### 程式解說

##### 一起看看專案的 `music.py`
##### 有問題也可以翻 API Reference

----

#### VoiceChannel.connect() 連接 voice channel

![](https://i.imgur.com/f8ijcRq.png)

----

#### 重要的 class : ＶoiceＣlient

![](https://i.imgur.com/R9iFvx5.png)

---

### Wrap 

----

#### 今天學到的指令

* 傳文字，圖片，Embed
* 間隔 / 定時 指令
* Event
* 簡易 Music Bot

----

#### 沒教到的酷東西

* 複雜 Music Bot
* Cog 實作
* 訊息複誦，清理訊息
* 子命令
* Reaction 拿身分組 (on_role_reaction_add)
* [可以翻頁的 Embed](https://stackoverflow.com/questions/55075157/discord-rich-embed-buttons)

----

#### 番外 : 怎麼讓 Discord Bot 24 小時運行

1. Heroku : 較簡單，但一個月開超過500小時要付錢
2. [repl.it : ](https://www.youtube.com/watch?v=UT1h9un4Cpo&list=PLSCgthA1Anif1w6mKM3O6xlBGGypXtrtN&index=17)比較繁瑣，但可以掛很久

----

### That's It !
### 謝謝大家