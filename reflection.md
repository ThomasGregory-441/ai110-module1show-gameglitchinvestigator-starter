# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
When I first ran the game, it opened normally as a number guessing game with a difficulty setting, guess box, hints, score, and developer debug information. While testing the game, I noticed that the hints were backwards. For example, when the secret number was 8 and I guessed 20, the game told me to go higher instead of lower. I also noticed that the displayed attempts, score, and history were one guess behind, and starting a new game did not completely reset the previous game's score, history, or win status.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Secret = 8, guess = 20 | Game should tell me to go lower | Game displayed "Go HIGHER!" | None |
| Guesses = 20, 5, 6 | After three guesses, attempts should be 3 and history should contain all three guesses | Game showed 2 attempts and history only contained 20 and 5 | None |
| Click "New Game" after winning | New game should reset the score, history, attempts, and win status | New secret was generated and attempts reset, but score stayed at 35, old history remained, and the game still said "You already won" | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
I used GitHub Copilot in VS Code and ChatGPT as AI teammates while investigating, testing, and repairing the game. One correct suggestion from Copilot was that the high and low hint messages were reversed in the guess-checking logic. I verified this by examining the code and manually testing the game with a secret number of 18: guessing 17 correctly displayed "Go HIGHER!" after the fix, while guessing 19 displayed "Go LOWER!".

I did not accept every AI suggestion as written. During the first refactor, Copilot proposed changing the existing starter tests because its version of `check_guess()` returned an `(outcome, message)` tuple instead of the outcome string expected by the tests. I chose not to modify the starter tests and ran `python -m pytest`, which showed that all three tests expected `"Win"`, `"Too High"`, or `"Too Low"` as strings. I then asked Copilot to revise the implementation to preserve the existing test contract while keeping the corrected user-facing messages, and the three starter tests passed afterward.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
I decided that a bug was fixed only after checking both the behavior of the application and the automated tests. For the reversed hint bug, I manually tested a secret number of 18 and confirmed that guessing 17 displayed "Go HIGHER!" and guessing 19 displayed "Go LOWER!". For the New Game bug, I won a game, clicked New Game, and verified that the attempts and score reset to 0, the history was cleared, the status returned to playing, the input field was empty, and a new secret was generated within the selected difficulty range.

AI also helped me design regression tests for the repaired behavior. The hint-message test checks that guesses above and below the secret produce the correct user-facing directions. The New Game test checks that the game state is completely reset instead of carrying information from the previous game. After completing the fixes and regression tests, I ran `python -m pytest` and all 6 tests passed.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I learned that Streamlit reruns the Python script when the user interacts with the application, but values stored in `st.session_state` can remain between those reruns. This explained why simply calling `st.rerun()` did not fix the New Game bug. The old score, history, and `"won"` status were still stored because the initialization code only supplied default values when those session-state keys did not already exist. I also learned that changing the input widget's key for a new game can create a fresh input field instead of carrying the previous guess into the next game.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One debugging habit I would reuse is reproducing a bug manually before changing the code and then verifying the repair with both manual testing and automated tests. Having a specific example, such as the secret being 18 and testing guesses of 17 and 19, made it much easier to determine whether the behavior was actually correct.

When using AI in the future, I would continue asking it to explain its reasoning and show proposed changes before applying them. This project showed me that AI-generated code can be useful, but it should still be reviewed and tested instead of automatically accepted. The failed starter tests were especially useful because they showed that an AI suggestion could appear reasonable while still violating the existing program's expected behavior.