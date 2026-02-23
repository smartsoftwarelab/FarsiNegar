# FarsiNegar  
<img width="1129" height="528" alt="image" src="https://github.com/user-attachments/assets/548ad9e1-eb6e-4888-bf22-6d45637165a0" />

### A Prototype Web Application for Persian Grammar and Writing Correction Using Large Language Models  

**Supervisor:** Dr. Amir Jalali Bidgoli  
**Author:** Mahdieh Ghasemzadeh  
**Date:** February 2026  


<br><br>
## 📌 Introduction

With the rapid growth of digital text production and the increasing use of Persian in educational, research, and service systems, writing quality has become more important than ever. Grammatical errors, weak sentence structures, incorrect punctuation, and improper word usage can reduce readability and distort meaning.

FarsiNegar is a prototype web application designed to detect and correct writing and grammatical issues in Persian texts using Large Language Models (LLMs). The system analyzes user-submitted text and provides correction suggestions to improve clarity and correctness.

The main goal of this project is to gain practical experience in applying Large Language Models to Natural Language Processing (NLP) tasks and implementing them within a functional web-based system.


<br><br>
## 🎯 Problem Statement

Although Persian is widely used in digital environments, it still lacks powerful and accessible intelligent grammar-checking tools compared to some other languages.

Users often face:

- Grammatical errors  
- Weak sentence structures  
- Incorrect punctuation  
- Redundant expressions  
- Spelling mistakes  

Manual proofreading is time-consuming, and existing tools are often limited in accuracy.

This project aims to design and implement a system capable of automatically identifying writing issues in Persian text and providing meaningful correction suggestions using modern NLP techniques.


<br><br>
## 🚀 Project Overview

FarsiNegar is a web-based prototype application that allows users to submit Persian text and receive corrected output along with writing suggestions.

The system provides two editing modes:

### 1️⃣ Quick Edit Mode
- The user submits text.
- The system automatically returns a fully corrected version.

### 2️⃣ Interactive Edit Mode
- The system highlights individual grammatical, spelling, and structural issues.
- The user reviews each suggestion and chooses whether to apply corrections manually.

This dual-mode design allows users to choose between speed and control depending on their editing needs.


<br><br>
## 🏗️ System Architecture

The application follows a client-server architecture.

### 🔹Front-End
- HTML  
- CSS  
- JavaScript  
- TailwindCSS  

Responsibilities:
- Receiving user input  
- Displaying corrected text  
- Presenting suggestions  

### 🔹Back-End
- Django Framework  

Responsibilities:
- Text processing  
- Communication with the language model API  
- Generating correction suggestions  

### 🔹Communication
- REST API endpoints connect the front-end and back-end.
- This separation improves scalability, maintainability, and extensibility.

### 🔹Database
- PostgreSQL  
- Relational database design  
- Used for storing processed documents  

### 🔹Language Model
- OpenAI ChatGPT-3 API

  
<br><br>
## ✨ Implemented Features

- Persian text input and processing  
- Automatic grammar and writing correction  
- Two editing modes (Quick & Interactive)  
- Highlighted error suggestions  
- Selective correction by the user  
- Document storage and retrieval  
- Structured relational database design  

<br><br>
## 🔜 Planned Features
- User authentication (Sign up / Login)
- Improved model accuracy
- Support for different writing styles


<br><br>
## ⚠️ Limitations

- The selected language model (ChatGPT-3) has limited accuracy for Persian grammar correction compared to newer models.
- Access to more advanced model APIs was restricted.
- Performance under high user traffic has not been fully optimized.
- The system has not yet been fine-tuned on specialized Persian corpora.


<br><br>
## 🔮 Future Improvements

- Fine-tuning models on Persian datasets  
- Improved correction accuracy for specialized texts  
- Support for multiple writing styles  
- User authentication system (Sign up / Login)  
- Performance optimization for scalability  



<br><br>
## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript, TailwindCSS  
- **Backend:** Django  
- **Database:** PostgreSQL  
- **AI Model:** OpenAI ChatGPT-3 API  


<br><br>
## 📌 Project Status

Prototype version — under development.

<br><br>

<img width="1920" height="2914" alt="finaleePoster" src="https://github.com/user-attachments/assets/b92fd551-c4ef-48f6-9fc4-d624d42b14c9" />

