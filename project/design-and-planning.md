## Design and Planning Document

Project Name<br />
Design and Planning Document <br />
??/??/??, <br />
Version major.minor<br />

**Instructions**<br />
This is a design and planning document template for SWPP. Please fill out this template carefully.  

This will be a living document. For the first sprint you will fill in the document with the design details as you can see them before the first sprint. In subsequent sprints you will expand this document.

You have to use Github wiki for this document.

**Submission**<br />
You must send an email to swpp-staff@spl.snu.ac.kr with a PDF version of your document by the deadline.

You must send the email by the deadline in the class calendar. This is a HARD deadline.

**Document Revision History**<br />
Your first version of this document is version 1.0. After that minor changes increment the minor version number (e.g., 1.1, 1.2, …) and major changes increment the major version number and set the minor number to zero (e.g., 2.0, 3.0, …). We will follow this convention with other documents as well.

            Rev. 1.0 YYYY-MM-DD - initial version

**System Architecture**<br />
Here you should describe the **high-level architecture** of your system: the major pieces and how they fit together. Use graphical notations as much as possible in preference to English sentences. For example, you could describe the architecture using UML, if your system lends itself to these descriptions. Try to use standard architectural elements (e.g., pipe-and-filter, client-server, event-based, model-view-controller). Make sure to describe the major interfaces between components, which you will describe in more detail in the "Design details" section below.

**Design Details**<br />
In this section go those important facets that are not at the level of “architecture,” such as descriptions of critical algorithms, protocols, and key invariants. Also, wherever possible items should be linked back to your specification. Ideally, you can match up everything in the specification with where it is implemented in the design.

We expect that once this document is completed you will split into subteams to implement the various major components. To be ready for such a split, you need to have a precise idea of how the components are interacting, and how you are going to start implementing them. A complete class-level design might not be always possible so early, but you need to specify at least the API among the major components. Use UML when appropriate.

If there are messages sent between clients and servers, you should identify **what messages and what data they contain, and in what format, and in what order they should be sent.**

We expect to see a more refined design for the features to be included in the current sprint, and perhaps a more rough design for the features to be implemented in future sprints.  

If you have considered alternative designs, please describe briefly your reasons for choosing the final design.

**Implementation Plan**<br />
Break down each user story described in your requirements document into programming tasks. Determine the difficulty of each task, and try to estimate the number of developer-days that the tasks should take. Try to also determine dependencies among tasks. Then, you should list all of the tasks to be done in the current sprint, a preliminary assignment of tasks to people in the group, estimates of the time for each task, dependencies between tasks, and a preliminary division into sprints (e.g., which features are implemented in the first sprint, second sprint, and so on). The plan should be designed to get some prototype system running as quickly as possible and then growing towards to the full project over a sequence of sprints. Please pay extra attention to the dependency relationships between tasks; you will almost certainly run into the situation where one bit isn't done but everything else is waiting for it. In that case, you want to know exactly where resources need to go, and how urgent each bit is (hint: NOT proportional to its size or importance in the whole system).

Try to identify the major risks for the project in general and the plan in particular. Explain what the risks are and discuss how you plan to mitigate them.

**Testing Plan**<br />
In this section goes a brief description of how you plan to test the system. Thought should be given to how mostly automatic testing can be carried out, so as to maximize the limited number of human hours you will have for testing your system. The effort you put early on on automated testing will pay off when you have to ensure that you are not breaking existing functionality in future sprints.
Consider the following kinds of testing:

- **Unit testing**: explain for what modules you plan to write unit tests, and what framework you plan to use.<br />
- **Functional testing**: What APIs you plan to test? How will you test them? What tools you will use? Will you write mocks?<br />
- **Acceptance & integration testing**: how do you plan to test the user interface and scenarios?<br />

**Registering Issues**<br />
You have to register Github issues regarding tasks for design, implementation, and testing and mark them with milestones.

**Design and planning document grading guidelines**<br />
These are the grading guidelines that staff will use to evaluate your document.

| Max points  | Design |
|-------------|--------|
| 8 | Are all parts of the document in agreement with the product requirements? |
| 10 | Is the architecture of the system described, with the major components and their interfaces? |
| 10 | Are all the external interfaces to the system specified in detail? |
| 10 | Are the major internal interfaces (e.g., client-server) specified in detail? |
| 8 | Is there sufficient detail in the design to start Iteration 1? |
| 4 | Is there reasonable detail in the design for features in future iterations? |
| | **Planning** |
| 8 | Is the plan for Iteration 1 sufficiently complete to start the implementation ? |
| 4 | Are the subteams identified and has enough thought been given to parallelization of effort and team dependencies? |
| 4 | Is there a discussion of the risks associated with this plan?  |
| 4 | Are the testing activities scheduled at the appropriate times? |
| | **Testing** |
| 5 | Does the design take into account testability of the various units, components, and subsystems ? |
| 4 | Is there a discussion of how unit testing will be done? |
| 6 | Is there a discussion of how functional (API) testing will be done automatically? |
| 4 | Is there a discussion of how acceptance/integration testing will be done? |
| | **Clarity** |
| 4 | Is the solution at a fairly consistent and appropriate level of detail? |
| 4 | Is the solution clear enough to be turned over to an independent group for implementation and still be understood? |
| 5 | Is the document making good use of semi-formal notation (UML, diagrams, etc) |
| 4 | Is the document identifying common architectural or design patterns, where appropriate? |
| 4 | Is the document carefully written, without typos and grammatical errors? | 
