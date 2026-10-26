# Automated E2E Testing with Playwright + Python

> **Playbook status: in progress.** I'm building this repo as a practical guide to how I approach browser testing, from a clear manual question to a repeatable automated check. It uses SauceDemo's public training storefront and public demo credentials. I'm still adding examples and checking the suite as the site changes.

[![Playwright QA Playbook](https://github.com/OperaAxe/PROJECT-1-AUTOMATED-E2E-TEST-SUITE/actions/workflows/playwright.yml/badge.svg)](https://github.com/OperaAxe/PROJECT-1-AUTOMATED-E2E-TEST-SUITE/actions/workflows/playwright.yml)

## Why this project exists

I want the tests in this repository to answer useful questions about a real browser journey, not just make a green badge. For example: can a user sign in, see the catalogue, add two products, review the cart, and remove one without the cart state becoming confusing?

The target is [SauceDemo](https://www.saucedemo.com/), a public training storefront. This is not a client project or a production commerce system. The demo site is external, so an outage or site change can affect results; I investigate the cause before calling a failure a product defect.

## What the current suite checks

| Area | Example | Expected result |
|---|---|---|
| Successful login | `standard_user / secret_sauce` | User reaches the Products page |
| Incorrect password | Valid username with a wrong password | Login is rejected with an error |
| Missing input | Leave username or password blank | The form explains which field is required |
| Locked account | `locked_out_user / secret_sauce` | Access is blocked with a clear message |
| Product catalogue | Open inventory | Six demo products render |
| Cart | Add Backpack and Bike Light | Badge and cart contents show two products |
| Removal | Remove the Backpack | The Backpack disappears; the Bike Light stays |

## Run it locally

Use Python 3.11 or newer.

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
pytest -v
```

Generate a shareable HTML report:

```bash
mkdir -p reports test-results
pytest -v --junitxml=test-results/junit.xml --html=reports/pytest-report.html --self-contained-html
```

To run against a compatible staging clone, set `BASE_URL` before running pytest:

```bash
# macOS/Linux
export BASE_URL="https://your-staging-host/"
# Windows PowerShell
$env:BASE_URL = "https://your-staging-host/"
pytest -v
```

## How I use this as a playbook

I start with the user journey and the question the test should answer. Then I identify the evidence that proves the outcome, choose stable locators, and automate only the checks that are worth repeating.

A useful example is cart removal: removing the Backpack should not remove the Bike Light as a side effect. The test checks both sides of that expectation. A success toast alone would not prove the remaining cart state is correct.

## Current limits and next steps

- The suite depends on a public demo site, so external availability and site changes can affect results.
- It covers a small set of login, catalogue, and cart flows; it is not a claim of complete coverage.
- The tests do not submit payment or create real orders.
- Next I want to add more deliberate edge cases, improve failure evidence, and keep the manual reasoning alongside the automated checks.

I’m sharing the repository as a work in progress because that is what it is. I’d rather show a small suite I can explain and maintain than claim results I have not measured.

## Contact

- GitHub: [OperaAxe](https://github.com/OperaAxe)
- LinkedIn: [davidchristianj](https://linkedin.com/in/davidchristianj)
- Upwork: [Christian David](https://upwork.com/freelancers/~010e703beaa0687103)
