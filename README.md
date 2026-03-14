

# Student Portal - Django Web Application

## Project Overview

The **Student Portal** is a lightweight web application designed to manage student records efficiently. Built using the **Django framework** and **Bootstrap 5**, it serves as a practical demonstration of dynamic web development, database-less data persistence, and responsive UI design.

---

## 1. Landing Page

The home screen welcomes users to the portal and provides a clear entry point to the core functionalities of the application.

* **Feature**: Clean, centralized call-to-action buttons for navigation.
* **Technology**: High-level Django template rendering.

---

## 2. Students Dashboard

This section displays all currently registered students in a structured, easy-to-read table format.

* **Feature**: Responsive table showing ID, Name, Course (with colored badges), and Email.
* **Actions**: Individual "View Details" buttons for every record.

---

## 3. Search Implementation

The portal includes a functional search engine to filter through the in-memory student list.

* **Feature**: Case-insensitive search by ID, Name, or Email.
* **Utility**: A "Clear" button to quickly reset filters and return to the full list.

---

## 4. Student Registration

A dedicated form allows for the seamless addition of new student records to the system.

* **Feature**: User-friendly form with placeholder guidance.
* **Validation**: Captures Full Name, Course, and Email Address before saving to the in-memory list.

---

## 5. Technical About Page

This section provides an "under-the-hood" look at the project's architecture and the technologies utilized.

* **Core Technical Features**:
* **In-Memory Storage**: Data persists in global Python lists while the server is running.
* **Bootstrap 5 UI**: Modern interface utilizing the latest Bootstrap components.
* **Template Inheritance**: DRY architecture for a maintainable codebase.



---

## Technical Stack

* **Backend**: Python / Django
* **Frontend**: HTML5, CSS3, Bootstrap 5
* **Architecture**: MVT (Model-View-Template)

*Developed as a technical demonstration during the Internship Evaluation Phase at Bajaj Institute of Technology.*

