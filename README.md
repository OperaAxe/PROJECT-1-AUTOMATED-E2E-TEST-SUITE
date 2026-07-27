# Automated Regression Suite with Playwright + Python + GitHub Actions

---

## Overview

A Playwright and Python test suite that runs on every code push. It automates regression testing for core user flows, catching regressions before they reach production. The suite is integrated with GitHub Actions, so tests run automatically on every pull request and push to main.

---

## The Problem

**Before this project:**

- Manual regression testing took 4+ hours per release cycle
- Tests were often skipped on small releases to save time
- Bugs that could have been caught early reached production
- Emergency rollbacks happened monthly
- Developers wasted hours debugging issues found too late
- No automated safety net for releases

**The Impact:**

- Frustrated users
- Stressed developers
- Delayed releases
- Revenue loss from broken critical flows

---

## The Goal

> Build an automated test suite that runs on every code push. Regression tests should take under 5 minutes. Bugs should be caught before they reach production.

---

## The Approach

### 1. Choose the Stack

| Tool | Why It Was Chosen |
|------|-------------------|
| Playwright | Modern, fast, works across browsers. Better than Selenium |
| Python | Familiar, readable, easy to write and maintain tests |
| GitHub Actions | Free, integrates with GitHub, runs on every push |
| Allure Report | Detailed HTML reports with visual test results |
| Slack API | Real-time notifications on test status |

### 2. Identify Critical User Flows

Before writing any code, I mapped out what absolutely had to work for the application to function. These became the test suite priorities.

| Priority | Flow | Why It Matters |
|----------|------|----------------|
| P1 | User login | If login breaks, no one can use the app |
| P1 | Checkout process | If checkout breaks, revenue stops |
| P2 | Product search | If search fails, users can't find products |
| P2 | Profile updates | If updates fail, users get frustrated |
| P3 | Password reset | If reset fails, support tickets spike |

### 3. Design the Test Architecture
