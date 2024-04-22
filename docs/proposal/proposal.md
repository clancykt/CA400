# School of Computing &mdash; Year 4 Project Proposal Form

## SECTION A

|                     |                                      |
|---------------------|--------------------------------------|
|Project Title:       | Loqui:Voice Powered Python Assistant |
|Student 1 Name:      | Katie Clancy                         |
|Student 1 ID:        | 19452724                             |
|Student 2 Name:      | Niall Egan                           |
|Student 2 ID:        | 19378906                             |
|Project Supervisor:  | Michael Scriney                      |

## SECTION B

### Introduction

Loqui will be a speech-to-text desktop application for programming with Python.

### Outline

We will aim to create a desktop application that implements speech recognition, giving the user the ability to give speech as input when programming rather than typing. We will use basic Python concepts to demonstrate our workings, so the user should be able to put together a basic Python script by speaking into an input device when complete.

### Background

We took advice & suggestions from several lecturers and formulated this idea with the help of prof. Michael Scriney having noticed a gap in the area of acessibility to programming on the fly.

### Achievements

- Creation of a user-friendly desktop application that shows elements of a 'good UI' (learned in CA357 User Interface Design & Implementation) 
- Working implementation of Speech Recognition and 'Speech Synthesis' (speech to text)
- Cause for potential further development of the working system

### Justification

The application should be easily practicable to any kind of user, particularly beginner programmers. Created with the user in mind, it should act as an interactive approach to learning the basics of the Pythin programming language and be easily acessible and operable.

It should also be useful to teachers & lecturers in simplifying the process of showing how the language works at it's core.

### Programming language(s)

- Python
- Java
- JavaScript

### Programming tools / Tech stack
SPEECH-TO-TEXT SYSTEM:
- The Rasa Toolkit will handle capturing the suer's speech and processing it into useable text

TOOLS:
- The API will be built using FastAPI
- The endpoints will be tested with Postman

INTERFACE TOOLS:
The UI will be built with a number of tools 
- Electron -> creating desktop application
- React -> designing user Interface
- Jest -> creating UI unit tests

### Hardware

No non-standard hardware will be required for this project.

### Learning Challenges

- We will have to  use and understand a number of new technologies while working on thsi project. One of the new areas we are working with is speech-to-text systems. While Rasa will help, we will need to understand how to handle the inputs and outputs of data from these systems.

- Creating desktop apps with Electron is also new ground for us. While we have some experience with web apps, we will need to understand the unique factors of the desktop environent.

### Breakdown of work

#### Student 1

Katie:
I will be working on the Text-to-Speech and code assistance system. This will involve setting up Rasa to capture voice input from users and building a system to recognize Python coding terms from the Raza output and have it return the correct syntax template.

#### Student 2

Niall:
I will be working on the Desktop App and Api end of the project. This will involve creating a desktop app using Electron, designing a User Interface for the app and building an Api to pass data from the desktop app to the Text-to-Speech/Code Assistance system.
