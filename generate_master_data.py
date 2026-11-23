import json

# 40 realistic employees across 4 teams and 3 shifts for Design Sheetmetal India operations
employees = [
    # Team Alpha (Flashings & Trims Keying) - Lead: Priya Nair
    {"id": "EMP-101", "name": "Rohan Sharma", "team": "Team Alpha (Flashings & Trims)", "shift": "Shift A", "role": "Senior Keying Specialist", "status": "Present", "checkin": "05:54 AM", "checkout": "14:26 PM", "accuracy": 99.4, "avatar": "RS", "manager": "Priya Nair", "skills": {"orderKeying": "Expert", "flashingInterp": "Expert", "bitsProcessing": "Proficient", "doubleChecking": "Proficient", "qualityReview": "Intermediate", "customerClarifications": "Intermediate", "specializedDrawings": "Expert"}, "certifications": ["Colorbond Precision Level 3", "AS 1562.1 Compliance"], "baselineOrders": 28, "baselineFlashings": 190, "baselineBits": 55},
    {"id": "EMP-102", "name": "Priya Nair", "team": "Team Alpha (Flashings & Trims)", "shift": "Shift A", "role": "Shift A Team Leader", "status": "Present", "checkin": "05:48 AM", "checkout": "--", "accuracy": 99.8, "avatar": "PN", "manager": "David Harrison", "skills": {"orderKeying": "Expert", "flashingInterp": "Expert", "bitsProcessing": "Expert", "doubleChecking": "Expert", "qualityReview": "Expert", "customerClarifications": "Expert", "specializedDrawings": "Expert"}, "certifications": ["Six Sigma Green Belt", "Victorian Sheetmetal Standards"], "baselineOrders": 15, "baselineFlashings": 110, "baselineBits": 30},
    {"id": "EMP-105", "name": "Rajesh Kumar", "team": "Team Alpha (Flashings & Trims)", "shift": "Shift A", "role": "Keying Specialist", "status": "Present", "checkin": "06:02 AM", "checkout": "--", "accuracy": 98.9, "avatar": "RK", "manager": "Priya Nair", "skills": {"orderKeying": "Proficient", "flashingInterp": "Expert", "bitsProcessing": "Proficient", "doubleChecking": "Intermediate", "qualityReview": "Intermediate", "customerClarifications": "Developing", "specializedDrawings": "Proficient"}, "certifications": ["Custom Ridge & Valley SOP"], "baselineOrders": 24, "baselineFlashings": 165, "baselineBits": 45},
    {"id": "EMP-106", "name": "Sneha Reddy", "team": "Team Alpha (Flashings & Trims)", "shift": "Shift B", "role": "Shift B Keying Lead", "status": "Present", "checkin": "13:50 PM", "checkout": "--", "accuracy": 99.1, "avatar": "SR", "manager": "David Harrison", "skills": {"orderKeying": "Expert", "flashingInterp": "Expert", "bitsProcessing": "Proficient", "doubleChecking": "Expert", "qualityReview": "Proficient", "customerClarifications": "Proficient", "specializedDrawings": "Proficient"}, "certifications": ["Afternoon Shift Dispatch Sign-off"], "baselineOrders": 26, "baselineFlashings": 175, "baselineBits": 50},
    {"id": "EMP-109", "name": "Amit Verma", "team": "Team Alpha (Flashings & Trims)", "shift": "Shift C", "role": "Night Keying Specialist", "status": "Present", "checkin": "21:50 PM", "checkout": "--", "accuracy": 98.7, "avatar": "AV", "manager": "Rahul Deshmukh", "skills": {"orderKeying": "Proficient", "flashingInterp": "Proficient", "bitsProcessing": "Intermediate", "doubleChecking": "Intermediate", "qualityReview": "Developing", "customerClarifications": "Developing", "specializedDrawings": "Proficient"}, "certifications": ["Night Shift Safety & Keying"], "baselineOrders": 22, "baselineFlashings": 155, "baselineBits": 40},
    {"id": "EMP-111", "name": "Arjun Nair", "team": "Team Alpha (Flashings & Trims)", "shift": "Shift A", "role": "Keying Specialist", "status": "Present", "checkin": "05:59 AM", "checkout": "--", "accuracy": 99.0, "avatar": "AN", "manager": "Priya Nair", "skills": {"orderKeying": "Proficient", "flashingInterp": "Proficient", "bitsProcessing": "Proficient", "doubleChecking": "Proficient", "qualityReview": "Intermediate", "customerClarifications": "Developing", "specializedDrawings": "Intermediate"}, "certifications": ["Standard Barge & Apron Master"], "baselineOrders": 26, "baselineFlashings": 180, "baselineBits": 52},
    {"id": "EMP-114", "name": "Kavita Patil", "team": "Team Alpha (Flashings & Trims)", "shift": "Shift B", "role": "Keying Specialist", "status": "Late", "checkin": "14:18 PM", "checkout": "--", "accuracy": 98.2, "avatar": "KP", "manager": "Sneha Reddy", "skills": {"orderKeying": "Intermediate", "flashingInterp": "Proficient", "bitsProcessing": "Developing", "doubleChecking": "Developing", "qualityReview": "Developing", "customerClarifications": "Developing", "specializedDrawings": "Intermediate"}, "certifications": ["Junior Keying Level 1"], "baselineOrders": 20, "baselineFlashings": 135, "baselineBits": 35},
    {"id": "EMP-116", "name": "Deepa Krishnan", "team": "Team Alpha (Flashings & Trims)", "shift": "Shift A", "role": "Senior Keying Specialist", "status": "Present", "checkin": "05:56 AM", "checkout": "--", "accuracy": 99.3, "avatar": "DK", "manager": "Priya Nair", "skills": {"orderKeying": "Expert", "flashingInterp": "Expert", "bitsProcessing": "Expert", "doubleChecking": "Proficient", "qualityReview": "Proficient", "customerClarifications": "Proficient", "specializedDrawings": "Expert"}, "certifications": ["Parapet & Box Gutter Specialist"], "baselineOrders": 25, "baselineFlashings": 172, "baselineBits": 49},
    {"id": "EMP-119", "name": "Aditya Bhat", "team": "Team Alpha (Flashings & Trims)", "shift": "Shift C", "role": "Keying Specialist", "status": "Present", "checkin": "21:55 PM", "checkout": "--", "accuracy": 98.8, "avatar": "AB", "manager": "Rahul Deshmukh", "skills": {"orderKeying": "Proficient", "flashingInterp": "Proficient", "bitsProcessing": "Proficient", "doubleChecking": "Intermediate", "qualityReview": "Intermediate", "customerClarifications": "Developing", "specializedDrawings": "Intermediate"}, "certifications": ["Colorbond Standard Profiles"], "baselineOrders": 23, "baselineFlashings": 160, "baselineBits": 44},
    {"id": "EMP-121", "name": "Suresh Nair", "team": "Team Alpha (Flashings & Trims)", "shift": "Shift B", "role": "Keying Specialist", "status": "Present", "checkin": "13:58 PM", "checkout": "--", "accuracy": 99.0, "avatar": "SN", "manager": "Sneha Reddy", "skills": {"orderKeying": "Proficient", "flashingInterp": "Proficient", "bitsProcessing": "Proficient", "doubleChecking": "Proficient", "qualityReview": "Intermediate", "customerClarifications": "Developing", "specializedDrawings": "Intermediate"}, "certifications": ["Fast-Track Dispatch Certified"], "baselineOrders": 24, "baselineFlashings": 168, "baselineBits": 46},
    {"id": "EMP-124", "name": "Swati Kulkarni", "team": "Team Alpha (Flashings & Trims)", "shift": "Shift A", "role": "Keying Specialist", "status": "Present", "checkin": "05:52 AM", "checkout": "--", "accuracy": 99.5, "avatar": "SK", "manager": "Priya Nair", "skills": {"orderKeying": "Expert", "flashingInterp": "Expert", "bitsProcessing": "Expert", "doubleChecking": "Proficient", "qualityReview": "Intermediate", "customerClarifications": "Intermediate", "specializedDrawings": "Proficient"}, "certifications": ["Expansion Joints & Box Gutters"], "baselineOrders": 27, "baselineFlashings": 188, "baselineBits": 55},

    # Team Beta (Architectural & Cladding Panels) - Lead: Pooja Gupta
    {"id": "EMP-103", "name": "Vikram Patel", "team": "Team Beta (Architectural Panels)", "shift": "Shift B", "role": "Panel Detailer", "status": "Approved Leave", "checkin": "--", "checkout": "--", "accuracy": 98.6, "avatar": "VP", "manager": "Pooja Gupta", "skills": {"orderKeying": "Proficient", "flashingInterp": "Proficient", "bitsProcessing": "Developing", "doubleChecking": "Intermediate", "qualityReview": "Intermediate", "customerClarifications": "Intermediate", "specializedDrawings": "Expert"}, "certifications": ["Standing Seam Cladding SOP"], "baselineOrders": 20, "baselineFlashings": 140, "baselineBits": 35},
    {"id": "EMP-108", "name": "Meera Joshi", "team": "Team Beta (Architectural Panels)", "shift": "Shift A", "role": "Senior Panel Detailer", "status": "Present", "checkin": "05:51 AM", "checkout": "--", "accuracy": 99.2, "avatar": "MJ", "manager": "Pooja Gupta", "skills": {"orderKeying": "Expert", "flashingInterp": "Expert", "bitsProcessing": "Intermediate", "doubleChecking": "Proficient", "qualityReview": "Proficient", "customerClarifications": "Proficient", "specializedDrawings": "Expert"}, "certifications": ["Complex Facade Systems Level 3"], "baselineOrders": 21, "baselineFlashings": 142, "baselineBits": 38},
    {"id": "EMP-110", "name": "Pooja Gupta", "team": "Team Beta (Architectural Panels)", "shift": "Shift A", "role": "Team Leader", "status": "Present", "checkin": "05:45 AM", "checkout": "--", "accuracy": 99.6, "avatar": "PG", "manager": "David Harrison", "skills": {"orderKeying": "Expert", "flashingInterp": "Expert", "bitsProcessing": "Proficient", "doubleChecking": "Expert", "qualityReview": "Expert", "customerClarifications": "Expert", "specializedDrawings": "Expert"}, "certifications": ["Architectural Metal Systems Lead"], "baselineOrders": 16, "baselineFlashings": 115, "baselineBits": 32},
    {"id": "EMP-112", "name": "Neha Iyer", "team": "Team Beta (Architectural Panels)", "shift": "Shift B", "role": "Panel Detailer", "status": "Approved Leave", "checkin": "--", "checkout": "--", "accuracy": 98.4, "avatar": "NI", "manager": "Pooja Gupta", "skills": {"orderKeying": "Intermediate", "flashingInterp": "Proficient", "bitsProcessing": "Developing", "doubleChecking": "Developing", "qualityReview": "Developing", "customerClarifications": "Developing", "specializedDrawings": "Proficient"}, "certifications": ["Corrugated & Rib Profiles"], "baselineOrders": 19, "baselineFlashings": 130, "baselineBits": 30},
    {"id": "EMP-118", "name": "Sunita Rao", "team": "Team Beta (Architectural Panels)", "shift": "Shift B", "role": "Panel Detailer", "status": "Absent", "checkin": "--", "checkout": "--", "accuracy": 97.9, "avatar": "SR", "manager": "Pooja Gupta", "skills": {"orderKeying": "Intermediate", "flashingInterp": "Intermediate", "bitsProcessing": "Developing", "doubleChecking": "Developing", "qualityReview": "Developing", "customerClarifications": "Developing", "specializedDrawings": "Proficient"}, "certifications": ["Panel Detailing Basics"], "baselineOrders": 18, "baselineFlashings": 125, "baselineBits": 28},
    {"id": "EMP-120", "name": "Divya Hegde", "team": "Team Beta (Architectural Panels)", "shift": "Shift A", "role": "Panel Detailer", "status": "Present", "checkin": "06:01 AM", "checkout": "--", "accuracy": 99.2, "avatar": "DH", "manager": "Pooja Gupta", "skills": {"orderKeying": "Proficient", "flashingInterp": "Proficient", "bitsProcessing": "Proficient", "doubleChecking": "Intermediate", "qualityReview": "Intermediate", "customerClarifications": "Intermediate", "specializedDrawings": "Proficient"}, "certifications": ["Roof Penetration Flashings"], "baselineOrders": 22, "baselineFlashings": 150, "baselineBits": 42},
    {"id": "EMP-123", "name": "Harish Pillai", "team": "Team Beta (Architectural Panels)", "shift": "Shift C", "role": "Panel Detailer", "status": "Present", "checkin": "21:49 PM", "checkout": "--", "accuracy": 98.5, "avatar": "HP", "manager": "Rahul Deshmukh", "skills": {"orderKeying": "Proficient", "flashingInterp": "Intermediate", "bitsProcessing": "Intermediate", "doubleChecking": "Intermediate", "qualityReview": "Developing", "customerClarifications": "Developing", "specializedDrawings": "Proficient"}, "certifications": ["Interlocking Panel Systems"], "baselineOrders": 20, "baselineFlashings": 138, "baselineBits": 34},
    {"id": "EMP-125", "name": "Gaurav Sen", "team": "Team Beta (Architectural Panels)", "shift": "Shift B", "role": "Panel Detailer", "status": "Present", "checkin": "13:52 PM", "checkout": "--", "accuracy": 98.9, "avatar": "GS", "manager": "Pooja Gupta", "skills": {"orderKeying": "Proficient", "flashingInterp": "Proficient", "bitsProcessing": "Intermediate", "doubleChecking": "Intermediate", "qualityReview": "Developing", "customerClarifications": "Developing", "specializedDrawings": "Proficient"}, "certifications": ["Cassette Facade Systems"], "baselineOrders": 21, "baselineFlashings": 145, "baselineBits": 36},
    {"id": "EMP-126", "name": "Bhavna Chawla", "team": "Team Beta (Architectural Panels)", "shift": "Shift A", "role": "Panel Detailer", "status": "Present", "checkin": "05:58 AM", "checkout": "--", "accuracy": 99.1, "avatar": "BC", "manager": "Pooja Gupta", "skills": {"orderKeying": "Proficient", "flashingInterp": "Proficient", "bitsProcessing": "Proficient", "doubleChecking": "Intermediate", "qualityReview": "Intermediate", "customerClarifications": "Intermediate", "specializedDrawings": "Proficient"}, "certifications": ["Architectural Capping Standards"], "baselineOrders": 22, "baselineFlashings": 148, "baselineBits": 38},

    # Team Gamma (Double-Check & Technical Audit) - Lead: Manoj Tiwari
    {"id": "EMP-104", "name": "Ananya Sen", "team": "Team Gamma (Double-Check & Audit)", "shift": "Shift A", "role": "Senior Checking Auditor", "status": "Present", "checkin": "05:58 AM", "checkout": "--", "accuracy": 99.9, "avatar": "AS", "manager": "Manoj Tiwari", "skills": {"orderKeying": "Expert", "flashingInterp": "Expert", "bitsProcessing": "Expert", "doubleChecking": "Expert", "qualityReview": "Expert", "customerClarifications": "Expert", "specializedDrawings": "Expert"}, "certifications": ["Master Drawing Auditor", "ISO 9001 Auditor"], "baselineOrders": 0, "baselineFlashings": 0, "baselineBits": 0},
    {"id": "EMP-107", "name": "Karthik Sundaram", "team": "Team Gamma (Double-Check & Audit)", "shift": "Shift B", "role": "Double-Check Specialist", "status": "Present", "checkin": "13:55 PM", "checkout": "--", "accuracy": 99.7, "avatar": "KS", "manager": "Manoj Tiwari", "skills": {"orderKeying": "Expert", "flashingInterp": "Expert", "bitsProcessing": "Proficient", "doubleChecking": "Expert", "qualityReview": "Proficient", "customerClarifications": "Proficient", "specializedDrawings": "Proficient"}, "certifications": ["Brake Press Bend Audit Certified"], "baselineOrders": 0, "baselineFlashings": 0, "baselineBits": 0},
    {"id": "EMP-113", "name": "Sanjay Menon", "team": "Team Gamma (Double-Check & Audit)", "shift": "Shift C", "role": "Double-Check Auditor", "status": "Present", "checkin": "21:52 PM", "checkout": "--", "accuracy": 99.8, "avatar": "SM", "manager": "Rahul Deshmukh", "skills": {"orderKeying": "Expert", "flashingInterp": "Expert", "bitsProcessing": "Proficient", "doubleChecking": "Expert", "qualityReview": "Proficient", "customerClarifications": "Intermediate", "specializedDrawings": "Expert"}, "certifications": ["Night Shift Sign-Off Authority"], "baselineOrders": 0, "baselineFlashings": 0, "baselineBits": 0},
    {"id": "EMP-117", "name": "Manoj Tiwari", "team": "Team Gamma (Double-Check & Audit)", "shift": "Shift A", "role": "Quality & Audit Lead", "status": "Present", "checkin": "05:40 AM", "checkout": "--", "accuracy": 100.0, "avatar": "MT", "manager": "David Harrison", "skills": {"orderKeying": "Expert", "flashingInterp": "Expert", "bitsProcessing": "Expert", "doubleChecking": "Expert", "qualityReview": "Expert", "customerClarifications": "Expert", "specializedDrawings": "Expert"}, "certifications": ["Quality Lead Auditor", "Root Cause Analysis Master"], "baselineOrders": 0, "baselineFlashings": 0, "baselineBits": 0},
    {"id": "EMP-122", "name": "Radhika Das", "team": "Team Gamma (Double-Check & Audit)", "shift": "Shift B", "role": "Double-Check Specialist", "status": "Present", "checkin": "13:52 PM", "checkout": "--", "accuracy": 99.6, "avatar": "RD", "manager": "Manoj Tiwari", "skills": {"orderKeying": "Proficient", "flashingInterp": "Expert", "bitsProcessing": "Proficient", "doubleChecking": "Expert", "qualityReview": "Proficient", "customerClarifications": "Intermediate", "specializedDrawings": "Proficient"}, "certifications": ["Australian Tolerances Spec Level 2"], "baselineOrders": 0, "baselineFlashings": 0, "baselineBits": 0},
    {"id": "EMP-127", "name": "Tarun Kapoor", "team": "Team Gamma (Double-Check & Audit)", "shift": "Shift A", "role": "Technical Auditor", "status": "Present", "checkin": "05:49 AM", "checkout": "--", "accuracy": 99.7, "avatar": "TK", "manager": "Manoj Tiwari", "skills": {"orderKeying": "Proficient", "flashingInterp": "Expert", "bitsProcessing": "Proficient", "doubleChecking": "Expert", "qualityReview": "Proficient", "customerClarifications": "Proficient", "specializedDrawings": "Proficient"}, "certifications": ["Pre-Fabrication Cladding Verification"], "baselineOrders": 0, "baselineFlashings": 0, "baselineBits": 0},
    {"id": "EMP-128", "name": "Shalini Nair", "team": "Team Gamma (Double-Check & Audit)", "shift": "Shift B", "role": "Technical Auditor", "status": "Present", "checkin": "13:54 PM", "checkout": "--", "accuracy": 99.5, "avatar": "SN", "manager": "Manoj Tiwari", "skills": {"orderKeying": "Proficient", "flashingInterp": "Proficient", "bitsProcessing": "Proficient", "doubleChecking": "Expert", "qualityReview": "Intermediate", "customerClarifications": "Developing", "specializedDrawings": "Proficient"}, "certifications": ["Flashing Dimension Checker"], "baselineOrders": 0, "baselineFlashings": 0, "baselineBits": 0},

    # Team Delta (Structural Trims & Heavy Gauge) - Lead: Rahul Deshmukh
    {"id": "EMP-115", "name": "Rahul Deshmukh", "team": "Team Delta (Structural Trims)", "shift": "Shift C", "role": "Night Operations Lead", "status": "Present", "checkin": "21:44 PM", "checkout": "--", "accuracy": 99.5, "avatar": "RD", "manager": "David Harrison", "skills": {"orderKeying": "Expert", "flashingInterp": "Expert", "bitsProcessing": "Expert", "doubleChecking": "Expert", "qualityReview": "Expert", "customerClarifications": "Expert", "specializedDrawings": "Expert"}, "certifications": ["Heavy Gauge Bending & Cross-Midnight Command"], "baselineOrders": 24, "baselineFlashings": 160, "baselineBits": 45},
    {"id": "EMP-129", "name": "Vikas Malhotra", "team": "Team Delta (Structural Trims)", "shift": "Shift A", "role": "Structural Detailer", "status": "Present", "checkin": "05:50 AM", "checkout": "--", "accuracy": 99.2, "avatar": "VM", "manager": "Rahul Deshmukh", "skills": {"orderKeying": "Proficient", "flashingInterp": "Expert", "bitsProcessing": "Expert", "doubleChecking": "Proficient", "qualityReview": "Intermediate", "customerClarifications": "Intermediate", "specializedDrawings": "Expert"}, "certifications": ["Heavy Gauge Structural Flashing Level 2"], "baselineOrders": 22, "baselineFlashings": 150, "baselineBits": 50},
    {"id": "EMP-130", "name": "Alok Mishra", "team": "Team Delta (Structural Trims)", "shift": "Shift B", "role": "Structural Detailer", "status": "Present", "checkin": "13:57 PM", "checkout": "--", "accuracy": 98.7, "avatar": "AM", "manager": "Rahul Deshmukh", "skills": {"orderKeying": "Proficient", "flashingInterp": "Proficient", "bitsProcessing": "Proficient", "doubleChecking": "Intermediate", "qualityReview": "Developing", "customerClarifications": "Developing", "specializedDrawings": "Proficient"}, "certifications": ["Industrial Gutters & Aprons"], "baselineOrders": 21, "baselineFlashings": 145, "baselineBits": 48},
    {"id": "EMP-131", "name": "Kiran George", "team": "Team Delta (Structural Trims)", "shift": "Shift A", "role": "Structural Detailer", "status": "Present", "checkin": "05:53 AM", "checkout": "--", "accuracy": 99.0, "avatar": "KG", "manager": "Rahul Deshmukh", "skills": {"orderKeying": "Proficient", "flashingInterp": "Proficient", "bitsProcessing": "Expert", "doubleChecking": "Proficient", "qualityReview": "Intermediate", "customerClarifications": "Intermediate", "specializedDrawings": "Proficient"}, "certifications": ["Commercial Facade Extrusions"], "baselineOrders": 23, "baselineFlashings": 155, "baselineBits": 52},
    {"id": "EMP-132", "name": "Nidhi Shah", "team": "Team Delta (Structural Trims)", "shift": "Shift B", "role": "Structural Detailer", "status": "Present", "checkin": "13:59 PM", "checkout": "--", "accuracy": 98.9, "avatar": "NS", "manager": "Rahul Deshmukh", "skills": {"orderKeying": "Proficient", "flashingInterp": "Proficient", "bitsProcessing": "Proficient", "doubleChecking": "Intermediate", "qualityReview": "Intermediate", "customerClarifications": "Developing", "specializedDrawings": "Proficient"}, "certifications": ["Galvanized & Zincalume Prep"], "baselineOrders": 22, "baselineFlashings": 148, "baselineBits": 46},
    {"id": "EMP-133", "name": "Pranav Shinde", "team": "Team Delta (Structural Trims)", "shift": "Shift C", "role": "Structural Detailer", "status": "Present", "checkin": "21:54 PM", "checkout": "--", "accuracy": 98.6, "avatar": "PS", "manager": "Rahul Deshmukh", "skills": {"orderKeying": "Intermediate", "flashingInterp": "Proficient", "bitsProcessing": "Proficient", "doubleChecking": "Intermediate", "qualityReview": "Developing", "customerClarifications": "Developing", "specializedDrawings": "Proficient"}, "certifications": ["Night Shift Heavy Duty SOP"], "baselineOrders": 20, "baselineFlashings": 140, "baselineBits": 42},
    {"id": "EMP-134", "name": "Tanvi Rane", "team": "Team Delta (Structural Trims)", "shift": "Shift A", "role": "Structural Detailer", "status": "Present", "checkin": "05:57 AM", "checkout": "--", "accuracy": 99.3, "avatar": "TR", "manager": "Rahul Deshmukh", "skills": {"orderKeying": "Expert", "flashingInterp": "Expert", "bitsProcessing": "Proficient", "doubleChecking": "Proficient", "qualityReview": "Intermediate", "customerClarifications": "Intermediate", "specializedDrawings": "Proficient"}, "certifications": ["Tapered Industrial Gutter Master"], "baselineOrders": 24, "baselineFlashings": 162, "baselineBits": 50},
    {"id": "EMP-135", "name": "Varun Singhal", "team": "Team Delta (Structural Trims)", "shift": "Shift B", "role": "Structural Detailer", "status": "Present", "checkin": "13:51 PM", "checkout": "--", "accuracy": 98.8, "avatar": "VS", "manager": "Rahul Deshmukh", "skills": {"orderKeying": "Proficient", "flashingInterp": "Proficient", "bitsProcessing": "Proficient", "doubleChecking": "Intermediate", "qualityReview": "Developing", "customerClarifications": "Developing", "specializedDrawings": "Intermediate"}, "certifications": ["Ridge Roll Profiling"], "baselineOrders": 21, "baselineFlashings": 142, "baselineBits": 44},
    {"id": "EMP-136", "name": "Yamini Rawat", "team": "Team Delta (Structural Trims)", "shift": "Shift C", "role": "Structural Detailer", "status": "Present", "checkin": "21:58 PM", "checkout": "--", "accuracy": 98.4, "avatar": "YR", "manager": "Rahul Deshmukh", "skills": {"orderKeying": "Intermediate", "flashingInterp": "Intermediate", "bitsProcessing": "Proficient", "doubleChecking": "Developing", "qualityReview": "Developing", "customerClarifications": "Developing", "specializedDrawings": "Intermediate"}, "certifications": ["Junior Structural Detailer"], "baselineOrders": 19, "baselineFlashings": 132, "baselineBits": 40},
    {"id": "EMP-137", "name": "Chetan Somani", "team": "Team Delta (Structural Trims)", "shift": "Shift A", "role": "Structural Detailer", "status": "Present", "checkin": "06:03 AM", "checkout": "--", "accuracy": 99.0, "avatar": "CS", "manager": "Rahul Deshmukh", "skills": {"orderKeying": "Proficient", "flashingInterp": "Proficient", "bitsProcessing": "Proficient", "doubleChecking": "Proficient", "qualityReview": "Intermediate", "customerClarifications": "Developing", "specializedDrawings": "Proficient"}, "certifications": ["Heavy Gauge Tolerances"], "baselineOrders": 23, "baselineFlashings": 154, "baselineBits": 48},
    {"id": "EMP-138", "name": "Geetika Vyas", "team": "Team Delta (Structural Trims)", "shift": "Shift B", "role": "Structural Detailer", "status": "Present", "checkin": "13:53 PM", "checkout": "--", "accuracy": 99.2, "avatar": "GV", "manager": "Rahul Deshmukh", "skills": {"orderKeying": "Proficient", "flashingInterp": "Expert", "bitsProcessing": "Proficient", "doubleChecking": "Proficient", "qualityReview": "Intermediate", "customerClarifications": "Intermediate", "specializedDrawings": "Proficient"}, "certifications": ["Custom Architectural Aprons"], "baselineOrders": 24, "baselineFlashings": 158, "baselineBits": 50},
    {"id": "EMP-139", "name": "Ishaan Saxena", "team": "Team Delta (Structural Trims)", "shift": "Shift A", "role": "Structural Detailer", "status": "Present", "checkin": "05:46 AM", "checkout": "--", "accuracy": 99.4, "avatar": "IS", "manager": "Rahul Deshmukh", "skills": {"orderKeying": "Expert", "flashingInterp": "Expert", "bitsProcessing": "Expert", "doubleChecking": "Proficient", "qualityReview": "Proficient", "customerClarifications": "Intermediate", "specializedDrawings": "Expert"}, "certifications": ["Senior Heavy Trim Specialist"], "baselineOrders": 25, "baselineFlashings": 170, "baselineBits": 54},
    {"id": "EMP-140", "name": "Madhav Kaul", "team": "Team Delta (Structural Trims)", "shift": "Shift C", "role": "Structural Detailer", "status": "Present", "checkin": "21:47 PM", "checkout": "--", "accuracy": 98.7, "avatar": "MK", "manager": "Rahul Deshmukh", "skills": {"orderKeying": "Proficient", "flashingInterp": "Proficient", "bitsProcessing": "Proficient", "doubleChecking": "Intermediate", "qualityReview": "Intermediate", "customerClarifications": "Developing", "specializedDrawings": "Proficient"}, "certifications": ["Night Shift Safety Specialist"], "baselineOrders": 21, "baselineFlashings": 144, "baselineBits": 45}
]

print(f"Generated {len(employees)} employees across 4 teams.")

# Generate Biometric Punches feed for today
punches = [
    {"punchId": "PCH-9001", "empId": "EMP-102", "empName": "Priya Nair", "type": "Office IN", "timeIST": "05:48:12", "timeAEST": "11:18:12", "device": "Terminal-01 (Main Gate)", "status": "Verified", "source": "Biometric Reader"},
    {"punchId": "PCH-9002", "empId": "EMP-117", "empName": "Manoj Tiwari", "type": "Office IN", "timeIST": "05:40:44", "timeAEST": "11:10:44", "device": "Terminal-03 (Audit Hub)", "status": "Verified", "source": "Biometric Reader"},
    {"punchId": "PCH-9003", "empId": "EMP-110", "empName": "Pooja Gupta", "type": "Office IN", "timeIST": "05:45:21", "timeAEST": "11:15:21", "device": "Terminal-01 (Main Gate)", "status": "Verified", "source": "Biometric Reader"},
    {"punchId": "PCH-9004", "empId": "EMP-108", "empName": "Meera Joshi", "type": "Office IN", "timeIST": "05:51:02", "timeAEST": "11:21:02", "device": "Terminal-02 (Keying Floor)", "status": "Verified", "source": "Biometric Reader"},
    {"punchId": "PCH-9005", "empId": "EMP-101", "empName": "Rohan Sharma", "type": "Office IN", "timeIST": "05:54:19", "timeAEST": "11:24:19", "device": "Terminal-01 (Main Gate)", "status": "Verified", "source": "Biometric Reader"},
    {"punchId": "PCH-9006", "empId": "EMP-116", "empName": "Deepa Krishnan", "type": "Office IN", "timeIST": "05:56:45", "timeAEST": "11:26:45", "device": "Terminal-02 (Keying Floor)", "status": "Verified", "source": "Biometric Reader"},
    {"punchId": "PCH-9007", "empId": "EMP-104", "empName": "Ananya Sen", "type": "Office IN", "timeIST": "05:58:30", "timeAEST": "11:28:30", "device": "Terminal-03 (Audit Hub)", "status": "Verified", "source": "Biometric Reader"},
    {"punchId": "PCH-9008", "empId": "EMP-111", "empName": "Arjun Nair", "type": "Office IN", "timeIST": "05:59:12", "timeAEST": "11:29:12", "device": "Terminal-01 (Main Gate)", "status": "Verified", "source": "Biometric Reader"},
    {"punchId": "PCH-9009", "empId": "EMP-105", "empName": "Rajesh Kumar", "type": "Office IN", "timeIST": "06:02:18", "timeAEST": "11:32:18", "device": "Terminal-01 (Main Gate)", "status": "Verified", "source": "Biometric Reader"},
    {"punchId": "PCH-9010", "empId": "EMP-101", "empName": "Rohan Sharma", "type": "Break START", "timeIST": "09:15:00", "timeAEST": "14:45:00", "device": "Terminal-02 (Keying Floor)", "status": "Verified", "source": "Biometric Reader", "breakCategory": "Tea/Refreshment"},
    {"punchId": "PCH-9011", "empId": "EMP-101", "empName": "Rohan Sharma", "type": "Break END", "timeIST": "09:30:14", "timeAEST": "15:00:14", "device": "Terminal-02 (Keying Floor)", "status": "Verified", "source": "Biometric Reader", "breakCategory": "Tea/Refreshment"},
    {"punchId": "PCH-9012", "empId": "EMP-101", "empName": "Rohan Sharma", "type": "Break START", "timeIST": "12:10:00", "timeAEST": "17:40:00", "device": "Terminal-02 (Keying Floor)", "status": "Verified", "source": "Biometric Reader", "breakCategory": "Lunch"},
    {"punchId": "PCH-9013", "empId": "EMP-101", "empName": "Rohan Sharma", "type": "Break END", "timeIST": "12:40:05", "timeAEST": "18:10:05", "device": "Terminal-02 (Keying Floor)", "status": "Verified", "source": "Biometric Reader", "breakCategory": "Lunch"},
    {"punchId": "PCH-9014", "empId": "EMP-101", "empName": "Rohan Sharma", "type": "Office OUT", "timeIST": "14:26:40", "timeAEST": "19:56:40", "device": "Terminal-01 (Main Gate)", "status": "Verified", "source": "Biometric Reader"},
    {"punchId": "PCH-9015", "empId": "EMP-106", "empName": "Sneha Reddy", "type": "Office IN", "timeIST": "13:50:11", "timeAEST": "19:20:11", "device": "Terminal-01 (Main Gate)", "status": "Verified", "source": "Biometric Reader"},
    {"punchId": "PCH-9016", "empId": "EMP-107", "empName": "Karthik Sundaram", "type": "Office IN", "timeIST": "13:55:00", "timeAEST": "19:25:00", "device": "Terminal-03 (Audit Hub)", "status": "Verified", "source": "Biometric Reader"},
    {"punchId": "PCH-9017", "empId": "EMP-114", "empName": "Kavita Patil", "type": "Office IN", "timeIST": "14:18:22", "timeAEST": "19:48:22", "device": "Terminal-01 (Main Gate)", "status": "Flagged for Review", "source": "Biometric Reader", "notes": "Late arrival (+18m past 14:00 scheduled start)"},
    {"punchId": "PCH-9018", "empId": "EMP-115", "empName": "Rahul Deshmukh", "type": "Office IN", "timeIST": "21:44:10", "timeAEST": "03:14:10", "device": "Terminal-01 (Main Gate)", "status": "Verified", "source": "Biometric Reader"},
    {"punchId": "PCH-9019", "empId": "EMP-109", "empName": "Amit Verma", "type": "Office IN", "timeIST": "21:50:35", "timeAEST": "03:20:35", "device": "Terminal-02 (Keying Floor)", "status": "Verified", "source": "Biometric Reader"},
    {"punchId": "PCH-9020", "empId": "EMP-113", "empName": "Sanjay Menon", "type": "Office IN", "timeIST": "21:52:19", "timeAEST": "03:22:19", "device": "Terminal-03 (Audit Hub)", "status": "Verified", "source": "Biometric Reader"}
]

# Generate detailed employee attendance timelines for Rohan Sharma (Flagship 360 example) and peers
timelines = {
    "EMP-101": {
        "empId": "EMP-101",
        "firstEntry": "05:54 AM",
        "lastExit": "14:26 PM",
        "expectedStart": "06:00 AM",
        "expectedEnd": "14:30 PM",
        "earlyMinutes": 6,
        "lateMinutes": 0,
        "timeOnPremises": "8h 32m",
        "recordedBreakDuration": "45m",
        "netAttendedDuration": "7h 47m",
        "overtimeStatus": "None (Standard Shift)",
        "missingPunches": False,
        "regularizationStatus": "Verified Compliant",
        "events": [
            {"time": "05:54", "type": "Office IN", "label": "Office Entry (Main Gate)", "status": "Verified"},
            {"time": "09:15", "type": "Break START", "label": "Morning Tea Break", "status": "Verified"},
            {"time": "09:30", "type": "Break END", "label": "Break Return (15m)", "status": "Verified"},
            {"time": "12:10", "type": "Break START", "label": "Lunch Break", "status": "Verified"},
            {"time": "12:40", "type": "Break END", "label": "Lunch Return (30m)", "status": "Verified"},
            {"time": "14:26", "type": "Office OUT", "label": "Shift Departure (Main Gate)", "status": "Verified"}
        ]
    },
    "EMP-114": {
        "empId": "EMP-114",
        "firstEntry": "14:18 PM",
        "lastExit": "--",
        "expectedStart": "14:00 PM",
        "expectedEnd": "22:30 PM",
        "earlyMinutes": 0,
        "lateMinutes": 18,
        "timeOnPremises": "In Progress",
        "recordedBreakDuration": "0m",
        "netAttendedDuration": "In Progress",
        "overtimeStatus": "None",
        "missingPunches": False,
        "regularizationStatus": "Exception (Late Arrival)",
        "events": [
            {"time": "14:18", "type": "Office IN", "label": "Office Entry (Main Gate)", "status": "Flagged (Late +18m)"}
        ]
    },
    "EMP-115": {
        "empId": "EMP-115",
        "firstEntry": "21:44 PM",
        "lastExit": "-- (Crosses Midnight to 06:30 AM)",
        "expectedStart": "22:00 PM",
        "expectedEnd": "06:30 AM (+1 Day)",
        "earlyMinutes": 16,
        "lateMinutes": 0,
        "timeOnPremises": "In Progress (Night Shift)",
        "recordedBreakDuration": "0m",
        "netAttendedDuration": "In Progress",
        "overtimeStatus": "None",
        "missingPunches": False,
        "regularizationStatus": "Verified Compliant",
        "events": [
            {"time": "21:44", "type": "Office IN", "label": "Night Shift Entry (Main Gate)", "status": "Verified"}
        ]
    }
}

# Shift handovers
handovers = [
    {
        "id": "HO-2027-089",
        "fromShift": "Shift A (Day)",
        "toShift": "Shift B (Afternoon)",
        "outgoingLead": "Priya Nair",
        "incomingLead": "Sneha Reddy",
        "timestamp": "2027-03-24 14:15 IST",
        "status": "Acknowledged",
        "pendingOrders": 8,
        "urgentJobs": "Melbourne Hospital St. Vincent Roof Capping (Order #ORD-AU-89450) - Priority release before 16:00 AEDT",
        "incompleteAudits": "3 tapered valley gutters under double-check with Team Gamma",
        "customerClarifications": "Awaiting architect confirmation on parapet pitch for Geelong commercial site",
        "staffingNotes": "Kavita Patil arrived 18m late; Shift B has full coverage with 9 keyers active",
        "actionItems": [
            {"task": "Release St. Vincent hospital order package to Melbourne brake press queue", "owner": "Sneha Reddy", "done": True},
            {"task": "Verify rev 3 CAD drawing for Dandenong warehouse ridge capping", "owner": "Karthik Sundaram", "done": False},
            {"task": "Close root-cause investigation notes on QC-2027-084", "owner": "Manoj Tiwari", "done": True}
        ]
    },
    {
        "id": "HO-2027-088",
        "fromShift": "Shift C (Night)",
        "toShift": "Shift A (Day)",
        "outgoingLead": "Rahul Deshmukh",
        "incomingLead": "Priya Nair",
        "timestamp": "2027-03-24 06:10 IST",
        "status": "Archived",
        "pendingOrders": 4,
        "urgentJobs": "Apex Commercial warehouse apron flashing batch",
        "incompleteAudits": "All night double-checks cleared by Sanjay Menon",
        "customerClarifications": "None outstanding",
        "staffingNotes": "Clean night shift, 0 attendance anomalies",
        "actionItems": [
            {"task": "Transition standing seam profiles to Team Beta morning detailers", "owner": "Priya Nair", "done": True}
        ]
    }
]

# Management alerts (Exceptions inbox)
alerts = [
    {
        "id": "ALT-501",
        "type": "Missing Punch",
        "priority": "Medium",
        "empId": "EMP-118",
        "empName": "Sunita Rao",
        "team": "Team Beta (Architectural Panels)",
        "message": "No biometric OUT punch recorded for previous shift cycle.",
        "assignedTo": "Pooja Gupta",
        "status": "Open",
        "created": "Today 08:30 IST",
        "resolution": ""
    },
    {
        "id": "ALT-502",
        "type": "Quality Case Review",
        "priority": "High",
        "empId": "EMP-105",
        "empName": "Rajesh Kumar",
        "team": "Team Alpha (Flashings & Trims)",
        "message": "Resupply Case #QC-2027-084 pending root-cause verification for Melbourne dry-fit variance.",
        "assignedTo": "Manoj Tiwari",
        "status": "In Progress",
        "created": "Today 07:15 IST",
        "resolution": "Drawing markup revision B clash identified; corrective action prompt staged."
    },
    {
        "id": "ALT-503",
        "type": "Staffing Threshold",
        "priority": "High",
        "empId": "EMP-111",
        "empName": "Arjun Nair",
        "team": "Team Alpha (Flashings & Trims)",
        "message": "Leave request creates potential staffing dip on March 26 (minimum 8 keyers threshold).",
        "assignedTo": "Priya Nair",
        "status": "Open",
        "created": "Today 06:45 IST",
        "resolution": ""
    },
    {
        "id": "ALT-504",
        "type": "Late Arrival",
        "priority": "Low",
        "empId": "EMP-114",
        "empName": "Kavita Patil",
        "team": "Team Alpha (Flashings & Trims)",
        "message": "Biometric entry recorded 18m past 14:00 scheduled shift start time.",
        "assignedTo": "Sneha Reddy",
        "status": "Acknowledged",
        "created": "Today 14:20 IST",
        "resolution": "Shift supervisor confirmed transit delay; compensatory 20m logged."
    },
    {
        "id": "ALT-505",
        "type": "Shift Handover Review",
        "priority": "Medium",
        "empId": "EMP-106",
        "empName": "Sneha Reddy",
        "team": "Team Alpha (Flashings & Trims)",
        "message": "Urgent hospital capping order requires priority dispatch sign-off before 16:00 AEDT.",
        "assignedTo": "Sneha Reddy",
        "status": "Resolved",
        "created": "Today 14:16 IST",
        "resolution": "Job package validated and sent to Tullamarine laser schedule."
    }
]

# Skills list
skills_definitions = [
    {"key": "orderKeying", "name": "Order Keying Speed & Precision", "desc": "High-velocity translation of customer take-offs into CAD parameters"},
    {"key": "flashingInterp", "name": "Flashing Interpretation", "desc": "Girth, bend sequence, hemming, and tolerance calculation"},
    {"key": "bitsProcessing", "name": "Custom Bits Processing", "desc": "Complex non-standard stop-ends, sumps, and transitions"},
    {"key": "doubleChecking", "name": "Double-Checking Rigor", "desc": "Secondary independent verification of geometries and quantities"},
    {"key": "qualityReview", "name": "Quality Review & Audit", "desc": "Root-cause diagnostics, resupply prevention, and SOP coaching"},
    {"key": "customerClarifications", "name": "Customer Drawing Clarification", "desc": "Identifying architectural ambiguities and issuing RFIs"},
    {"key": "specializedDrawings", "name": "Specialized Architectural Profiles", "desc": "Standing seam, interlocking cassette panels, and heritage curves"}
]

# Existing leave requests, quality cases, awards, production records
# Let's preserve all existing items and augment them cleanly
with open("/Users/raksh/.gemini/antigravity/scratch/pulse-showcase/initial_data.json", "r") as f:
    old_data = json.load(f)

master_data = {
    "employees": employees,
    "biometricPunches": punches,
    "employeeAttendanceTimelines": timelines,
    "handovers": handovers,
    "alerts": alerts,
    "skillsDefinitions": skills_definitions,
    "leaveRequests": old_data.get("leaveRequests", []),
    "qualityCases": old_data.get("qualityCases", []),
    "productionRecords": old_data.get("productionRecords", []),
    "awards": old_data.get("awards", []),
    "biometricMachine": {
        "deviceModel": "BioPulse-X Enterprise Multi-Terminal",
        "deviceStatus": "Demo Mode — Simulated Biometric Data",
        "activeTerminals": 3,
        "lastSyncTime": "06:17:09 IST",
        "totalPunchesToday": len(punches),
        "protocol": "Simulated Webhook / Secure Event Stream"
    }
}

with open("/Users/raksh/.gemini/antigravity/scratch/pulse-showcase/initial_data.json", "w") as f:
    json.dump(master_data, f, indent=2)

print("Updated initial_data.json with full master operational schema!")
