"""
Student Score Analysis Tool
Loads student data from CSV and generates score statistics and summary report
"""

import csv
import os

def load_student_data(filename="data.csv"):
    """Load CSV data with validation and error handling"""
    students = []
    errors = []
    
    # Check if file exists
    if not os.path.exists(filename):
        print("ERROR: File 'data.csv' not found!")
        print(f"Current directory: {os.getcwd()}")
        return students, errors
    
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            
            if reader.fieldnames is None:
                print("ERROR: CSV file is empty or has no header!")
                return students, errors
            
            # Load rows with validation
            for row_num, row in enumerate(reader, start=2):
                if row is None or not any(row.values()):
                    continue
                
                # Check for missing score fields
                score_fields = ['math score', 'reading score', 'writing score']
                missing_fields = [field for field in score_fields 
                                if field not in row or row[field].strip() == '']
                
                if missing_fields:
                    errors.append(f"Row {row_num}: Missing fields {missing_fields}")
                    continue
                
                # Validate scores are numeric
                try:
                    for field in score_fields:
                        float(row[field])
                    students.append(row)
                except ValueError as e:
                    errors.append(f"Row {row_num}: Invalid score value - {e}")
        
        # Display load results
        print(f"Loaded: {len(students)} valid students")
        if errors:
            print(f"Errors found: {len(errors)}")
            print("\nError details (first 5):")
            for error in errors[:5]:
                print(f"  - {error}")
        
        print(f"\nColumns: {list(students[0].keys())}")
        print("\nFirst 3 students:")
        for i, student in enumerate(students[:3]):
            print(f"\nStudent {i+1}:")
            print(f"  Gender: {student['gender']}")
            print(f"  Race/Ethnicity: {student['race/ethnicity']}")
            print(f"  Math Score: {student['math score']}")
            print(f"  Reading Score: {student['reading score']}")
            print(f"  Writing Score: {student['writing score']}")
    
    except Exception as e:
        print(f"ERROR reading file: {e}")
    
    return students, errors


def calculate_statistics(students):
    """Calculate statistics per subject with error handling"""
    if not students:
        print("ERROR: No valid student data loaded!")
        return
    
    subjects = ['math score', 'reading score', 'writing score']
    
    for subject in subjects:
        try:
            # Convert scores to floats, skip any that fail
            scores = []
            invalid_count = 0
            
            for student in students:
                if subject in student and student[subject].strip():
                    try:
                        scores.append(float(student[subject]))
                    except ValueError:
                        invalid_count += 1
                        continue
            
            if not scores:
                print(f"\n{subject.upper()}")
                print(f"  WARNING: No valid scores found!")
                continue
            
            # Calculate statistics
            mean_score = sum(scores) / len(scores)
            highest_score = max(scores)
            lowest_score = min(scores)
            
            print(f"\n{subject.upper()}")
            print(f"  Valid scores: {len(scores)}/{len(students)}")
            if invalid_count > 0:
                print(f"  Invalid scores skipped: {invalid_count}")
            print(f"  Mean:    {mean_score:.2f}")
            print(f"  Highest: {highest_score}")
            print(f"  Lowest:  {lowest_score}")
        
        except Exception as e:
            print(f"\nERROR calculating {subject}: {e}")


def print_summary_report(students, errors):
    """Print clean formatted summary with error handling"""
    if not students:
        print("ERROR: Cannot generate report - no valid student data available")
        return
    
    print("\n" + "="*70)
    print("STUDENT SCORES SUMMARY REPORT")
    print("="*70)
    print(f"Total Valid Students: {len(students)}")
    if errors:
        print(f"Records with errors: {len(errors)}")
    print("="*70)
    
    # Create formatted table
    subjects = ['math score', 'reading score', 'writing score']
    subject_names = ['Math', 'Reading', 'Writing']
    
    print(f"\n{'Subject':<15} {'Mean':<12} {'Highest':<12} {'Lowest':<12} {'Valid':<10}")
    print("-"*70)
    
    for subject, name in zip(subjects, subject_names):
        try:
            scores = []
            for student in students:
                if subject in student and student[subject].strip():
                    try:
                        scores.append(float(student[subject]))
                    except ValueError:
                        continue
            
            if scores:
                mean = sum(scores) / len(scores)
                highest = max(scores)
                lowest = min(scores)
                valid_pct = (len(scores) / len(students)) * 100
                print(f"{name:<15} {mean:<12.2f} {highest:<12.1f} {lowest:<12.1f} {valid_pct:<10.1f}%")
            else:
                print(f"{name:<15} {'N/A':<12} {'N/A':<12} {'N/A':<12} {'0.0%':<10}")
        except Exception as e:
            print(f"{name:<15} ERROR: {str(e)[:40]}")
    
    print("="*70)


if __name__ == "__main__":
    print("="*70)
    print("STUDENT SCORE ANALYSIS")
    print("="*70)
    print()
    
    # Load data
    students, errors = load_student_data("data.csv")
    
    # Calculate statistics
    print("\n" + "="*70)
    print("DETAILED STATISTICS")
    print("="*70)
    calculate_statistics(students)
    
    # Print summary report
    print_summary_report(students, errors)
