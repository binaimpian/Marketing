FONTS="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,400;0,700;0,900;1,400&family=Bricolage+Grotesque:wght@400;600;800&family=Space+Grotesk:wght@400;700&family=Playfair+Display:ital,wght@0,700;1,400&family=Baloo+2:wght@500;800&family=Shrikhand&family=Anton&family=Caveat:wght@700&family=Unbounded:wght@400;800&family=Archivo+Black&display=swap"
HEAD=f'<!doctype html><html><head><meta charset="utf-8"><link href="{FONTS}" rel="stylesheet"><style>*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;position:relative}}'
P={}

# 1 Bold Typography
P["01-bold-typography"]=("""body{background:#FFE600;font-family:'Archivo Black';color:#111}
.t{position:absolute;left:60px;top:40px;font-family:'Anton';font-size:248px;line-height:.86;letter-spacing:-.01em}
.t span{display:block}.o{color:#FFE600;-webkit-text-stroke:6px #111}
.b{position:absolute;left:60px;right:60px;top:60px;display:flex;justify-content:flex-end;font-size:26px}
.bar{position:absolute;left:0;right:0;bottom:0;height:390px;background:#111;color:#FFE600;padding:50px 60px}
.bar .r{display:flex;justify-content:space-between;font-size:58px;line-height:1.1}
.bar .s{font-family:'Space Grotesk';font-weight:700;font-size:28px;color:#fff;margin-top:14px;letter-spacing:.08em}
.cta{margin-top:44px;background:#FFE600;color:#111;font-size:44px;text-align:center;padding:26px;border-radius:0}
""","""<div class="b">[NAMA ORGANISASI]</div>
<div class="t"><span>JOM</span><span class="o">DATANG</span><span>OPEN</span><span>DAY</span></div>
<div class="bar"><div class="r"><span>SABTU 21.11.26</span><span>9AM–4PM</span></div>
<div class="s">SLOT TERHAD · [LOKASI] · [NO. WHATSAPP]</div>
<div class="cta">BOOKING SLOT SEKARANG →</div></div>""")

# 2 Minimalis premium
P["02-minimalis-premium"]=("""body{background:#F3EEE6;font-family:'Space Grotesk';color:#22201C}
.f{position:absolute;inset:50px;border:1.5px solid #22201C55}
.top{position:absolute;top:100px;left:0;right:0;text-align:center;letter-spacing:.4em;font-size:22px}
.h{position:absolute;top:330px;left:0;right:0;text-align:center;font-family:'Fraunces';font-weight:400;font-size:150px;line-height:1}
.h i{display:block;font-style:italic;font-size:70px;margin-bottom:20px;color:#9A7B4F}
.line{position:absolute;left:50%;top:700px;width:1px;height:120px;background:#22201C}
.d{position:absolute;top:860px;left:0;right:0;text-align:center;font-size:34px;letter-spacing:.2em}
.d small{display:block;font-size:24px;margin-top:16px;color:#6B655B;letter-spacing:.3em}
.cta{position:absolute;bottom:130px;left:50%;transform:translateX(-50%);border:1.5px solid #22201C;padding:24px 50px;font-size:24px;letter-spacing:.3em;background:#22201C;color:#F3EEE6;white-space:nowrap}
.ft{position:absolute;bottom:80px;left:0;right:0;text-align:center;font-size:18px;color:#6B655B;letter-spacing:.2em}
""","""<div class="f"></div><div class="top">[NAMA ORGANISASI]</div>
<div class="h"><i>Jom datang ke</i>Open Day</div><div class="line"></div>
<div class="d">SABTU · 21 NOVEMBER 2026<small>9:00 PAGI — 4:00 PETANG</small></div>
<div class="cta">BOOKING SLOT SEKARANG</div><div class="ft">SLOT TERHAD · [LOKASI]</div>""")

# 3 Ceria playful
P["03-ceria-playful"]=("""body{background:#FFF4E0;font-family:'Baloo 2';color:#2D2A6E}
.c{position:absolute;border-radius:50%}
.h{position:absolute;top:210px;left:0;right:0;text-align:center;font-weight:800;line-height:.95}
.h .a{font-size:90px;color:#FF6B6B;transform:rotate(-4deg);display:inline-block}
.h .b{font-size:196px;display:block;color:#2D2A6E;text-shadow:8px 8px 0 #FFC93C}
.sub{position:absolute;top:720px;left:0;right:0;text-align:center;font-size:36px;font-weight:500}
.pills{position:absolute;top:810px;left:0;right:0;display:flex;justify-content:center;gap:24px}
.pills div{background:#fff;border:4px solid #2D2A6E;border-radius:30px;padding:16px 34px;font-size:40px;font-weight:800;box-shadow:6px 6px 0 #2D2A6E}
.cta{position:absolute;bottom:150px;left:120px;right:120px;background:#FF6B6B;color:#fff;text-align:center;font-size:52px;font-weight:800;padding:20px;border-radius:60px;border:4px solid #2D2A6E;box-shadow:0 10px 0 #2D2A6E}
.ft{position:absolute;bottom:70px;left:0;right:0;text-align:center;font-size:28px;font-weight:500}
.br{position:absolute;top:80px;left:0;right:0;text-align:center;font-size:30px;font-weight:800}
.st{position:absolute;font-size:70px}
""","""<div class="c" style="width:300px;height:300px;background:#7ED6DF;left:-100px;top:-80px"></div>
<div class="c" style="width:220px;height:220px;background:#FFC93C;right:-60px;top:380px"></div>
<div class="c" style="width:160px;height:160px;background:#A29BFE;left:-50px;top:640px"></div>
<div class="c" style="width:260px;height:260px;background:#7ED6DF;right:-90px;bottom:-90px"></div>
<div class="st" style="left:130px;top:520px">✨</div><div class="st" style="right:150px;top:150px">🎈</div>
<div class="br">[Nama Organisasi]</div>
<div class="h"><span class="a">Jom Datang!</span><span class="b">OPEN DAY</span></div>
<div class="sub">Datang ramai-ramai, bawa keluarga! 💛</div>
<div class="pills"><div>📅 Sab, 21 Nov</div><div>⏰ 9am – 4pm</div></div>
<div class="cta">Booking Slot Sekarang!</div><div class="ft">Slot terhad · [No. WhatsApp]</div>""")

# 4 Kad jemputan
P["04-kad-jemputan"]=("""body{background:#123B32;font-family:'Playfair Display';color:#E9D8A6}
.card{position:absolute;inset:70px;border:3px solid #C9A85C;padding:20px}
.card::after{content:"";position:absolute;inset:16px;border:1px solid #C9A85C88}
.in{position:absolute;inset:0;text-align:center;padding-top:130px}
.k{font-family:'Space Grotesk';letter-spacing:.45em;font-size:22px;color:#C9A85C}
.a{font-style:italic;font-weight:400;font-size:60px;margin-top:70px}
.h{font-weight:700;font-size:150px;line-height:1;color:#F5E6C0;margin-top:20px}
.orn{color:#C9A85C;font-size:40px;margin:40px 0}
.d{font-family:'Space Grotesk';font-size:34px;letter-spacing:.1em;line-height:1.7}
.cta{display:inline-block;margin-top:60px;background:#C9A85C;color:#123B32;font-family:'Space Grotesk';font-weight:700;font-size:30px;letter-spacing:.2em;padding:24px 50px}
.ft{font-family:'Space Grotesk';font-size:20px;letter-spacing:.2em;margin-top:30px;color:#C9A85CBB}
""","""<div class="card"><div class="in"><div class="k">[NAMA ORGANISASI]</div>
<div class="a">Dengan hormatnya menjemput anda ke</div><div class="h">Open Day</div>
<div class="orn">✦ ✦ ✦</div><div class="d">SABTU, 21 NOVEMBER 2026<br>9:00 PAGI – 4:00 PETANG</div>
<div class="cta">BOOKING SLOT SEKARANG</div><div class="ft">SLOT TERHAD · [LOKASI]</div></div></div>""")

# 5 Tiket
P["05-tiket-event"]=("""body{background:#1B1B3A;font-family:'Space Grotesk';color:#1B1B3A}
.br{position:absolute;top:80px;left:0;right:0;text-align:center;color:#fff;font-size:28px;letter-spacing:.3em}
.tk{position:absolute;left:110px;right:110px;top:180px;height:900px;background:#FF5E5B;border-radius:30px;transform:rotate(-3deg);box-shadow:0 40px 80px #0008}
.main{padding:60px 60px 0}
.lb{font-weight:700;letter-spacing:.3em;font-size:22px}
.h{font-family:'Unbounded';font-weight:800;font-size:100px;line-height:1;color:#fff;margin-top:20px}
.row{display:flex;gap:30px;margin-top:40px}
.row div{flex:1;border-top:3px solid #1B1B3A;padding-top:14px;font-size:22px;letter-spacing:.15em;font-weight:700}
.row b{display:block;font-size:44px;letter-spacing:0;margin-top:6px}
.perf{position:absolute;left:0;right:0;top:640px;border-top:5px dashed #1B1B3A}
.perf::before,.perf::after{content:"";position:absolute;width:70px;height:70px;border-radius:50%;background:#1B1B3A;top:-37px}
.perf::before{left:-35px}.perf::after{right:-35px}
.stub{position:absolute;left:60px;right:60px;top:700px;display:flex;justify-content:space-between;align-items:center}
.stub .adm{font-family:'Unbounded';font-weight:800;font-size:44px;color:#fff}
.stub .adm small{display:block;font-family:'Space Grotesk';font-size:22px;color:#1B1B3A;letter-spacing:.2em}
.bc{width:220px;height:140px;background:repeating-linear-gradient(90deg,#1B1B3A 0 6px,transparent 6px 10px,#1B1B3A 10px 12px,transparent 12px 20px)}
.cta{position:absolute;bottom:90px;left:110px;right:110px;background:#FFD166;text-align:center;font-weight:700;font-size:44px;padding:28px;border-radius:18px}
""","""<div class="br">[NAMA ORGANISASI]</div>
<div class="tk"><div class="main"><div class="lb">TIKET MASUK PERCUMA</div><div class="h">JOM<br>DATANG<br>OPEN DAY</div>
<div class="row"><div>TARIKH<b>21.11.26</b></div><div>HARI<b>SABTU</b></div><div>MASA<b>9AM–4PM</b></div></div></div>
<div class="perf"></div><div class="stub"><div class="adm"><small>SLOT TERHAD</small>ADMIT ONE</div><div class="bc"></div></div></div>
<div class="cta">🎟️ BOOKING SLOT SEKARANG!</div>""")

# 6 Kalendar
P["06-save-the-date"]=("""body{background:#E8F1FF;font-family:'Bricolage Grotesque';color:#0B2A6F}
.br{position:absolute;top:70px;left:80px;font-weight:800;font-size:28px}
.h{position:absolute;top:130px;left:80px;font-weight:800;font-size:92px;line-height:1}
.h span{color:#2F6BFF}
.cal{position:absolute;left:80px;right:80px;top:380px;background:#fff;border-radius:36px;box-shadow:0 30px 60px #0B2A6F22;overflow:hidden}
.cal .top{background:#2F6BFF;color:#fff;padding:24px 40px;display:flex;justify-content:space-between;font-weight:800;font-size:36px}
.g{display:grid;grid-template-columns:repeat(7,1fr);padding:30px 30px 40px;text-align:center;font-size:40px;font-weight:600;row-gap:34px}
.g .w{font-size:20px;color:#7A8BB3;font-weight:800}
.g .m{color:#C9D3EA}
.g .x{position:relative;color:#fff}
.g .x::before{content:"";position:absolute;width:90px;height:90px;border-radius:50%;background:#FF4D6D;left:50%;top:50%;transform:translate(-50%,-50%);z-index:0}
.g .x b{position:relative}
.time{position:absolute;left:80px;top:1080px;font-size:40px;font-weight:800}
.time small{display:block;font-size:24px;color:#4A5F92;font-weight:600}
.cta{position:absolute;right:80px;top:1070px;background:#FF4D6D;color:#fff;font-weight:800;font-size:34px;padding:28px 36px;border-radius:20px}
.ft{position:absolute;bottom:70px;left:80px;font-size:24px;color:#4A5F92}
""","""<div class="br">[Nama Organisasi]</div><div class="h">Tandakan kalendar!<br><span>Open Day</span> kami</div>
<div class="cal"><div class="top"><span>NOVEMBER</span><span>2026</span></div><div class="g">
<div class="w">AHD</div><div class="w">ISN</div><div class="w">SEL</div><div class="w">RAB</div><div class="w">KHA</div><div class="w">JUM</div><div class="w">SAB</div>
"""+"".join(f'<div class="{"x" if d==21 else ""}"><b>{d}</b></div>' for d in range(1,29))+"""</div></div>
<div class="time">Sabtu · 9am – 4pm<small>Slot terhad!</small></div><div class="cta">Booking Slot Sekarang →</div>
<div class="ft">📍 [Lokasi] · 📱 [No. WhatsApp]</div>""")

# 7 Retro
P["07-retro-groovy"]=("""body{background:#FFF1D6;font-family:'Bricolage Grotesque';color:#4A2511}
.sun{position:absolute;left:50%;top:600px;transform:translateX(-50%);width:1500px;height:1500px;border-radius:50%;
background:radial-gradient(circle,#F9C74F 0 18%,#F8961E 18% 30%,#F3722C 30% 42%,#E05A2B 42% 54%,#90323D 54% 66%,transparent 66%)}
.br{position:absolute;top:70px;left:0;right:0;text-align:center;font-weight:800;font-size:28px;letter-spacing:.2em}
.h{position:absolute;top:140px;left:0;right:0;text-align:center;font-family:'Shrikhand';font-size:180px;line-height:.95;color:#E05A2B;text-shadow:6px 6px 0 #4A2511}
.h small{display:block;font-size:80px;color:#4A2511;text-shadow:none}
.info{position:absolute;top:900px;left:0;right:0;text-align:center;color:#FFF1D6;font-weight:800;font-size:56px;line-height:1.2}
.info small{display:block;font-size:34px;font-weight:600}
.cta{position:absolute;bottom:90px;left:50%;transform:translateX(-50%);white-space:nowrap;background:#FFF1D6;color:#90323D;font-family:'Shrikhand';font-size:48px;padding:20px 50px;border-radius:60px}
""","""<div class="sun"></div><div class="br">[NAMA ORGANISASI]</div>
<div class="h"><small>jom datang</small>Open Day!</div>
<div class="info">Sabtu, 21 Nov 2026<small>9:00 pagi – 4:00 petang · slot terhad</small></div>
<div class="cta">Booking Slot Sekarang!</div>""")

# 8 Bento grid
P["08-bento-grid"]=("""body{background:#F4F4F0;font-family:'Bricolage Grotesque';color:#111;padding:50px}
.g{display:grid;grid-template-columns:1fr 1fr 1fr;grid-template-rows:110px 420px 240px 200px 160px;gap:20px;height:1250px}
.c{border-radius:32px;padding:32px;position:relative;overflow:hidden}
.br{grid-column:1/4;background:#fff;display:flex;align-items:center;justify-content:space-between;font-weight:800;font-size:28px}
.br span{background:#C6F432;padding:8px 18px;border-radius:30px;font-size:22px}
.hero{grid-column:1/4;background:#111;color:#fff}
.hero small{font-size:40px;font-weight:600;color:#C6F432}
.hero h1{font-size:190px;line-height:.88;font-weight:800;margin-top:10px}
.dt{background:#C6F432;grid-row:3/5}
.dt b{display:block;font-size:170px;line-height:.9;font-weight:800}
.dt span{font-size:34px;font-weight:600}
.tm{background:#fff;grid-column:2/4}
.lb{font-size:22px;font-weight:600;color:#666;letter-spacing:.1em}
.tm div{font-size:76px;font-weight:800;margin-top:10px}
.a1{background:#B9C7FF;font-size:32px;font-weight:800;display:flex;align-items:flex-end}
.a2{background:#FFB4A2;font-size:32px;font-weight:800;display:flex;align-items:flex-end}
.cta{grid-column:1/4;background:#5B3CFF;color:#fff;display:flex;align-items:center;justify-content:space-between;font-size:52px;font-weight:800}
.cta i{font-style:normal;background:#fff;color:#5B3CFF;width:90px;height:90px;border-radius:50%;display:grid;place-items:center}
""","""<div class="g"><div class="c br">[Nama Organisasi]<span>SLOT TERHAD</span></div>
<div class="c hero"><small>Jom datang ke</small><h1>Open<br>Day ✦</h1></div>
<div class="c dt"><b>21</b><span>Nov 2026<br>Sabtu</span></div>
<div class="c tm"><div class="lb">MASA</div><div>9am — 4pm</div></div>
<div class="c a1">🏛️ Lawatan<br>dipandu</div><div class="c a2">💬 Sesi<br>Q&amp;A</div>
<div class="c cta">Booking Slot Sekarang!<i>→</i></div></div>""")

# 9 Neon futuristic
P["09-neon-futuristic"]=("""body{background:#07060F;font-family:'Unbounded';color:#fff}
.gl{position:absolute;border-radius:50%;filter:blur(90px)}
.grain{position:absolute;inset:0;opacity:.18;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.9'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)'/%3E%3C/svg%3E")}
.br{position:absolute;top:80px;left:80px;font-size:22px;letter-spacing:.3em;color:#ffffffaa}
.h{position:absolute;top:300px;left:80px;font-weight:800;font-size:170px;line-height:.92}
.h span{display:block;background:linear-gradient(90deg,#00F0FF,#B14CFF,#FF3DAE);-webkit-background-clip:text;color:transparent}
.k{position:absolute;top:220px;left:84px;font-size:36px;font-weight:400;color:#00F0FF}
.inf{position:absolute;top:780px;left:80px;right:80px;display:flex;gap:20px}
.inf div{flex:1;border:1.5px solid #ffffff40;border-radius:24px;padding:28px;background:#ffffff0d;font-family:'Space Grotesk';font-size:22px;letter-spacing:.2em;color:#ffffffaa}
.inf b{display:block;font-family:'Unbounded';font-size:46px;color:#fff;letter-spacing:0;margin-top:10px}
.cta{position:absolute;bottom:130px;left:80px;right:80px;text-align:center;padding:32px;border-radius:60px;background:linear-gradient(90deg,#00F0FF,#B14CFF,#FF3DAE);font-weight:800;font-size:40px;color:#07060F;box-shadow:0 0 60px #B14CFF88}
.ft{position:absolute;bottom:70px;left:0;right:0;text-align:center;font-family:'Space Grotesk';font-size:22px;color:#ffffff88;letter-spacing:.15em}
""","""<div class="gl" style="width:600px;height:600px;background:#B14CFF66;right:-200px;top:-100px"></div>
<div class="gl" style="width:500px;height:500px;background:#00F0FF44;left:-200px;top:600px"></div>
<div class="grain"></div><div class="br">[NAMA ORGANISASI]</div><div class="k">// jom datang</div>
<div class="h">OPEN<span>DAY_26</span></div>
<div class="inf"><div>TARIKH<b>21 NOV</b></div><div>MASA<b>9AM–4PM</b></div></div>
<div class="cta">BOOKING SLOT SEKARANG ↗</div><div class="ft">SABTU · SLOT TERHAD · [LOKASI]</div>""")

# 10 Collage sticker
P["10-kolaj-sticker"]=("""body{background:#EDE6DA;font-family:'Archivo Black';color:#111}
.paper{position:absolute;background:#fff;box-shadow:0 8px 20px #0002}
.tape{position:absolute;width:160px;height:44px;background:#F7E27Acc}
.h1{position:absolute;left:70px;top:150px;background:#111;color:#fff;font-size:120px;padding:10px 30px;transform:rotate(-3deg)}
.h2{position:absolute;left:150px;top:330px;background:#FF4F2E;color:#fff;font-size:190px;padding:0 30px;transform:rotate(2deg);line-height:1.1}
.h3{position:absolute;left:90px;top:560px;background:#3B6CFF;color:#fff;font-size:190px;padding:0 30px;transform:rotate(-2deg);line-height:1.1}
.note{position:absolute;right:70px;top:800px;width:400px;background:#FFF27A;padding:30px;transform:rotate(4deg);font-family:'Caveat';font-size:52px;line-height:1.1;box-shadow:0 10px 20px #0002}
.dt{position:absolute;left:70px;top:820px;width:500px;padding:34px;transform:rotate(-2deg)}
.dt div{font-size:56px;line-height:1.05}.dt small{font-family:'Space Grotesk';font-weight:700;font-size:30px;display:block;margin-top:12px}
.br{position:absolute;top:60px;left:70px;font-family:'Caveat';font-size:48px}
.cta{position:absolute;bottom:80px;left:70px;right:70px;background:#111;color:#C6F432;text-align:center;font-size:50px;padding:28px;transform:rotate(-1deg)}
.stk{position:absolute;right:90px;top:90px;width:190px;height:190px;border-radius:50%;background:#C6F432;display:grid;place-items:center;text-align:center;font-size:30px;transform:rotate(12deg);line-height:1}
""","""<div class="br">[nama organisasi] presents ↓</div>
<div class="stk">SLOT<br>TERHAD!</div>
<div class="h1">JOM DATANG</div><div class="h2">OPEN</div><div class="h3">DAY!</div>
<div class="paper dt"><div class="tape" style="left:170px;top:-20px;transform:rotate(-4deg)"></div><div>SABTU<br>21.11.2026</div><small>9:00 PAGI – 4:00 PETANG</small></div>
<div class="note">Tengok sendiri, tanya terus. Jumpa sana! :)</div>
<div class="cta">BOOKING SLOT SEKARANG!</div>""")

for k,(css,html) in P.items():
    open(k+".html","w").write(HEAD+css+"</style></head><body>"+html+"</body></html>")
