# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
========================================
        PawPal — Today's Schedule
========================================

Buddy (Golden Retriever)
------------------------------
  [Pending] Morning walk at 7:00 AM (daily)
  [Pending] Feed breakfast at 8:00 AM (daily)
  [Pending] Evening walk at 6:00 PM (daily)

Luna (Siamese)
------------------------------
  [Pending] Feed breakfast at 8:30 AM (daily)
  [Pending] Clean litter box at 12:00 PM (daily)
  [Pending] Brush fur at 5:00 PM (weekly)

========================================
Total pending tasks: 6
========================================  ...
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```
python - m pytest

The tests cover sorting, recurrence of tasks, and conflict detection.

Sample test output:

```
=============== test session starts ===============
platform win32 -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\sajja\Downloads\ai110-module2show-pawpal-starter
plugins: anyio-4.13.0
collected 12 items                                 

tests\test_pawpal.py ............            [100%]

=============== 12 passed in 0.14s ================
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting |sort_by_time() | e.g., by priority, duration |
| Filtering | filter_tasks()| e.g., skip tasks if time runs out |
| Conflict handling |detect_conflicts() | e.g., overlapping time slots |
| Recurring tasks | _schedule_next() | e.g., daily vs. weekly |

## 📸 Demo Walkthrough

### UI features

The Streamlit app (`app.py`) is organized into four sections:

- **Owner** — enter a name, email, and phone number and click "Create Owner." Once created, the owner's contact info is displayed below the form.
- **Add a Pet** — enter a pet's name, species, breed, age, and weight and click "Add Pet." Registered pets appear in a table as they're added.
- **Schedule a Task** — pick a pet, describe the task, set a time and frequency (`daily`, `weekly`, or `monthly`), and click "Add Task" to attach it to that pet.
- **Today's Schedule** — shows each pet's pending tasks sorted chronologically, surfaces any scheduling conflicts as warnings, and provides a "Mark Done" control to complete a task on the spot.

### Example workflow

1. Create an owner (e.g., "Jordan").
2. Add a pet (e.g., "Mochi," a Shiba Inu).
3. Schedule a task for Mochi — e.g., "Morning walk" at 8:00 AM, daily.
4. Open "Today's Schedule" to see Mochi's task listed alongside any other pets' tasks, sorted by time.
5. Click "Mark Done" on the task — the Scheduler marks it complete and, for daily/weekly tasks, automatically schedules the next occurrence.

### Key Scheduler behaviors shown

- **Sorting** — `sort_by_time()` orders every pet's task list chronologically, regardless of the order tasks were entered in.
- **Conflict warnings** — `detect_conflicts()` displays a warning banner whenever two tasks for the same pet share the same time and date (e.g. two 6:00 PM tasks).
- **Filtering** — `filter_tasks()` powers the pending-only view, so completed tasks drop out of the schedule automatically.
- **Recurrence** — clicking "Mark Done" on a daily/weekly task calls `complete_task()`, which schedules that task's next occurrence behind the scenes.

### Sample CLI output (`python main.py`)

```
==================================================
  Conflict Detection
==================================================
  WARNING: Buddy has a time conflict at 6:00 PM on 2026-06-30 — "Evening walk" and "Feed dinner"

==================================================
  Today's Full Schedule (sorted by time)
==================================================
  [Pending] Morning walk at 7:00 AM on 2026-06-30 (daily)
  [Pending] Feed breakfast at 8:00 AM on 2026-06-30 (daily)
  [Pending] Feed breakfast at 8:30 AM on 2026-06-30 (daily)
  [Pending] Clean litter box at 12:00 PM on 2026-06-30 (daily)
  [Pending] Brush fur at 5:00 PM on 2026-06-30 (weekly)
  [Pending] Evening walk at 6:00 PM on 2026-06-30 (daily)
  [Pending] Feed dinner at 6:00 PM on 2026-06-30 (daily)
```
