from playwright.sync_api import sync_playwright
import json
import os
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1440,'height':1000});errors=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto(os.environ.get('GUILDOPS_URL','http://127.0.0.1:8771/guildops.html'))
 page.get_by_role('button',name='＋ 提出任務').click()
 page.locator('#title').fill('研究驗證任務')
 page.locator('#description').fill('完成自主工作流驗證 <script>alert(1)</script>')
 page.locator('#xp').fill('120')
 page.get_by_role('button',name='送出提案').click()
 card=page.locator('article').filter(has_text='研究驗證任務')
 assert card.get_by_role('button',name='審核通過').count()==0
 page.locator('#actor').select_option('admin')
 page.once('dialog',lambda d:d.accept('120'))
 card.get_by_role('button',name='審核通過').click()
 page.locator('#actor').select_option('lin')
 card.get_by_role('button',name='承接任務',exact=True).click()
 page.locator('#actor').select_option('chen')
 assert card.get_by_role('button',name='提交成果').count()==0
 page.locator('#actor').select_option('lin')
 page.once('dialog',lambda d:d.accept('已完成驗證與交付'))
 card.get_by_role('button',name='提交成果').click()
 assert page.locator('#members').inner_text().find('120 XP')==-1
 page.locator('#actor').select_option('admin')
 page.once('dialog',lambda d:d.accept('補上測試結果'))
 card.get_by_role('button',name='要求補件').click()
 assert '進行中' in card.inner_text()
 page.locator('#actor').select_option('lin')
 page.once('dialog',lambda d:d.accept('已補上測試結果'))
 card.get_by_role('button',name='提交成果').click()
 page.locator('#actor').select_option('admin')
 card.get_by_role('button',name='驗收通過').click()
 assert '已完成' in card.inner_text()
 assert card.get_by_role('button',name='驗收通過').count()==0
 assert '120 XP' in page.locator('#members').inner_text()
 assert 'Lv.2' in page.locator('#members').inner_text()
 before=page.evaluate('JSON.parse(localStorage.getItem("guildops-v1"))')
 page.reload()
 assert before==page.evaluate('JSON.parse(localStorage.getItem("guildops-v1"))')
 with page.expect_download() as info:page.get_by_role('button',name='匯出 JSON 備份').click()
 backup=info.value.path();assert json.load(open(backup))==before
 page.once('dialog',lambda d:d.accept())
 page.get_by_role('button',name='重設範例資料').click()
 assert page.locator('article').filter(has_text='研究驗證任務').count()==0
 page.once('dialog',lambda d:d.accept())
 page.locator('#file').set_input_files(str(backup))
 page.wait_for_function('JSON.parse(localStorage.getItem("guildops-v1")).tasks.length === 4')
 assert '120 XP' in page.locator('#members').inner_text()
 page.locator('#file').set_input_files({'name':'bad.json','mimeType':'application/json','buffer':b'{"version":1,"tasks":[],"audit":"bad"}'})
 page.get_by_role('status').filter(has_text='備份格式無效').wait_for()
 assert len(page.evaluate('JSON.parse(localStorage.getItem("guildops-v1")).tasks'))==4
 page.locator('#search').fill('不存在的任務')
 assert page.locator('article').count()==0
 page.locator('#search').fill('')
 page.screenshot(path='/workspace/demosite/guildops-desktop.png',full_page=True)
 page.set_viewport_size({'width':390,'height':844})
 assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
 page.screenshot(path='/workspace/demosite/guildops-mobile.png',full_page=True)
 assert not errors,errors
 b.close()
print('PASS: lifecycle, role UI, revision, XP/rank, no repeat award, persistence, export/import, invalid import, escaped content, search and mobile layout.')
