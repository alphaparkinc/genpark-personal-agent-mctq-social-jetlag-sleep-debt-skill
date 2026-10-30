# -*- coding: utf-8 -*-
"""MCTQ Social Jetlag & Sleep Debt Pacer for GenPark Personal Agent."""
import json
from typing import Dict, Any

class MCTQSocialJetlagSleepDebtPacer:
    @staticmethod
    def calculate_mctq_corrected_mid_sleep(sleep_onset_free_hours: float, sleep_duration_free_hours: float, sleep_duration_work_hours: float) -> Dict[str, Any]:
        raw_mid_sleep_free = (sleep_onset_free_hours + (sleep_duration_free_hours / 2.0)) % 24.0
        # MSFsc correction formula: MSFsc = MSF - (SDF - SDW) / 2 if SDF > SDW
        if sleep_duration_free_hours > sleep_duration_work_hours:
            oversleep = sleep_duration_free_hours - sleep_duration_work_hours
            msfsc = (raw_mid_sleep_free - (oversleep / 2.0)) % 24.0
        else:
            msfsc = raw_mid_sleep_free
            
        msfsc = round(msfsc, 2)
        if msfsc < 3.0: chronotype = "EXTREME_EARLY_LARK"
        elif msfsc <= 4.0: chronotype = "MODERATE_EARLY"
        elif msfsc <= 5.5: chronotype = "INTERMEDIATE_NORMAL"
        elif msfsc <= 7.0: chronotype = "MODERATE_LATE_OWL"
        else: chronotype = "EXTREME_LATE_NIGHT_OWL"

        h = int(msfsc)
        m = int((msfsc - h) * 60)
        return {
            "raw_mid_sleep_free": raw_mid_sleep_free,
            "corrected_mid_sleep_msfsc": f"{h:02d}:{m:02d}",
            "chronotype_classification": chronotype,
            "weekly_workday_sleep_deficit_hours": round(max(0.0, sleep_duration_free_hours - sleep_duration_work_hours) * 5.0, 1)
        }

    @staticmethod
    def compute_social_jetlag_and_debt_recovery(mid_sleep_work_hours: float, mid_sleep_free_hours: float, weekly_sleep_debt_hours: float = 6.0) -> Dict[str, Any]:
        social_jetlag = round(abs(mid_sleep_free_hours - mid_sleep_work_hours), 2)
        tier = "HIGH_METABOLIC_RISK" if social_jetlag > 2.0 else ("MODERATE_MISALIGNMENT" if social_jetlag > 1.0 else "OPTIMAL_CIRCADIAN_STABILITY")
        
        return {
            "social_jetlag_hours": social_jetlag,
            "circadian_strain_tier": tier,
            "weekly_sleep_debt_hours": weekly_sleep_debt_hours,
            "recovery_strategy": [
                "Cap weekend wake-up delay to within 60 minutes of weekday alarm",
                "Repay sleep debt via 20-30 min afternoon naps (13:00-14:30) rather than sleeping in",
                "Anchor circadian clock with 15 minutes of outdoor sunlight within 30 min of waking"
            ]
        }
