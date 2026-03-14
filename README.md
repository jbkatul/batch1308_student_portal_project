To ensure your images render correctly on platforms like GitHub while maintaining the specific file path you provided, I have recreated the **README.md** using encoded paths.

Since your local path (`G:\Pictures\Screenshots\`) is on your personal drive, it will only render for you locally. If you plan to share this project, it is highly recommended to move these images into a folder named `screenshots` inside your project directory.

---

# Student Portal - Django Web Application

## Project Overview

The **Student Portal** is a lightweight web application designed to manage student records efficiently. Built using the **Django framework** and **Bootstrap 5**, it serves as a practical demonstration of dynamic web development, database-less data persistence, and responsive UI design.

---

## 1. Landing Page

The home screen welcomes users to the portal and provides a clear entry point to the core functionalities of the application.

<img src="file:///G:/Pictures/Screenshots/Screenshot%20(141).png" alt="Home Page" width="100%">

* **Feature**: Clean, centralized call-to-action buttons for navigation.
* **Technology**: High-level Django template rendering.

---

## 2. Students Dashboard

This section displays all currently registered students in a structured, easy-to-read table format.

<img src="file:///G:/Pictures/Screenshots/Screenshot%20(139).png" alt="Students List" width="100%">

* **Feature**: Responsive table showing ID, Name, Course (with colored badges), and Email.
* **Actions**: Individual "View Details" buttons for every record.

---

## 3. Search Implementation

The portal includes a functional search engine to filter through the in-memory student list.

<img src="file:///G:/Pictures/Screenshots/Screenshot%20(144).png" alt="Search Results" width="100%">

* **Feature**: Case-insensitive search by ID, Name, or Email.
* **Utility**: A "Clear" button to quickly reset filters and return to the full list.

---

## 4. Student Registration

A dedicated form allows for the seamless addition of new student records to the system.

<img src="file:///G:/Pictures/Screenshots/Screenshot%20(140).png" alt="Add New Student" width="100%">

* **Feature**: User-friendly form with placeholder guidance.
* **Validation**: Captures Full Name, Course, and Email Address before saving to the in-memory list.

---

## 5. Technical About Page

This section provides an "under-the-hood" look at the project's architecture and the technologies utilized.

<img src="file:///G:/Pictures/Screenshots/Screenshot%20(142).png" alt="About Overview" width="100%">
<img src="file:///G:/Pictures/Screenshots/Screenshot%20(143).png" alt="Core Features" width="100%">

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

---

**Important Note for Rendering:** If you are viewing this on a web browser or GitHub, the images may not appear because they point to a local `G:` drive. To fix this permanently for others to see, place the images in your project folder and change the path to:
`src="screenshots/Screenshot%20(139).png"`

Would you like me to show you how to write the **Installation Guide** so you can share this project with your mentors?
