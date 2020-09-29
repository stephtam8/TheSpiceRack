# Tasks

In this document, an overview of essential tasks -- broken down by subject matter / segment of project -- is enumerated
and assigned to contributors.

## Core Functionality (Server / Backend)

1. Investigate methods of parsing websites for specific data, targeting machine-learning driven approaches.
2. Investigate optical character recognition (OCR) techniques and implementations.
3. Design `Recipe` model -- what information could a recipe include? What must it include?
4. Identify programming language, frameworks (if any), etc. to implement server.
5. Develop relational database to store `Recipe` objects. For proof-of-concept, target `SQLite`.
6. Research and prototype parsing strategies identified in (1) in language of choice from (4).
7. Research and prototype OCR parsing functionality investigated in (2).
8. Develop REST API to pass data between server and client application(s).
9. Develop user-management functionality (authentication, per-user data storage, etc.).

## Client Application -- Web

1. Define web-development framework to create the application.
2. Define CSS and other design principles.
3. Create "user-management" page(s) for signing up, logging in, managing user information.
4. Create "home" webpage.
5. Create "recipe viewer" webpage.
6. Create form to upload recipe source to be parsed and stored.
7. Create page(s) to manually create, edit, and delete recipes.

## Stretch Goals

1. Create native mobile application(s) for iOS and/or Android devices. Functionality will mirror and expand upon web
   application.
2. Develop meal-planning functionality.
3. Develop grocery list functionality.
