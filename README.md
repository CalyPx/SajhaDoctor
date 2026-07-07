# 🏥 SajhaDoctor (साझा डाक्टर) — Telehealth Platform

<div align="center">
  <img src="Frontend/public/logo.png" alt="SajhaDoctor Logo" width="220"/>
  <p><strong>Connecting Patients and Doctors Across Nepal — Anytime, Anywhere.</strong></p>
  
  [![React Version](https://img.shields.io/badge/React-v19.1.0-blue?style=flat-square&logo=react)](https://react.dev/)
  [![Vite Version](https://img.shields.io/badge/Vite-v7.0.4-646CFF?style=flat-square&logo=vite)](https://vite.dev/)
  [![Firebase](https://img.shields.io/badge/Firebase-v12.12.0-FFCA28?style=flat-square&logo=firebase&logoColor=black)](https://firebase.google.com/)
  [![TailwindCSS](https://img.shields.io/badge/TailwindCSS-v4.1.11-38B2AC?style=flat-square&logo=tailwindcss)](https://tailwindcss.com/)
  [![NMC Verified](https://img.shields.io/badge/NMC_Doctors-Verified-green?style=flat-square)](https://www.nmc.org.np/)
</div>

---

## 🌟 Introduction & Project Vision

**SajhaDoctor (साझा डाक्टर)** is a state-of-the-art, bilingual (English & Nepali) telehealth web application built to bridge the healthcare accessibility gap in Nepal. 

### The Core Problem in Nepal
In Nepal, medical resources and NMC-certified specialist doctors are heavily concentrated in Kathmandu and other major cities. Citizens in rural and mountainous areas often have to walk 4+ hours or travel days just for minor medical checkups and consultations. 

### The SajhaDoctor Solution
SajhaDoctor offers an affordable, immediate, and high-quality remote solution. Through secure video consultations, patient-doctor matching, health record vaults, and digital prescriptions, families across Nepal can receive expert medical advice from the comfort of their homes.

---

## 🚀 Key Features

### 👤 Patient Portal
* **Verified Doctor Directory:** Browse and filter NMC-certified medical specialists across categories like Cardiology, Dermatology, Pediatrics, Orthopedics, and General Medicine.
* **Instant Consultations & Appointments:** Schedule virtual appointments at convenient slots with transparent consultation fees.
* **Digital Medical Vault:** Access personal health records, upload vitals, and view past medical history securely.
* **Prescription Tracker:** Receive and download digital prescriptions issued by doctors to purchase medications directly from local pharmacies.
* **Bilingual Experience:** Seamlessly switch the entire application interface between English and Devanagari (नेपाली) with a single click.

### 🥼 Doctor Portal
* **Practitioner Dashboard:** Overview of daily/weekly schedules, pending appointments, and patient queues.
* **E-Prescription System:** Write and issue digital prescriptions securely directly through the platform.
* **Patient History Records:** View history, previous diagnoses, test results, and notes uploaded by patients to provide personalized care.
* **Consultation Analytics:** Track total consultations done, earnings, and patient satisfaction ratings over time.

---

## 🛠️ Technology Stack & Architecture

SajhaDoctor is engineered with a modern, high-performance web architecture:

### Frontend
* **Core:** React 19 & Vite (for lightning-fast development builds and optimized asset bundles).
* **Routing:** React Router v7 / v8 for client-side routing.
* **Styling:** Tailwind CSS (v4) for responsive utility-first layouts, supplemented by custom components and interactive animations using Framer Motion.
* **Icons:** Lucide React.
* **Bilingual Core:** Lightweight context-based translation framework (`LanguageContext`) translating Devanagari and English locales instantly.

### Backend & Infrastructure
* **Authentication:** Firebase Authentication (for email/password registration, password resets, and session persistence).
* **Database:** Firebase Firestore (NoSQL database managing doctor specialties, user profiles, real-time appointments, and prescriptions).
* **Cloud Storage:** Firebase Storage (for patient medical records, profile images, and digital signatures).

---

## 📂 Project Structure

A clean, modular layout separates layout components, styles, utility functions, and view pages:

```bash
Frontend/
├── public/                 # Static assets, logos, doctor avatars
├── src/
│   ├── assets/             # SVG and vector files
│   ├── components/         # Reusable structural components (Landing pages, Navbars, Error boundaries, Protected routes)
│   ├── i18n/               # Language Context and translation dictionaries (EN/NE)
│   ├── pages/              # Portal pages and shells
│   │   ├── Auth/           # Firebase Auth logic, registration for patients & doctors
│   │   ├── Patient/        # Patient Dashboard pages (Find Doctor, Medical Records, Appointments)
│   │   ├── Doctor/         # Doctor Dashboard pages (Prescriptions, Patients, Appointments, Analytics)
│   │   └── DashboardShell.jsx # Integrated modular dashboard wrapper for both roles
│   ├── styles/             # Global CSS rules and custom theme utilities
│   ├── utils/              # Helper functions and hooks
│   ├── firebase.js         # Firebase client initialization
│   └── main.jsx            # Application entry point
├── package.json            # Build configs & dependencies
└── vite.config.js          # Vite build optimizations
```

---

## ⚙️ Getting Started & Local Installation

Follow these steps to set up the development environment and run SajhaDoctor on your local machine:

### Prerequisites
Make sure you have [Node.js](https://nodejs.org/) (version 18 or above) installed.

### 1. Clone the Repository
```bash
git clone https://github.com/Code4Sake/SajhaDoctor.git
cd SajhaDoctor/Frontend
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Setup Firebase Configuration
Open `src/firebase.js` and input your Firebase project credentials or customize them:
```javascript
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT_ID.firebasestorage.app",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID"
}
```

### 4. Setup Environment Variables
Create a `.env` file in the root of the `Frontend` directory if you need API backend urls:
```env
VITE_API_URL=http://localhost:8000
VITE_APP_NAME=SajhaDoctor
VITE_DEBUG_MODE=true
```

### 5. Run the Local Development Server
```bash
npm run dev
```
Open your browser and navigate to `http://localhost:5173` to view the running app.

---

## 🎨 UI Showcase

<div align="center">
  <table border="0">
    <tr>
      <td>
        <img src="Frontend/public/doctor-1.png" width="260" alt="Specialist Doctor Card"/>
      </td>
      <td>
        <img src="Frontend/public/doctor-2.png" width="260" alt="Consultation Portal"/>
      </td>
      <td>
        <img src="Frontend/public/doctor-3.png" width="260" alt="Telehealth Interface"/>
      </td>
    </tr>
  </table>
</div>

---

## 🤝 Contributing
Contributions to SajhaDoctor are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

---

## 📄 License
This project is licensed under the MIT License.

---

<div align="center">
  <p><i>"हाम्रो लक्ष्य: हरेक नेपालीका लागि सुलभ र गुणस्तरीय स्वास्थ्य सेवा।" (Our goal: Accessible and quality healthcare for every Nepali.)</i></p>
</div>
