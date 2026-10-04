from playwright.sync_api import sync_playwright
from datetime import datetime

print("W1 D3 Assignment 2 - Playwright Cricbuzz scorecard")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        "https://www.cricbuzz.com/live-cricket-scorecard/151554/ind-vs-wi-3rd-odi-west-indies-tour-of-india-2026",
        wait_until="domcontentloaded",
        timeout=60000
    )

    page.wait_for_timeout(5000)

    page.screenshot(path="cricbuzz.png", full_page=True)

    print("Screenshot taken and saved as cricbuzz.png")
    #print("Page title:", page.title())
    #print("Page URL:", page.url)

    now = datetime.now()

    date_value = now.strftime("%d-%m-%Y")
    time_value = now.strftime("%H-%M-%S")

    try:
        scorecard_text = page.locator("body").inner_text(timeout=10000)

        #print("Scorecard text:")
        #print(scorecard_text)

    except Exception as e:
        print("Could not read page text.")
        print("Error:", e)

    filename = f"scorecard_{date_value}_{time_value}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(scorecard_text)

    print("Scorecard saved!")
    print("File:", filename)

    browser.close()