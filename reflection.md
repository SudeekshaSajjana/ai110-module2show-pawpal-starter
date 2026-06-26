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
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
