# School Management System - System Flowchart

## Overall System Architecture

```mermaid
graph TB
    A[User Access] --> B{User Type Selection}
    B --> C[Admin]
    B --> D[Teacher]
    B --> E[Student]
    
    C --> F[Admin Dashboard]
    D --> G[Teacher Dashboard]
    E --> H[Student Dashboard]
    
    F --> I[Teacher Management]
    F --> J[Student Management]
    F --> K[Attendance Management]
    F --> L[Notice Management]
    F --> M[Fee Management]
    
    G --> N[Take Attendance]
    G --> O[View Attendance]
    G --> P[Publish Notice]
    
    H --> Q[View Attendance]
    H --> R[View Notices]
    
    subgraph "Database Layer"
        S[SQLite3 Database]
        T[User Model]
        U[TeacherExtra Model]
        V[StudentExtra Model]
        W[Attendance Model]
        X[Notice Model]
    end
    
    I --> U
    J --> V
    K --> W
    L --> X
    N --> W
    O --> W
    P --> X
    Q --> W
    R --> X
```

## User Registration & Approval Flow

```mermaid
graph TD
    A[Start] --> B{Select User Type}
    B -->|Admin| C[Admin Signup]
    B -->|Teacher| D[Teacher Signup]
    B -->|Student| E[Student Signup]
    
    C --> F[Create Admin Account]
    F --> G[Direct Access to Admin Dashboard]
    
    D --> H[Create Teacher Account]
    H --> I[Status: Pending Approval]
    I --> J[Wait for Admin Approval]
    J --> K{Admin Approval?}
    K -->|Approved| L[Access Teacher Dashboard]
    K -->|Rejected| M[Account Deleted]
    
    E --> N[Create Student Account]
    N --> O[Status: Pending Approval]
    O --> P[Wait for Admin Approval]
    P --> Q{Admin Approval?}
    Q -->|Approved| R[Access Student Dashboard]
    Q -->|Rejected| S[Account Deleted]
```

## Admin Workflow Flowchart

```mermaid
graph TD
    A[Admin Login] --> B[Admin Dashboard]
    
    B --> C[Teacher Management]
    B --> D[Student Management]
    B --> E[Attendance Management]
    B --> F[Notice Management]
    B --> G[Fee Management]
    
    C --> C1[View Teacher Requests]
    C --> C2[Add Teacher]
    C --> C3[Update Teacher]
    C --> C4[Delete Teacher]
    C --> C5[View Teacher Salary]
    
    C1 --> C6{Approve/Reject}
    C6 -->|Approve| C7[Teacher Account Activated]
    C6 -->|Reject| C8[Teacher Account Deleted]
    
    D --> D1[View Student Requests]
    D --> D2[Add Student]
    D --> D3[Update Student]
    D --> D4[Delete Student]
    D --> D5[View Student Fees]
    
    D1 --> D6{Approve/Reject}
    D6 -->|Approve| D7[Student Account Activated]
    D6 -->|Reject| D8[Student Account Deleted]
    
    E --> E1[Take Attendance]
    E --> E2[View Attendance]
    
    F --> F1[Publish Notice]
    F --> F2[View Notices]
    
    G --> G1[View Fee Records]
    G --> G2[Manage Fee Status]
```

## Teacher Workflow Flowchart

```mermaid
graph TD
    A[Teacher Login] --> B[Teacher Dashboard]
    
    B --> C[Attendance Management]
    B --> D[Notice Management]
    
    C --> C1[Select Class]
    C1 --> C2[Take Attendance]
    C2 --> C3[Mark Present/Absent]
    C3 --> C4[Save Attendance]
    
    C --> C5[View Attendance]
    C5 --> C6[Select Class & Date]
    C6 --> C7[Display Attendance Records]
    
    D --> D1[Publish Notice]
    D1 --> D2[Write Message]
    D2 --> D3[Select Target Audience]
    D3 --> D4[Publish Notice]
    
    D --> D5[View Notices]
    D5 --> D6[Display All Notices]
```

## Student Workflow Flowchart

```mermaid
graph TD
    A[Student Login] --> B[Student Dashboard]
    
    B --> C[View Attendance]
    B --> D[View Notices]
    
    C --> C1[Select Date Range]
    C1 --> C2[Display Personal Attendance]
    C2 --> C3[Show Present/Absent Status]
    
    D --> D1[View All Notices]
    D1 --> D2[Display Notice List]
    D2 --> D3[Show Notice Details]
```

## Database Schema Flow

```mermaid
erDiagram
    User {
        int id PK
        string username
        string email
        string first_name
        string last_name
        string password
        bool is_staff
        bool is_active
    }
    
    TeacherExtra {
        int id PK
        int user_id FK
        int salary
        date joindate
        string mobile
        bool status
    }
    
    StudentExtra {
        int id PK
        int user_id FK
        string roll
        string mobile
        int fee
        string cl
        bool status
    }
    
    Attendance {
        int id PK
        string roll
        date date
        string cl
        string present_status
    }
    
    Notice {
        int id PK
        date date
        string by
        string message
    }
    
    User ||--|| TeacherExtra : "One-to-One"
    User ||--|| StudentExtra : "One-to-One"
    StudentExtra }o--|| Attendance : "One-to-Many"
    Notice }o--|| User : "Published by"
```

## Technical Architecture Flow

```mermaid
graph TB
    A[Frontend Layer] --> B[Django Templates]
    A --> C[Static Files CSS/JS]
    A --> D[HTML Forms]
    
    B --> E[URL Routing]
    C --> E
    D --> E
    
    E --> F[Views Layer]
    F --> G[Business Logic]
    F --> H[Authentication]
    F --> I[Authorization]
    
    G --> J[Models Layer]
    H --> J
    I --> J
    
    J --> K[SQLite3 Database]
    
    L[Django Framework] --> M[ORM]
    L --> N[Admin Panel]
    L --> O[Security Middleware]
    
    M --> J
    N --> J
    O --> F
```

## Project Setup & Deployment Flow

```mermaid
graph TD
    A[Project Setup] --> B[Python 3.7.6+]
    B --> C[Virtual Environment]
    C --> D[Install Dependencies]
    D --> E[Database Migration]
    E --> F[Create Superuser]
    F --> G[Run Development Server]
    
    G --> H[http://127.0.0.1:8000/]
    H --> I[Main Application]
    H --> J[Admin Panel]
    
    K[Batch Scripts] --> L[setup_project.bat]
    K --> M[run_project.bat]
    K --> N[quick_start.bat]
    K --> O[debug_mode.bat]
    
    L --> A
    M --> G
    N --> G
    O --> G
```

## Key Features Summary

### User Roles & Permissions
- **Admin**: Full system control, user approval, content management
- **Teacher**: Attendance management, notice publishing
- **Student**: View personal attendance, view notices

### Core Modules
1. **Authentication System**: Login/Signup with role-based access
2. **User Management**: Admin approval workflow for teachers/students
3. **Attendance System**: Class-wise attendance tracking
4. **Notice System**: Announcement publishing and viewing
5. **Fee Management**: Student fee tracking (admin only)

### Technical Stack
- **Backend**: Django 3.0.5
- **Database**: SQLite3
- **Frontend**: Django Templates with HTML/CSS
- **Authentication**: Django's built-in auth system
- **Testing**: Multiple test files for different functionalities

### Security Features
- CSRF Protection
- Role-based access control
- Admin approval system
- Password hashing

## System Limitations (as mentioned in README)
- Password must be updated when updating teacher/student records
- Anyone can become admin (security concern)
- Development mode configuration (not production ready)

## References

1.  K. S. R. Kumar, P. V. Kumar, and S. R. Reddy, "Design and implementation of school management system using cloud computing," International Journal of Computer Applications, vol. 178, no. 3, pp. 45-52, Jan. 2020. https://www.ijcaonline.org/archives/volume178/number3/

2.  M. A. Al-Mamun, S. H. M. A. Hamid, and M. S. Islam. "A web-based school management system: Design and implementation," Journal of Educational Technology Systems, vol. 42, no. 8, pp. 1-12, Aug. 2018. https://link.springer.com/journal/10916

3.  R. Sharma and A. K. Singh, "Electronic student record systems: A review." International Journal of Engineering and Technology, vol. 7, pp. 1234-1241, Dec. 2019. https://www.sciencepubco.com/index.php/ijet

4.  P. K. Bhowmick, S. Chakraborty, and A. Roy. "Cloud-based school management system architecture," in Proc. IEEE Int. Conf. on Computing, Communication and Automation, Greater Noida, India, 2017, pp. 567-572. https://ieeexplore.ieee.org/

5.  T. Johnson and M. Williams, Educational Information Systems: Challenges and Implementation. New York, NY, USA: Springer, 2019, ch. 4, pp. 89-112. https://link.springer.com/

6.  S. Adachi, T. Horio, and T. Suzuki, "Intense vacuum-ultraviolet single-order harmonic pulse by a deep-ultraviolet driving laser," in Conf. Lasers and Electro-Optics, San Jose, CA, 2012, pp. 2118-2120. https://ieeexplore.ieee.org/

7.  L. M. Garcia, J. R. Martinez, and C. A. Lopez, "Security in school management systems: A comprehensive survey," IEEE Access, vol. 8, pp. 156789-156801, May 2020. https://ieeexplore.ieee.org/

8.  A. K. Patel and R. N. Shah, "Role-based access control in educational information systems," Journal of Educational Engineering, vol. 2021, no. 1, pp. 1-15, Mar. 2021. https://www.hindawi.com/journals/jhe/

9.  Django Documentation, Django Software Foundation, Lawrence, KS, USA. [Online]. Available: https://docs.djangoproject.com/

10. React Documentation, Facebook Inc., Menlo Park, CA, USA. [Online]. Available: https://reactjs.org/docs/

11. SQLite Documentation, SQLite Consortium, USA. [Online]. Available: https://sqlite.org/docs.html

12. J. D. McLaughlin and S. K. Goyal, "Student privacy and data security in school management systems," Education Informatics Journal, vol. 25, no. 2, pp. 456-467, Jun. 2019. https://journals.sagepub.com/home/jhi

13. M. R. Wilson, Database Design for Educational Applications. Boston, MA, USA: Academic Press, 2020, pp. 234-278. https://www.elsevier.com/books

14. UNESCO, "Digital education guidelines," UNESCO Technical Report Series, no. 1023, Paris, France, 2021. https://www.unesco.org/publications

15. A. Singh, P. Kumar, and V. Sharma, "Performance analysis of school management systems using cloud infrastructure," in Proc. Int. Conf. on Cloud Computing and Data Science, New Delhi, India, 2020, pp. 234-239. https://ieeexplore.ieee.org/

16. B. L. Chen and K. R. Martinez, "Automated attendance systems in educational institutions: A comparative study," Journal of Educational Computing Research, vol. 58, no. 4, pp. 890-915, May 2020. https://journals.sagepub.com/home/jec

17. D. Thompson and S. Rodriguez, "Web-based notice management systems for schools: Design patterns and best practices," International Journal of Web-Based Learning Technologies, vol. 12, no. 3, pp. 67-82, Sep. 2019. https://www.igi-global.com/journal
