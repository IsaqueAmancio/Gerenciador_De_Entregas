from playwright.sync_api import sync_playwright
lista_to = ['br1','br2','br3','br4','br5','br6','br7','br8','br9','br10']
with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    pag = browser.new_page()
    pag.goto("https://www.google.com.br/maps/preview")
    print(pag.title())
    pag.fill('input[name="q"]','av.bariloche,104')
    pag.keyboard.press("Enter")
    pag.wait_for_timeout(700)
    pag.click('button[class="g88MCb S9kvJb "]')
    pag.fill('input[class="tactile-searchbox-input"]','av.grimaldo tolaine,1143')
    pag.keyboard.press("Enter")
    pag.wait_for_timeout(700)
    tempo_dist = pag.inner_text('div[class="FkdJRd vRIAEd dS8AEf"]')
    tempo_dist = tempo_dist.split('\n')
    print(tempo_dist[3])
    pag.wait_for_timeout(30000)
    