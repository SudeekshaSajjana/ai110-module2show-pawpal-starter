# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.

Three core actions a user should be able to perform are seeing the daily tasks, adding tasks, and adding information.

- What classes did you include, and what responsibilities did you assign to each?

Owner class - this represents the person who owns the pet(s). The attributes this class would hold are name, email, phone, and pets. The methods it would have are adding pets, removing pets, and showing formatted contact details. 

Pet class - represents the pet. The attributes it would have are name, species, breed, age, weight, and medical history. The methods it would have are showing a summary of the pet, adding a piece of information in the medical record, and updating weight.

Appointment class - this represents a schedules event that gets added to the schedule. The attributes this class would hold are date, type, pet, provider, and notes. The methods it would hold are reschedule, cancel, and getting a summary.

Caregiver class - this represents a vet, groomer, or sitter. It's attributes would be name, role, availability, and appointments. The methods it would hold are adding appointments, showing future appointments, and checking to see if a time slot is open.

**b. Design changes**

- Did your design change during implementation?

Yes, the design changed during implementation.

- If yes, describe at least one change and why you made it.

One of the changes that I made was changing the main classes that the app would use. Originally, the four main classes were Owner, Pet, Appointment, and Caregiver. After implementation, the four main classes became Task, Pet, Owner, and Scheduler. The reason for this change was because this made more sense to the main function of the app.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

Some constraints that my scheduler consider are the time of day, date, frequency, and completion status. I decided what mattered most by having the scheduler flag overlaps, but it doesn't build a time budgeted plan or rank tasks.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.

One tradeoff that the scheduler was making was giving the user multiple warnings, which isn't sufficient and not organized. 

- Why is that tradeoff reasonable for this scenario?

This tradeoff is reasonable since it isn't a huge error that would cause the whole app to stop working, but rather an aesthetic issue that would make the app look cleaner if it was fixed.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?

I used AI for various uses such as brainstorming ideas, writing code, and refactoring code.

- What kinds of prompts or questions were most helpful?

The prompts that were the most helpful to ask AI were telling it to draft ideas and brainstorm concepts. Doing this, the AI explained how exactly these ideas worked and how to implement them.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.

One moment where I didn't accept the AI suggestion was when it suggested rewrite one of the methods in a more "pythonic" way. I didn't accept this suggestion since it made more sense to keep the code the way that it was orignally to keep the code cleaner and easier to understand.

- How did you evaluate or verify what the AI suggested?

I looked at the code that the AI was suggesting and compared it to the original code and see which code was more efficient.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

Some of the behaviors I tested are conflict detection, recurrence logic, and sorting correctness. These tests are important to make sure that there aren't any conflicts and making sure everything is sorted.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I'm pretty confident that the scheduler will work. Some edge cases that I would add if I had more time is adding a test that fixes the sort_by_time() robustness.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I'm most satisifed with how the classes are written and the methods that entail of the classes. 

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

One thing I would improve is possibly adding more tests in the pytest file to test for more specfic things.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

One importatnt thing I've learned is that AI doesn't always have the best and most efficient solutions. It is always important to double check the changes AI is making and making sure to not blindly accept the code AI writes.