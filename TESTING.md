# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

In this section, you need to convince the assessors that you have conducted enough testing to legitimately believe that the site works well.
Essentially, in this part, you should go over all of your project's features, and ensure that they all work as intended,
with the project providing an easy and straightforward way for the users to achieve their goals.

Feature-by-Feature Testing:

Go through each feature of your portfolio site and detail the testing process for each.

Explain the functionality and demonstrate how it aligns with the intended purpose. This could include:

- Navigation: Ensuring smooth transitions between pages, links directing to the correct destinations.
- Responsive Design: Checking for compatibility across various devices and screen sizes.
- Portfolio Display: Verifying that projects are properly showcased with accurate descriptions, images, and links.
- Contact Form: Testing the form submission process, ensuring the user receives a confirmation, and you receive the message.

User Experience Testing:

- Usability Testing: Have users (or simulated users) interact with the site and provide feedback. Document any issues encountered and the resolutions implemented.
- Accessibility Testing: Confirm compliance with accessibility standards (e.g., screen reader compatibility, proper alt text for images, keyboard navigation).

Compatibility Testing:

- Browser Compatibility: Testing on different browsers (Chrome, Firefox, Safari, Edge, etc.) to ensure consistent performance.
- Device Compatibility: Ensuring functionality across various devices (desktops, laptops, tablets, and mobile phones).
- Performance Testing (optional):
	- Speed and Load Testing: Tools like PageSpeed Insights or GTmetrix to check page load times and optimize where necessary.
	- Scalability Testing: Assess how the site handles increased traffic or usage.

Regression Testing:

After implementing fixes or updates, ensure that previous features and functionalities still work as intended. This prevents new changes from breaking existing features.

Documentation and Logs:

Maintain records of testing procedures, results, and any bugs encountered along with their resolutions. This helps demonstrate a systematic approach to testing and problem-solving.
User Feedback Incorporation:

If applicable, mention how user feedback has been taken into account and implemented to enhance the user experience.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## Code Validation

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use the space to discuss code validation for any of your own code files (where applicable).
You are not required to validate external libraries/frameworks, such as imported Bootstrap, Materialize, Font Awesome, etc.

**IMPORTANT**: You must provide a screenshot for each file you validate.

**PRO TIP**: Always validate the live site pages, not your local code. There could be subtle/hidden differences.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | art.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/dark-castle-lite/main/art.py) | ![screenshot](documentation/validation/validation-art.png) | |
|  | chapters.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/dark-castle-lite/main/chapters.py) | ![screenshot](documentation/validation/validation-chapters.png) | |
|  | classes.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/dark-castle-lite/main/classes.py) | ![screenshot](documentation/validation/validation-classes.png) | |
|  | mechanics.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/dark-castle-lite/main/mechanics.py) | ![screenshot](documentation/validation/validation-mechanics.png) | |
|  | run.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/dark-castle-lite/main/run.py) | ![screenshot](documentation/validation/validation-run.png) | |
|  | utilities.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/dark-castle-lite/main/utilities.py) | ![screenshot](documentation/validation/validation-utilities.png) | |

## Browser Compatibility

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to discuss testing the live/deployed site on various browsers.

Consider testing AT LEAST 3 different browsers, if available on your system.

You DO NOT need to use all of the browsers below, just pick any 3 (minimum).

Recommended browsers to consider:
- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://www.microsoft.com/edge)
- [Safari](https://support.apple.com/downloads/safari)
- [Brave](https://brave.com/download)
- [Opera](https://www.opera.com/download)

**IMPORTANT**: You must provide screenshots of the tested browsers, to "prove" that you've actually tested them.

Please note, there are services out there that can test multiple browser compatibilities at the same time.
Some of these are paid services, but some are free.
If you use these, you must provide a link to the source used for attribution, and multiple screenshots of the results.

Sample browser testing documentation:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser-chrome-home.png) | ![screenshot](documentation/browsers/browser-chrome-about.png) | ![screenshot](documentation/browsers/browser-chrome-contact.png) | ![screenshot](documentation/browsers/browser-chrome-etc.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser-firefox-home.png) | ![screenshot](documentation/browsers/browser-firefox-about.png) | ![screenshot](documentation/browsers/browser-firefox-contact.png) | ![screenshot](documentation/browsers/browser-firefox-etc.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/browser-edge-home.png) | ![screenshot](documentation/browsers/browser-edge-about.png) | ![screenshot](documentation/browsers/browser-chrome-edge.png) | ![screenshot](documentation/browsers/browser-edge-etc.png) | Works as expected |
| Safari | ![screenshot](documentation/browsers/browser-safari-home.png) | ![screenshot](documentation/browsers/browser-safari-about.png) | ![screenshot](documentation/browsers/browser-safari-contact.png) | ![screenshot](documentation/browsers/browser-safari-etc.png) | Minor CSS differences |
| Brave | ![screenshot](documentation/browsers/browser-brave-home.png) | ![screenshot](documentation/browsers/browser-brave-about.png) | ![screenshot](documentation/browsers/browser-brave-contact.png) | ![screenshot](documentation/browsers/browser-brave-etc.png) | Works as expected |
| Opera | ![screenshot](documentation/browsers/browser-opera-home.png) | ![screenshot](documentation/browsers/browser-opera-about.png) | ![screenshot](documentation/browsers/browser-opera-contact.png) | ![screenshot](documentation/browsers/browser-opera-etc.png) | Minor differences |
| repeat for any other tested browsers | x | x | x | x | x |

## Responsiveness

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to discuss testing the live/deployed site on various device sizes.

The minimum requirement is for the following 3 tests:
- Mobile
- Tablet
- Desktop

**IMPORTANT**: You must provide screenshots of the tested responsiveness, to "prove" that you've actually tested them.

Using the "amiresponsive" mockup image (or similar) does not suffice the requirements.
Consider using some of the built-in device sizes in the Developer Tools.

If you have tested the project on your actual mobile phone or tablet, consider also including screenshots of these as well.
It showcases a higher level of manual tests, and can be seen as a positive inclusion!

Sample responsiveness testing documentation:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/responsive-mobile-home.png) | ![screenshot](documentation/responsiveness/responsive-mobile-about.png) | ![screenshot](documentation/responsiveness/responsive-mobile-contact.png) | ![screenshot](documentation/responsiveness/responsive-mobile-etc.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/responsive-tablet-home.png) | ![screenshot](documentation/responsiveness/responsive-tablet-about.png) | ![screenshot](documentation/responsiveness/responsive-tablet-contact.png) | ![screenshot](documentation/responsiveness/responsive-tablet-etc.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsiveness/responsive-desktop-home.png) | ![screenshot](documentation/responsiveness/responsive-desktop-about.png) | ![screenshot](documentation/responsiveness/responsive-desktop-contact.png) | ![screenshot](documentation/responsiveness/responsive-desktop-etc.png) | Works as expected |
| XL Monitor | ![screenshot](documentation/responsiveness/responsive-xl-home.png) | ![screenshot](documentation/responsiveness/responsive-xl-about.png) | ![screenshot](documentation/responsiveness/responsive-xl-contact.png) | ![screenshot](documentation/responsiveness/responsive-xl-etc.png) | Scaling starts to have minor issues |
| 4K Monitor | ![screenshot](documentation/responsiveness/responsive-4k-home.png) | ![screenshot](documentation/responsiveness/responsive-4k-about.png) | ![screenshot](documentation/responsiveness/responsive-4k-contact.png) | ![screenshot](documentation/responsiveness/responsive-4k-etc.png) | Noticeable scaling issues |
| Google Pixel 7 Pro | ![screenshot](documentation/responsiveness/responsive-pixel-home.png) | ![screenshot](documentation/responsiveness/responsive-pixel-about.png) | ![screenshot](documentation/responsiveness/responsive-pixel-contact.png) | ![screenshot](documentation/responsiveness/responsive-pixel-etc.png) | Works as expected |
| iPhone 14 | ![screenshot](documentation/responsiveness/responsive-iphone-home.png) | ![screenshot](documentation/responsiveness/responsive-iphone-about.png) | ![screenshot](documentation/responsiveness/responsive-iphone-contact.png) | ![screenshot](documentation/responsiveness/responsive-iphone-etc.png) | Works as expected |
| repeat for any other tested devices | x | x | x | x | x |

## Lighthouse Audit

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports.
Avoid testing the local version (especially if developing in Gitpod), as this can have knock-on effects of performance.

If you don't have Lighthouse in your Developer Tools,
it can be added as an [extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk).

Don't just test the home page (unless it's a single-page application).
Make sure to test the Lighthouse Audit results for all of your pages.

**IMPORTANT**: You must provide screenshots of the results, to "prove" that you've actually tested them.

Sample Lighthouse testing documentation:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | Some minor warnings |
| About | ![screenshot](documentation/lighthouse/lighthouse-about-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-about-desktop.png) | Some minor warnings |
| Gallery | ![screenshot](documentation/lighthouse/lighthouse-gallery-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-gallery-desktop.png) | Slow response time due to large images |
| x | x | x | repeat for any other tested pages/sizes |

## Defensive Programming

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

MS3 (Flask) | MS4/PP4/PP5 (Django):
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable.
Ideally, tests cases should focus on each individual section of every page on the website.
Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine,
consider documenting tests on each element of the page
(ie. button clicks, input box validation, navigation links, etc.) by testing them in their happy flow,
and also the bad/exception flow, mentioning the expected and observed results,
and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot (Before) | Screenshot (After) | Screenshot (After(alt))
| --- | --- | --- | --- | --- | --- | --- | --- |
| Homescreen | | | | | | | |
| | Homescreen is expected to take the user to choose name screen when "p" is entered | Tested the feature by entering "p" on homescreen | The feature behaved as expected, and it prompted the user to choose a name | Test concluded and passed | ![screenshot](documentation/features/feature-homescreen.png) | ![screenshot](documentation/features/feature-enter-name.png) |
| | Homescreen is expected to take user to page 1 of the instructions screen when "i" is entered | Tested the feature by entering "i" on homepage | The feature behaved as expected and took the user to page 1 of the instructions screen| Test concluded and passed | ![screenshot](documentation/features/feature-homescreen.png) | ![screenshot](documentation/features/feature-instructions-page1.png) |
| | Homescreen is expected to display invalid input message when user enters any value other that "h" or "i" | Tested the feature by entering multiple different values, including letters, numbers, and special characters, on homepage | The feature behaved as expected and displayed invalid input message when user entered anything other than "h" or "i" | Test concluded and passed | ![screenshot](documentation/features/feature-homescreen.png) | ![screenshot](documentation/features/feature-homescreen-invalid.png) |
| Instructions | | | | | | | |
| | Instructions screen is expected to take the user to choose name screen when "p" is entered | Tested the feature by entering "p" on insctructions screen (tested on all 5 pages) | The feature behaved as expected, and it prompted the user to choose a name | Test concluded and passed | ![screenshot](documentation/features/feature-instructions-page1.png) | ![screenshot](documentation/features/feature-enter-name.png) |
| | Instructions screen is expected to take the user the homescreen when "h" is entered | Tested the feature by entering "h" on insctructions screen (tested on all 5 pages) | The feature behaved as expected, and took the user to the homescreen | Test concluded and passed | ![screenshot](documentation/features/feature-instructions-page1.png) | ![screenshot](documentation/features/feature-homescreen.png) |
| | Instructions screen is expected to take the user to page 1 of instrucitons screen when "1" is entered | Tested the feature by entering "1" on insctructions screen (tested on all 5 pages) | The feature behaved as expected, and took the user to page 1  | Test concluded and passed | ![screenshot](documentation/features/feature-instructions-page2.png) | ![screenshot](documentation/features/feature-instructions-page1.png) |
| | Instructions screen is expected to take the user to page 2 of instrucitons screen when "2" is entered | Tested the feature by entering "2" on insctructions screen (tested on all 5 pages) | The feature behaved as expected, and took the user to page 2 | Test concluded and passed | ![screenshot](documentation/features/feature-instructions-page1.png) | ![screenshot](documentation/features/feature-instructions-page2.png) |
| | Instructions screen is expected to take the user to page 3 of instrucitons screen when "3" is entered | Tested the feature by entering "3" on insctructions screen (tested on all 5 pages) | The feature behaved as expected, and took the user to page 3 | Test concluded and passed | ![screenshot](documentation/features/feature-instructions-page1.png) | ![screenshot](documentation/features/feature-instructions-page3.png) |
| | Instructions screen is expected to take the user to page 4 of instrucitons screen when "4" is entered | Tested the feature by entering "4" on insctructions screen (tested on all 5 pages) | The feature behaved as expected, and took the user to page 4 | Test concluded and passed | ![screenshot](documentation/features/feature-instructions-page1.png) | ![screenshot](documentation/features/feature-instructions-page4.png) |
| | Instructions screen is expected to take the user to page 5 of instrucitons screen when "5" is entered | Tested the feature by entering "5" on insctructions screen (tested on all 5 pages) | The feature behaved as expected, and took the user to page 5 | Test concluded and passed | ![screenshot](documentation/features/feature-instructions-page1.png) | ![screenshot](documentation/features/feature-instructions-page5.png) |
| | Instructions screen is expected to display invalid input message when user enters any value other than "h", "p", "1", "2", "3", "4", or "5" | Tested the feature by entering multiple different values, including letters, numbers, and special characters, on insctructions screen (tested on all 5 pages) | The feature behaved as expected, and displayed invalid input messaged when the user entered any value other than "h", "p", "1", "2", "3", "4", or "5" | Test concluded and passed | ![screenshot](documentation/features/feature-instructions-page1.png) | ![screenshot](documentation/features/feature-instructions-invalid.png) |
| Enter Name | | | | | | | |
| | Enter player name screen is expected to take the user to select character screen when a valid name is entered (between 1 & 15 characters, no special characters) | Tested the feature by entering a valid name on enter name screen | The feature behaved as expected, and took user to select character screen | Test concluded and passed | ![screenshot](documentation/features/feature-enter-name-test.png) | ![screenshot](documentation/features/feature-select-character.png) |
| | Enter player name screen is expected to display invalid input message when user enters any value less than 1 character long | Tested the feature by entering an empty string | The feature behaved as expected, and displayed error specific message | Test concluded and passed | ![screenshot](documentation/features/feature-enter-name.png) | ![screenshot](documentation/features/feature-enter-name-0.png) |
| | Enter player name screen is expected to display invalid input message when user enters any value with more than 15 characters | Tested the feature by entering a string of more than 15 characters | The feature behaved as expected, and displayed error specific message | Test concluded and passed | ![screenshot](documentation/features/feature-enter-name.png) | ![screenshot](documentation/features/feature-enter-name-15.png) |
| | Enter player name screen is expected to display invalid input message when user enters any value containing special characters | Tested the feature by entering a string containing special characters | The feature behaved as expected, and displayed error specific message | Test concluded and passed | ![screenshot](documentation/features/feature-enter-name.png) | ![screenshot](documentation/features/feature-enter-name-special.png) |
| Select Character | | | | | | | |
| | Select Character screen is expected to take the user to intro chapter when a valid number is selected entered | Tested the feature by entering a valid number on character select screen | The feature behaved as expected, and took user to intro chapter | Test concluded and passed | ![screenshot](documentation/features/feature-select-character-valid.png) | ![screenshot](documentation/features/feature-intro-chapter.png) |
| | Select Character screen is expected to display invalid input message if user doesn't input a valid number | Tested the feature by entering multiple invalid values on character select screen | The feature behaved as expected, and displayed invalid value message | Test concluded and passed | ![screenshot](documentation/features/feature-select-character.png) | ![screenshot](documentation/features/feature-select-character-invalid.png) |
| Intro Chapter | | | | | | | |
| | Intro Chapter is expected to take the user to chapter 1a when "o" is entered| Tested the feature by entering "o" on intro chapter | The feature behaved as expected, and took user to chapter 1a | Test concluded and passed | ![screenshot](documentation/features/feature-intro-chapter.png) | ![screenshot](documentation/features/feature-chapter-1a.png) |
| | Intro Chapter is expected to take the user to chapter 1b when "w" is entered | Tested the feature by entering "w" on intro chapter | The feature behaved as expected, and took user to chapter 1b | Test concluded and passed | ![screenshot](documentation/features/feature-intro-chapter.png) | ![screenshot](documentation/features/feature-chapter-1b.png) |
| | Intro Chapter is expected to display invalid input message when any value other than "w" or  "o" is entered | Tested the feature by entering multiple invalid values on intro chapter | The feature behaved as expected, and displayed error message | Test concluded and passed | ![screenshot](documentation/features/feature-intro-chapter.png) | ![screenshot](documentation/features/feature-intro-chapter-invalid.png) |
| Chapter 1a| | | | | | | |
| | Chapter 1a is expected to have the user successfully pick up the chainmail item, or enter combat when the user enters "y" (random outcome based on cunning stat) | Tested the feature by entering a "y" on chapter 1a multiple times to achive both outcomes | The feature behaved as expected, and randomly initiated either outcome | Test concluded and passed | ![screenshot](documentation/features/feature-chapter-1a-decision.png) | ![screenshot](documentation/features/feature-chapter-1a-y-success.png) | ![screenshot](documentation/features/feature-chapter-1a-y-fail.png) |
| | Chapter 1a is expected to have the user leave the chainmail behind if "n" is entered | Tested the feature by entering "n" on chapter 1a | The feature behaved as expected, and resumed the chapter by not picking up the chainmail | Test concluded and passed | ![screenshot](documentation/features/feature-chapter-1a-decision.png) | ![screenshot](documentation/features/feature-chapter-1a-n.png) |
| | Chapter 1a is expected to display invalid input message when any value other than "y" or  "n" is entered | Tested the feature by entering multiple invalid values on Chapter 1a | The feature behaved as expected, and displayed error message | Test concluded and passed | ![screenshot](documentation/features/feature-chapter-1a-decision.png) | ![screenshot](documentation/features/feature-chapter-1a-decision-invalid.png) |
| Run Game Decision 1 | | | | | | | |
| | Decision 1 in the run_game() function is expected to take the player to chapter 2a if they enter "l" | Tested the feature by entering "l" for decision 1 | The feature behaved as expected, and took the user to chapter 2a  | Test concluded and passed | ![screenshot](documentation/features/feature-run-game-decision01.png) | ![screenshot](documentation/features/feature-chapter-2a.png) |
| | Decision 1 in the run_game() function is expected to take the player to chapter 2b if they enter "r" | Tested the feature by entering "r" for decision 1 | The feature behaved as expected, and took the user to chapter 2b | Test concluded and passed | ![screenshot](documentation/features/feature-run-game-decision01.png) | ![screenshot](documentation/features/feature-chapter-2b.png) |
| | Decision 1 in the run_game() function is expected to display invalid input message when any value other than "l" or  "r" is entered | Tested the feature by entering multiple invalid values on decision 1 | The feature behaved as expected, and displayed error message | Test concluded and passed | ![screenshot](documentation/features/feature-run-game-decision01.png) | ![screenshot](documentation/features/feature-run-game-decision01-invalid.png) |
| Chapter 2a | | | | | | | |
| | Chapter 2a is expected to have the player successfully free the item, or enter combat when the user enters "y" (random outcome based on cunning stat) | Tested the feature by entering a "y" on chapter 2a multiple times to achive both outcomes | The feature behaved as expected, and randomly initiated either outcome | Test concluded and passed | ![screenshot](documentation/features/feature-chapter-2a-decision.png) | ![screenshot](documentation/features/feature-chapter-2a-y-success.png) | ![screenshot](documentation/features/feature-chapter-2a-y-fail.png) |
| | Chapter 2a is expected to have the player ignore the item if "n" is entered | Tested the feature by entering "n" on Chapter 2a | The feature behaved as expected, and resumed the chapter by not picking up the item | Test concluded and passed | ![screenshot](documentation/features/feature-chapter-2a-decision.png) | ![screenshot](documentation/features/feature-chapter-2a-n.png) |
| | Chapter 2a is expected to display invalid input message when any value other than "y" or  "n" is entered | Tested the feature by entering multiple invalid values on Chapter 2a| The feature behaved as expected, and displayed error message | Test concluded and passed | ![screenshot](documentation/features/feature-chapter-2a-decision.png) | ![screenshot](documentation/features/feature-chapter-2a-invalid.png) |
| Run Game Decision 2 | | | | | | | |
| | Decision 2 in the run_game() function is expected to take the player to chapter 3a if they enter "u" | Tested the feature by entering "u" for decision 2 | The feature behaved as expected, and took the user to chapter 3a  | Test concluded and passed | ![screenshot](documentation/features/feature-run-game-decision02.png) | ![screenshot](documentation/features/feature-chapter-3a.png) |
| | Decision 2 in the run_game() function is expected to take the player to chapter 3b if they enter "d" | Tested the feature by entering "d" for decision 2 | The feature behaved as expected, and took the user to chapter 3b | Test concluded and passed | ![screenshot](documentation/features/feature-run-game-decision02.png) | ![screenshot](documentation/features/feature-chapter-3b.png) |
| | Decision 2 in the run_game() function is expected to display invalid input message when any value other than "u" or  "d" is entered | Tested the feature by entering multiple invalid values on decision 2 | The feature behaved as expected, and displayed error message | Test concluded and passed | ![screenshot](documentation/features/feature-run-game-decision02.png) | ![screenshot](documentation/features/feature-run-game-decision02-invalid.png) |
| Chapter 3a | | | | | | | |
| | Chapter 3a is expected to resume the chapter down two different paths where the user touches the mirror, if they enter "y" (outcome is dependent on wether the player has an item or not) | Tested the feature by entering a "y" on chapter 3a with and without an item to achive both outcomes | The feature behaved as expected, and initiated the corrisponding outcome | Test concluded and passed | ![screenshot](documentation/features/feature-chapter-3a-decision.png) | ![screenshot](documentation/features/feature-chapter-3a-y-noitem.png) | ![screenshot](documentation/features/feature-chapter-3a-y-item.png) |
| | Chapter 3a is expected to resume the chapter where the player doesn't touch the mirror if "n" is entered | Tested the feature by entering "n" on Chapter 3a | The feature behaved as expected, and resumed the chapter by touching the mirror | Test concluded and passed | ![screenshot](documentation/features/feature-chapter-3a-decision.png) | ![screenshot](documentation/features/feature-chapter-3a-n.png) |
| | Chapter 3a is expected to display invalid input message when any value other than "y" or  "n" is entered | Tested the feature by entering multiple invalid values on Chapter 3a| The feature behaved as expected, and displayed error message | Test concluded and passed | ![screenshot](documentation/features/feature-chapter-3a-decision.png) | ![screenshot](documentation/features/feature-chapter-3a-invalid.png) |
| Run Game Decision 3 | | | | | | | |
| | Decision 3 in the run_game() function is expected to take the player to chapter 4a if they enter "d" | Tested the feature by entering "d" for decision 3 | The feature behaved as expected, and took the user to chapter 4a  | Test concluded and passed | ![screenshot](documentation/features/feature-run-game-decision03.png) | ![screenshot](documentation/features/feature-chapter-4a.png) |
| | Decision 3 in the run_game() function is expected to take the player to chapter 4b if they enter "p" | Tested the feature by entering "p" for decision 3 | The feature behaved as expected, and took the user to chapter 4b | Test concluded and passed | ![screenshot](documentation/features/feature-run-game-decision03.png) | ![screenshot](documentation/features/feature-chapter-4b.png) |
| | Decision 3 in the run_game() function is expected to display invalid input message when any value other than "d" or  "p" is entered | Tested the feature by entering multiple invalid values on decision 3 | The feature behaved as expected, and displayed error message | Test concluded and passed | ![screenshot](documentation/features/feature-run-game-decision03.png) | ![screenshot](documentation/features/feature-run-game-decision03-invalid.png) |
| Chapter 4a | | | | | | | |
| | If the player fails the initial Cunning check, Chapter 4a is expected to check the players Might stat and resume the chapter if it is >= 9, or results in game over if not, when the player enters "m" | Tested the feature by entering "m" on chapter 4a with and without Might >= 9 | The feature behaved as expected, and initiated the corrisponding outcome | Test concluded and passed | ![screenshot](documentation/features/feature-chapter-4a-decision.png) | ![screenshot](documentation/features/feature-chapter-4a-m-success.png) | ![screenshot](documentation/features/feature-chapter-4a-m-fail.png) |
| | If the player fails the initial Cunning check, Chapter 4a is expected to check the players Wisdom stat and resume the chapter if it is >= 9, or results in game over if not, when the player enters "w" | Tested the feature by entering "w" on chapter 4a with and without Wisdom >= 9 | The feature behaved as expected, and initiated the corrisponding outcome | Test concluded and passed | ![screenshot](documentation/features/feature-chapter-4a-decision.png) | ![screenshot](documentation/features/feature-chapter-4a-w-success.png) | ![screenshot](documentation/features/feature-chapter-4a-w-fail.png) |
| | Chapter 4a is expected to display invalid input message when any value other than "m" or  "w" is entered | Tested the feature by entering multiple invalid values on Chapter 4a| The feature behaved as expected, and displayed error message | Test concluded and passed | ![screenshot](documentation/features/feature-chapter-4a-decision.png) | ![screenshot](documentation/features/feature-chapter-4a-invalid.png) |
| Chapter 5a | | | | | | | |
| | Chapter 5a is expected to take the player to the Champion's Spirit boss if they enter "a" | Tested the feature by entering "a" on chapter 5a | The feature behaved as expected, and took player to Champion's Spirit boss | Test concluded and passed | ![screenshot](documentation/features/feature-chapter-5a-decision.png) | ![screenshot](documentation/features/feature-boss-1.png) |
| | Chapter 5a is expected to take the player to the Protector of Knowledge boss if they enter "l" | Tested the feature by entering "l" on chapter 5a | The feature behaved as expected, and took player to Protector of Knowledge boss | Test concluded and passed | ![screenshot](documentation/features/feature-chapter-5a-decision.png) | ![screenshot](documentation/features/feature-boss-2.png) |
| | Chapter 5a is expected to take the player to the Hoarder Dragon boss if they enter "t" | Tested the feature by entering "t" on chapter 5a | The feature behaved as expected, and took player to Hoarder Dragon boss | Test concluded and passed | ![screenshot](documentation/features/feature-chapter-5a-decision.png) | ![screenshot](documentation/features/feature-boss-3.png) |
| | Chapter 5a is expected to display invalid input message when any value other than "a", "l" or  "t" is entered | Tested the feature by entering multiple invalid values on Chapter 5a| The feature behaved as expected, and displayed error message | Test concluded and passed | ![screenshot](documentation/features/feature-chapter-5a-decision.png) | ![screenshot](documentation/features/feature-chapter-5a-invalid.png) |
| Item Choice | | | | | | | |
| | Whenever the player is presented with an item choice, outside of combat, it is expected to replace the player's current item with the new item when the player enters "y" | Tested the feature by entering "y" on each of the item choices outside of combat | The feature behaved as expected, and replaced the player's current item with the new item | Test concluded and passed | ![screenshot](documentation/features/feature-item-choice-y.png) | ![screenshot](documentation/features/feature-item-choice-y-inventory.png) |
| | Whenever the player is presented with an item choice, outside of combat, it is expected to ignore the item, and the player's current item will remain the same if the player enters "n" | Tested the feature by entering "n" on each of the item choices outside of combat | The feature behaved as expected, and ignored the item, while keeping the current held item| Test concluded and passed | ![screenshot](documentation/features/feature-item-choice-n.png) | ![screenshot](documentation/features/feature-item-choice-n-inventory.png) |
| | Whenever the player is presented with an item choice, outside of combat, it is expected to display invalid input message when any value other than "y" or  "n" is entered | Tested the feature by entering multiple invalid values on each item choice| The feature behaved as expected, and displayed error message | Test concluded and passed | ![screenshot](documentation/features/feature-item-choice.png) | ![screenshot](documentation/features/feature-item-choice-invalid.png) |
| Cambat | | | | | | | |
| | During combat, entering "l" is expected to perform a light attack, showing the damage output or "attack missed" message for the enemy & the player (random chance) | Tested the feature by entering "l" multiple times during combat | The feature behaved as expected, displayed damage output or "attack missed" message | Test concluded and passed | ![screenshot](documentation/features/feature-combat.png) | ![screenshot](documentation/features/feature-combat-light-attack.png) | ![screenshot](documentation/features/feature-combat-missed-light-attack.png) |
| | During combat, entering "h" is expected to perform a heavy attack, showing the damage output or "attack missed" message for the enemy & the player (random chance) | Tested the feature by entering "h" multiple times during combat | The feature behaved as expected, displayed damage output or "attack missed" message | Test concluded and passed | ![screenshot](documentation/features/feature-combat.png) | ![screenshot](documentation/features/feature-combat-heavy-attack.png) | ![screenshot](documentation/features/feature-combat-missed-heavy-attack.png) |
| | During combat, entering "i" is expected to display the current held item's description, or display "You don't currently have an item!" message if the player doesn't have an item | Tested the feature by entering "i" with and without an item during combat | The feature behaved as expected, displayed the corrisponding message | Test concluded and passed | ![screenshot](documentation/features/feature-combat.png) | ![screenshot](documentation/features/feature-combat-noitem.png) | ![screenshot](documentation/features/feature-combat-item.png) |
| | During combat, entering "i" is expected to display the current held item's description, or display "You don't currently have an item!" message if the player doesn't have an item | Tested the feature by entering "i" with and without an item during combat | The feature behaved as expected, displayed the corrisponding message | Test concluded and passed | ![screenshot](documentation/features/feature-combat.png) | ![screenshot](documentation/features/feature-combat-noitem.png) | ![screenshot](documentation/features/feature-combat-item.png) |



| | Whenever the player is presented with an item choice, outside of combat, it is expected to display invalid input message when any value other than "y" or  "n" is entered | Tested the feature by entering multiple invalid values on each item choice| The feature behaved as expected, and displayed error message | Test concluded and passed | ![screenshot](documentation/features/feature-item-choice.png) | ![screenshot](documentation/features/feature-item-choice-invalid.png) |





| About | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature03.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature04.png) |
| Gallery | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature05.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature06.png) |
| Contact | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature07.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature08.png) |
| repeat for all remaining pages | x | x | x | x | x |

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Another way of performing defensive testing is a simple Pass/Fail for each test.
The assessors prefer the above method, with the full test explained, but this is also acceptable in most cases.

When in doubt, use the above method instead, and delete the table below.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Gallery | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| Contact | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |
| repeat for all remaining pages | x | x | x | x |

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Repeat for all other tests, as applicable to your own site.
The aforementioned tests are just an example of a few different project scenarios.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

This section is primarily used for JavaScript and Python applications,
but feel free to use this section to document any HTML/CSS bugs you might run into.

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bugs/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

## Unfixed Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/bugs/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/bugs/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

> [!NOTE]  
> There are no remaining bugs that I am aware of.
