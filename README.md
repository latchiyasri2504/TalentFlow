# TalentFlow
### AI-Powered Resume Parser & Multi-Channel 2FA Onboarding Pipeline

## Project Overview

TalentFlow is an automated student onboarding backend application designed to simplify the registration process through intelligent resume parsing and secure multi-factor authentication.

The system allows students to upload resumes, extract relevant personal information, register their accounts, and proceed through an OTP-based verification workflow.

## Key Features

- **Resume Upload:** Supports PDF and DOCX file formats.
- **Resume Parsing:** Extracts email addresses, phone numbers, skills, and text from uploaded resumes.
- **User Registration:** Collects and manages student registration details.
- **Secure Password Management:** Protects passwords using Argon2 hashing.
- **OTP Verification:** Supports OTP generation, hashed storage, and expiry validation.
- **JWT Authentication:** Provides token generation for authenticated access.
- **Database Integration:** Stores user, resume, and OTP information using PostgreSQL.
- **Profile Management:** Provides profile retrieval and update API endpoints.
- **Student Dashboard:** Includes a backend dashboard endpoint.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API development |
| PostgreSQL | Database management |
| SQLAlchemy | Database ORM |
| PDFPlumber | PDF text extraction |
| Python-DOCX | DOCX processing |
| Argon2 | Password hashing |
| PyJWT | Token authentication |
| Pydantic | Data validation |
| Uvicorn | Application server |

## Project Structure

```text
TalentFlow/
│
├── app/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── main.py
│   ├── database.py
│   └── init_db.py
│
├── uploads/
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### Step 1: Clone Repository

```bash
git clone YOUR_REPOSITORY_URL
cd TalentFlow
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Configure Environment Variables

Create a `.env` file in the root directory.

```env
DATABASE_URL=postgresql+asyncpg://postgres:YOUR_PASSWORD@localhost:5432/talentflow_db
SECRET_KEY=YOUR_SECRET_KEY
```

Create the PostgreSQL database named `talentflow_db`.

### Step 6: Initialize Database

```bash
python -m app.init_db
```

### Step 7: Start the Application

```bash
python -m uvicorn app.main:app --reload
```

### Step 8: Access API Documentation

Open your browser:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/v1/resume/parse` | Upload and parse resume |
| POST | `/api/v1/auth/register` | Register student |
| POST | `/api/v1/auth/send-otp` | Generate OTP |
| POST | `/api/v1/auth/verify-2fa` | Verify OTP |
| GET | `/api/v1/profile` | Retrieve profile |
| PATCH | `/api/v1/profile` | Update profile |
| GET | `/dashboard/student` | Student dashboard |

## Security Implementation

- Argon2 password hashing.
- SHA-256 OTP hashing.
- OTP expiration validation.
- JWT token generation.
- Secure database-backed user management.

## Project Benefits

- Reduces manual student data entry.
- Simplifies resume-based onboarding.
- Supports multiple resume formats.
- Improves account security.
- Provides modular backend architecture.
- Supports future frontend integration.

## Future Enhancements

- Complete end-to-end registration testing.
- Integrate real email and WhatsApp OTP providers.
- Implement browser-based TOTP authentication.
- Improve resume data extraction.
- Complete frontend and dashboard integration.
- Deploy the application to a cloud platform.

## Conclusion

TalentFlow provides a modular backend solution for modern student onboarding. By combining resume processing, secure authentication, OTP verification, and database integration, the project establishes a foundation for an efficient and scalable EdTech onboarding platform.

