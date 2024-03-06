# Documentation Style Guide for Foundry 2.0

## Concepts

- **HOWTOs**: Short guides focusing on specific tasks within the Via Foundry Platform. They provide step-by-step instructions to help users accomplish a particular task or solve a specific problem.
- **Training Modules**: These are comprehensive learning resources designed to provide hands-on experience with the platform's features. A series of example problems challenge users, building upon their existing knowledge and skills.
- **Courses**: Structured educational programs that cover broader topics related to the Via Foundry Platform. Courses are designed to impart in-depth knowledge and skills, often comprising multiple Training Modules and HOWTOs.

## UI Styling Guidelines

- Maintain consistency with Via Foundry 1.0's interface to ensure a seamless user transition to Foundry 2.0.
- Use accessible color schemes and fonts, ensuring readability and usability for all users, including those with visual impairments.
- Incorporate responsive design principles to ensure the UI is functional and aesthetically pleasing across different devices and screen sizes.

## Playwright Tests for Documentation Images

- Tag tests with the specific page or link in the documentation to facilitate easy reference and updates.
- Implement `toHaveScreenshot` test assertions to ensure visual consistency and functionality of UI elements across updates. Code examples should demonstrate how to capture and compare screenshots of specific UI components or workflows within the documentation.

```javascript
// Example of a Playwright test for documentation screenshots
test('homepage has expected UI elements', async ({ page }) => {
  await page.goto('/homepage');
  expect(await page.screenshot()).toHaveScreenshot('homepage.png');
});
```

## Inclusive Language

- Avoid using ableist language that could unintentionally marginalize or exclude individuals based on physical abilities or mental health. For example, instead of terms like "crazy" or "insane" to describe unexpected behavior in code, use "unexpected", "unusual", or "surprising".

## Definitions of Done (D.O.D)

When working on Courses, Training Modules, and HOWTOs they are the general guidelines for completing a task

### HOWTOs

HOWTOs are short (~0-15m) bite sized videos + instructional for how to accomplish basic tasks on the Via Foundry platform. Users are expected to rely heavily on these instructionals as they onboard onto the platform. 

Courses and Training Modules can be supported by HOWTOs

#### Common Definition of Done for HOWTOs
- [ ] Create short video [edit down to relevant steps]
- [ ] Generate step-by-step documentation
- [ ] Compile docs and embed video in documentation under “HOWTOs“
- [ ] Naming, “How to {how-to-name}”
- [ ] Review documentation and video for correctness

### Training Modules

Module are moderate length (~30-1hr) length collections of videos and documentation focused on establishing Best Practices on the Via Foundry 2.0 platform. Users are expected to seek out this documentation as they create their own pipelines on the platform.

Courses can be supported by Training Modules

#### Common Definition of Done [Needs to be refined]

- [ ] Defined learning goals for training module
- [ ] Related HOWTOs are previewed in content
- [ ] Naming, “Training: {module-name}”

### Courses

#### Common Definition of Done [Needs to be refined]

- [ ] Defined learning goals for Course
- [ ] Training Modules: A set of example problems is created, offering hands-on experience with advanced features of the Via Foundry Platform. These should be designed to challenge and build upon the users' existing knowledge.
- [ ] Syllabus: A detailed syllabus is available, outlining the objectives, learning outcomes, module summaries, and prerequisites, ensuring attendees know what to expect and what they will learn.
- [ ] Slides: A comprehensive slide deck is prepared for Internal Bioinformaticians, providing them with a resource to adapt and use for presenting the course to other users. Slides should include theoretical concepts, practical examples, and notes for presenters.
- [ ] Documentation Update: Update Via Foundry documentation website is updated to include the new training modules and self-guided courses, making these resources easily accessible to users. s

## Future Developments

- Explore the integration of Playwright tests into an automated system for generating video documentation. This system would capture key workflows within the platform, automatically generating up-to-date video HOWTOs.
- Incorporate text scripts and synthesized voice narration to these videos, ensuring they are accessible and informative. This approach leverages the existing test infrastructure to streamline the creation and maintenance of dynamic, engaging educational content.

# Incorporating Google Documentation Style Highlights

- Ensure clarity and conciseness in all documentation, avoiding jargon and technical language when possible.
- Use active voice to engage the reader and make the content more direct and easier to understand.
- Provide clear examples and practical scenarios to illustrate concepts and procedures, enhancing the learning experience for users.
