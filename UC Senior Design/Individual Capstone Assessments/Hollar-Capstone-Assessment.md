# Capstone Assessment

<!-- 
For this assignment you will write a 5-paragraph Individual Capstone Assessment.

• One paragraph introduction about what your senior design project is all about from your academic perspective.

• Two paragraphs on how your collective college experiences will guide the development of your project.

The first paragraph should focus on how the college curriculum and the second paragraph on your co-op experiences. 
Discuss the role of specific CS courses (include course numbers and titles), and your specific co-op employers (include 
company names and job titles). In these paragraphs you should discuss technical and non-technical skills, how you 
acquired them, and how you expect to apply them.

• Final two paragraphs on your motivation and preliminary project approach 
  – Discuss why you are motivated/excited to participate in the project 
  – Discuss your preliminary approach to designing a solution
  – Discuss what your expected results and accomplishments will be
  – Discuss how you will self-evaluate your contributions: how will you know when you
    are done and whether or not you have done a good job?

• Deliverable Requirement: Five total paragraphs; Minimum of 6 sentences per paragraph.
-->

## Introduction

Our capstone project aims to create a recipe parsing and storage application, using technologies such as machine
learning (ML) and optical character recognition (OCR) for parsing various sources of recipes. Sources of recipes may
include third-party websites (e.g. Bon Appetit) or handwritten recipes. OCR will enable most sources to be adequately
scanned into the application, however. Aside from parsing recipes, the project will sufficiently demonstrate our skills
in creating database-backed web applications. It will also challenge us to create an effective, user-friendly interface
for exploring recipes. Academically, this project will be a challenging demonstration of various computer science topics
in a (relatively) complete, marketable product.

## Experiences

This project capitalizes on knowledge gained during the University of Cincinnati's Computer Science
curriculum, including but not limited to:

1. Machine Learning (Deep Learning - CS 5173)
2. Information Retrieval (CS 5154)
3. Relational Database fundamentals (CS 5151)
4. User Interfaces

This project aims to demonstrate a breadth of computer science topics rolled into one (marketable!) product. The topics
listed above are key fields in many enterprises; one must not look far to see multi-billion (indeed, trillion) dollar
companies heavily invest in machine learning and information retrieval techniques. The project will also employ
knowledge acquired in more rudimentary CS topics from UC for its implementation details -- topics such as
Data Structures, Algorithms, and Python programming, among others, are likely to be of great use.

The project will also capitalize on cooperative education experiences the team has had. For myself, I've worked 5 co-op
semesters at the same company -- Etegent Technologies Ltd. -- and continued work on a part-time basis between co-op
semesters. The company focuses on data science -- the corporate slogan is "Revealing that which is hidden" -- and my
projects there lend me confidence in my ability to parse and analyze various data sources. Specifically, I've been
involved heavily in creating algorithms for loading numerous geospatial data sources, creating user-interface designs to
aid intepreting said data, and supporting the development of a relational database to manage users and their workspaces.
Aside from those technical skills, my work experience has also enabled me to efficiently perform quality assurance,
including the development of unit tests. My work experience also improved various soft-skills, including project
management and remote collaboration.

## Motivation and Initial Approach

Our motivation was originally outlined in our project description:

> Finding, collecting, and cooking recipes can be a daunting task. There are numerous hurdles for people to effectively
> manage their recipes.
>
> ...we want to avoid instances in which we must have custom behavior for each input source. A general
> solution that works broadly is a key goal of this project.

This is a problem I've been faced with during quarantine from COVID-19 -- cooking at home became a much more prominent
part of my life. You'd never believe the number of recipe aggregation websites that make it hard to find the relevant
information about a recipe without being inundated with advertisements, popups, or long personal blogs no one wants to
read. Our goal here is to solidly improve the user experience of collecting and managing digital recipes.

Our preliminary approach will be to investigate methods of parsing websites for recipe information, ideally using
machine learning to comb through raw HTML for relevant information. We also must investigate OCR techniques, considering
implemeting our own character recognition learning model using public datasets.

Key, measurable accomplishments of this project should include:

1. A mostly accurate OCR algorithm for parsing handwritten / typed recipes; without investigating typical accuracy of
   OCR systems, it is difficult to describe "mostly accurate."
2. A mostly accurate machine learning model for scraping recipe information from _any_ website which may contain a
   recipe, completely avoiding per-website parsing strategies.
3. A user-interface capable of typical CRUD (create, read, update, delete) database operations on recipes, using the
   parsing techniques described above for the "create" and "update" tasks as needed.

Evaluating my own contributions will simply entail checking how much I've contributed to the success of our intended
accomplishments, and how much I helped my team members work towards those goals as well.
