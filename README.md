# Playwright E2E Tests — Python

[![CI](https://github.com/OperaAxe/PROJECT-1-AUTOMATED-E2E-TEST-SUITE/actions/workflows/playwright.yml/badge.svg)](https://github.com/OperaAxe/PROJECT-1-AUTOMATED-E2E-TEST-SUITE/actions/workflows/playwright.yml)

Python, pytest, and Playwright tests for the public [SauceDemo training storefront](https://www.saucedemo.com/). The suite focuses on login, the product catalogue, and cart behaviour.

This is a practice project against a public demo site, not client work or a production commerce test.

## Current coverage

| Area | Check |
|---|---|
| Login | Valid credentials, incorrect password, missing fields, locked-out user |
| Inventory | The expected demo products appear |
| Cart | Adding products updates the badge and cart contents |
| Removal | Removing one product leaves the other product in the cart |

The cart-removal case checks the remaining state, not just whether the clicked button disappeared.

## Run locally

Requires Python 3.11 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
pytest -v
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

For an authorized staging copy of the app, set `BASE_URL` before running the suite:

```bash
export BASE_URL="https://your-staging-host/"
pytest -v
```

## Known limits

**Status: in development.** Coverage is limited to the listed flows. The tests do not submit payment or create real orders. Because the default target is a public demo site, an outage or a site change can affect a run; a failed test needs investigation before it is treated as an application defect.
