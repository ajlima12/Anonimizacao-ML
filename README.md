# Anonymization Demo (Bank context)

This project demonstrates:
- generating synthetic/augmented records (weighted averaging)
- searching for a specific person in the dataset (before anonymization)
- anonymization techniques: swapping/shuffling, masking & hashing, generalization and perturbation
- producing several Excel outputs for inspection

## Files in the package
- `project/main.py` - CLI demo to search / anonymize / augment
- `project/anonymizer.py` - anonymization functions
- `data/dataset_original.xlsx` - original generated dataset (1000 rows)
- `data/dataset_augmented_weighted.xlsx` - original + 500 synthetic (weighted)
- `data/dataset_swapped_shuffled.xlsx` - columns swapped/shuffled, names pseudonymized
- `data/dataset_generalized_k_anonymity.xlsx` - generalized view (k-anonymity style)
- `data/dataset_anonymized_masked.xlsx` - masked & hashed sensitive fields
- `requirements.txt` - python dependencies

## How to run (Visual Studio / Visual Studio Code)
1. Open Visual Studio Code or Visual Studio.
2. Create a Python environment (recommended: venv) and install requirements:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # on Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Run search example:
   ```bash
   python project/main.py --data data/dataset_original.xlsx --action search --name "Ana Julia Lima De Oliveira"
   ```
4. Run anonymization (mask):
   ```bash
   python project/main.py --data data/dataset_original.xlsx --action anonymize --method mask --out data/out_masked.xlsx
   ```
5. Run augment (create synthetic records):
   ```bash
   python project/main.py --data data/dataset_original.xlsx --action augment --out data/out_augmented.xlsx
   ```

**Warning:** This is an educational demo. Do not use with real personal data in production without following legal/regulatory privacy guidance (LGPD in Brazil, GDPR, etc.).