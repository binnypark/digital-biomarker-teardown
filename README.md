# Digital Biomarker Teardown

**Thesis:** A wearable can detect a neurodegeneration signal from gait, but the binding
constraint on a remote-monitoring startup is *reimbursement*, not accuracy. This project
proves both halves — build the signal, then reason about whether anyone pays for it.

## What's here
- `notebooks/01_analysis.ipynb` — the full pipeline: load -> EDA -> features -> model -> evaluation
- `src/features.py` — gait feature-engineering helpers
- `reports/memo.md` — the strategy memo (the reimbursement-bottleneck argument)
- `data/DATA.md` — where to get the dataset (data is **not** committed)

## The two halves
1. **Signal.** Gait/actigraphy classifier distinguishing neurodegenerative decline from controls.
2. **Economics.** TAM sizing + RPM/RTM reimbursement pathway -> where does a startup capture value?

## Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab   # open notebooks/01_analysis.ipynb
```

## Headline result (fill in after you build)
> Gait-based classifier, ROC-AUC 0.__, sensitivity 0.__, specificity 0.__.
> Top features: ________. Reimbursement gap identified: ________.

