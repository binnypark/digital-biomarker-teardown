"""Gait feature engineering.
"""
import numpy as np
import pandas as pd


def stride_time_variability(strides: np.ndarray) -> float:
    """Coefficient of variation of stride time. Higher CV = less regular gait,
    a validated marker of neurodegeneration."""
    strides = np.asarray(strides, dtype=float)
    strides = strides[np.isfinite(strides)]
    if strides.mean() == 0 or len(strides) < 2:
        return np.nan
    return strides.std(ddof=1) / strides.mean()


def swing_stance_ratio(swing: np.ndarray, stance: np.ndarray) -> float:
    """Mean swing / mean stance. Shifts with impaired push-off / balance."""
    swing, stance = np.asarray(swing, float), np.asarray(stance, float)
    m_stance = np.nanmean(stance)
    return np.nan if m_stance == 0 else np.nanmean(swing) / m_stance


def cadence(stride_intervals: np.ndarray) -> float:
    """Steps per minute, approximated from stride intervals (seconds)."""
    m = np.nanmean(np.asarray(stride_intervals, float))
    return np.nan if not m else 60.0 / m


def left_right_asymmetry(left: np.ndarray, right: np.ndarray) -> float:
    """Normalized L/R difference. Neurodegeneration often presents asymmetrically."""
    l, r = np.nanmean(np.asarray(left, float)), np.nanmean(np.asarray(right, float))
    denom = (l + r) / 2
    return np.nan if denom == 0 else abs(l - r) / denom


def build_feature_row(record: pd.DataFrame) -> dict:
    """Map ONE subject's raw record -> one feature dict."""
    return {
        "stride_cv":       stride_time_variability(record["L_stride"]),
        "swing_stance":    swing_stance_ratio(record["L_swing"], record["L_stance"]),
        "cadence":         cadence(record["L_stride"]),
        "asymmetry":       left_right_asymmetry(record["L_stride"], record["R_stride"]),
        "stride_median":   record["L_stride"].median(),
        "stride_iqr":      record["L_stride"].quantile(.75) - record["L_stride"].quantile(.25),
        "dbl_support_pct": record["dbl_support_pct"].mean(),
        "swing_pct_std":   record["L_swing_pct"].std(),
    }
