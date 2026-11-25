const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:1});
for(const f of fs.readdirSync('.').filter(f=>/^\d\d-.*\.html$/.test(f))){await p.goto('file://'+process.cwd()+'/'+f,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:f.replace('.html','.png')});}
await b.close()})()
