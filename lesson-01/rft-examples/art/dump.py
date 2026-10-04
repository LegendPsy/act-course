import asyncio,json
from playwright.async_api import async_playwright
URL='file:///home/claude/act-course/lesson-01/rft-examples/index.html'
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    pg=await b.new_page(viewport={'width':1600,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    await pg.goto(URL);await pg.wait_for_timeout(500)
    d=await pg.evaluate('({steps:__lena.steps.map(s=>s.st),W:__lena.widths(),NODES:__lena.NODES,ORDER:__lena.EXIT_ORDER,MAX:__lena.MAX,MARK:__lena.MARK})')
    json.dump(d,open('lena-dump.json','w'),ensure_ascii=False)
    print('errors',errs,'MAX',d['MAX'],d['MARK'])
    await b.close()
asyncio.run(m())
