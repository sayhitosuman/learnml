# Student Score Analysis

**Loads student exam data from CSV and generates mean, highest, and lowest scores per subject with error handling for missing files and invalid data.**

## How to Run

```bash
python analyze_scores.py
```

## Sample Output

```
======================================================================
STUDENT SCORE ANALYSIS
======================================================================

Loaded: 1000 valid students

Columns: ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course', 'math score', 'reading score', 'writing score']

First 3 students:

Student 1:
  Gender: female
  Race/Ethnicity: group B
  Math Score: 72
  Reading Score: 72
  Writing Score: 74

Student 2:
  Gender: female
  Race/Ethnicity: group C
  Math Score: 69
  Reading Score: 90
  Writing Score: 88

Student 3:
  Gender: female
  Race/Ethnicity: group B
  Math Score: 90
  Reading Score: 95
  Writing Score: 93

======================================================================
DETAILED STATISTICS
======================================================================

MATH SCORE
  Valid scores: 1000/1000
  Mean:    66.09
  Highest: 100.0
  Lowest:  0.0

READING SCORE
  Valid scores: 1000/1000
  Mean:    69.17
  Highest: 100.0
  Lowest:  17.0

WRITING SCORE
  Valid scores: 1000/1000
  Mean:    68.05
  Highest: 100.0
  Lowest:  10.0

======================================================================
STUDENT SCORES SUMMARY REPORT
======================================================================
Total Valid Students: 1000
======================================================================

Subject         Mean         Highest      Lowest       Valid
----------------------------------------------------------------------
Math            66.09        100.0        0.0          100.0     %
Reading         69.17        100.0        17.0         100.0     %
Writing         68.05        100.0        10.0         100.0     %
======================================================================
```

## Files

- `data.csv` - Input data file containing student demographics and test scores
- `analyze_scores.py` - Main analysis script
- `first.ipynb` - Jupyter notebook version of the analysis
