# Module 4 Project — Part 2: Study Tracker API Design

**Your Name:** Nicco Gonzalez
**Date:** 06-28-2026

---

## The App: Study Tracker

Design a REST API for a "Study Tracker" app. Students can:
- Log study sessions (course, duration, notes)
- Set study goals (target hours per course per week)
- View their progress and summaries

---

## Section 1 — Resources

List the resources your API will manage. Suggested: Students, Courses, Study Sessions, Goals.

| Resource       | Key Attributes |
|----------------|----------------|
| Students       | student_id, name, email |
| Courses        | course_id, course_name, department |
| Study Sessions | session_id, student_id, course_id, duration, notes, created_at |
| Goals          | goal_id, student_id, course_id, target_hours, week_start |


---

## Section 2 — Relationships

Describe how your resources relate to each other:

- Student ↔ Course:  Many-to-many (students enroll in multiple courses)
- Student ↔ Study Session: One-to-many (a student can log many sessions)
- Course ↔ Study Session: One-to-many (each session belongs to one course)
- Student ↔ Goal: One-to-many (each student can set multiple goals per course/week)


---

## Section 3 — Endpoints

Design at least:
- Full CRUD for study_sessions (5 endpoints)
- 3+ endpoints for related resources
- 1+ filtering endpoint

| Method | URI                     | Description                  | Auth Required? |
|--------|-------------------------|------------------------------|----------------|
| GET    | /students               | List all students            | Yes            |
| GET    | /students/{id}          | Get single student           | Yes            |
| POST   | /students               | Create new student           | Yes            |
| PUT    | /students/{id}          | Update student               | Yes            |
| DELETE | /students/{id}          | Delete student               | Yes            |
| GET    | /study_sessions         | Get all study sessions       | Yes            |
| POST   | /study_sessions         | Create a study session       | Yes            |
| PUT    | /study_sessions/{id}    | Update session               | Yes            |
| DELETE | /study_sessions/{id}    | Delete session               | Yes            |
| GET    | /students/{id}/progress | Get progress summary         | Yes            |
| GET    | /courses?department=CS  | Filter courses by department | Yes            |

---

## Section 4 — Request/Response Schemas

### POST /study_sessions — Create a new session

**Request body:**
```json
{
  "student_id": 1,
  "course_id": 101,
  "duration_minutes": 90,
  "notes": "Reviewed REST API concepts and practiced endpoints"
}

```

**Success response (201):**
```json
{
  "session_id": 501,
  "student_id": 1,
  "course_id": 101,
  "duration_minutes": 90,
  "notes": "Reviewed REST API concepts and practiced endpoints",
  "created_at": "2026-06-28T12:00:00Z"
}

```

### GET /students/{id}/progress

**Response (200):**
```json
{
  "student_id": 1,
  "total_hours_this_week": 12.5,
  "goals": [
    {
      "course_id": 101,
      "target_hours": 10,
      "completed_hours": 8.5
    }
  ],
  "completion_percentage": 83
}
```

---

## Section 5 — Authentication

| Endpoint                   | Auth Required | Notes                  |
|----------------------------|---------------|------------------------|
|GET /courses	             |     Yes 	     | View available courses |
|POST /study_sessions	     |     Yes 	     | Must be logged in      |
|GET /students/{id}/progress |	   Yes	     | Private student data   |
|DELETE /study_sessions/{id} |	   Yes	     | Only owner can delete  |

**Auth method and rationale:**
> Token-based authentication (e.g., JWT) would be used to ensure only logged-in students can create, modify, or view personal study data. This protects private academic activity and prevents unauthorized access.

---

## Section 6 — Error Responses for POST /study_sessions

| Status Code | When it occurs                                                                |
|-------------|-------------------------------------------------------------------------------|
|     201     | Study session created successfully                                            |
|     400     | Missing or invalid input data                                                 |
|     401     | User is not authenticated                                                     |
|     404     | Student or course not found                                                   |
|     422     | Valid request format but semantic validation failed (e.g., negative duration) |
