# Where Wearable Neuro-Monitoring Captures Value

*Analysis memo — Binny Park, July 2026*
*Companion to: gait-classifier notebook (`notebooks/01_analysis.ipynb`)*

## Summary

A wearable can detect neurodegenerative gait decline well — a random-forest classifier reaches **0.97 cross-validated ROC-AUC** on public sensor data, driven almost entirely by measures of *gait irregularity*. But detection quality is not what Medicare pays for. Under the 2026 Physician Fee Schedule, remote-monitoring reimbursement is triggered by three things — an FDA-cleared device, enough days of transmitted data, and documented clinical time spent acting on it — **none of which is the algorithm**. The strategic implication: a wearable startup's defensible value is less about model accuracy than about regulatory clearance, adherence engineering, and billing integration.

## 1. The signal (from the analysis)

- **Dataset:** PhysioNet *Gait in Neurodegenerative Disease* database — force-sensor stride recordings from ALS, Huntington's, and Parkinson's patients vs. healthy controls (n = 64; 48 disease / 16 control).
- **Features:** 8 engineered gait metrics (stride variability, swing/stance ratios, cadence, left–right asymmetry, robust spread).
- **Model:** random forest, **0.968 CV ROC-AUC**; logistic-regression baseline 0.878.
- **What carries the signal:** the top three features — stride IQR (0.25), stride CV (0.18), and swing-percent variability (0.17) — are all measures of *rhythmic irregularity*, together ~60% of the model's decision. Neurodegeneration shows up as loss of gait regularity, and cheap sensors measure it.
- **One-line takeaway:** a wearable *can* flag decline from gait. Detection is solved.

**Limitations:**
- Only 16 controls, so specificity estimates are unstable (held-out control recall was 0.50 on 4 subjects — one patient swings it 25 points). The CV AUC is the trustworthy number; any single split is noisy at this sample size.
- The dataset is ALS/HD/PD, not the senior cognitive-decline population a company like RemNeuro targets. The *method* transfers; the specific model would need revalidation on the target population before any clinical claim.

## 2. The market

- Aging U.S. population and a shift toward value-based and at-home care make continuous gait/mobility monitoring a large and growing addressable market.
- A 2023 review documents the aging-population and their intentions to use wearable devices: https://pmc.ncbi.nlm.nih.gov/articles/PMC9868808/
- Buyers are not just patients: health systems (readmission and fall risk), payers (total-cost-of-care), senior-living operators, and pharma (trial endpoints and adherence).
- The US Remote Patient Market is estimated to be $9.4B in 2025, with a 25% CAGR until 2035: https://www.rootsanalysis.com/reports/telemedicine-tools-and-software-providers-market.html
- Over 90% of adults over 65 years old have one or more chronic conditions: https://www.cdc.gov/chronic-disease/about/index.html

## 3. The reimbursement pathway

*All figures: 2026 Medicare Physician Fee Schedule, national non-facility averages; geographic adjustment (GPCI) applies. Verify against the CMS final rule before citing externally.*

Medicare pays for Remote Physiologic Monitoring (RPM) through a code family split into two kinds of activity — **supplying the device / collecting data**,and **clinical time managing the patient**:

| Code | What it pays for | ~2026 rate | Key requirement |
|------|------------------|-----------|-----------------|
| 99453 | One-time device setup + patient education | $21.71 (once) | Per device, per episode |
| 99454 | Device supply + data, 16+ days/mo | $52.11/mo | **≥16 transmission days** |
| 99445 | Device supply + data, 2–15 days/mo *(new 2026)* | $52.11/mo | **≥2 transmission days** |
| 99457 | First 20 min clinical management | $52.11/mo | **Interactive human communication** |
| 99470 | First 10 min management *(new 2026)* | $26.05/mo | Not combinable with 99457 |
| 99458 | Each additional 20 min | $41.42/mo | Add-on to 99457 |
(Source: https://rimidi.com/news/2026-rpm-and-ccm-reimbursement-codes-and-payment-updates)

A single fully-enrolled patient generates roughly **$100–$145/month** ongoing (99454 + 99457, plus 99458 when management time runs long), and ~$200 in month one with setup.
At scale, ~100 patients billing the base codes is on the order of **$120K/year** in recurring revenue.

**The three things that actually unlock payment:**
1. **An FDA-cleared medical device.** RPM billing requires the device meet the FDA definition of a medical device. This is a regulatory gate, not an algorithmic one.
2. **Transmission days.** 99454 requires data on ≥16 days; the new 99445 lowers the floor to ≥2 days. Payment depends on *the patient wearing the device*, not on what the model concludes.
3. **Documented clinical time and action.** The management codes require interactive human communication and documentation of *what data was reviewed and what clinical decision followed*. CMS is explicit that reimbursement rewards clinical action, not passive data accumulation.

**Diagnostic Accuracy not necessary in reimbursement requirements.** A 0.97-AUC model and a 0.75-AUC model bill identically. The fee schedule pays for device-supply and clinician-time, full stop.

For context, Remote *Therapeutic* Monitoring (RTM, CPT 98975–98981) is the adjacent track for non-physiologic data — adherence, therapy engagement, patient-reported outcomes — and notably allows non-medical-grade devices and apps. A gait/mobility product may fit RPM (physiologic) or RTM depending on how the data and claims are framed; the choice has real regulatory and billing consequences worth deciding deliberately.

## 4. So what — where value concentrates

If reimbursement rewards *device + days + documented time* rather than *detection quality*,
then a wearable startup's competitive advantage is not the classifier. It is:

- **Regulatory clearance** — getting to (and maintaining) FDA medical-device status is the gate to the entire RPM revenue stream. This is a durable moat competitors can't skip.
- **Adherence engineering** — revenue is gated on hitting transmission-day thresholds. A device and app that keep seniors actually wearing and transmitting (passive/ambient sensing, cellular-connected, low setup friction) directly convert to billable months. The 2026 addition of the 2-day 99445 code makes continuous-wear wearables especially well-positioned.
- **Billing + workflow integration** — the management codes only pay if clinical time is captured and documented correctly. Software that generates a defensible audit trail and slots into care-team workflow is where dollars are won or lost; most practices under-collect because their billing is misconfigured.
- **The algorithm's real job** — not to be sold as "accuracy," but to generate *actionable alerts* that (a) justify and structure billable clinical management time, and (b) improve outcomes that matter in value-based and payer contracts, where detection quality finally does translate into money via reduced downstream cost.

**Recommendation:** Compete on clearance, adherence, and integration. Treat the model as necessary infrastructure, not the differentiator — and position detection quality where it actually monetizes: outcomes-based contracting, not fee-for-service accuracy.

## 5. Risks / what would change this
- **Coverage policy shifts.** RPM rates and thresholds are reset annually; the revenue model is exposed to CMS rule changes (though 2026 moved favorably, adding lower-threshold codes).
- **FDA pathway cost and timing** for software-as-a-medical-device.
- **Real-world data quality** — in-clinic gait signal (this analysis) is cleaner than free-living wearable data; adherence and noise degrade both the model and the billable-days count.
- **Payer skepticism** on value-based contracts, where the accuracy argument lives.
- **External validity** — the model must be revalidated on the actual target population before any clinical or commercial claim.

- **S. 1399, the Health Tech Investment Act.** AI is already deep in medicine and this bill would let capital flow more freely into the space, giving people room to take the risk of building novel tools. It's the closest thing to a policy tailwind for this kind of work. It doesn't change my core argument: it's still a bill in committee, and it prices on the manufacturer's submitted cost, not diagnostic accuracy — so "accuracy isn't the moat" holds even under it, and its outpatient-APC framing probably doesn't reach a home-monitoring product. But the bigger read is directional: if a model this simple can flag neurodegeneration, the pathway these bills are trying to build for is coming whether or not this particular one passes.