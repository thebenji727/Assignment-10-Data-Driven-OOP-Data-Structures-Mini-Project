from collections import defaultdict
from domain.analysis_result import AnalysisResult

class Analyzer:
    def analyze(self, records, min_mag=3.0):
        filtered = [r for r in records if r.magnitude >= min_mag]

        grouped = defaultdict(int)

        for r in filtered:
            day = r.time.date()
            grouped[day] += 1

        avg_daily = sum(grouped.values()) / len(grouped)
        burst_days = [day for day, count in grouped.items() if count > avg_daily]

        conclusion = (
            "Supported"
            if len(burst_days) > len(grouped) * 0.3
            else "Inconclusive"
        )

        return AnalysisResult(avg_daily, burst_days, conclusion)