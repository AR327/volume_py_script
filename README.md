# Volume Scripts Repository

This repository contains volume scripts for working with Excel reports and data merges.

## Included script

- `ehr_appointment_report_merge_py.py`: reads workbook sheets, extracts patient and facility data, and consolidates rows into a merged Excel file.

## Setup

1. Install Python and Git on your machine.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the environment and install dependencies:
   ```bash
   pip install pandas openpyxl
   ```

## Usage

```bash
python ehr_appointment_report_merge_py.py
```

Update the `INPUT_FILE` and `OUTPUT_FILE` constants in `ehr_appointment_report_merge_py.py` as needed.
